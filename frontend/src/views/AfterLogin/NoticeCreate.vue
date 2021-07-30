<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="noticeCreateTitle">공지사항 작성</h1>

    <b-form id="createForm">
      <h2 id="title">제목</h2>
      <b-form-input id="titleName" size="lg"
        >8월 급식 안내 및 메뉴표</b-form-input
      >
      <h2 id="content">내용</h2>
      <b-form-textarea id="contentText"> </b-form-textarea>
      <h2 id="fileName">파일 첨부</h2>
      <input type="file" accept="image/*" id="fileUpload" />
      <!-- <button id="fileUploadBtn">파일첨부</button> -->

      <h3>
        <button id="cancelBtn">취소</button>
        <button id="saveBtn">저장</button>
      </h3>
    </b-form>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "NoticeCreate",
  data() {
    return {
      contents: `8월 1일부터 31일 까지 급식표가 첨부되어 있습니다.
        메뉴 확인 부탁드립니다.

        또한 급식비가 인상되어 기존 130,000원의 급식비가
        1,300,000원으로 변경되었으니 참고 부탁드립니다.`,
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
#cancelBtn {
  position: absolute;
  top: 90%;
  left: 36%;

  border-radius: 12px;

  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
}

#saveBtn {
  position: absolute;
  top: 90%;
  left: 53%;

  border-radius: 12px;

  color: rgb(38, 38, 255);
  background-color: #a8aafd;

  min-width: 11%;
}

#noticeCreateTitle {
  position: absolute;
  left: 22%;
}

#createForm {
  position: absolute;

  min-width: 70%;
  min-height: 75%;

  top: 112px;
  left: 25%;

  background-color: rgb(154, 201, 154);
  border-radius: 10px;
  /* z-index: 1; */

  font-size: 160%;
}

#createForm #title {
  position: absolute;
  left: 10%;
  top: 120px;
}

#createForm #titleName {
  position: absolute;
  left: 30%;
  top: 110px;

  width: 42vw;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
  /* z-index: 0; */
}

#content {
  position: absolute;
  left: 10%;
  top: 220px;
}

#contentText {
  position: absolute;
  left: 30%;
  top: 220px;

  max-width: 60%;
  min-width: 60%;
  min-height: 40%;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#fileName {
  position: absolute;
  left: 10%;
  top: 560px;
}

#fileUpload {
  position: absolute;
  left: 30%;
  top: 560px;

  max-width: 60%;
  min-width: 60%;

  background-color: rgb(248, 236, 196);
  border-radius: 13px;

  text-align: left;
  padding-left: 15px;
}

#fileUploadBtn {
  position: absolute;
  left: 85%;

  min-width: 14%;

  background-color: rgb(187, 187, 187);
  border-radius: 13px;

  font-size: 80%;
}
</style>