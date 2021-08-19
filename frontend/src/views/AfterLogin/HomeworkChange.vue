<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle">숙제 수정</h1>

    <b-form id="noticeChangeForm">
      <h1 id="homeworkTitle">숙제 작성</h1>

      <!-- 제목 -->
      <h2 id="sub-title" style="font-size: 32px">제목</h2>
      <b-form-input
        id="titleName"
        v-model="homework.title"
        :formatter="formatTitle"
      ></b-form-input>

      <h2 id="endTitle">마감일</h2>
      <input
        type="datetime-local"
        id="endDate"
        name="trip-start"
        v-model="homework.end"
      />

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px">내용</h2>
      <b-form-textarea
        id="contentText"
        v-model="homework.content"
      ></b-form-textarea>

      <!-- 파일 업로드 -->
      <h2 id="fileUploadTitle" style="font-size: 32px">파일 첨부</h2>
      <input
        type="file"
        id="files"
        ref="files"
        accept="image/*"
        multiple
        v-on:change="handleFileUpload()"
        enctype="multipart/form-data"
      />

      <!-- 취소/저장 버튼 -->
      <button id="cancelBtn">취소</button>
      <button id="saveBtn">수정</button>
    </b-form>

  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBar.vue'
import NavBar from "@/components/NavBar.vue";
import { mapState } from 'vuex'

export default {
  name: "HomeworkChange",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function() {
    return {
      homework: {
        'title':this.selected_homework.title,
        'content':this.selected_homework.content,
        'end':this.selected_homework.end,
      }
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    homeworkChange: function () {
      const homework_id = this.selected_homework.id
      axios({
          method: "put",
          url: `http://i5a205.p.ssafy.io:8000/homework/detail/${homework_id}/`,
          headers: this.headers,
          data: this.homework,
      })
        .then((res) => {
        console.log(res.data)
        })
        .catch((err) => {
        console.log(err);
        });
    },
  },
  computed: {
    ...mapState([
        'headers',
        'selected_homework',
    ]),
  },
  created: function() {
    this.setToken()
    this.getHomeworkDetail()
  }
};
</script>

<style>
#homeworkTitle {
  position: absolute;
  left: 22%;
}

#noticeChangeForm {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeChangeForm #title {
  position: absolute;
  left: 100px;
  top: 70px;
}

#noticeChangeForm #titleName {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeChangeForm #content {
  position: absolute;
  left: 100px;
  top: 220px;
}

#noticeChangeForm #contentText {
  position: absolute;
  left: 250px;
  top: 220px;

  max-width: 700px;
  min-width: 700px;
  max-height: 300px;
  min-height: 300px;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeChangeForm #cancelBtn {
  position: absolute;
  top: 90%;
  left: 36%;

  border-radius: 12px;

  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#noticeChangeForm #saveBtn {
  position: absolute;
  top: 90%;
  left: 53%;

  border-radius: 12px;

  color: rgb(38, 38, 255);
  background-color: #a8aafd;

  min-width: 11%;
}
</style>