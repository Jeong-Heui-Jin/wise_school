<template>
  <!-- 선생님 페이지 -->
  <div
    style="font-family: 'Jua', sans-serif"
    variant="light"
    v-if="this.now_user.usertype === 1"
    id="homework-student"
  >
    <NavSideBar />
    <NavBar />

    <h1 id="homeworkTitle">{{selected_submited_homework.name}} 친구의 숙제</h1>

    <div id="homework-wrapper">
      <div id="homework-content-wrapper">
        <div id="homework-content-title">내용</div>
        <textarea readonly id="homework-content-text" v-model="selected_submited_homework.content"></textarea>
      </div>
      <div id="homework-file-wrapper" v-if="selected_submited_homework.submithomeworkfile_set">
        <img :src="selected_submited_homework.submithomeworkfile_set[0].image" alt="">
      </div>

      <button id="btn-cancel" @click="goHomeworkStatus">닫기</button>
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
      text:"adsfasdfa",
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
          console.log("res.data :", res.data);
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
            // console.log(temp);
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
    },
    goHomeworkStatus: function (homework) {
      this.$store.dispatch("selectHomework", homework);
      this.$router.push({ name: "HomeworkStatus" });
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
    ...mapState(["headers", "now_user","information_homework", "selected_submited_homework"]),
  },
  created: function () {
    this.setToken();
    this.getClassNum();
    console.log(this.selected_submited_homework.submithomeworkfile_set[0].image)
  },
};
</script>

<style>
#homeworkTitle {
  position: fixed;
  top: 10px;
  left: 120px;
}

#homework-student #homework-wrapper{
  position:absolute;
  display: flex;
  flex-direction: column;

  top: 112px;
  left: 370px;

  max-width: 700px;
  min-width: 700px;

  min-height: 300px;

  padding: 30px 40px;
  border-radius: 20px;

  background-color: #dcffaa;
}

#homework-wrapper #homework-content-wrapper{
  text-align: left;
  width: 100%;
}

#homework-content-wrapper #homework-content-title {
  font-size: 25px;
  margin: 0 0px 5px 10px;
}

#homework-content-wrapper #homework-content-text {
  width: 100%;
  min-height: 300px;

  border-radius: 20px;
  padding: 15px;

  font-size: 25px;

  resize: none;
}

#homework-content-wrapper #homework-content-text:focus {
  outline: none;
}

#homework-wrapper #btn-cancel {
  border-radius: 12px;
  border: 0px;
  color: red;
  background-color: #fcb6b6;

  min-width: 11%;
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