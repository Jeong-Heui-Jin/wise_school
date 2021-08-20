<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavBar />
    <NavSideBar />

    <h1 id="homeworkTitle">숙제 검사</h1>

    <!-- Homework Create Button -->
    <div v-if="now_user.usertype===1">
      <button id="homeworkCreateBtn" @click="goHomeworkCreate()">
      숙제 추가하기
      </button>
    </div>
    

    <!-- table/button/pagination div -->
    <div id="homeworkForm">
      <b-table
        id="homeworkTable my-table"
        :hover="true"
        :small="false"
        :borderless="true"
        :fields="fields"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
        @row-clicked="goHomeworkView"
      >
        <template #cell(isSubmit)="data">
          <b-button
            variant="outline-danger"
            v-if="data.item.isSubmit === '제출하기'"
            @click="goSubmit(data.item.id)"
          >
            {{ data.item.isSubmit }}</b-button
          >
          <b-button
            variant="outline-primary"
            v-if="data.item.isSubmit === '제출완료'"
            @click="goHomeworkView(data.item)"
          >
            {{ data.item.isSubmit }}</b-button
          >
        </template>
        <template #cell(submitHomework)="data">
          <b-button
            variant="outline-primary"
            @click="goHomeworkStatus(data.item)"
          >
            {{ data.item.submitHomework }}</b-button
          >
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
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "Homework",
  data: function () {
    return {
      perPage: 8,
      currentPage: 1,
      fields: [
        // Title name 변경
        { key: "id", label: "번호" },
        { key: "title", label: "숙제 제목" },
        { key: "end", label: "종료일" },
        { key: "submitHomework", label: "제출 인원" },
        { key: "isSubmit", label: "제출 현황" },
      ],
      items: [],
      classNum: 1,
      // usertype: this.now_user.usertype,
      isSubmit: false,
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
    goSubmit: function (homework_id) {
      this.$router.push({
        name: "HomeworkSubmit",
        params: { id: homework_id },
      });
    },
    getHomeworkList: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/homework/list/",
        // url: "http://127.0.0.1:8000/homework/list/",
        headers: this.headers,
      })
        .then((res) => {
          if (this.now_user.usertype === 2) {
            this.fields.splice(3, 1); // 제출인원 탭 제거
            // print
            // console.log(this.fields);
          } else {
            this.fields.splice(4, 1); // 제출현황 탭 제거
            // print
            // console.log(this.fields);
          }
          console.log("res.data in axios get :", res.data);
          for (let i = 0; i < res.data.length; ++i) {
            // console.log("hi");
            temp = {
              id: res.data[i].id,
              // 글자수 30자 이상이면 ... 표시
              title:
                res.data[i].title.length < 30
                  ? res.data[i].title
                  : res.data[i].title.substring(0, 30) + "...",
              end: res.data[i].end,
              submitHomework:
                String(res.data[i].submithomework_count) +
                "/" +
                String(this.classNum),
              isSubmit: "제출하기",
            };
            // console.log("this.now_user.usertype :", this.now_user.usertype);
            if (this.now_user.usertype === 2) {
              // console.log(this.fields);
              for (let j = 0; j < res.data[i].submithomework_set.length; ++j) {
                if (
                  res.data[i].submithomework_set[j].student === this.now_user.id
                ) {
                  temp["isSubmit"] = "제출완료";
                  break;
                }
              }
            }

            // console.log(temp);
            this.items.push(temp);
          }

          // 모든 items의 end 데이터를 가공한다.
          for (let i = 0; i < this.items.length; ++i) {
            var temp = this.items[i].end;

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
          // console.log("this.items :", this.items);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goHomeworkCreate: function () {
      window.open("/homework_create", "_self");
    },
    goHomeworkView: function (homework) {
      console.log("homework :", homework);
      this.$store.dispatch("selectHomework", homework);
      this.$router.push({ name: "HomeworkView" });
    },
    goHomeworkStatus: function (info_homework) {
      this.$store.dispatch("selectInfoHomework", info_homework);
      this.$router.push({ name: "HomeworkStatus" });
    },
    getClassNum: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/class-members/",
        headers: this.headers,
      })
        .then((res) => {
          // this.$store.dispatch("selectInfoHomework", info_homework);
          // console.log("res :", res);
          // 선생님을 제외한 학생의 수 저장
          this.classNum = res.data.students.length;
          // console.log("this.classNum :", this.classNum);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    rows() {
      return this.items.length;
    },
    ...mapState(["headers", "now_user"]),
  },
  created: function () {
    this.setToken();
    this.getHomeworkList();
    this.getClassNum();
    // this.usertype = this.now_user.usertype;
    // this.now_user.usertype = 2;
  },
};
</script>

<style>
#homeworkTitle {
  position: fixed;
  top: 10px;
  left: 120px;
  margin-left: 220px;
  margin-top: 20px;
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

#homeworkForm #paginationForm {
  /* position: absolute; */
  /* left: 220px; */
  /* align: center; */
  bottom: 50px;
}
</style>