<template>
  <div id="home" style="font-family: 'Jua', sans-serif">
    <NavBar/>
    <NavSideBar/>

    <h3 id="date">{{ year }}년 {{ month }}월 {{ date }}일 {{ day }}</h3>
    <div>
      <!-- 수업참여 숙제 -->
      <div id="top-2" class="d-flex fixed-top">
      <!-- 수업참여 -->
        <div id="attend-class" style="margin-right: 18px;">
          <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/blackboard.png" alt="수업참여"/>
            <p>수업 참여</p>
          </div>
          <b-button id="class-btn" variant="warning" @click="enterRoom">교실<br/>입장하기</b-button>
        </div>
      <!-- 숙제 -->
        <div id="homework">
          <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/homework.png" alt="숙제"/>
            <p>숙제</p>
            <button style="margin-left: auto; margin-right: 10px; font-size: 32px; border: 0px; background-color: #e0edd4;" @click="$router.push('/homework')">+</button>
            <!-- <p>+</p> -->
          </div>
          <ul id="list" v-for="homework in homeworks" :key="homework.title">
            <li @click="goHomeworkView">- {{ homework.title }}</li>
          </ul>
        </div>  
      </div>
      <!-- 공지사항 -->
      <div id="notes" class="fixed-top">
        <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/alert.png" alt="공지사항"/>
            <p>공지사항</p>
            <button style="margin-left: auto; margin-right: 10px; font-size: 32px; border: 0px; background-color: #ffecd5;" @click="$router.push('/notice')">+</button>
            <!-- <p>+</p> -->
        </div>
        <ul id="list" v-for="notice in notices" :key="notice.title">
            <li @click="goNoticeView">- {{ notice.title }}</li>
        </ul>
      </div>
      <!-- 오늘의 시간표 -->
      <div id="timetable-form" class="fixed-top">
        <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/schedule.png" alt="시간표"/>
            <p style="margin-bottom: 0px;">오늘의 시간표</p>
        </div>
        <!-- 시간표 내용 -->
        <div id="timeschedule">
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBar.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    NavSideBar,
    NavBar
  },
  data() {
    return {
      usertype: 1,
      year: 0,
      month: 0,
      day: 0,
      date: '',
      homeworks: [],
      notices: [],
      timeschedules: [
        {subject: '국어', book: '말하기/듣기/쓰기', time:'09:00 ~ 09:50'},
        {subject: '수학', book: '수학/수학과익힘', time:'10:00 ~ 10:50'},
        {subject: '사회', book: '사회과부도', time:'11:00 ~ 11:50'},
        {subject: '과학', book: '관찰', time:'13:00 ~ 13:50'},
        {subject: '영어', book: 'Elementary School', time:'14:00 ~ 14:50'},
      ],
      attendanceValue: "", // 출석체크
    }
  },
  methods: {
    getNow: function () {
      const arr=['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일'];

      const today = new Date();
      this.year = today.getFullYear();
      this.month = today.getMonth() + 1;
      this.day = arr[today.getDay()];
      this.date = today.getDate();
    },
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getList: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/classroom/home/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
          this.homeworks = res.data.homeworks
          this.notices = res.data.notices
          this.timetable = res.data.timetable

          // 숙제 제목 긴 경우 뒤 생략
          for (let i = 0; i < this.homeworks.length; ++i) {
            var homeworkTitle = this.homeworks[i].title;
            if (homeworkTitle.length > 18) {
              this.homeworks[i].title = homeworkTitle.substring(0, 18) + "..."
            }
          }

          // 공지 제목 긴 경우 뒤 생략
          for (let i = 0; i < this.notices.length; ++i) {
            var noticeTitle = this.notices[i].title;
            if (noticeTitle.length > 30) {
              this.homeworks[i].title = noticeTitle.substring(0, 30) + "..."
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setUser: function () {
      axios({
        method: 'get',
        url: 'http://i5a205.p.ssafy.io:8000/accounts/profile/',
        headers: this.headers,
        })
        .then((res) => {
          this.$store.dispatch('setUser', res.data)
          this.usertype = this.now_user.usertype
        })
        .catch(err => {
          console.log(err)
      });
    },
    enterRoom: function () {
      const now_at = new Date();
			let hour = now_at.getHours();
			let minutes = now_at.getMinutes();

			if (hour===9 && 0<=minutes<=10) {
				this.attendanceValue = "출석";	
			} else  {
				this.attendanceValue = "지각";
			} 
			// console.log("출석", this.attendanceValue);
      axios({
				method: "post",
				url: "http://i5a205.p.ssafy.io:8000/student-manage/attendance/",
				data: {
          status: this.attendanceValue,
          student_id: this.now_user.id,
          classroom_id: this.now_user.classroom
        },
				headers: this.headers
			})
			.then((res) => {
        // console.log("출석 성공");
				console.log(res, "success postAttendance");
        window.class = window.open("https://i5a205.p.ssafy.io:8080");
      
        // window.class = window.open("https://localhost:8081");
        const user = {
          msgType: "init_classroom",
          classroom: this.now_user.classroom,
          userName: this.now_user.name,
          userType: this.now_user.usertype,
          userToken: localStorage.getItem('jwt')
        }
        // setTimeout(()=> window.class.postMessage(user, 'https://i5a205.p.ssafy.io:8080'), 2000);
        window.addEventListener('message', function(e) {
          if (e.data.msgType === "connection_fail") {
            console.log("Connection refused: Time Out!")
            clearInterval(window.interval1);
            window.class.close();
            window.class=""

          } else if (e.data.msgType === "connect") {
            console.log("Connect to Classroom Successfully.")
            clearInterval(window.interval1);
          } else if (e.data.msgType === "leave_class") {
            console.log("Leave Classroom Successfully.")
            window.class.close();
            window.class="";
          }
        });

        window.interval1=setInterval(()=> window.class.postMessage(user, 'https://i5a205.p.ssafy.io:8080'), 500); // 0.5초 간격으로 정보 전송
        // window.interval1=setInterval(()=> window.class.postMessage(user, 'https://localhost:8081'), 500); // 0.5초 간격으로 정보 전송
      
			})
			.catch((err) => {
        console.log("실패");
				console.log(err);
			});

    },
    goHomeworkView: function (homework) {
      this.$store.dispatch('selectHomework', homework);
      window.open("/homework_view", "_self");
      // this.$router.push({ name: 'HomeworkView'})
    },
    goNoticeView: function (notice) {
      this.$store.dispatch('selectNotice', notice);
      // this.$router.push({ name: 'NoticeView'})
    }
  },
  created() {
    this.setToken();
    this.setUser();
    this.getList();
    this.getNow();
    this.$nextTick(() => {
      const timeBody = document.querySelector('#timeschedule');
      // const imgName = "@/assets/whale.png"
      var cnt = 0;

      timeBody.innerHTML = this.timeschedules.map((li) => {
        cnt += 1;
        return `
          <div class="d-flex" id="time-card">
            <div id="class-time">
              <h2>${cnt}교시</h2>
              <p>${li.time}</p>
            </div>
            <div id="subject">
              <h3>${li.subject}</h3>
              <p>${li.book}</p>
            </div>
          </div>
          `;
      }).join("");
    });
  },
  mounted() {
    // console.log(this.$route.params.authority);
    // this.authority = this.$route.params.authority;
  },
  computed: {
    ...mapState([
      'headers',
      'now_user',
    ]),
  },
}
</script>

<style>
#home #date {
  position: absolute;
  left: 350px;
  top: 30px;
}

