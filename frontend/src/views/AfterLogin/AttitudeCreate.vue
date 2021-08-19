<template>
  <div id="attitude-Create" style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="attitude-create-form">
      <h1 id="attitude-title">&lt;{{ name }}&gt; 학생 태도 작성</h1>

      <!-- 제목 -->
      <h2 id="attitude-name" style="font-size: 32px">학생 이름</h2>
      <input
        readonly
        id="iattitude-name-input"
        v-model="name"
        :formatter="formatTitle"
      />

      <h2 id="today-date">작성일</h2>
      <input
        readonly
        type="text"
        id="today-date-input"
        name="created-at"
        v-model="today"
      />

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px">내용</h2>
      <b-form-textarea id="contentText" v-model="content"></b-form-textarea>

      <!-- 취소/저장 버튼 -->
      <button id="btn-save" @click="createNote">저장</button>
      <button id="btn-cancel" @click="cancel">취소</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "AttitudeCreate",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function () {
    return {
      name:"",
      number:"",
      today:"",
      content:"",
    };
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },

    createNote () {
        axios({
            method: "post",
            url: `http://i5a205.p.ssafy.io:8000/student-manage/note/${this.number}/`,
            headers: this.headers,
            data: {
                content: this.content,
            },
        })
        .then((res)=>{
            console.log(res.data)
            
        })
        .catch(err=>{
            console.log(err);
            alert(this.number);
        })

        this.$router.push({ name:'AttitudeInfo', params:{'id': this.number} })
    },

    getStudents () {
        axios({
            method: "get",
            url: 'http://i5a205.p.ssafy.io:8000/accounts/students/',
            headers: this.headers,
        })
        .then((res) => {
            res.data.forEach((student)=>{
                if(student.info.number === this.number) {
                    this.name = student.name;
                }
            });

        })
        .catch((err) => {
            console.log(err);
        });
    },

    setDate () {
        const today = new Date();
        this.today= today.getFullYear() + '-' + this.zeroPadding(today.getMonth()+1) + '-' + this.zeroPadding(today.getDate());
    },

    zeroPadding (num) {
        return num>10?String(num):"0"+String(num);
    },

    cancel () {
        this.$router.push({ name:'AttitudeInfo', params:{'id': this.number} });
    },
  },

  computed: {
    ...mapState([
        "headers",
    ]),
  },

  created: function () {
    this.number=Number(this.$route.params.id)
    this.setToken();
    this.setDate();
    this.getStudents();
  },
};
</script>

<style>
#attitude-create-form {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#attitude-create-form #attitude-title {
  position: absolute;
  top: -92px;
  left: -20px;
}

#attitude-create-form #attitude-name {
  position: absolute;
  left: 100px;
  top: 70px;
}

#attitude-create-form #iattitude-name-input {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#attitude-create-form #today-date {
  position: absolute;
  left: 100px;
  top: 135px;
}

#attitude-create-form #today-date-input {
  position: absolute;
  left: 250px;
  top: 135px;

  width: 700px;
  font-size: 90%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#attitude-create-form #content {
  position: absolute;
  left: 100px;
  top: 200px;
}

#attitude-create-form #contentText {
  position: absolute;
  left: 250px;
  top: 200px;

  max-width: 700px;
  min-width: 700px;
  max-height: 220px;
  min-height: 220px;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#attitude-create-form #fileUploadTitle {
  position: absolute;
  left: 100px;
  top: 445px;
  background-color: transparent;
}

#attitude-create-form #files {
  position: absolute;
  left: 250px;
  top: 440px;

  max-width: 700px;
  min-width: 700px;

  background-color: rgb(248, 236, 196);
  border-radius: 13px;

  text-align: left;
  padding-left: 15px;
}

#attitude-create-form #btn-cancel {
  position: absolute;
  top: 550px;
  left: 670px;

  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#attitude-create-form #btn-save {
  position: absolute;
  top: 550px;
  left: 330px;

  border-radius: 12px;
  border: 0px;
  color: rgb(38, 38, 255);
  background-color: #a8aafd;

  min-width: 11%;
}
</style>
