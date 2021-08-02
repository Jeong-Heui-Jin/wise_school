<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1>숙제 검사</h1>

    <!-- 번호, 숙제 제목, 종료일, 제출 -->
    <b-table id="homeworkForm" hover :items="items"></b-table>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Homework",
  data() {
    return {
      items: [
        {
          homeworkTitle: "수학익힘책 16쪽 풀기",
          endDate: "7.19(월)",
          submitInfo: "1/6",
        },
        {
          homeworkTitle: "어린왕자 읽기",
          endDate: "7.16(금)",
          submitInfo: "4/6",
        },
        {
          homeworkTitle: "수학익힘책 16쪽 풀기",
          endDate: "7.16(금)",
          submitInfo: "3/6",
        },
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
#homeworkForm {
  position: absolute;

  max-width: 70%;
  min-width: 70%;
  max-height: 75%;
  min-height: 75%;

  top: 112px;
  left: 25%;
}
</style>