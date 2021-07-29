<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="noticeCreateTitle">공지사항 작성</h1>

    <div id="createForm">
      <h3>
        <button id="cancelBtn">취소</button>
        <button id="saveBtn">저장</button>
      </h3>
    </div>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "NoticeCreate",
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
  background-color: #f5a8a8;

  min-width: 11%;
}

#saveBtn {
  position: absolute;
  top: 90%;
  left: 53%;

  border-radius: 12px;

  color: rgb(45, 45, 255);
  background-color: #9a9cff;

  min-width: 11%;
}

#noticeCreateTitle {
  position: absolute;
  left: 22%;
}

#createForm {
  position: absolute;

  min-width: 70%;
  min-height: 550px;

  top: 112px;
  left: 25%;

  background-color: rgb(157, 230, 157);
  border-radius: 10px;
}
</style>