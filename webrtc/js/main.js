'use strict';

// body 돔 요소
const body = document.querySelector('body')

// 비디오태그 생성(자동재생, 인라인재생, 음소거) 및 레퍼런스 반환
function createVideoTag(){
    const video = document.createElement('video')
    video.autoplay=true
    // video.setAttribute('muted','')
    video.muted = true
    video.playsInline=true
    body.appendChild(video)
    return video
}

// 방에 두명이상 있는지 판단
var isChannelReady = false;
// 내가 방 생성자인지 판단
var isInitiator = false;
// 현재 p2p연결이 되었는지 판단
var isStarted = false;
// 내 영상
var localStream;
// 나와 상대의 연결?
var pc=new Map();
// 상대 영상들(1:N 확장을 위해 Map으로 만듬)
var remoteStream = new Map();
// turn 서버 사용 가능 판단
var turnReady;
// ice서버의 정보, 스턴서버 or 턴 서버 만들어서 넣어야할듯
var pcConfig = {
  'iceServers': [{
    'urls': 'stun:stun.l.google.com:19302'
  }]
};


// Set up audio and video regardless of what devices are present.
var sdpConstraints = {
  offerToReceiveAudio: true,
  offerToReceiveVideo: true
};

/////////////////////////////////////////////

var room = 'foo';

// 서버에 바인딩 요청(connected 메시지 송신)
var socket = io.connect()

// 연결 후 첫 메시지
if (room !== '') {
  // create or join 메시지 서버에 전송
  socket.emit('create or join', room);
  console.log('Attempted to create or  join room', room);
}

// 첫 접속자일 경우 서버에서 이 메시지가 돌아옴.
socket.on('created', function(room) {
  console.log('Created room ' + room);
  isInitiator = true;
});

socket.on('full', function(room) {
  console.log('Room ' + room + ' is full');
});

// 방을 만든 후 누군가 접속한다면 join 메시지를 받음.
socket.on('join', function (room){
  console.log('Another peer made a request to join room ' + room);
  console.log('This peer is the initiator of room ' + room + '!');
  isChannelReady = true;
});

// 만들어진 방에 접속을 시도한다면, 이 메시지를 받음
socket.on('joined', function(room) {
  console.log('joined: ' + room);
  isChannelReady = true;
});

socket.on('log', function(array) {
  console.log.apply(console, array);
});

////////////////////////////////////////////////
// 서버를 이용해 상대에게 원하는 정보 전송
function sendMessage(message) {
  console.log('Client sending message: ', message);
  socket.emit('message', message);
}

// 서버측으로 부터 전달받은 상대방의 정보
socket.on('message', function(message) {
  console.log('Client received message:', message);
  if (message.type === 'got user media') { // got user media는 클라이언트 비디오가 준비 완료되면 발생
    maybeStart(message.socketId);
  } else if (message.type === 'offer') { // offer는 방 생성자가 보내는 것으로, 이걸 받은 사람은 방에 접속한 사람임.
    if (!isInitiator && !isStarted) { // 통신준비가 되었으면
      maybeStart(message.socketId);
    }
    pc.get(message.socketId).setRemoteDescription(new RTCSessionDescription(message)); // 상대의 SDP 등록
    doAnswer(message.socketId); // 상대에게 answer 전송
  } else if (message.type === 'answer' && isStarted) { // 누군가 접속하면 방 생성자가 받는 메시지
    pc.get(message.socketId).setRemoteDescription(new RTCSessionDescription(message)); // 상대의 SDP 등록
  } else if (message.type === 'candidate' && isStarted) { // iceCandidte 결과로 서로에게 전송하는 메시지.
    var candidate = new RTCIceCandidate({
      sdpMLineIndex: message.label,
      candidate: message.candidate
    });
    pc.get(message.socketId).addIceCandidate(candidate); // 참여자 정보 등록
  } else if (message.type === 'bye' && isStarted) {
    handleRemoteHangup(message.socketId);
  }
});

////////////////////////////////////////////////////
// 영상 및 오디오 속성 제어
const mediaOption = {
  // audio: true,
  video: true/*{
    mandatory: {
      maxWidth: 160,
      maxHeight: 120,
      maxFrameRate: 5,
    },
    // optional: [
    //   { googNoiseReduction: true }, // Likely removes the noise in the captured video stream at the expense of computational effort.
    //   { facingMode: 'user' }, // Select the front/user facing camera or the rear/environment facing camera if available (on Phone)
    // ],
  },*/
};

// 자신의 video태그
var localVideo = document.querySelector('#localVideo');
// var remoteVideo = document.querySelector('#remoteVideo');
// 상대방의 video태그들
var remoteVideo = new Map();

// 자신의 영상 준비
navigator.mediaDevices.getUserMedia(mediaOption)
.then(gotStream)
.catch(function(e) {
  alert('getUserMedia() error: ' + e.name);
});
// 정상적으로 불러왔으면 스트림 등록
function gotStream(stream) {
  console.log('Adding local stream.');
  localStream = stream;
  localVideo.srcObject = stream;
  // 영상 통신 준비가 되었다는 신호
  sendMessage('got user media');
  // 방 생성자만 이 코드가 실행됨
  if (isInitiator) {
    maybeStart();
  }
}

var constraints = {
  video: true
};

console.log('Getting user media with constraints', constraints);

