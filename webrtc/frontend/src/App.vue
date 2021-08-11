<template>
	<div id="main-container" class="container">	
		<div id="session" v-if="session">
			<div id="session-header">
				<h1 id="session-title">{{ mySessionId }}</h1>
			</div>
			<div id="video-container" class="col-md-6" >
				<user-video :stream-manager="publisher" @click.native="updateMainVideoStreamManager(publisher)"/>
				<user-video v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
			</div>
			<div v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub">
				<div v-if="JSON.parse(sub.stream.connection.data).clientData === 'Screen Sharing'">
					<user-video style="width:1280px; height:720px;" :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
				</div>
			</div>
		</div>
		<div class="menu-wrapper" id="menu-wrapper">
			<!-- 우하단 플로팅 메뉴 -->
			<div class="menu-opener" id="menu-opener-shadow" @click="showMenus">
				<!-- 그림자효과 -->
				<div class="menu-opener" id="menu-more">+</div>
			</div>
			<!-- 학생 리스트 -->
			<div class="menu-hide menu" id="menu-student-list" @click="showStudents"></div>
			<!-- 화면공유 -->
			<div class="menu-hide menu" id="menu-other" @click="startScreenSharing">+</div>
			<!-- 나가기 버튼 -->
			<div class="menu-hide menu" id="menu-exit" @click="leaveSession"></div>
		</div>
		<div class="student-hide" id="student-wrapper">
			<div class="student">
				<div class="student-profile"></div>
				<div class="student-name">박명수</div>
				<div class="student-function-wrapper">
					<div class="student-function" id="student-mute"></div>
					<div class="student-function" id="student-cam"></div>
					<div class="student-function" id="student-alert"></div>
				</div>
			</div>
			<div class="student" v-for="sub in subscribers" :key="sub.stream.connection.connectionId">
				<div class="student-profile"></div>
				<div class="student-name"> {{ JSON.parse(sub.stream.connection.data).clientData }} </div>
				<div class="student-function-wrapper">
					<div class="student-function" id="student-mute" @click="muteStudent(sub.stream.connection)"></div>
					<div class="student-function" id="student-cam"></div>
					<div class="student-function" id="student-alert" @click="makeMessage(sub.stream.connection)"></div>
				</div>
			</div>
		</div>
		<!-- 경고 메시지 수신창 -->
		<div class="alert-message-wrapper" v-if='alertMessage' @click="closeModal">
			<div class="alert-message-background"></div>
			<div class="alert-message-modal" >
				<div class="alert-message-title">선생님이 쪽지를 보냈어요</div>
				<div class="alert-message-content"> {{alertMessage}} </div>
			</div>
		</div>
		<!-- 경고 메시지 작성창 -->
		<div class="alert-message-write-wrapper no-drag" v-if="isAlertWriting">
			<div class="alert-message-write">
				<div class="alert-message-write-nav">
					<div class="alert-message-write-to">{{JSON.parse(alertTo.data).clientData}}</div><div class="alert-message-write-close" @click="closeWriter">X</div>
				</div>
				<div class="alert-message-write-foot">
					<div><textarea v-model="sendMessage" class="alert-message-write-content" placeholder="내용을 입력하세요."></textarea></div>
					<div class="alert-message-write-send" @click="alertStudent">전송</div>
				</div>
			</div>
		</div>
	</div>
	
	
</template>

<script>
import axios from 'axios';
import { OpenVidu } from 'openvidu-browser';
import UserVideo from './components/UserVideo';

axios.defaults.headers.post['Content-Type'] = 'application/json';

//const OPENVIDU_SERVER_URL = "https://" + location.hostname + ":4443";
const OPENVIDU_SERVER_URL = "https://" + "i5a205.p.ssafy.io";
const OPENVIDU_SERVER_SECRET = "1234";

