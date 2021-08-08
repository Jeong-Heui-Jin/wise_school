<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="noticeCreateForm">
      <h1 id="homeworkTitle">숙제 작성</h1>
      <!-- 제목 -->
      <h2 id="sub-title" style="font-size: 32px">제목</h2>
      <b-form-input id="titleName" v-model="createValue.title"></b-form-input>

      <h2 id="endTitle">마감일</h2>
      <input
        type="datetime-local"
        id="endDate"
        name="trip-start"
        v-model="createValue.end"
      />

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px">내용</h2>
      <b-form-textarea
        id="contentText"
        v-model="createValue.content"
      ></b-form-textarea>

      <!-- 취소/저장 버튼 -->
      <button id="saveBtn" @click="homeworkCreate">저장</button>
      <button id="cancelBtn">취소</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from 'vuex';

export default {
  name: "HomeworkCreate",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function() {
    return {
      createValue: {
        title: "",
        end: "",
        content: "",
      },
    };
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    homeworkCreate: function (event) {
      event.preventDefault();
      axios({
        method: "post",
        // url: "http://i5a205.p.ssafy.io:8000/homework/list/",
        url: 'http://127.0.0.1:8000/homework/list/',
        headers: this.headers,
        data: this.createValue,
      })
        .then((res) => {
          console.log(res)
          this.$router.push({
            name: "HomeworkView",
            params: { homework: res },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {
    this.setToken()
  }
};
</script>

<style>
#noticeCreateForm {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeCreateForm #homeworkTitle {
  position: absolute;
  top: -92px;
  left: -20px;
}

#noticeCreateForm #sub-title {
  position: absolute;
  left: 100px;
  top: 70px;
}

#noticeCreateForm #titleName {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeCreateForm #endTitle {
  position: absolute;
  left: 100px;
  top: 135px;
}

#noticeCreateForm #endDate {
  position: absolute;
  left: 250px;
  top: 135px;

  width: 700px;
  font-size: 90%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeCreateForm #content {
  position: absolute;
  left: 100px;
  top: 200px;
}

#noticeCreateForm #contentText {
  position: absolute;
  left: 250px;
  top: 200px;

  max-width: 700px;
  min-width: 700px;
  max-height: 300px;
  min-height: 300px;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeCreateForm #cancelBtn {
  position: absolute;
  top: 550px;
  left: 670px;

  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#noticeCreateForm #saveBtn {
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