<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="homeworkViewForm">
      <h1 id="homeworkViewTitle">숙제 보기</h1>
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
      <div>
        <b-modal id="modal-center" centered title="첨부 사진">
          <!-- <img :src="imageUrl" class="card-img-top" alt="..."> -->
          <p>숙제 사진</p>
        </b-modal>
      </div>
      <button id="fileBtn" v-b-modal.modal-center>상세보기</button>
      <button id="cancelBtn" @click="goHomeworkList">닫기</button>
      <div v-if="usertype === 1">
        <button id="homeworkChangeBtn" @click="editHomework">수정</button>
        <button id="homeworkDeleteBtn" @click="deleteHomework">삭제</button>
      </div>
      <button id="submitBtn" @click="goSubmit()">숙제 제출</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
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
      usertype: 2,
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
          console.log(res.data);
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
      this.$router.push({ name: "Homework" });
    },
    editHomework: function () {},
    deleteHomework: function (event) {
      event.preventDefault();
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/homework/detail/${this.selected_homework.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res);
          // this.$router.push({ name: 'Homework' })
          window.open("/homework", "_self");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    viewFiles: function () {},
    goSubmit: function () {
      this.$router.push({
        name: "HomeworkSubmit",
        params: { id: this.homework.id },
      });
      // window.open(`/homework-submit/${this.homework.id}`, "_self");
    },
  },
  computed: {
    ...mapState(["headers", "selected_homework", "now_user"]),
    // imageUrl : function () {
    //   const imagePath = this.homework.homeworkfile_set[0].image
    //   return `http://127.0.0.1:8000/${imagePath}`
    // }
  },
  created: function () {
    this.setToken();
    this.getHomeworkDetail();
    this.usertype = this.now_user.usertype;
  },
};
</script>

<style>
#homeworkViewForm {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#homeworkViewForm #homeworkViewTitle {
  position: fixed;
  top: 10px;
  left: 120px;
  margin-left: 220px;
  margin-top: 20px;
}

#homeworkViewForm #sub-title {
  position: absolute;
  left: 100px;
  top: 70px;
}

#homeworkViewForm #titleName {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#homeworkViewForm #endTitle {
  position: absolute;
  left: 100px;
  top: 135px;
}

#homeworkViewForm #endDate {
  position: absolute;
  left: 250px;
  top: 135px;

  width: 700px;
  font-size: 90%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#homeworkViewForm #content {
  position: absolute;
  left: 100px;
  top: 200px;
}

#homeworkViewForm #contentText {
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

#homeworkViewForm #cancelBtn {
  position: absolute;
  top: 550px;
  left: 650px;

  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#homeworkViewForm #fileBtn {
  position: absolute;
  top: 550px;
  left: 350px;

  border-radius: 12px;
  border: 0px;
  color: rgb(0, 87, 46);
  background-color: #b6e0fc;

  min-width: 11%;
}

#homeworkViewForm #submitBtn {
  position: absolute;
  top: 550px;
  left: 500px;

  border-radius: 12px;
  border: 0px;
  color: rgb(0, 87, 46);
  background-color: #b6fcc5;

  min-width: 11%;
}

#homeworkViewForm #homeworkChangeBtn {
  position: absolute;
  top: 17px;
  left: 965px;

  border-radius: 7px;
  border: 0px;
  color: rgb(190, 140, 32);
  background-color: rgb(249, 249, 252);

  font-size: 60%;

  width: 55px;
  height: 25px;
}

#homeworkViewForm #homeworkDeleteBtn {
  position: absolute;
  top: 17px;
  left: 1025px;

  border-radius: 7px;
  border: 0px;
  color: rgb(190, 140, 32);
  background-color: rgb(249, 249, 252);

  font-size: 60%;

  width: 55px;
  height: 25px;
}
</style>