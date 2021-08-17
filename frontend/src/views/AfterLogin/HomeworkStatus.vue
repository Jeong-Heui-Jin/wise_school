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

      studentInfo: null,
      homeworkInfo: null,
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
        // url: `http://127.0.0.1:8000/homework/submit-detail/${this.infomation_homework.id}/`,
        // url: `http://i5a205.p.ssafy.io:8000/homework/submit-detail/73/`,
        url: `http://i5a205.p.ssafy.io:8000/homework/detail/73/`,
        headers: this.headers,
      })
        .then((res) => {
          this.homeworkInfo = res.data;
          console.log("getHomeworkStatusDetail :", this.homeworkInfo);
          // console.log("ininsssss", this.studentInfo);
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
          this.studentInfo = res.data;
          console.log("getStudentInfo :", this.studentInfo);
          // console.log("ininhhhh", this.homeworkInfo);

          var temp = null;
          for (let i = 0; i < this.studentInfo.students.length; ++i) {
            console.log("야호");
            for (
              let hw = 0;
              hw < this.homeworkInfo.submithomework_count;
              ++hw
            ) {
              if (
                this.studentInfo.students[i].id ===
                this.homeworkInfo.submithomework_set[hw].id
              ) {
                temp = {
                  studentName: this.studentInfo.students[i].name,
                  isSubmit: true,
                  submitDate:
                    this.homeworkInfo.submithomework_set[hw].registertime,
                };

                this.items.push(temp);
              } else {
                temp = {
                  studentName: this.studentInfo.students[i].name,
                  isSubmit: false,
                  submitDate: "",
                };

                this.items.push(temp);
              }
            }
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(["headers", "infomation_homework"]),
  },
  created: function () {
    this.setToken();
    // console.log(this.infomation_homework);
    this.getHomeworkStatusDetail();
    this.getStudentInfo();
  },
};
</script>
