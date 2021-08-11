<template>
	<div id="main-container" class="container">
		<!-- <div id="join" v-if="!session">
			<div id="img-div"><img src="resources/images/openvidu_grey_bg_transp_cropped.png" /></div>
			<div id="join-dialog" class="jumbotron vertical-center">
				<h1>Join a video session</h1>
				<div class="form-group">
					<p>
						<label>Participant</label>
						<input v-model="myUserName" class="form-control" type="text" required>
					</p>
					<p>
						<label>Session</label>
						<input v-model="mySessionId" class="form-control" type="text" required>
					</p>
					<p class="text-center">
						<button class="btn btn-lg btn-success" @click="joinSession()">Join!</button>
					</p>
				</div>
			</div>
		</div> -->
		

		<div id="session" v-if="session">
			<div id="session-header">
				<h1 id="session-title">{{ mySessionId }}</h1>
				
			</div>
			<!-- <div id="main-video" class="col-md-6">
				<user-video :stream-manager="mainStreamManager"/>
			</div> -->
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
			<div class="menu-opener" id="menu-opener-shadow" @click="showMenus">
				<!-- 그림자효과 -->
				<div class="menu-opener" id="menu-more">+</div>
			</div>
			<div class="menu-hide menu" id="menu-student-list" @click="showStudents"></div>

			<!-- 화면공유 -->
			<div class="menu-hide menu" id="menu-other" @click="startScreenSharing">+</div>

			<!-- 나가기 버튼 -->
			<div class="menu-hide menu" id="menu-exit" @click="leaveSession"></div>
			<!-- <input v-if="menu" class="btn btn-large btn-danger" type="button" id="buttonLeaveSession" @click="leaveSession" value="Leave session"> -->
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
					<div class="student-function" id="student-alert" @click="alertStudent(sub.stream.connection)"></div>
				</div>
			</div>
			<!-- <div class="student-wrapper1"></div>
			<div class="student-wrapper2"></div>
			<div class="student-wrapper3"></div> -->
		</div>

		<!-- <div id="sharingvideo" style="width:1280px; height:720px;" v-if="isScreenShared" background-color="grey">
			<user-video v-for="sub in subscribers" :key="sub.stream.connection.connectionId" :stream-manager="sub" @click.native="updateMainVideoStreamManager(sub)"/>
		</div> -->

	</div>
	
	
</template>

<script>
import axios from 'axios';
import { OpenVidu } from 'openvidu-browser';
import UserVideo from './components/UserVideo';

axios.defaults.headers.post['Content-Type'] = 'application/json';

//const OPENVIDU_SERVER_URL = "https://" + location.hostname + ":4443";
const OPENVIDU_SERVER_URL = "https://" + "i5a205.p.ssafy.io";
//console.log(location.hostname)
//const OPENVIDU_SERVER_SECRET = "MY_SECRET";
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

			// 학급코드 (X반)
			mySessionId: '0110121',
			// 사용자 이름 (조싸피)
			myUserName: 'SSAFY' + Math.floor(Math.random() * 100),
			// 메뉴 오픈상태
			menu: false,
			// 화면공유 상태
			isScreenShared: false,
			screenShareName: "Screen Sharing"
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
			var students = []
			this.subscribers.forEach(student=>{
				console.log(student.stream.connection.data["clientData"])
			});
			students
			// console.log('Me:')
			console.log(JSON.parse(this.publisher.stream.connection.data))
			this.showMenus()
			const studentList = document.getElementById("student-wrapper")
			console.log(studentList.classList);
			// 학생 목록 창 열기
			studentList.classList.toggle("student-hide");
			// 왼쪽으로 메뉴 밈
			document.getElementById("menu-wrapper").classList.toggle("menu-move")
		},

		muteStudent (connection) {
			const studentConnectionId = connection.connectionId;
			const studentName = JSON.parse(connection.data).clientData;

			console.log(studentConnectionId, studentName);
		},
		
		alertStudent (connection) {
			const studentName = JSON.parse(connection.data).clientData;
			this.session.signal({
				data: `야 ${studentName} 집중해!!!!`,  // Any string (optional)
				to: [connection],                     // Array of Connection objects (optional. Broadcast to everyone if empty)
				type: 'alert'             // The type of message (optional)
			})
			.then(() => {
				console.log('alert successfully sent');
			})
			.catch(error => {
				console.error(error);
			});
		},

		startScreenSharing () {
			this.OVForScreenShare = new OpenVidu();
			// this.OVForScreenShare.setAdvancedConfiguration(
			// 	{ screenShareChromeExtension: "https://chrome.google.com/webstore/detail/EXTENSION_NAME/EXTENSION_ID" }
			// );
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
					// publisher.once('accessAllowed', () => {
                    //     publisher.stream.getMediaStream().getVideoTracks()[0].addEventListener('ended', this.leaveSessionForScreenSharing)        
                    // });
					publisher.once('accessAllowed', () => {
						try {
							console.log("subscriber >>>>> ", this.subscribers);
							this.isScreenShared=true;
							publisher.stream.getMediaStream().getVideoTracks()[0].addEventListener('ended', () => {
								console.log('User pressed the "Stop sharing" button');
								this.leaveSessionForScreenSharing()
								this.isScreenShared=false;
							});
                            // this.sessionScreen.publish(this.sharingPublisher);						
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
		}

	},

	created() {
		// 접속 시 바로 연결설정 시작.
		this.joinSession()
	}
}
</script>