/*if (location.hostname !== 'localhost') {
  requestTurn(
    'https://computeengineondemand.appspot.com/turn?username=41784574&key=4080218913'
  );
}*/

// 조건이 맞으면 코드 실행
function maybeStart(socketId) {
  console.log('>>>>>>> maybeStart() ', isStarted, localStream, isChannelReady);
  // 통신 대상이 있고, 자신의 영상이 준비 되었다면
  if (!isStarted && typeof localStream !== 'undefined' && isChannelReady) {
    console.log('>>>>>> creating peer connection');
    console.log(socketId)
    // 피어 생성(연결을 위한 정보)
    createPeerConnection(socketId);
    // 상대 클라이언트의 스트림 등록
    pc.get(socketId).addStream(localStream);
    isStarted = true;
    console.log('isInitiator', isInitiator);
    if (isInitiator) {
      doCall(socketId);
    }
    // isInitiator=true // 1:N 실험을 위해 추가
  }
}

window.onbeforeunload = function() {
  sendMessage('bye');
};

/////////////////////////////////////////////////////////
// 연결 정보 생성
function createPeerConnection(socketId) {
  try {
    if(!pc.has(socketId)){
        pc.set(socketId, new RTCPeerConnection(null))
    } 
    // pc.get(socketId) = new RTCPeerConnection(null);
    // addCandidate 시 발생
    pc.get(socketId).onicecandidate = handleIceCandidate;
    // addStream 시 발생
    pc.get(socketId).onaddstream = (param)=>handleRemoteStreamAdded(param, socketId);
    pc.get(socketId).onremovestream = handleRemoteStreamRemoved;
    console.log('Created RTCPeerConnnection');
  } catch (e) {
    console.log('Failed to create PeerConnection, exception: ' + e.message);
    alert('Cannot create RTCPeerConnection object.');
    return;
  }
}

function handleIceCandidate(event) {
  console.log('icecandidate event: ', event);
  // 내 정보 상대에게 전송
  if (event.candidate) {
    sendMessage({
      type: 'candidate',
      label: event.candidate.sdpMLineIndex,
      id: event.candidate.sdpMid,
      candidate: event.candidate.candidate
    });
  } else {
    console.log('End of candidates.');
  }
}

function handleCreateOfferError(event) {
  console.log('createOffer() error: ', event);
}

function doCall(socketId) {
  console.log('Sending offer to peer');
  // caller가 SDP를 만들어서 전송
  pc.get(socketId).createOffer((SDP)=>setLocalAndSendMessage(SDP, socketId), handleCreateOfferError);
}

function doAnswer(socketId) {
  console.log('Sending answer to peer.');
  // callee가 연결설정을 완료하기 위해 SDP를 만들어서 전송
  pc.get(socketId).createAnswer().then(
    (SDP)=>setLocalAndSendMessage(SDP, socketId),
    onCreateSessionDescriptionError
  );
}

// 시그널링 서버를 이용해 SDP 전송
function setLocalAndSendMessage(sessionDescription, socketId) {
  pc.get(socketId).setLocalDescription(sessionDescription);
  console.log('setLocalAndSendMessage sending message', sessionDescription);
  sendMessage(sessionDescription);
}

function onCreateSessionDescriptionError(error) {
  trace('Failed to create session description: ' + error.toString());
}

function requestTurn(turnURL) {
  var turnExists = false;
  for (var i in pcConfig.iceServers) {
    if (pcConfig.iceServers[i].urls.substr(0, 5) === 'turn:') {
      turnExists = true;
      turnReady = true;
      break;
    }
  }
  if (!turnExists) {
    console.log('Getting TURN server from ', turnURL);
    // No TURN server. Get one from computeengineondemand.appspot.com:
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var turnServer = JSON.parse(xhr.responseText);
        console.log('Got TURN server: ', turnServer);
        pcConfig.iceServers.push({
          'urls': 'turn:' + turnServer.username + '@' + turnServer.turn,
          'credential': turnServer.password
        });
        turnReady = true;
      }
    };
    xhr.open('GET', turnURL, true);
    xhr.send();
  }
}

// addStream 이벤트 핸들러
function handleRemoteStreamAdded(event, socketId) {
  console.log('Remote stream added.');
  // 상대방 소켓 아이디에 비디오 DOM 요소 매핑
  if(!remoteVideo.has(socketId)){
    const video = createVideoTag()
    remoteVideo.set(socketId, video)
  }
//   remoteStream = event.stream;
// 해당 비디오에 상대방 영상 스트림 등록
  remoteStream.set(socketId, event.stream)
  remoteVideo.get(socketId).srcObject = remoteStream.get(socketId);
//   remoteVideo.classList.add("remoteVideoInChatting");
//   localVideo.classList.add("localVideoInChatting");
}

function handleRemoteStreamRemoved(event) {
  console.log('Remote stream removed. Event: ', event);
}

function hangup() {
  console.log('Hanging up.');
  stop();
  sendMessage('bye');
}

function handleRemoteHangup(socketId) {
  remoteVideo.classList.remove("remoteVideoInChatting");
  localVideo.classList.remove("localVideoInChatting");
	
  console.log('Session terminated.');
  stop(socketId);
  isInitiator = false;
}

function stop(socketId) {
  isStarted = false;
  pc.get(socketId).close();
  pc.delete(socketId)
//   pc = null;
}