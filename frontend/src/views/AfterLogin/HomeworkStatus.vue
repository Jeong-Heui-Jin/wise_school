<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1>안녕</h1>

    <!-- Table -->
    <div id="homeworkStatusForm">
      <b-table
        id="homeworkStatusTable my-table"
        :hover="true"
        :small="false"
        :borderless="true"
        :fields="fields"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
      >
      </b-table>

      <!-- Pagination -->
      <b-pagination
        id="paginationForm"
        pills
        v-model="currentPage"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "HomeworkStatus",
  data: function () {
    return {
      perPage: 10,
      currentPage: 1,
      fields: [
        { key: "studentName", label: "학생 이름" },
        { key: "isSubmit", label: "제출 여부" },
        { key: "submitDate", label: "제출일" },
      ],
      items: [],
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
    getHomeworkStatusDetail: function () {
      axios({
        method: "get",
        url: `http://i5a205.p.ssafy.io:8000/homework/submit-detail/1/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log("res :", res);
          // temp = {};
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getStudentInfo: function () {
      axios({
        method: "get",
        url: `http://i5a205.p.ssafy.io:8000/accounts/class-members/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log("res :", res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(["infomation_homework"]),
  },
  created: function () {
    this.setToken();
    console.log(this.infomation_homework);
    this.getHomeworkStatusDetail();
    this.getStudentInfo();
  },
};
</script>
