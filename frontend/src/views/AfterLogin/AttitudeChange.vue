<template>
  <div
    id="attitude-Create"
    style="font-family: 'Jua', sans-serif"
    variant="light"
  >
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="attitude-create-form">
      <h1 id="attitude-title">
        &lt;{{ selected_attitude.name }}&gt; 학생 태도 작성
      </h1>

      <!-- 제목 -->
      <h2 id="attitude-name" style="font-size: 32px">학생 이름</h2>
      <input
        readonly
        id="iattitude-name-input"
        v-model="selected_attitude.name"
      />

      <h2 id="today-date">작성일</h2>
      <input
        readonly
        type="text"
        id="today-date-input"
        name="created-at"
        v-model="selected_attitude.registertime.split('T')[0]"
      />

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px">내용</h2>
      <b-form-textarea id="contentText" v-model="selected_attitude.content"></b-form-textarea>

      <!-- 취소/저장 버튼 -->
      <button id="btn-save" @click="updateNote">수정</button>
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
  name: "AttitudeChange",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function() {
    return {
      name: "",
      number: "",
      today: "",
      content: "",
    };
  },
  methods: {
    setToken: function() {
      this.$store.dispatch("setToken");
    },

    updateNote() {
      axios({
        method: "put",
        url: `http://i5a205.p.ssafy.io:8000/student-manage/note/detail/${this.selected_attitude.id}/`,
        headers: this.headers,
        data: {
          content: this.selected_attitude.content,
        },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
        this.$router.push({
        name: "AttitudeInfo",
        params: { id: this.selected_attitude.student },
      });
    },

    cancel() {
      this.$router.push({
        name: "AttitudeInfo",
        params: { id: this.selected_attitude.student },
      });
    },
  },

  computed: {
    ...mapState(["headers", "selected_attitude"]),
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
