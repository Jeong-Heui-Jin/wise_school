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
    <b-form id="attitude-view-form">
      <h1 id="attitude-title">
        &lt;{{ selected_attitude.name }}&gt; 학생 태도
      </h1>

      <!-- 작성 정보 -->
      <div id="attitude-header">
        <div id="attitude-name-wrapper">
          <h2 id="attitude-name" style="font-size: 32px">학생 이름</h2>
          <input
            readonly
            class="attitude-input"
            id="attitude-name-input"
            v-model="selected_attitude.name"
            :formatter="formatTitle"
          />
        </div>
        <div id="attitude-date-wrapper">
          <h2 id="today-date">작성일</h2>
          <input
            readonly
            class="attitude-input"
            id="today-date-input"
            name="created-at"
            v-model="selected_attitude.registertime.split('T')[0]"
          />
        </div>
      </div>

      <!-- 내용 -->
      <div id="attitude-content-wrapper">
        <b-form-textarea
          class="attitude-textarea"
          readonly
          id="contentText"
          v-model="selected_attitude.content"
        ></b-form-textarea>
      </div>

      <!-- 삭제/수정/닫기 버튼 -->
      <div id="btn-wrapper">
        <button id="btn-delete" @click="deleteAttribute">삭제</button>
        <button id="btn-save" @click="goUpdateAttribute">수정</button>
        <button id="btn-cancel" @click="cancel">닫기</button>
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "AttitudeView",
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function() {
      this.$store.dispatch("setToken");
    },

    goUpdateAttribute() {
      this.$router.push({ name: "AttitudeChange" });
    },

    getStudents() {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/students/",
        headers: this.headers,
      })
        .then((res) => {
          res.data.forEach((student) => {
            if (student.info.number === this.number) {
              this.name = student.name;
            }
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    deleteAttribute() {
      if (!confirm("정말로 삭제하시겠습니까?")) return;

      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/student-manage/note/detail/${this.selected_attitude.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
          alert("삭제되었습니다.");
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

  created: function() {
    this.setToken();
  },
};
</script>

<style>
#attitude-view-form {
  position: fixed;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 1000px;
  height: 600px;

  top: 112px;
  left: 370px;

  padding: 50px 30px;
  padding-bottom: 30px;

  background-color: #d3ebbe;
  border-radius: 20px;

  font-size: 30px;
}

#attitude-view-form #attitude-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 90%;
}

#attitude-header #attitude-name-wrapper {
  display: flex;
  align-items: center;
}

#attitude-name-wrapper #attitude-name {
  align-items: center;
  margin: 0;
}

#attitude-header #attitude-date-wrapper {
  display: flex;
  align-items: center;
}

#attitude-date-wrapper #today-date {
  margin: 0;
}

#attitude-view-form #attitude-title {
  position: absolute;
  top: -92px;
  left: -20px;
}

#attitude-view-form #btn-wrapper {
  text-align: end;
  margin: 0 10px;
}

#attitude-view-form .attitude-input {
  background-color: rgb(248, 236, 196);
  border: 0px;
  border-radius: 20px;
  margin-left: 30px;
  padding: 5px 10px;
}

#attitude-view-form .attitude-input:focus {
  outline: none;
}

#attitude-view-form .attitude-textarea {
  background-color: rgb(248, 236, 196);
  border: 0px;
  border-radius: 20px;

  height: 380px;
  resize: none;

  font-size: 32px;
}

#attitude-view-form .attitude-textarea:focus {
  outline: none;
}

#attitude-view-form #btn-delete {
  border-radius: 20px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;
  min-width: 11%;
}
#attitude-view-form #btn-cancel {
  border-radius: 20px;
  border: 0px;
  color: rgb(219, 69, 0);
  background-color: #ffd560;
  margin-left: 20px;

  min-width: 11%;
}

#attitude-view-form #btn-save {
  border-radius: 20px;
  border: 0px;
  color: rgb(38, 38, 255);
  background-color: #8cdbff;
  margin-left: 20px;

  min-width: 11%;
}
</style>
