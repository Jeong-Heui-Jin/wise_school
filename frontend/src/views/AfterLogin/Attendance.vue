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
        <b-col class="subject" :class="student.mon.status" @click="statusChange(student,0)">{{student.mon.status}}</b-col>
        <b-col class="subject" :class="student.tue.status" @click="statusChange(student, 1)">{{student.tue.status}}</b-col>
        <b-col class="subject" :class="student.wed.status" @click="statusChange(student, 2)">{{student.wed.status}}</b-col>
        <b-col class="subject" :class="student.thu.status" @click="statusChange(student, 3)">{{student.thu.status}}</b-col>
        <b-col class="subject" :class="student.fri.status" @click="statusChange(student, 4)">{{student.fri.status}}</b-col>
      </b-row>      
    </b-container>
    <div v-if="isChangingStatus" class="status-change-container">
      <div class="status-change-background" @click="closeModal"></div>
      <div class="status-change-wrapper">
        <div class="status-change-title">출결 상태 변경</div>
        <div class="status-change-status">
          <div>- 학생 이름 : {{changeInfo.name}}</div>
          <div>- 상태 변경 : <span style="color:blue; font-size:30px">{{changeInfo.status}}</span> --->
            <select class="status-change-combo" id="combo" name="status" >
              <option value="출석">출석</option>
              <option value="조퇴">조퇴</option>
              <option value="지각">지각</option>
              <option value="결석">결석</option>
            </select>
          </div>
        </div>
        <div class="status-change-content" style="text-align: center; padding:10px" >
          <div class="btn-save" @click="statusChangeRequest">저장</div>
          <!-- <div>
            <textarea name="" id="status-change-reason" cols="30" rows="10"></textarea>
            
          </div> -->
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
        // "two":{...
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
        // }, ...
      ],
      isChangingStatus:false,
      changeInfo:{},
      day: ["mon", "tue", "wed", "thu", "fri"],
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
            mon: {
              status:"",
              attendance_id:"",
            },
            tue:{
              status:"",
              attendance_id:"",
            },
            wed: {
              status:"",
              attendance_id:"",
            },
            thu:{
              status:"",
              attendance_id:"",
            },
            fri: {
              status:"",
              attendance_id:"",
            },
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
                    
                      if(attendance.status==="출석") { // 출석은 무조건 반영
                        // student[`${day[i]}`] = attendance.status;
                        // student['attendance_id'] = attendance.id;
                        student[`${day[i]}`] = {
                          status: attendance.status,
                          attendance_id: attendance.id,
                        }
                        console.log(attendance)

                      } else if (attendance.status==="조퇴") {
                        student[`${day[i]}`] = {
                          status: attendance.status,
                          attendance_id: attendance.id,
                        }
                        console.log(attendance.id)
                        console.log(student['attendance_id'])
                      } else if (!student[`${day[i]}`].status) {
                        student[`${day[i]}`] = {
                          status: attendance.status,
                          attendance_id: attendance.id,
                        }
                        console.log(attendance)

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
              if(!student[`${day[i]}`].status) {
                student[`${day[i]}`].status="결석";
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
    adjustStatusColor: function () {
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
    statusChange: function (student, day) {
      this.isChangingStatus = true;
      this.changeInfo={
        attendance_id: student[`${this.day[day]}`].attendance_id,
        student: student,
        status: student[`${this.day[day]}`].status,
        name: student.name,
        day:day,
      }
    },
    statusChangeRequest: function () {
      var newStatus = document.querySelector('#combo').value;

      if (this.changeInfo.status === newStatus) {
        alert("출결 상태가 변하지 않았습니다. 다시 선택해 주세요.")
        return;
      }
      console.log(123, this.changeInfo)

      axios({
        method: "PUT",
        url: `http://i5a205.p.ssafy.io:8000/student-manage/attendance/detail/${this.changeInfo.attendance_id}/`,
        data: {
          status: newStatus
        },
        headers: this.headers
      })
      .then((res) => {
        console.log(res)
        this.changeInfo.student[`${this.day[this.changeInfo.day]}`].status=newStatus;
        alert("수정에 성공했습니다.");
      })
      .catch((err) => {
        console.log(err);
      });
      this.$router.go();
      
      
    //   axios({
    //     method: "post",
		// 		url: "http://i5a205.p.ssafy.io:8000/student-manage/attendance/detail/10/",
		// 		data: {
    //       status: this.attendanceValue,
    //       student_id: this.now_user.id,
    //       classroom_id: this.now_user.classroom
    //     },
		// 		headers: this.headers
    //   })
    //     .then((res) => {
    //       console.log(res)
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    },
    closeModal: function () {
      this.isChangingStatus=false;
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
    this.adjustStatusColor();
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

#attendance .status-change-container {
  position: fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  z-index: 5;
  display: flex;
  justify-content: center;
  align-items: center;
}

.status-change-container .status-change-background {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: black;
  opacity: 0.3;
}

.status-change-container .status-change-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width:500px;

  background-color: white;
  z-index: 6;
}

.status-change-wrapper .status-change-title {
  font-size: 30px;
  font-weight: bold;
  text-align: left;
  margin: 25px;
}

.status-change-wrapper .status-change-status {
  display: flex;
  flex-direction: column;
  font-size: 24px;
  text-align: left;
  margin: 0 25px;
}

.status-change-status .status-change-combo {
  width: 200px;
  text-align-last: center;
  text-align: center;
  -ms-text-align-last: center;
  -moz-text-align-last: center;
}

.status-change-wrapper .status-change-content {
  font-size: 20px;
  text-align: left;
  margin: 0 25px;
}

.status-change-content .btn-save {
  display: inline-block;
  color:#ffffff;
  background-color: #003de4;
  border-radius: 20px;
  padding: 2px 20px;
  font-size: 16px;
  
}

.status-change-content .btn-save:hover {
  background-color: #3060e4;
}

.status-change-content .btn-save:active {
  background-color: #a3aabd;
}

.status-change-content textarea {
  width:100%;
  resize: none;
  border: 2px solid #6ce9ff;
  border-radius: 20px;
  margin: 10px 0;
}

.status-change-content textarea:focus {
  outline: none;
}

</style>