export default {
	name: 'App',

	components: {
		UserVideo,
	},

	data () {
		return {
			OV: undefined,
			session: undefined,
			mainStreamManager: undefined,
			publisher: undefined,
			subscribers: [],

			// 화면 공유
			OVForScreenShare: undefined,
			sessionForScreenShare: undefined,
			mainStreamManager2: undefined,
			sharingPublisher: undefined,

			// 사용자 정보
			mySessionId: '0110121', // 학급 코드(0110121) 및 webRTC 룸 number
			myUserName: 'SSAFY' + Math.floor(Math.random() * 100), // 사용자 이름, webRTC 상에서 표시될 이름
			
			// 상태 관리 변수
			menu: false,			// 메뉴 오픈상태
			isScreenShared: false,	// 화면공유 상태
			isAlertWriting:false,	// 메시지 작성 상태
			muted: null,			// 음소거 상태 
			screenShareName: "Screen Sharing",	// 화면 공유 스트림의 이름
			alertMessage:"",	// 선생님에게서 도착한 메시지 내용
			sendMessage:"",		// 작성중인 메시지 내용
			alertTo:"",			// 마지막으로 메시지를 작성중이던 학생의 정보

			
		}
	},

	methods: {
		joinSession () {
			// --- Get an OpenVidu object ---
			this.OV = new OpenVidu();

			// --- Init a session ---
			this.session = this.OV.initSession();

			// --- Specify the actions when events take place in the session ---

			// On every new Stream received...
			this.session.on('streamCreated', ({ stream }) => {
				const subscriber = this.session.subscribe(stream);
				this.subscribers.push(subscriber);
			});

			// On every Stream destroyed...
			this.session.on('streamDestroyed', ({ stream }) => {
				const index = this.subscribers.indexOf(stream.streamManager, 0);
				if (index >= 0) {
					this.subscribers.splice(index, 1);
				}
			});

			// On alert from teacher to you
			this.session.on('signal:alert', (msg)=>{
				console.log(msg.data)
				this.alertMessage=msg.data;
			})

			// On request mute from teacher to you
			this.session.on('signal:mute', ()=>{
				// 음소거를 해제시킬 때는 학생에게 물어봄.
				if(this.muted) {
					this.requestCancleMuted();
					return;
				}
				// 음소거 시킬 때는 바로 마이크를 끔
				this.publisher.publishAudio(this.muted);
				this.muted=!this.muted;
			})

			// --- Connect to the session with a valid user token ---

			// 'getToken' method is simulating what your server-side should do.
			// 'token' parameter should be retrieved and returned by your own backend
			this.getToken(this.mySessionId).then(token => {
				this.session.connect(token, { clientData: this.myUserName })
					.then(() => {

						// --- Get your own camera stream with the desired properties ---

						let publisher = this.OV.initPublisher(undefined, {
							audioSource: undefined, // The source of audio. If undefined default microphone
							videoSource: undefined, // The source of video. If undefined default webcam
							publishAudio: true,  	// Whether you want to start publishing with your audio unmuted or not
							publishVideo: true,  	// Whether you want to start publishing with your video enabled or not
							resolution: '640x480',  // The resolution of your video
							frameRate: 30,			// The frame rate of your video
							insertMode: 'APPEND',	// How the video is inserted in the target element 'video-container'
							mirror: false       	// Whether to mirror your local video or not
						});

						this.mainStreamManager = publisher;
						this.publisher = publisher;

						// --- Publish your stream ---

						this.session.publish(this.publisher);
						// 선생님은 마이크 켜진상태, 학생은 꺼진 상태로 들어옴
						if(this.user.type===2) {
							this.publisher.publishAudio(false);
							this.muted=true;
						} else {
							this.muted=false;
						}
					})
					.catch(error => {
						console.log('There was an error connecting to the session:', error.code, error.message);
					});
			});

			window.addEventListener('beforeunload', this.leaveSession)
		},

		leaveSession () {
			// --- Leave the session by calling 'disconnect' method over the Session object ---
			if (this.session) this.session.disconnect();

			this.session = undefined;
			this.mainStreamManager = undefined;
			this.publisher = undefined;
			this.subscribers = [];
			this.OV = undefined;

			window.removeEventListener('beforeunload', this.leaveSession);
		},

		updateMainVideoStreamManager (stream) {
			if (this.mainStreamManager === stream) return;
			this.mainStreamManager = stream;
		},

		/**
		 * --------------------------
		 * SERVER-SIDE RESPONSIBILITY
		 * --------------------------
		 * These methods retrieve the mandatory user token from OpenVidu Server.
		 * This behavior MUST BE IN YOUR SERVER-SIDE IN PRODUCTION (by using
		 * the API REST, openvidu-java-client or openvidu-node-client):
		 *   1) Initialize a Session in OpenVidu Server	(POST /openvidu/api/sessions)
		 *   2) Create a Connection in OpenVidu Server (POST /openvidu/api/sessions/<SESSION_ID>/connection)
		 *   3) The Connection.token must be consumed in Session.connect() method
		 */

		getToken (mySessionId) {
			return this.createSession(mySessionId).then(sessionId => this.createToken(sessionId));
		},

		// See https://docs.openvidu.io/en/stable/reference-docs/REST-API/#post-openviduapisessions
		createSession (sessionId) {
			return new Promise((resolve, reject) => {
				axios
					.post(`${OPENVIDU_SERVER_URL}/openvidu/api/sessions`, JSON.stringify({
						customSessionId: sessionId,
					}), {
						auth: {
							username: 'OPENVIDUAPP',
							password: OPENVIDU_SERVER_SECRET,
						},
					})
					.then(response => response.data)
					.then(data => resolve(data.id))
					.catch(error => {
						if (error.response.status === 409) {
							resolve(sessionId);
						} else {
							console.warn(`No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}`);
							if (window.confirm(`No connection to OpenVidu Server. This may be a certificate error at ${OPENVIDU_SERVER_URL}\n\nClick OK to navigate and accept it. If no certificate warning is shown, then check that your OpenVidu Server is up and running at "${OPENVIDU_SERVER_URL}"`)) {
								location.assign(`${OPENVIDU_SERVER_URL}/accept-certificate`);
							}
							reject(error.response);
						}
					});
			});
		},

		// See https://docs.openvidu.io/en/stable/reference-docs/REST-API/#post-openviduapisessionsltsession_idgtconnection
		createToken (sessionId) {
			return new Promise((resolve, reject) => {
				axios
					.post(`${OPENVIDU_SERVER_URL}/openvidu/api/sessions/${sessionId}/connection`, {}, {
						auth: {
							username: 'OPENVIDUAPP',
							password: OPENVIDU_SERVER_SECRET,
						},
					})
					.then(response => response.data)
					.then(data => resolve(data.token))
					.catch(error => reject(error.response));
			});
		},

		openMenu () {
			const menus = document.getElementsByClassName("menu");
			menus.forEach(menu => menu.classList.toggle("menu-hide"));
		},

		showMenus () {
			const more = document.getElementById("menu-more");
			more.classList.toggle("rotate-menu");
			this.openMenu();
		},

		showStudents () {
			this.subscribers.forEach(student=>{
				console.log(student.stream.connection.data["clientData"])
			});
			this.showMenus() // 메뉴 선택 후 메뉴상자 닫기
			// 화면 변경
			const studentList = document.getElementById("student-wrapper")
			studentList.classList.toggle("student-hide");	// 학생 목록 창 열기
			document.getElementById("menu-wrapper").classList.toggle("menu-move")	// 왼쪽으로 메뉴 밈
		},

		muteStudent (connection) {
			const studentConnectionId = connection.connectionId;
			const studentName = JSON.parse(connection.data).clientData;

			this.session.signal({
				data: "",  // 내용
				to: [connection],		// 상대방 정보(connection으로 전송)
				type: 'mute'			// 소켓 메시지 제목
			})
			.then(() => {
				console.log('mute request successfully sent');
			})
			.catch(error => {
				console.error(error);
			});

			console.log(studentConnectionId, studentName);
		},
		
		makeMessage (connection) {
			// 메시지 작성 창 열기
			this.alertTo = connection;
			this.isAlertWriting=true;
		},

		alertStudent () {
			if(!this.sendMessage) {
				alert("메시지 내용이 없습니다.");
				return;
			}

			this.session.signal({
				data: this.sendMessage,  // Any string (optional)
				to: [this.alertTo],                     // Array of Connection objects (optional. Broadcast to everyone if empty)
				type: 'alert'             // The type of message (optional)
			})
			.then(() => {
				console.log('alert successfully sent');
			})
			.catch(error => {
				console.error(error);
			});

			// 메시지 작성 창 닫기
			this.isAlertWriting=false;
			this.sendMessage="";
		},

		startScreenSharing () {
			this.OVForScreenShare = new OpenVidu();

			this.sessionForScreenShare = this.OVForScreenShare.initSession();

			var mySessionId = this.mySessionId;
			this.getToken(mySessionId).then(token => {
				this.sessionForScreenShare.connect(token, { clientData: this.screenShareName })
				.then(() => {
					let publisher = this.OVForScreenShare.initPublisher("sharingvideo", {
						audioSource: false,
						videoSource: "screen",      
                        publishVideo: true,  
						resolution: "1920x1980",
						frameRate: 10,           
                        insertMode: 'APPEND',    
                        mirror: false        
					});
					console.log("publisher",publisher);
					publisher.once('accessAllowed', () => {
						try {
							console.log("subscriber >>>>> ", this.subscribers);
							this.isScreenShared=true;
							publisher.stream.getMediaStream().getVideoTracks()[0].addEventListener('ended', () => {
								console.log('User pressed the "Stop sharing" button');
								this.leaveSessionForScreenSharing()
								this.isScreenShared=false;
							});					
						} catch (error) {
							console.error('Error applying constraints: ', error);
						}
					});

					publisher.once('accessDenied', () => { 
						console.warn('ScreenShare: Access Denied');
					});

					this.mainStreamManager2 = publisher;
                    this.sharingPublisher = publisher;

                    this.sessionForScreenShare.publish(this.sharingPublisher);

				}).catch((error => {

					console.warn('There was an error connecting to the session:', error.code, error.message);

				}));
			});

			window.addEventListener('beforeunload', this.leaveSessionForScreenSharing)
		},

		leaveSessionForScreenSharing () {
			if (this.sessionForScreenShare) this.sessionForScreenShare.disconnect();

            this.sessionForScreenShare = undefined;
            this.mainStreamManager2 = undefined;
            this.sharingPublisher = undefined;
            this.OVForScreenShare = undefined;

            window.removeEventListener('beforeunload', this.leaveSessionForScreenSharing);
		},
		
		closeModal () {
			this.alertMessage="";
		},

		closeWriter () {
			this.isAlertWriting=false;
		},
		
		requestCancleMuted () {
			const res = confirm("마이크를 킬까요?");	// 포커스가 있는 상태에서만 동작, 아니면 무조건 false 반환

			if(res) {
				this.publisher.publishAudio(true);
				this.muted = !this.muted;
			}
		},
	},

	created() {
		// 접속 시 바로 연결설정 시작.
		this.joinSession()
		// console.log(opener)
		
		// var child = window.open("https://localhost:8080");
		// const user={
		// 	name:"조동윤",
		// 	id:"Token",
		// 	type:"2"
		// }
		// window.ABC = user;
		// child.ABCD = user;
		// 이미지 preload
		document.createElement("img").src = "resources/images/memo2.png"
	}
}
</script>