#home #top-2 {
  position: absolute;
  left: 330px;
  top: 100px;
}

#home #home-title {
  vertical-align: center;
  margin-top: 15px;
}

#home #attend-class {
  min-width: 350px;
  min-height: 300px;
  border-radius: 20px;
  margin-right: 50px;
  background-color: #ccf0ef;
}

#home #attend-class #class-btn {
  min-width: 250px;
  min-height: 100px;
  border-radius: 20px;
  margin-top: 50px;
  font-size: 40px;
}

#home #list{
  margin-top: 15px;
  font-size: 20px;
  text-align: left;
}

#home-title img{
  margin-left: 15px;
}

#home-title p{
  margin-left: 15px;
  font-size: 32px;
  margin-top: 15px;
}

/* #home-title p{
  margin-left: auto;
  font-size: 40px;
  margin-top: 10px;
  margin-right: 20px;
} */

#home #homework {
  border-radius: 20px;
  background-color: #e0edd4;
  width: 382px;
  height: 335px;
}

#home #img{
  max-width: 100px;
  max-height: 60px;
}

#home #notes{
  position: absolute;
  left: 330px;
  top: 450px;
  max-width: 750px;
  min-width: 750px;
  min-height: 300px;
  border-radius: 20px;
  background-color: #ffecd5;
}

#home #timetable-form {
  position: absolute;
  top: 100px;
  left: 1100px;
  margin-right: 35px;
  border-radius: 20px;
  min-width: 300px;
  max-width: 300px;
  height: 650px;
  border: 2px solid aqua;
}

#timeschedule #time-card {
  max-width: 250px;
  margin-top: 23px;
}

#timeschedule #class-time {
  min-width: 150px;
}

#time-card #subject {
  min-width: 130px;
  border-radius: 20px;
  background-color:aquamarine;
  text-align: center;
  padding-top: 12px;
}
#time-card #subject p {
  font-size: 12px;
}
</style>