<template>
  <div id="home" style="font-family: 'Jua', sans-serif">
    <!-- 백엔드와 연동하여 권한을 확인한 후 해당 페이지를 띄워줄 예정 -->
    <NavBar/>
    <div v-if="authority==='0'"><NavSideBarAdmin/></div>
    <div v-else-if="authority==='1'"><NavSideBarTeacher/></div>
    <div v-else><NavSideBarStudent/></div>

    <h3 id="date">{{ year }}년 {{ month }}월 {{ date }}일 {{ day }}</h3>
    <div>
      <!-- 수업참여 숙제 -->
      <div id="top-2" class="d-flex fixed-top">
      <!-- 수업참여 -->
        <div id="attend-class">
          <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/blackboard.png" alt="수업참여"/>
            <p>수업 참여</p>
          </div>
          <b-button id="class-btn" variant="warning">교실<br/>입장하기</b-button>
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
            <li>- {{ homework.title }}</li>
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
            <li>- {{ notice.title }}</li>
        </ul>
      </div>
      <!-- 오늘의 시간표 -->
      <div id="timetable-form" class="fixed-top">
        <div class="d-flex justify-content-left" id="home-title">
            <img id="img" src="@/assets/schedule.png" alt="시간표"/>
            <p>오늘의 시간표</p>
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
import NavSideBarAdmin from '@/components/NavSideBarAdmin.vue'
import NavSideBarTeacher from '@/components/NavSideBarTeacher.vue'
import NavSideBarStudent from '@/components/NavSideBarStudent.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    NavSideBarAdmin,
    NavSideBarTeacher,
    NavSideBarStudent,
    NavBar
  },
  data() {
    return {
      authority: '1',
      year: 0,
      month: 0,
      day: 0,
      date: '',
      homeworks: [
        // {title: '수학 익힘책 16쪽~23쪽'},
        // {title: '<어린왕자>읽기'},
        // {title: '알파벳 10번씩 쓰기'},
        // {title: '한자 15,000번씩 쓰기'},
        // {title: '줄넘기 연습하기'}
      ],
      notices: [
        // {title: '8월 급식메뉴 알림판'},
        // {title: '7/20 가정통신문'},
        // {title: '7/21 가정통신문'},
        // {title: '공지공지'},
        // {title: '사항사항'}
      ],
      timeschedules: [
        {subject: '국어', book: '말하기/듣기/쓰기', time:'09:00 ~ 09:50'},
        {subject: '수학', book: '수학/수학과익힘', time:'10:00 ~ 10:50'},
        {subject: '사회', book: '사회과부도', time:'11:00 ~ 11:50'},
        {subject: '과학', book: '관찰', time:'13:00 ~ 13:50'},
        {subject: '영어', book: 'Elementary School', time:'14:00 ~ 14:50'},
      ]
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
        // url: 'http://i5a205.p.ssafy.io:8000/classroom/home/',
        url: 'http://127.0.0.1:8000/classroom/home/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
          this.homeworks = res.data.homeworks
          this.notices = res.data.notices
          this.timetable = res.data.timetable
        })
        .catch((err) => {
          console.log(err);
        });
    },
    setUser: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/profile/',
        headers: this.headers,
        })
        .then((res) => {
          this.$store.dispatch('setUser', res.data)
        })
        .catch(err => {
          console.log(err)
      })
    }
  },
  created() {
    this.setToken();
    this.setUser();
    this.getList();
    this.getNow();
    console.log(this.now_user)
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
  min-width: 350px;
  min-height: 300px;
  border-radius: 20px;
  background-color: #e0edd4;
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
  min-height: 680px;
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