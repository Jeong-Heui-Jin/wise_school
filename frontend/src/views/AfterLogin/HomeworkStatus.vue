<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1>{{information_homework.title}} 숙제 제출 명단</h1>

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
        @row-clicked="goHomeworkStudent"
      >
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
      homeworkInfo: [],
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
    getStudentInfo: function () {
      // 현재 숙제에 대한 정보 axios 요청
      axios({
        method: "get",
        url: `http://i5a205.p.ssafy.io:8000/homework/detail/${this.information_homework.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          // 성공한 경우 클래스 멤버 정보 axios 요청
          axios({
            method: "get",
            url: `http://i5a205.p.ssafy.io:8000/accounts/class-members/`,
            headers: this.headers,
          })
            .then((res_student) => {
              // print test
              console.log("getHomeworkStatusDetail", res);
              console.log("getStudentInfo", res_student);

              for (let i = 0; i < res.data.submithomework_count; ++i) {
                console.log(
                  "res.data.submithomework_set[i]",
                  res.data.submithomework_set[i]
                );
              }

              for (let i = 0; i < res_student.data.students.length; ++i) {
                var thisStudentSubmit = false;
                let hw;

                var submitHomeworkLength = res.data.submithomework_count;
                for (hw = 0; hw < submitHomeworkLength; ++hw) {
                  if (
                    res_student.data.students[i].id ===
                    res.data.submithomework_set[hw].student
                  ) {
                    var data={
                      homeworkInfo:res.data.submithomework_set[hw],
                      name:res_student.data.students[i].name
                    }
                    data.homeworkInfo.name=res_student.data.students[i].name;
                    this.homeworkInfo.push(data)
                    this.homeworkInfo.name=res_student.data.students[i].name
                    thisStudentSubmit = true;
                    break;
                  }
                }

                var temp = null;

                if (thisStudentSubmit) {
                  temp = {
                    studentName: res_student.data.students[i].name,
                    isSubmit: "제출",
                    submitDate: res.data.submithomework_set[hw].registertime,
                  };
                } else {
                  temp = {
                    studentName: res_student.data.students[i].name,
                    isSubmit: "미제출",
                    submitDate: "",
                  };
                }

                // temp 가공
                if (thisStudentSubmit) {
                  temp["submitDate"] =
                    temp["submitDate"].substring(5, 7) +
                    "월 " +
                    temp["submitDate"].substring(8, 10) +
                    "일 " +
                    temp["submitDate"].substring(11, 13) +
                    "시 " +
                    temp["submitDate"].substring(14, 16) +
                    "분";
                }

                this.items.push(temp);
              }
            })
            .catch((error) => {
              console.error(error);
            });
        })
        .catch((error) => {
          console.error(error);
        });
    },

    goHomeworkStudent (e) {
      if(e.isSubmit==="제출") {   // 제출자만 화면이 넘어감.
        // console.log(e.isSubmit)
        console.log(this.homeworkInfo)
        this.homeworkInfo.forEach((arr)=>{
          if(arr.name === e.studentName) {
            this.$store.dispatch("selectSubmitedHomework", arr.homeworkInfo);
            this.$router.push({ name: "HomeworkStudent" });
          }
        });
      }
    }
  },
  computed: {
    rows() {
      return this.items.length;
    },
    ...mapState(["headers", "information_homework"]),
  },
  created: function () {
    this.setToken();
    // console.log(this.information_homework);
    this.getStudentInfo();
  },
};
</script>

<style>
#homeworkStatusForm {
  position: fixed;

  max-width: 1000px;
  min-width: 1000px;
  height: 600px;

  top: 152px;
  left: 400px;

  font-size: 130%;
}
</style>