'use strict';

var os = require('os');
var nodeStatic = require('node-static');
//var http = require('http');
var socketIO = require('socket.io')();

// 동영상 퍼미션을 위해 ssl 통신이 필요.
const https = require('https');
// 파일 서버 구현 위함.
const fs = require('fs');
// ssl 통신을 위한 인증서
const options = {
    key: fs.readFileSync('./keys/private.pem'),
    cert: fs.readFileSync('./keys/public.pem')
};

// 이부분은 아마 keys 폴더를 포함하지 않게 수정해야할 것 같음
var fileServer = new(nodeStatic.Server)();
let app = https.createServer(options, (req, res) => {
    fileServer.serve(req, res);
}).listen(8081);

console.log('Started chating server...');

// 연결 요청 대기 상태
var io = socketIO.listen(app);
// (socket.io).on("A", B) : 다른 곳에서 소켓을 통해 A 메시지를 날리면, B 콜백함수 실행하는 구조
// connection 메시지는 소켓이 바인드되면 자동으로 날리는 메시지임.
io.sockets.on('connection', function (socket) {

    // 클라이언트 측에 로그 메시지를 전송하기 위한 코드.
    function log() {
        var array = ['Message from server:'];
        // 파라미터로 넘어온 인자들을 arr와 합침
        array.push.apply(array, arguments);
        // io.emit을 하면 전체 전송이 되고, socket.emit을 하면 대상 클라이언트에게 1:1로 메시지를 보냄.
        // 서버를 호출한 대상 클라이언트에게 log 메시지와 파라미터로 array를 전송
        socket.emit('log', array);
    }

    // 클라이언트에서 message로 메시지를 보냈을 때 처리코드
    socket.on('message', function (message) {
        log('Client said: ', message);

        // 연결 종료 시 bye 메시지를 보내게 구현할 것이고, 그때만 동작하는 코드
        if (message === "bye" && socket.rooms['foo']) {
            io.of('/').in('foo').clients((error, socketIds) => {
                if (error) throw error;

                socketIds.forEach(socketId => {
                    //	if (socket.id===socketId) console.log('-------------------************');
                    //			else socket.broadcast.emit('message', message);
                    io.sockets.sockets[socketId].leave('foo');
                });

            });
        } //else {
        // for a real app, would be room-only (not broadcast)
        // 대부분 여기로 분기
        // 클라이언트가 접속해서 자신의 영상이 준비되면 이 메시지를 전송함.
        // 상대편의 소켓 id를 전송해야해서 모두 집어넣음
        if (message === "got user media") {
            var buf = {
                type: message,
                socketId: socket.id
            }
            message = buf;
        }
        if (message === "bye") {
            var buf = {
                type: message,
                socketId: socket.id
            }
            message = buf;
        }
        if (message.type === 'offer') {
            message.socketId = socket.id;
        }
        if (message.type === 'answer') {
            message.socketId = socket.id;
        }
        if (message.type === 'candidate') {
            message.socketId = socket.id;
        }
        // 호출한 클라이언트를 제외한 모든 클라이언트에게 송신
        socket.broadcast.emit('message', message);

    });

    // 처음 페이지를 키면 클라이언트가 보내는 메시지.
    socket.on('create or join', function (room) {
        log('Received request to create or join room ' + room);

        // room 이름으로 생성된 방이 있는지 검색.
        // io.sockets.adapter 내에는 접속자들, 생성된 룸들이 맵으로 정의되어 있음.
        var clientsInRoom = io.sockets.adapter.rooms.get(room);
        // console.log(io.sockets.adapter)
        // console.log(clientsInRoom)
        // 방이 있으면 방 안의 사람 수, 없으면 0
        var numClients = clientsInRoom ? clientsInRoom.size : 0;
        log('Room ' + room + ' now has ' + numClients + ' client(s)');

        // 첫 접속자일 경우(방 생성)
        if (numClients === 0) {
            // room 생성 및 접속
            socket.join(room);

            // console.log(clientsInRoom)
            // console.log("@@@@@@@@")
            // console.log(io.sockets.adapter.rooms.get('foo'))
            // console.log(io.sockets.adapter.rooms.get('foo').size)

            // // 방에 접속한 모든 소켓들의 id 출력.
            // io.sockets.adapter.rooms.get('foo').forEach(i => console.log(i))

            log('Client ID ' + socket.id + ' created room ' + room);
            // 클라이언트에게 created 메시지 (방을 성공적으로 만들었다는 시그널) 반환, room과 본인 소켓 id 돌려줌
            socket.emit('created', room, socket.id);
            console.log('created');
        } else if (numClients >= 1) { // 최초 생성자가 아닌 경우 분기
            log('Client ID ' + socket.id + ' joined room ' + room);
            // room 내 모든 사람에게 join 메시지 (누군가 접속했다는 시그널) 전송
            io.sockets.in(room).emit('join', room);
            // 만들어져있는 room에 접속
            socket.join(room);
            // 클라이언트에게 joined 메시지 (room에 접속했다는 확인 시그널) 전송
            socket.emit('joined', room, socket.id);
            // 아직 활용하지 않은 메시지
            io.sockets.in(room).emit('ready');
            console.log('joined');
        } /*else if (numClients>1){
            // log('Client ID ' + socket.id + ' joined room ' + room);
            socket.emit('many')
        }*/ else { // 방이 가득찼다면
            socket.emit('full', room);
        }
    });
    // 서버의 ip 주소 확인 코드
    socket.on('ipaddr', function () {
        var ifaces = os.networkInterfaces();
        for (var dev in ifaces) {
            ifaces[dev].forEach(function (details) {
                if (details.family === 'IPv4' && details.address !== '127.0.0.1') {
                    socket.emit('ipaddr', details.address);
                }
            });
        }
    });

    // 소켓 연결해제 시 자동으로 호출
    socket.on('disconnect', ()=>{
        // log('Received request to disconnect room ' + room);
        console.log(`client ${socket.id} is quit`)
    })

    // 클라이언트와 연결해제 잘 해보려고 만들었는데 아직 안 씀
    socket.on('bye', function () {
        console.log('received bye');
    });

});
