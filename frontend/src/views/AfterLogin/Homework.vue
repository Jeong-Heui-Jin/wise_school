<template>
  <div
    class="fixed-top d-flex align-items-center justify-content-center"
    id="homeworkBaseForm"
    style="font-family: 'Jua', sans-serif"
    variant="light"
  >
    <!-- <NavSideBar />
    <NavBar /> -->

    <h1 id="title">숙제 검사</h1>

    <div>
      <!-- Homework Create Button -->
      <button id="homeworkCreateBtn" @click="goHomeworkCreate()">
        숙제 추가하기
      </button>

      <!-- table/button/pagination div -->
      <div id="homeworkForm">
        <b-table
          id="homeworkTable my-table"
          :hover="true"
          :small="false"
          :borderless="true"
          :items="items"
          :fields="fields"
          :per-page="perPage"
          :current-page="currentPage"
        >
          <!-- 번호 column -->
          <!-- <template #cell(index)="data">
          {{ data.index + 1 }}
        </template> -->

          <!-- items column -->
          <template #cell(items)="data">
            {{ data.items }}
          </template>
        </b-table>

        <!-- Pagination -->
        <b-pagination
          id="paginationForm"
          pills
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
          align="center"
        ></b-pagination>
      </div>
    </div>

    <div></div>
  </div>
</template>

<script>
// import NavSideBar from "@/components/NavSideBarTeacher.vue";
// import NavBar from "@/components/NavBar.vue";

export default {
  name: "Homework",
  data() {
    return {
      perPage: 8,
      currentPage: 1,
      fields: [
        // Title name 변경
        { key: "homework_id", label: "번호" },
        { key: "Title", label: "숙제 제목" },
        { key: "EndTime", label: "종료일" },
        { key: "submitInfo", label: "제출" },
      ],
      items: [
        {
          homework_id: "17",
          Title: "수학익힘책 16쪽 풀기",
          EndTime: "7.19(월)",
          submitInfo: "1/6",
        },
        {
          homework_id: "16",
          Title: "어린왕자 읽기",
          EndTime: "7.16(금)",
          submitInfo: "4/6",
        },
        {
          homework_id: "15",
          Title: "알파벳 10번씩 쓰기",
          EndTime: "7.16(금)",
          submitInfo: "3/6",
        },
        {
          homework_id: "14",
          Title: "한자 15000번 쓰기",
          EndTime: "7.15(목)",
          submitInfo: "2/6",
        },
        {
          homework_id: "13",
          Title: "기하와 벡터 3페이지 풀어오기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "12",
          Title: "만화책 3권 읽고 오기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "11",
          Title: "아이유 노래 1곡 듣기",
          EndTime: "7.14(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "10",
          Title: "숙제 10",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "9",
          Title: "숙제 9",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "8",
          Title: "숙제 8",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "7",
          Title: "숙제 7",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "6",
          Title: "숙제 6",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "5",
          Title: "숙제 5",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "4",
          Title: "숙제 4",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "3",
          Title: "숙제 3",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "2",
          Title: "숙제 2",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
        {
          homework_id: "1",
          Title: "숙제 1",
          EndTime: "7.13(수)",
          submitInfo: "6/6",
        },
      ],
    };
  },
  components: {
    // NavSideBar,
    // NavBar,
  },
  methods: {
    goHomeworkCreate: function () {
      window.open("/homework_create", "_self");
    },
  },
  computed: {
    rows() {
      return this.items.length;
    },
  },
};
</script>

<style>
#homeworkBaseForm {
  background-color: white;
}

#homeworkBaseForm #title {
  position: fixed;
  top: 10px;
  /* left: 22%; */
}

#homeworkForm {
  /* position: fixed; */

  /* 최대 가로/세로 길이 설정 */
  /* 너비는 최소/최대 길이 동일 설정 */
  max-width: 1000px;
  min-width: 1000px;
  height: 600px;
  /* min-height: 75%; */

  top: 112px;
  left: 350px;

  /* font-size 증가 */
  font-size: 130%;
}

#homeworkForm #homeworkTable {
  position: absolute;
  top: 60px;
}

#homeworkCreateBtn {
  /* position: absolute;
  top: 112px;
  left: 1200px; */

  min-width: 155px;

  border-radius: 10px;
  border: 0px;
  background-color: #dcffaa;
}

#paginationForm {
  /* position: absolute; */
  /* left: 220px; */
  /* align: center; */
  bottom: 50px;
}
</style>