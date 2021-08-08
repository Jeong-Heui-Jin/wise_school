<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle">숙제 검사</h1>

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
        @row-clicked="goHomeworkView"
      >
        <!-- items column -->
        <template #cell(items)="data">
          <b-link>{{ data.items }}</b-link>
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
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Homework",
  data: function() {
    return {
      perPage: 8,
      currentPage: 1,
      fields: [
        // Title name 변경
        { key: "id", label: "번호" },
        { key: "title", label: "숙제 제목" },
        { key: "end", label: "종료일" },
        // { key: "submitInfo", label: "제출" },
      ],
      items: [
        // {
        //   homework_id: "17",
        //   title: "수학익힘책 16쪽 풀기",
        //   end: "7.19(월)",
        //   // submitInfo: "1/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "16",
        //   title: "어린왕자 읽기",
        //   end: "7.16(금)",
        //   // submitInfo: "4/6",
        //   content: "어린왕자 읽기",
        // },
        // {
        //   homework_id: "15",
        //   title: "알파벳 10번씩 쓰기",
        //   end: "7.16(금)",
        //   // submitInfo: "3/6",
        //   content: "알파벳 10번씩 쓰기",
        // },
        // {
        //   homework_id: "14",
        //   title: "한자 15000번 쓰기",
        //   end: "7.15(목)",
        //   // submitInfo: "2/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "13",
        //   title: "기하와 벡터 3페이지 풀어오기",
        //   end: "7.14(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "12",
        //   title: "만화책 3권 읽고 오기",
        //   end: "7.14(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "11",
        //   title: "아이유 노래 1곡 듣기",
        //   end: "7.14(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "10",
        //   title: "숙제 10",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "9",
        //   title: "숙제 9",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "8",
        //   title: "숙제 8",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "7",
        //   title: "숙제 7",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "6",
        //   title: "숙제 6",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "5",
        //   title: "숙제 5",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "4",
        //   title: "숙제 4",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "3",
        //   title: "숙제 3",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "2",
        //   title: "숙제 2",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
        // {
        //   homework_id: "1",
        //   title: "숙제 1",
        //   end: "7.13(수)",
        //   // submitInfo: "6/6",
        //   content: "수학익힘책 16쪽 풀기",
        // },
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getHomeworkList: function () {
      axios({
        method: "get",
        // url: "http://i5a205.p.ssafy.io:8081/homework/list/",
        url: 'http://127.0.0.1:8000/homework/list/',
        headers: this.setToken(),
      })
        .then((res) => {
          // console.log(res)
          this.items = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goHomeworkCreate: function () {
      window.open("/homework_create", "_self");
    },
    goHomeworkView: function (homework) {
      console.log(homework);
      this.$router.push({ name: 'HomeworkView', params:homework })
      // router.push({
      //   path: "/homework_view",
      //   query: { title: this.items.Title, Content: this.items.Content },
      // });
      // setTimeout(() => console.log("after"), 30000); // test
      // window.open("/homework_view", "_self");
    },
  },
  computed: {
    rows() {
      return this.items.length;
    },
  },
  created: function() {
    this.getHomeworkList()
  }
};
</script>

<style>
#homeworkTitle {
  position: fixed;
  top: 10px;
  left: 120px;
}

#homeworkForm {
  position: fixed;

  /* 최대 가로/세로 길이 설정 */
  /* 너비는 최소/최대 길이 동일 설정 */
  max-width: 1000px;
  min-width: 1000px;
  height: 600px;
  /* min-height: 75%; */

  top: 152px;
  left: 400px;

  /* font-size 증가 */
  font-size: 130%;
}

#homeworkForm #homeworkTable {
  position: absolute;
  top: 60px;
}

#homeworkCreateBtn {
  position: absolute;
  top: 112px;
  left: 1200px;

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