<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="title">숙제 작성</h1>

    <!-- 작성 Form -->
    <b-form id="noticeCreateForm">
      <!-- 제목 -->
      <h2 id="sub-title" style="font-size: 32px;">제목</h2>
      <b-form-input id="titleName"></b-form-input>

      <!-- 내용 -->
      <h2 id="content" style="font-size: 32px;">내용</h2>
      <b-form-textarea id="contentText"></b-form-textarea>

      <!-- 취소/저장 버튼 -->
      <button id="saveBtn">저장</button>
      <button id="cancelBtn">취소</button>
    </b-form>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "HomeworkCreate",
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
#homeworkTitle {
  position: absolute;
  left: 350px;
}

#noticeCreateForm {
  position: absolute;
  left: 350px;
  min-width: 1000px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeCreateForm #sub-title {
  position: absolute;
  left: 50px;
  top: 70px;
}

#noticeCreateForm #titleName {
  position: absolute;
  left: 180px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeCreateForm #content {
  position: absolute;
  left: 50px;
  top: 180px;
}

#noticeCreateForm #contentText {
  position: absolute;
  left: 180px;
  top: 180px;

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
  top: 520px;
  left: 600px;

  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#noticeCreateForm #saveBtn {
  position: absolute;
  top: 520px;
  left: 300px;

  border-radius: 12px;
  border: 0px;
  color: rgb(38, 38, 255);
  background-color: #a8aafd;

  min-width: 11%;
}
</style>