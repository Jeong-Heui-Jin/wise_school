<template>
	<div id="main-container" class="container">	
		<!-- 학생 리스트 창 -->
		<!-- <div class="student-hide no-drag" id="student-wrapper"> -->
		<div class="no-drag" id="student-wrapper">
			<div class="side-wrapper">
				<div id="logo">
					<img src="../public/resources/images/logo.png" alt="">
				</div>
				<div id="clock">
					<div id="noon"></div>
					<div id="time"></div>
				</div>
				<!-- 다른 사람 계정. -->
				<!-- <div v-for="sub in subscribers" :key="sub.stream.connection.connectionId">
					<div class="student" v-if="JSON.parse(sub.stream.connection.data).clientData !== 'Screen Sharing'">
						<div class="student-profile"></div>
						<div class="student-name"> {{ JSON.parse(sub.stream.connection.data).clientData }} </div>
						<div class="student-function-wrapper">
							<div class="student-function" id="student-mute" @click="muteStudent(sub.stream.connection)">
								<img src="../public/resources/images/unmute.png" alt="" v-if="sub.muted">
								<img src="../public/resources/images/mute.png" alt="" v-else>
							</div>
							<div class="student-function student-hand-up-clicked" id="student-hand-up" @click="downHand(sub)" v-if="sub.handUp">
								<img src="../public/resources/images/hand_up.png" alt="">
							</div>
							<div class="student-function" id="student-hand-up" @click="downHand(sub)" v-else>
								<img src="../public/resources/images/hand_up.png" alt="">
							</div>
							<div class="student-function" id="student-alert" @click="makeMessage(sub.stream.connection)">
								<img src="../public/resources/images/chat.png" alt="">
							</div>
						</div>
					</div>
				</div> -->
			</div>
			<!-- 나가기 버튼 -->
			<div class="exit" @click="leaveSession">
				<img id="exit" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.226065.png" alt="">
			</div>
		</div>

		<div class="no-drag" id="session" v-if="session">
			<div id="session-header">
				<div class="session-title">
					화목한 {{ mySessionId }}반
					<div class="session-personel">
						<div class="session-personel-image"><img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.084093.png" alt=""></div>
						<div id="session-count">{{count}} </div>
					</div>
				</div>
				<div class="my-function">
					<div class="function" id="mic" @click="muteMyVoice">
						<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.942401.png" alt="" v-if="!muted">
						<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:20.017923.png" alt="" v-else>
					</div>
					<!-- 화면공유 -->														
					<div class="function" id="screen-sharing" @click="startScreenSharing">
						<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.311077.png" alt="">
					</div>
					<div class="function" id="hand-up" @click="raiseMyHand">
						<!-- 라임색 손들기 아이콘 -->
						<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.824859.png" alt="" v-if="handUp">
						<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.115793.png" alt="" v-else>
					</div>
				</div>
				<div class="session-title"></div>
			</div>
			<div id="video-container" v-if="isScreenShared">
				<!-- <user-video :stream-manager="teacher" @click.native="updateMainVideoStreamManager(teacher)" v-if="teacher"/> -->
				<div class="video-wrapper" style="width:100%;">
					<div class="user-video-wrapper" id="user-video-wrapper" style="left:0;">
						<user-video id="my-video" style="width:10%;" :stream-manager="publisher" @click.native="updateMainVideoStreamManager(publisher)"/>
						<div id="user-video-while-shared" style="width:10%;" v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub">
							<div class="test" v-if="JSON.parse(sub.stream.connection.data).clientData !== 'Screen Sharing'">
								<user-video :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
							</div>
						</div>
					</div>
					<div style="width:100%;" v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub">
						<div class="video-screen-sharing" v-if="JSON.parse(sub.stream.connection.data).clientData === 'Screen Sharing'">
							<user-video style="width: 100%; " :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
						</div>
					</div>
				</div>
			</div>
			<div id="video-container" v-else>
				<!-- <user-video :stream-manager="teacher" @click.native="updateMainVideoStreamManager(teacher)" v-if="teacher"/> -->
				<div class="user-video" style="" >
					<user-video id="my-video" :stream-manager="publisher" @click.native="updateMainVideoStreamManager(publisher)"/>
				</div>
				
				<div class="user-video" id="user-video" style="width:30%;" v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub">
					<div class="test">
						<user-video :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
						<div class="video-function">
							<div class="student-function" id="student-mute" @click="muteStudent(sub.stream.connection)">
								<img style="width:25px; height:25px;" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.359956.png" alt="" v-if="sub.muted">
								<img style="width:25px; height:25px;" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.186597.png" alt="" v-else>
							</div>
							<div class="student-function student-hand-up-clicked" id="student-hand-up" @click="downHand(sub)" v-if="sub.handUp">
								<img style="width:25px; height:25px;" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.792856.png" alt="">
							</div>
							<div class="student-function" id="student-hand-up" @click="downHand(sub)" v-else>
								<img style="width:25px; height:25px;" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.792856.png" alt="">
							</div>
							<div class="student-function" id="student-alert" @click="makeMessage(sub.stream.connection)">
								<img style="width:25px; height:25px;" src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.727092.png" alt="">
							</div>
						</div>
					</div>
				</div>
			</div>
			<div id="btn-left" v-if="count>16">
				<div class="btn-move" @click="move(-1)">
					<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:12.914434.png" alt="">
				</div>
			</div>
			<div id="btn-right" v-if="count>16">
				<div class="btn-move" @click="move(1)">
					<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.008388.png" alt="">
				</div>
			</div>
		</div>
		
		<!-- 경고 메시지 수신창 -->
		<div class="alert-message-wrapper" v-if='alertMessage' @click="closeModal">
			<div class="alert-message-background"></div>
			<div class="alert-message-modal" >
				<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2010:47:19.882288.png" alt="">
				<div class="alert-message-title">{{receivedFrom}}님이 쪽지를 보냈어요</div>
				<div class="alert-message-content"> {{alertMessage}} </div>
			</div>
		</div>
		<!-- 경고 메시지 작성창 -->
		<div class="alert-message-write-wrapper no-drag" v-if="isAlertWriting">
			<div class="alert-message-write">
				<div class="alert-message-write-nav">
					<img src="http://dycho96.s3.ap-northeast-2.amazonaws.com/2021-08-2011:04:13.048204.png" alt="">
					<div class="alert-message-write-to">{{alertTo}}</div><div class="alert-message-write-close" @click="closeWriter">X</div>
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
			myUserType: '2',			// 사용자 등급. 관리자 선생님 학생

			// 상태 관리 변수
			menu: false,			// 메뉴 오픈상태
			isScreenShared: false,	// 화면공유 상태
			isAlertWriting:false,	// 메시지 작성 상태
			muted: false,			// 음소거 상태 
			handUp: false,			// 손들기 상태
			screenShareName: "Screen Sharing",	// 화면 공유 스트림의 이름
			receivedFrom:"",		// 메시지 작성자
			alertMessage:"",	// 선생님에게서 도착한 메시지 내용
			sendMessage:"",		// 작성중인 메시지 내용
			target:"",			// 마지막으로 메시지를 작성중이던 학생의 정보
			alertTo:"",			// 메시지를 받을 학생 이름
			attendanceValue: {  // 학생 출석체크 상태 정보
				status:"",
				student_id:"4",
				classroom_id:"1"
			},
			teacher:"",
			count:1,			// 현재 방 인원
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
				subscriber.muted = JSON.parse(subscriber.stream.connection.data).clientVoice
				subscriber.handUp = false;
				if(JSON.parse(subscriber.stream.connection.data).clientType==="1") {
					this.teacher=subscriber;
				}
				this.subscribers.push(subscriber);

				this.checkScreenShared();
				this.sessionCount();
				document.getElementById("session-count").innerHTML = this.count;
				// if (this.isScreenShared) {
				// 	this.session.signal({
				// 		data: "",
				// 		to: [subscriber.stream.connection],
				// 		type: 'startScreenSharing'
				// 	})
				// }
			});

			// On every Stream destroyed...
			this.session.on('streamDestroyed', ({ stream }) => {
				const index = this.subscribers.indexOf(stream.streamManager, 0);
				if (index >= 0) {
					this.subscribers.splice(index, 1);
				}

				this.checkScreenShared();
				this.sessionCount();
				document.getElementById("session-count").innerHTML = this.count;
			});

			// On alert from teacher to you
			this.session.on('signal:alert', (msg)=>{
				if(msg.from.connectionId !== this.publisher.stream.connection.connectionId) {
					this.alertMessage=msg.data;
					this.receivedFrom = JSON.parse(msg.from.stream.connection.data).clientData;			
				}
			})

			// On request mute from teacher to you
			this.session.on('signal:muteRequest', ()=>{
				// 음소거를 해제시킬 때는 학생에게 물어봄.
				if(this.muted) {
					this.requestCancleMuted();
					return;
				}
				// 음소거 시킬 때는 바로 마이크를 끔
				this.muteMyVoice();
			})

			// On someone mute own voice
			this.session.on('signal:mute', (msg)=>{				
				const data = JSON.parse(msg.data);
				console.log(msg)
				// console.log(data);
				this.subscribers.forEach((sub)=>{
					if(data.connectionId === sub.stream.connection.connectionId) {
						sub.muted = data.muted;
					}
				})
			})

			// On someone raise hand
			this.session.on('signal:handUp', (msg)=>{				
				this.subscribers.forEach((sub)=>{
					if(msg.from.connectionId === sub.stream.connection.connectionId) {
						sub.handUp = msg.data==='true'?true:false;
					}
				})
			})

			// On request down hand from teacher to you
			this.session.on('signal:handDown', ()=>{
				this.raiseMyHand();
			})

			// On start screen share
			this.session.on('signal:startScreenSharing', ()=>{
				this.isScreenShared = true;
			})

			// On stop screen share
			this.session.on('signal:stopScreenSharing', ()=>{
				this.isScreenShared = false;
			})

			if (window.user) {
				this.myUserName= window.user.userName;
				this.mySessionId = String(window.user.classroom);
				this.myUserType = String(window.user.userType);
			}

			// --- Connect to the session with a valid user token ---

			if (this.myUserType==='2') {
				this.muted = !this.muted;
			}

			// 'getToken' method is simulating what your server-side should do.
			// 'token' parameter should be retrieved and returned by your own backend
			this.getToken(this.mySessionId).then(token => {
				this.session.connect(token, { clientData: this.myUserName, clientType: this.myUserType, clientVoice: this.muted, })
					.then(() => {

						// --- Get your own camera stream with the desired properties ---
						// var width = screen.availWidth;
						// var height = screen.availHeight*0.9;

						let publisher = this.OV.initPublisher(undefined, {
							audioSource: undefined, // The source of audio. If undefined default microphone
							videoSource: undefined, // The source of video. If undefined default webcam
							publishAudio: true,  	// Whether you want to start publishing with your audio unmuted or not
							publishVideo: true,  	// Whether you want to start publishing with your video enabled or not
							// resolution: '640x480',  // The resolution of your video
							// resolution: `${width}x${height}`,  // The resolution of your video
							resolution: '1280x648',  // The resolution of your video
							frameRate: 30,			// The frame rate of your video
							insertMode: 'APPEND',	// How the video is inserted in the target element 'video-container'
							mirror: false       	// Whether to mirror your local video or not
						});

						this.mainStreamManager = publisher;
						this.publisher = publisher;

						// --- Publish your stream ---

						this.session.publish(this.publisher)
						.then(()=>{
							if(this.myUserType==="2") { 
								publisher.publishAudio(false);	// 학생은 마이크 꺼진 상태로 들어옴
								// this.getAttendanceStatus();		// 학생 출석체크
						}
						});

						// // 선생님은 마이크 켜진상태, 학생은 꺼진 상태로 들어옴
						// if(this.myUserType==="2") {
						// 	// 마이크 불러오는 타이밍을 감안해서 2초 후 작동
						// 	setTimeout(()=>publisher.publishAudio(false), 2000);
						// }
					})
					.catch(error => {
						console.log('There was an error connecting to the session:', error.code, error.message);
					});
			});

			window.addEventListener('beforeunload', this.leaveSession)
		},

		leaveSession () {
			// --- Leave the session by calling 'disconnect' method over the Session object ---;
			if (this.session) this.session.disconnect()

			this.session = undefined;
			this.mainStreamManager = undefined;
			this.publisher = undefined;
			this.subscribers = [];
			this.OV = undefined;

			window.removeEventListener('beforeunload', this.leaveSession);
			(()=>{
				console.log("@@@@@@@@")
				window.opener.postMessage({
					msgType: "leave_class",
				},"http://i5a205.p.ssafy.io:8081");
			})();
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
			this.session.signal({
				data: "",  // 내용
				to: [connection],		// 상대방 정보(connection으로 전송)
				type: 'muteRequest'			// 소켓 메시지 제목
			})
			.then(() => {
				console.log('mute request successfully sent');
			})
			.catch(error => {
				console.error(error);
			});
		},
		
		makeMessage (connection) {
			// 메시지 작성 창 열기
			this.target=connection;

			if (this.target==null) {
				this.alertTo = "ALL";
				this.target="";
			} else {
				this.alertTo = JSON.parse(connection.data).clientData;
			}

			this.isAlertWriting=true;
		},

		alertStudent () {
			if(!this.sendMessage) {
				alert("메시지 내용이 없습니다.");
				return;
			}

			this.session.signal({
				data: this.sendMessage,  // Any string (optional)
				to: [this.target],                     // Array of Connection objects (optional. Broadcast to everyone if empty)
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
							this.session.signal({
								data: JSON.stringify(status),  // Any string (optional)
								to: [],
								type: 'startScreenSharing'             // The type of message (optional)
							})
							publisher.stream.getMediaStream().getVideoTracks()[0].addEventListener('ended', () => {
								console.log('User pressed the "Stop sharing" button');
								this.session.signal({
									data: JSON.stringify(status),  // Any string (optional)
									to: [],
									type: 'stopScreenSharing'             // The type of message (optional)
								})
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

		muteMyVoice () {
			this.publisher.publishAudio(this.muted);
			this.muted = !this.muted;
			if(!this.muted) {
				document.getElementById("mic").classList.add("function-clicked")
			} else {
				document.getElementById("mic").classList.remove("function-clicked")
			}
				

			const status = {
				connectionId: this.publisher.stream.connection.connectionId,
				muted: this.muted,
			}
			
			this.session.signal({
				data: JSON.stringify(status),  // Any string (optional)
				to: [],
				type: 'mute'             // The type of message (optional)
			})
			.then(() => {
				console.log('Message successfully sent');
			})
			.catch(error => {
				console.error(error);
			});
		},
		
		requestCancleMuted () {
			const res = confirm("마이크를 킬까요?");	// 포커스가 있는 상태에서만 동작, 아니면 무조건 false 반환

			if(res) {
				this.muteMyVoice();
			}
		},

		raiseMyHand () {
			// alert("손을 들었습니다.")
			document.getElementById("hand-up").classList.toggle("function-clicked");
			this.handUp = !this.handUp;

			this.session.signal({
				data: `${this.handUp}`,  // Any string (optional)
				to: [],
				type: 'handUp'             // The type of message (optional)
			})
		},

		downHand (sub) {
			// alert("손을 내렸습니다.")
			if(sub.handUp) {
				this.session.signal({
					data: "",  // Any string (optional)
					to: [sub.stream.connection],
					type: 'handDown'             // The type of message (optional)
				})
			}
		},

		getAttendanceStatus() {
			// console.log("출석체크");
			const now_at = new Date();
			let hour = now_at.getHours();
			let minutes = now_at.getMinutes();

			if (hour===9 && 0<=minutes<=10) {
				this.attendanceValue.status = "출석";	
			} else  {
				this.attendanceValue.status = "지각";
			} 
			// console.log("출석", this.attendanceValue);
			axios({
				method: "post",
				url: "http://i5a205.p.ssafy.io:8000/student-manage/attendance/",
				data: this.attendanceValue,
				headers: localStorage.getItem("jwt")})
			.then((res) => {
				// console.log("성공");
				console.log(res, "success postAttendance");
			})
			.catch((err) => {
				// console.log("실패");
				console.log(err);
			});
			
		},

		clock () {
			var currentDate = new Date();	// 현재시간
			
			var h = currentDate.getHours();
			var amPm = '오전';
			if(h >= 12){
				amPm = '오후';
				h = h==12? h.toString() : this.addZeros(h - 12);
			} else {
				h = this.addZeros(h);
			}
			var m = this.addZeros(currentDate.getMinutes() ,2);
			var s =  this.addZeros(currentDate.getSeconds(),2);
			
			document.getElementById('noon').innerHTML = amPm;
			document.getElementById('time').innerHTML = h+":"+m+":"+s;
		},

		addZeros (num) { // 자릿수 맞춰주기
			num = num.toString();
			return num.length < 2 ? "0"+num : num;
		},

		sessionCount () {
			var buf = 1
			this.subscribers.forEach((sub)=>{
				if(JSON.parse(sub.stream.connection.data).clientData!=="Screen Sharing") {
					buf +=1;
				}
			})
			this.count = buf;
			
			setTimeout(()=>{
				if(this.count == 1) {
					document.getElementsByClassName('user-video').forEach((video)=>{
						video.style.width=""
					});
				}
				else if(this.count<=4){
					document.getElementsByClassName('user-video').forEach((video)=>{
						video.style.width="50%"
					});
					document.getElementsByClassName('video-function').forEach((video)=>{
						video.style.width="50%"
					});
				} else if(this.count<=9){
					document.getElementsByClassName('user-video').forEach((video)=>{
						video.style.width="33%"
					});
					document.getElementsByClassName('video-function').forEach((video)=>{
						video.style.width="33%"
					});
				} else {
					document.getElementsByClassName('user-video').forEach((video)=>{
						video.style.width="24.5%"
					});
					document.getElementsByClassName('video-function').forEach((video)=>{
						video.style.width="24.5%"
					});
				}
			},500)
		},

		move (ny) {
			const videos = document.getElementById("video-container");
			const videoHeight = document.getElementsByClassName('video-stream')[0].offsetHeight;
			var y = Number(videos.style.top.slice(0,-2)) + videoHeight*ny;
			const diff = videoHeight - videos.offsetHeight;

			if (y > 0) y = 0;
			if (y< diff ) y = diff;

			videos.style.top=y;
		},

		checkScreenShared () {
			var buf = 0;
			this.subscribers.forEach((sub)=>{
				if(JSON.parse(sub.stream.connection.data).clientData==="Screen Sharing") {
					buf+=1;
				}
			});
			if (buf) {
				this.isScreenShared=true;
			} else {
				this.isScreenShared = false;
			}
		},
	},

	created() {
		setInterval(this.clock,1000);
		
		if (!window.opener) { // 직접 주소를 사용해서 들어왔을 때
			this.joinSession();
		} else {		// 학사 페이지를 통해 들어왔을 때

			window.timer=setTimeout(()=>{			// 응답 없을 시 창 종료
				alert("연결 상태가 좋지 않습니다. 다시 시도해주세요!");

				window.opener.postMessage({
					msgType: "connection_fail",
				// },"http://localhost:8080");
				},"http://i5a205.p.ssafy.io:8081");
			}, 2000);

			window.joinSession = this.joinSession;	// window 객체에 함수 연결
			window.addEventListener('message', function(e) {

				if (e.data.msgType === "init_classroom") {
					clearTimeout(window.timer);		// 타이머 종료
						window.opener.postMessage({
						msgType: "connect",
					// },"http://localhost:8080");
					},"http://i5a205.p.ssafy.io:8081");

					window.user=e.data;
					localStorage.setItem('jwt', e.data.userToken);
					window.joinSession();	// 데이터 수신 시 연결설정 시작.
				}
			});
		}
	}
}
</script>
