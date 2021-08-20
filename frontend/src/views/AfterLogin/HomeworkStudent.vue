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
        <!-- <img style="height:300px;width:600px; margin:10px; background-color:white;" :src="selected_submited_homework.submithomeworkfile_set[0].image" alt=""> -->
      </div>

      <button id="btn-cancel" @click="goHomeworkStatus">닫기</button>
    </div>
  </div>
</template>

<script>
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
    setToken: function () {
      this.$store.dispatch("setToken");
    },

    goHomeworkStatus: function (homework) {
      this.$store.dispatch("selectHomework", homework);
      this.$router.push({ name: "HomeworkStatus" });
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
  min-height: 100px;

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
</style>