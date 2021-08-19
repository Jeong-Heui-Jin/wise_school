<template>
  <div id="attitude-info" style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">{{student.name}} 학생 태도 </h1>

    <!-- Homework Create Button -->
    <button id="btn-attitude-create" @click="goAttitudeCreate">
      작성하기
    </button>

    <b-container id="attitude-container" v-if="attitudes.length>0">
      <!-- 요일 -->
      <b-row class="attitude-title" >
        <b-col cols="1">번호</b-col>
        <b-col cols="6">내용</b-col>
        <b-col cols="3">작성일</b-col>
        <b-col cols="2">작성자</b-col>
      </b-row>
      <b-row class="attitude-wrapper" v-for="attitude in attitudes" :key="attitude.id" @click="goAttitudeView(attitude)">
        <b-col cols="1">{{attitude.id}}</b-col>
        <b-col cols="6">{{attitude.content}}</b-col>
        <b-col cols="3">{{attitude.date}}</b-col>
        <b-col cols="2">{{attitude.teacher}}</b-col>
      </b-row>
    </b-container>
    <div id="attitude-container" v-else>아직 작성된 내용이 없습니다.</div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "AttitudeInfo",
  data: function () {
    return {
      student:{
        name: "",
      },
      number:"",
      attitudes:[],
      teachers:[],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },

    getAttitudes:async function () {
      console.log("Attitude")
      await axios({
        method: "get",
        url: `http://i5a205.p.ssafy.io:8000/student-manage/note/${this.number}/`,
        headers: this.headers,
      })
      .then((res) => {
        this.attitudes=res.data;
        this.attitudes.forEach((attitude)=>{
          const date = attitude.registertime.split('T')[0].split('-');
          attitude.date = date[0].slice(2)+'.'+date[1]+'.'+date[2];
          var buf="";
          this.teachers.forEach((teacher)=>{
            if(attitude.teacher === teacher.id){
              buf = teacher.name
            }
          });
          attitude.teacher=buf;
          attitude.name=this.student.name;
        });

      })
      .catch((err) => {
        console.log(err);
      });
    },

    async getTeachers () {
      await axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/accounts/teachers/',
        headers: this.headers,
      })
      .then((res) => {
        res.data.forEach((teacher)=>{
          this.teachers.push({
            name: teacher.name,
            id: teacher.id,
          });
        });

      })
      .catch((err) => {
        console.log(err);
      });
    },
    async getStudents () {
       await axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/accounts/students/',
        headers: this.headers,
      })
      .then((res) => {
        res.data.forEach((student)=>{
          if(student.info.number === this.number) {
            this.student.name = student.name;
          }
        });

      })
      .catch((err) => {
        console.log(err);
      });
    },

    getMembers: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/accounts/class-members/',
        headers: this.headers,
      })
      .then((res) => {
          console.log(res.data)
          res.data.teacher.forEach((teacher)=>{
            console.log(teacher)
            this.teachers[teacher.id] = teacher.name
          });
          console.log(this.teachers)
          this.student={
            name:"",
            id:"",
          }
      })
      .catch((err) => {
        console.log(err);
      });
    },
    
    goAttitudeCreate () {
      window.open(`/attitude_create/${this.number}`,"_self");
    },

    goAttitudeView (attitude) {
      this.$store.dispatch("selectAttitude", attitude);
      this.$router.push({ name: "AttitudeView" });
    },
  },
  computed: {
    rows() {
      return this.items.length;
    },
    ...mapState([
      "headers",
    ]),
  },
  created: async function () {
    this.number=Number(this.$route.params.id)
    this.setToken();
    await this.getStudents();
    await this.getTeachers();
    await this.getAttitudes();
    // this.getMembers();
    // this.getHomeworkList();
  },
};
</script>

<style>
#attitude-info #btn-attitude-create {
  position: absolute;
  top: 100px;
  left: 1000px;
  font-size: 20px;
  min-width: 155px;
  color: #0101d4;
  border-radius: 20px;
  border: 0px;
  background-color: #6cbfe0;
}

#attitude-info #attitude-container {
  position: absolute;
  top: 150px;
  left: 350px;
  width: 800px;
  max-width: 800px;
  min-width: 800px;
  border-bottom: 3px solid #47d4ff;
  font-size: 22px;
}

#attitude-container .attitude-title {
  border-bottom: 3px solid #47d4ff;
  padding: 0;
  color: #9c9c9c;
}

#attitude-container .attitude-wrapper {
  border-top: 1px solid #47d4ff;
  padding: 5px 0px;
}

#homeworkForm {
  position: fixed;

  /* 최대 가로/세로 길이 설정 */
  /* 너비는 최소/최대 길이 동일 설정 */
  max-width: 1000px;
  min-width: 1000px;
  height: 600px;
  /* min-height: 75%; */

  top: 152px;
  left: 400px;

  /* font-size 증가 */
  font-size: 130%;
}

#homeworkForm #homeworkTable {
  position: absolute;
  top: 60px;
}



#paginationForm {
  /* position: absolute; */
  /* left: 220px; */
  /* align: center; */
  bottom: 50px;
}
</style>