<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="noticeCreateForm">
      <h1 id="noticeTitle">공지 작성</h1>

      <!-- 제목 -->
      <h2 id="sub-title" style="font-size: 32px">제목</h2>
      <b-form-input
        id="titleName"
        v-model="createValue.title"
        :formatter="formatTitle"
      ></b-form-input>

      <!-- 중요도 -->
      <h2 id="isImportant">중요도</h2>
      <b-form-select
        v-model="createValue.is_important"
        :options="options"
        id="select"
      >
      </b-form-select>

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px">내용</h2>
      <b-form-textarea
        id="contentText"
        v-model="createValue.content"
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
      <button id="saveBtn" @click="noticeCreate">저장</button>
      <button id="cancelBtn">취소</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "HomeworkCreate",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function () {
    return {
      createValue: {
        title: "",
        is_important: 0,
        content: "",
      },
      files: "",
      options: [
        { text: "일반", value: 0 },
        { text: "중요", value: 1 },
      ],
    };
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    formatTitle: function (e) {
      return String(e).substring(0, 30);
    },
    noticeCreate: function (event) {
      event.preventDefault();
      axios({
        method: "post",
        // url: "http://127.0.0.1:8000/notice/",
        url: "http://i5a205.p.ssafy.io:8000/notice/",
        headers: this.headers,
        data: this.createValue,
      })
        .then((res) => {
          this.$store.dispatch("selectNotice", res.data);

          // 파일 저장
          if (this.files) {
            var formData = new FormData();
            formData.append("files", this.files);

            for (var i = 0; i < this.files.length; i++) {
              formData.append("files", this.files[i]);
            }

            axios({
              method: "post",
              // url: `http://127.0.0.1:8000/notice/file/${res.data.id}/`,
              url: `http://i5a205.p.ssafy.io:8000/notice/file/${res.data.id}/`,
              data: formData,
              headers: { "Content-Type": "multipart/form-data" },
            })
              .then(function (res) {
                console.log(res);
                console.log("SUCCESS!!");
              })
              .catch(function (err) {
                console.log(err);
              });
          }

          this.$router.push({ name: "NoticeView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    handleFileUpload() {
      this.files = this.$refs.files.files;
    },
  },
  computed: {
    ...mapState(["headers"]),
  },
  created: function () {
    this.setToken();
  },
};
</script>

<style>
#noticeCreateForm #select {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeCreateForm #noticeTitle {
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

#noticeCreateForm #isImportant {
  position: absolute;
  left: 100px;
  top: 135px;
}

#noticeCreateForm #select {
  position: absolute;
  left: 250px;
  top: 130px;
  width: 700px;
  height: 50px;
  font-size: 30px;
  padding: 5px;
  background-color: rgb(248, 236, 196);
}

.select {
  width: 80px;
  padding: 5px;
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
  max-height: 220px;
  min-height: 220px;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeCreateForm #fileUploadTitle {
  position: absolute;
  left: 100px;
  top: 445px;
  background-color: transparent;
}

#noticeCreateForm #files {
  position: absolute;
  left: 250px;
  top: 440px;

  max-width: 700px;
  min-width: 700px;

  background-color: rgb(248, 236, 196);
  border-radius: 13px;

  text-align: left;
  padding-left: 15px;
  padding: 10px;
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