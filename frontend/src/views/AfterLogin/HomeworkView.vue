<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="noticeViewForm">
      <h1 id="homeworkTitle">숙제 보기</h1>
      <!-- 제목 -->
      <h2 id="sub-title">제목</h2>
      <b-form-input readonly id="titleName" v-model="homework.title">{{
        homework.title
      }}</b-form-input>

      <h2 id="endTitle">마감일</h2>
      <b-form-input readonly id="endDate" v-model="homework.end">{{
        homework.end
      }}</b-form-input>
      <!-- <input type="date" id="endDate" name="trip-start" /> -->

      <!-- 내용 -->
      <h2 id="content">내용</h2>
      <b-form-textarea
        readonly
        id="contentText"
        plaintext
        v-model="homework.content"
        >{{ homework.content }}</b-form-textarea
      >

      <!-- 취소/수정/삭제 버튼 -->
      <button id="cancelBtn" @click="goHomeworkList">닫기</button>
      <button id="changeBtn" @click="editHomework">수정</button>
      <button id="deleteBtn" @click="deleteHomework">삭제</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "HomeworkView",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function () {
    return {
      homework: {},
    };
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    getHomeworkDetail: function () {
      axios({
          method: "get",
          url: `http://i5a205.p.ssafy.io:8000/homework/detail/${this.selected_homework.id}/`,
          headers: this.headers,
      })
        .then((res) => {
          this.homework = res.data;
          console.log(res.data)
          var temp = this.homework.end;
          // console.log(temp);

          this.homework.end =
            temp.substring(5, 7) +
            "월 " +
            temp.substring(8, 10) +
            "일 " +
            temp.substring(11, 13) +
            "시 " +
            temp.substring(14, 16) +
            "분";
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goHomeworkList: function () {
      // window.open("/homework", "_self");
      this.$router.push({ name: 'Homework' })
    },
    editHomework: function () {

    },
    deleteHomework: function (event) {
      event.preventDefault();
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/homework/detail/${this.selected_homework.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res)
          // this.$router.push({ name: 'Homework' })
          window.open("/homework", "_self");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapState(["headers", "selected_homework"]),
  },
  created: function () {
    this.setToken();
    this.getHomeworkDetail();
  },
};
</script>

<style>
#noticeViewForm {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeViewForm #homeworkTitle {
  position: absolute;
  top: -92px;
  left: -20px;
}

#noticeViewForm #sub-title {
  position: absolute;
  left: 100px;
  top: 70px;
}

#noticeViewForm #titleName {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeViewForm #endTitle {
  position: absolute;
  left: 100px;
  top: 135px;
}

#noticeViewForm #endDate {
  position: absolute;
  left: 250px;
  top: 135px;

  width: 700px;
  font-size: 90%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeViewForm #content {
  position: absolute;
  left: 100px;
  top: 200px;
}

#noticeViewForm #contentText {
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

#noticeViewForm #cancelBtn {
  position: absolute;
  top: 550px;
  left: 500px;

  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#noticeViewForm #changeBtn {
  position: absolute;
  top: 17px;
  left: 965px;

  border-radius: 7px;
  border: 0px;
  color: rgb(190, 140, 32);
  background-color: rgb(249, 249, 252);

  font-size: 60%;

  min-width: 5%;
}

#noticeViewForm #deleteBtn {
  position: absolute;
  top: 17px;
  left: 1025px;

  border-radius: 7px;
  border: 0px;
  color: rgb(190, 140, 32);
  background-color: rgb(249, 249, 252);

  font-size: 60%;

  min-width: 5%;
}
</style>