<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavBar />
    <NavSideBar />

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
        <!-- <template #cell(items)="data">
          <b-link>{{ data.items.submitHomework }}</b-link>
        </template> -->

        <!-- Button -->
        <template #cell(submitHomework)="data">
          <b-button> {{ data.item.submitHomework }} </b-button>
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
import NavSideBar from '@/components/NavSideBar.vue'
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "Homework",
  data: function () {
    return {
      perPage: 10,
      currentPage: 1,
      fields: [
        // Title name 변경
        { key: "id", label: "번호" },
        { key: "title", label: "숙제 제목" },
        { key: "end", label: "종료일" },
        { key: "submitHomework", label: "제출 인원" },
      ],
      items: [],
      classNum: 1,
      usertype: 2,
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    btnClick: function () {
      console.log("아야");
    },
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    getHomeworkList: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/homework/list/",
        headers: this.headers,
      })
        .then((res) => {
          // console.log(res.data);
          for (let i = 0; i < res.data.length; ++i) {
            temp = {
              id: res.data[i].id,
              title: res.data[i].title,
              end: res.data[i].end,
              submitHomework:
                String(res.data[i].submithomework_count) +
                "/" +
                String(this.classNum),
            };
            console.log(temp);
            this.items.push(temp);
          }
          // this.items = res.data;
          // console.log(this.items);
          // console.log(this.now_user);

          // 모든 items의 end 데이터를 가공한다.
          for (let i = 0; i < this.items.length; ++i) {
            var temp = this.items[i].end;
            // console.log(temp);

            this.items[i].end =
              temp.substring(5, 7) +
              "월 " +
              temp.substring(8, 10) +
              "일 " +
              temp.substring(11, 13) +
              "시 " +
              temp.substring(14, 16) +
              "분";

            // var submit = this.items[i].submithomework_count;
            // this.items[i].submithomework_count =
            //   String(submit) + "/" + String(this.classNum);
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
      this.$store.dispatch("selectHomework", homework);
      this.$router.push({ name: "HomeworkView" });
      // router.push({
      //   path: "/homework_view",
      //   query: { title: this.items.Title, Content: this.items.Content },
      // });
      // setTimeout(() => console.log("after"), 30000); // test
      // window.open("/homework_view", "_self");
    },
    getClassNum: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/class-members/",
        headers: this.headers,
      })
        .then((res) => {
          // 선생님을 제외한 학생의 수 저장
          this.classNum = res.data.length - 1;
          console.log(this.classNum);
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
    this.usertype = this.now_user.usertype
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