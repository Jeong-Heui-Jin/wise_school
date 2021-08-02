<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle">숙제 검사</h1>

    <!-- 설정 목록
    :hover -> 마우스 포인터를 어디 올렸는지 표시
    :small -> table의 사이즈를 작게할 것인지(false 처리)
    :borderless -> border 없앰
    -->

    <!-- table/button/pagination div -->
    <div id="homeworkForm">
      <b-table
        id="homeworkTable"
        :hover="true"
        :small="false"
        :borderless="true"
        :items="items"
        :fields="fields"
      >
        <!-- 번호 column -->
        <template #cell(index)="data">
          {{ data.index + 1 }}
        </template>

        <!-- items column -->
        <template #cell(items)="data">
          {{ data.items }}
        </template>
      </b-table>

      <!-- Homework Create Button -->
      <button id="homeworkCreateBtn" @click="goHomeworkCreate()">
        숙제 추가하기
      </button>

      <!-- Pagination -->
      <div class="mt-3">
        <b-pagination
          id="paginationForm"
          v-model="currentPage"
          pills
          :total-rows="rows"
        ></b-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Homework",
  data() {
    return {
      rows: 100,
      currentPage: 1,
      fields: [
        // Title name 변경
        { key: "index", label: "번호" },
        { key: "Title", label: "숙제 제목" },
        { key: "EndTime", label: "종료일" },
        { key: "submitInfo", label: "제출" },
      ],
      items: [
        {
          Title: "수학익힘책 16쪽 풀기",
          EndTime: "7.19(월)",
          submitInfo: "1/6",
        },
        {
          Title: "어린왕자 읽기",
          EndTime: "7.16(금)",
          submitInfo: "4/6",
        },
        {
          Title: "알파벳 10번씩 쓰기",
          EndTime: "7.16(금)",
          submitInfo: "3/6",
        },
        {
          Title: "한자 15000번 쓰기",
          EndTime: "7.15(목)",
          submitInfo: "2/6",
        },
        {
          Title: "기하와 벡터 3페이지 풀어오기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
        {
          Title: "만화책 3권 읽고 오기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
        {
          Title: "아이유 노래 1곡 듣기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    goHomeworkCreate: function () {
      window.open("/homework_create", "_self");
    },
  },
};
</script>

<style>
#homeworkTitle {
  position: absolute;
  left: 22%;
}

#homeworkForm {
  position: fixed;

  /* 최대 가로/세로 길이 설정 */
  /* 너비는 최소/최대 길이 동일 설정 */
  width: 1100px;
  height: 600px;
  /* min-height: 75%; */

  top: 112px;
  left: 370px;

  /* font-size 증가 */
  font-size: 130%;
}

#homeworkForm #homeworkTable {
  position: absolute;
  top: 60px;
}

#homeworkForm #homeworkCreateBtn {
  position: absolute;
  top: 5px;
  left: 900px;

  min-width: 155px;

  border-radius: 10px;
  background-color: #dcffaa;
}

#homeworkForm #paginationForm {
  position: absolute;

  left: 27%;
  bottom: 5%;
}
</style>