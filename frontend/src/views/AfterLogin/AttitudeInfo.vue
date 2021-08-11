<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle"> </h1>

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
import { mapState } from "vuex";

export default {
  name: "AttitudeInfo",
  data: function () {
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
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    getHomeworkList: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/homework/list/',
        headers: this.headers,
      })
        .then((res) => {
          this.items = res.data;

          // 모든 items의 end 데이터를 가공한다.
          for (let i = 0; i < this.items.length; ++i) {
            var temp = this.items[i].end;
            console.log(temp);

            this.items[i].end =
              temp.substring(5, 7) +
              "월 " +
              temp.substring(8, 10) +
              "일 " +
              temp.substring(11, 13) +
              "시 " +
              temp.substring(14, 16) +
              "분";
          }
      })
        .catch((err) => {
          console.log(err);
        });
    },
    goHomeworkCreate: function () {
      window.open("/homework_create", "_self");
    },
    goHomeworkView: function (homework) {
      this.$store.dispatch('selectHomework', homework);
      this.$router.push({ name: 'HomeworkView'})
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
    ...mapState(["headers"]),
  },
  created: function () {
    this.setToken();
    this.getHomeworkList();
  },
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