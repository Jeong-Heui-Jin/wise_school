<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1>숙제 검사</h1>

    <!-- 설정 목록
    :hover -> 마우스 포인터를 어디 올렸는지 표시
    :small -> table의 사이즈를 작게할 것인지
    :borderless -> border 없앰
    :items -> items에 있는 모든 데이터를 가져온다.
    -->
    <b-table
      id="homeworkForm"
      :hover="true"
      :small="false"
      :borderless="true"
      :items="items"
      :fields="fields"
    >
      <template #cell(index)="data">
        {{ data.index + 1 }}
      </template>

      <template #cell(items)="data">
        {{ data.items }}
      </template>
    </b-table>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Homework",
  data() {
    return {
      fields: [
        { key: "index", label: "번호" },
        { key: "homeworkTitle", label: "숙제 제목" },
        { key: "endDate", label: "종료일" },
        { key: "submitInfo", label: "제출" },
      ],
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
  /* min-height: 75%; */

  top: 112px;
  left: 25%;
}
</style>