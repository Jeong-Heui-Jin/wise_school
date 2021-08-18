<template>
  <div id="attendance" style="font-family: 'Jua', sans-serif">
    <NavSideBar/>
    <NavBar/>
    <h1 id="title">출석 관리</h1>
    <b-container class="attendance-wrapper">
      <!-- 요일 -->
      <b-row class="period" >
        <b-col class="subject" style="padding-bottom: 20px;">학생 이름</b-col>
        <b-col class="subject " style="padding-bottom: 20px;">월
          <div id="date">{{date[0].month}}.{{date[0].date}}</div>
        </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">화
          <div id="date">{{date[1].month}}.{{date[1].date}}</div>
        </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">수
          <div id="date">{{date[2].month}}.{{date[2].date}}</div>
        </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">목
          <div id="date">{{date[3].month}}.{{date[3].date}}</div>
        </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">금
          <div id="date">{{date[4].month}}.{{date[4].date}}</div>
        </b-col>
      </b-row>
      <b-row class="period" v-for="student in studentAttendances" :key="student.id">
        <div class="w-100"></div>
        <b-col class="subject name">{{student.name}}</b-col>
        <b-col class="subject" :class="student.mon">{{student.mon}}</b-col>
        <b-col class="subject" :class="student.tue">{{student.tue}}</b-col>
        <b-col class="subject" :class="student.wed">{{student.wed}}</b-col>
        <b-col class="subject" :class="student.thu">{{student.thu}}</b-col>
        <b-col class="subject" :class="student.fri">{{student.fri}}</b-col>
      </b-row>      
    </b-container>
    <div v-if="isChangingStatus" class="status-change-container" style="position:absolute;top:0;left:0; background-color:black; width:100%; height:100%; z-index: 5; opacity:0.3;">
      <div class="status-change-wrapper">
        <div class="status-change-title">출결 상태 변경</div>
        <div class="status-change-status">
          <ul>1</ul>
          <ul>2</ul>
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
  name: 'Attendance',
  components: {
    NavSideBar,
    NavBar
  },
  data: function() {
    return {
      attendances: {},
      date:{
        // "mon":{
        //   year: 2021,
        //   month: "08",
        //   date: "18",
        //   day: 2,
        // },
      },
      studentAttendances: [
        // {
        //   userCode:'1',
        //   name:"김우진",
        //   mon:"출석",
        //   tue:"지각",
        //   wed:"결석",
        //   thu:"취업",
        //   fri:"",
        // },
      ],
      isChangingStatus:false,
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getMembers: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/accounts/class-members/',
        headers: this.headers,
      })
      .then((res) => {
        this.studentAttendances=[];
        res.data.students.forEach((student)=>{
          const studentAttendance = {
            userCode: student.id,
            name: student.name?student.name:"null",
            mon: "",
            tue: "",
            wed: '',
            thu: '',
            fri: '',
          }
          this.studentAttendances.push(studentAttendance)
        })
      })
      .catch((err) => {
        console.log(err);
      });
    },
    getAttendances: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/student-manage/attendance/',
        headers: this.headers,
      })
        .then((res) => {
          this.attendances = res.data;
          var day = ["mon", "tue", "wed", "thu", "fri"];
          this.attendances.forEach((attendance)=>{
            const attendanceDate = attendance.registertime.split('T')[0].split('-');
            
            if (Number(attendanceDate[0])>=this.date[0].year) {

              for(var i=0; i<5; i+=1) {
                if (attendanceDate[1]===this.date[i].month && attendanceDate[2] === this.date[i].date) {
                  this.studentAttendances.forEach((student)=>{

                    if(student['userCode'] === attendance.student) {
                      if(attendance.student===6) {
                        console.log(attendance)
                      }
                      if(attendance.status==="출석") { // 출석은 무조건 반영
                        student[`${day[i]}`] = attendance.status;

                      } else if (attendance.status==="조퇴") {
                        student[`${day[i]}`] = attendance.status;

                      } else if (!student[`${day[i]}`]) {
                        student[`${day[i]}`] = attendance.status;

                      }
                    }
                  });
                }
              }
            }

          });
          
          this.studentAttendances.forEach((student)=>{
            const today = new Date().getDay();
            for(var i=0; i<today; i+=1) {
              if(!student[`${day[i]}`]) {
                student[`${day[i]}`]="결석";
              }
            }
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 날짜를 이번주로 맞춰주는 함수
    setWeek: function () {
      this.date=[];
      const today = new Date();
      const week = today.getDay();
      const diff = week-1; // 월요일과의 차이

      today.setDate(today.getDate() - diff);

      for(var i=0; i<5; i+=1) {
        this.date.push({
          year: today.getFullYear(),
          month: (this.zeroPadding(today.getMonth()+1)),
          date:this.zeroPadding(today.getDate()),
          day:today.getDay()-1,
        });

        today.setDate(today.getDate() + 1);
      }

    },
    zeroPadding: function (num) {
			return num < 10 ? "0"+num : String(num);
		},
    adjustColor: function () {
      document.getElementsByClassName("결석").forEach((el)=>{
        el.style.color="red";
      });
      document.getElementsByClassName("지각").forEach((el)=>{
        el.style.color="yellow";
      });
      document.getElementsByClassName("조퇴").forEach((el)=>{
        el.style.color="purple";
      });
      document.getElementsByClassName("출석").forEach((el)=>{
        el.style.color="blue";
      });
    },
  },
  computed: {
    ...mapState([
      'headers',
      'now_user',
    ]),
  },
  created: function() {
    this.setToken()
    this.getAttendances()
    this.setWeek();
    this.getMembers();
  },
  updated() {
    this.adjustColor();
  }
}
</script>

<style>
#attendance .attendance-wrapper {
  position: absolute;
  top: 90px;
  left: 350px;
  width: 900px;
  max-width: 900px;
  min-width: 900px;
}

.attendance-wrapper .subject {
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-width: 40px;
  font-size: 32px;
  text-align: center;
  padding: 10px !important;
  border: 1px solid #74dfd9;
  font-size: 28px;
}

.attendance-wrapper #date {
  font-size: 30px;
}
</style>