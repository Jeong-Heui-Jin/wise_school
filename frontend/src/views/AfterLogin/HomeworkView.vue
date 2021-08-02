<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle">숙제 보기</h1>

    <!-- 작성 Form -->
    <b-form id="noticeViewForm">
      <!-- 제목 -->
      <h2 id="title">제목</h2>
      <b-form-input id="titleName"></b-form-input>

      <!-- 내용 -->
      <h2 id="content">내용</h2>
      <b-form-textarea id="contentText"></b-form-textarea>

      <!-- 취소/저장 버튼 -->
      <button id="cancelBtn">취소</button>
      <button id="changeBtn">수정</button>
    </b-form>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "HomeworkView",
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
#homeworkTitle {
  position: absolute;
  left: 22%;
}

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

#noticeViewForm #title {
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

#noticeViewForm #content {
  position: absolute;
  left: 100px;
  top: 220px;
}

#noticeViewForm #contentText {
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

#noticeViewForm #cancelBtn {
  position: absolute;
  top: 90%;
  left: 36%;

  border-radius: 12px;

  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#noticeViewForm #changeBtn {
  position: absolute;
  top: 90%;
  left: 53%;

  border-radius: 12px;

  color: rgb(38, 38, 255);
  background-color: #a8aafd;

  min-width: 11%;
}
</style>