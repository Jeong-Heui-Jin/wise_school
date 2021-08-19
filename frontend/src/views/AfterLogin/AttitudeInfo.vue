<template>
  <div
    id="attitude-info"
    style="font-family: 'Jua', sans-serif"
    variant="light"
  >
    <NavSideBar />
    <NavBar />

    <h1 id="title">{{ student.name }} 학생 태도</h1>

    <!-- Homework Create Button -->
    <button id="btn-attitude-create" @click="goAttitudeCreate">
      작성하기
    </button>
    <div class="attitude-container">
      <b-container id="attitude-container" v-if="attitudes.length > 0">
        <!-- 요일 -->
        <b-row class="attitude-title">
          <b-col cols="1">번호</b-col>
          <b-col cols="6">내용</b-col>
          <b-col cols="3">작성일</b-col>
          <b-col cols="2">작성자</b-col>
        </b-row>
        <!-- 페이지네이션 -->
        <b-row
          class="attitude-wrapper"
          v-for="attitude in attitudes.slice((currentPage-1)*perPage, currentPage*perPage>attitudes.length?attitudes.length:currentPage*perPage)"
          :key="attitude.id"
          @click="goAttitudeView(attitude)"
        >
          <b-col cols="1">{{ attitude.id }}</b-col>
          <b-col cols="6">{{ attitude.content }}</b-col>
          <b-col cols="3">{{ attitude.date }}</b-col>
          <b-col cols="2">{{ attitude.teacher }}</b-col>
        </b-row>
      </b-container>
      <div id="attitude-container" v-else>아직 작성된 내용이 없습니다.</div>
      <!-- Pagination -->
      <div id="pagination-wrapper" v-if="attitudes">
        <div class="btn-prev" v-if="currentPage==1">
          <div class="btn-block" id="btn-first">&lt;&lt;</div>
          <div class="btn-block" id="btn-prev">&lt;</div>
        </div>
        <div class="btn-prev" v-else>
          <div class="btn-page" id="btn-first" @click="selectPage(1)">&lt;&lt;</div>
          <div class="btn-page" id="btn-prev" @click="selectPage((currentPage-1)<1?1:currentPage-1)">&lt;</div>
        </div>
        <div id="btn-page-wrapper">
          <!-- <div class="btn-page" id="btn">1</div> -->
        </div>
        <div class="btn-next" v-if="currentPage===totalPage">
          <div class="btn-block" id="btn-next">&gt;</div>
          <div class="btn-block" id="btn-last">&gt;&gt;</div>
        </div>
        <div class="btn-next" v-else>
          <div class="btn-page" id="btn-next" @click="selectPage((currentPage+1)>totalPage?totalPage:currentPage+1)">&gt;</div>
          <div class="btn-page" id="btn-last" @click="selectPage(totalPage)">&gt;&gt;</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "AttitudeInfo",
  data: function() {
    return {
      student: {
        name: "",
      },
      number: "",
      attitudes: [],
      teachers: [],
      perPage: 9,
      currentPage: 1,
      totalPage:0,
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function() {
      this.$store.dispatch("setToken");
    },

    getAttitudes: async function() {
      await axios({
        method: "get",
        url: `http://i5a205.p.ssafy.io:8000/student-manage/note/${this.number}/`,
        headers: this.headers,
      })
        .then((res) => {
          this.attitudes = res.data;
          this.attitudes.forEach((attitude) => {
            const date = attitude.registertime.split("T")[0].split("-");
            attitude.date = date[0].slice(2) + "." + date[1] + "." + date[2];
            var buf = "";
            this.teachers.forEach((teacher) => {
              if (attitude.teacher === teacher.id) {
                buf = teacher.name;
              }
            });
            attitude.teacher = buf;
            attitude.name = this.student.name;
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    async getTeachers() {
      await axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/teachers/",
        headers: this.headers,
      })
        .then((res) => {
          res.data.forEach((teacher) => {
            this.teachers.push({
              name: teacher.name,
              id: teacher.id,
            });
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async getStudents() {
      await axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/students/",
        headers: this.headers,
      })
        .then((res) => {
          res.data.forEach((student) => {
            if (student.info.number === this.number) {
              this.student.name = student.name;
            }
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },

    getMembers: function() {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/accounts/class-members/",
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data);
          res.data.teacher.forEach((teacher) => {
            console.log(teacher);
            this.teachers[teacher.id] = teacher.name;
          });
          console.log(this.teachers);
          this.student = {
            name: "",
            id: "",
          };
        })
        .catch((err) => {
          console.log(err);
        });
    },

    goAttitudeCreate() {
      window.open(`/attitude_create/${this.number}`, "_self");
    },

    goAttitudeView(attitude) {
      this.$store.dispatch("selectAttitude", attitude);
      this.$router.push({ name: "AttitudeView" });
    },

    paging () {
      this.totalPage = parseInt((this.attitudes.length)/this.perPage)+1;
      for(var i=1; i<=this.totalPage; i+=1) {
        const div = document.createElement("div")
        div.classList.add("btn-page");
        div.innerHTML=i
        div.addEventListener('click', (e)=>{
          this.currentPage=Number(e.target.innerHTML);
          this.selectPage(this.currentPage)
        })
        document.getElementById("btn-page-wrapper").appendChild(div)
      }
      
      this.selectPage(1)
    },

    selectPage (num) {
      this.currentPage=num;
      document.getElementById("btn-page-wrapper").children.forEach((el)=>{
        if(Number(el.innerHTML) === this.currentPage) {
          el.classList.add("selected")
        } else {
          el.classList.remove("selected")
        }
      });
    },
  },
  computed: {
    rows() {
      return this.attitudes.length;
    },
    ...mapState(["headers"]),
  },
  created: async function() {
    this.number = Number(this.$route.params.id);
    this.setToken();
    await this.getStudents();
    await this.getTeachers();
    await this.getAttitudes();
    this.paging();
    // this.getMembers();
    // this.getHomeworkList();
  },
};
</script>

<style>
#attitude-info #btn-attitude-create {
  position: absolute;
  top: 100px;
  left: 1000px;
  font-size: 20px;
  min-width: 155px;
  color: #0101d4;
  border-radius: 20px;
  border: 0px;
  background-color: #6cbfe0;
}

#attitude-info .attitude-container {
  position: absolute;
  top: 150px;
  left: 350px;
  max-width: 800px;
  min-width: 800px;
  height:550px;
}

#attitude-info #attitude-container {
  position: absolute;
  width: 800px;
  max-width: 800px;
  min-width: 800px;
  border-bottom: 3px solid #47d4ff;
  font-size: 22px;
}

#attitude-container .attitude-title {
  border-bottom: 3px solid #47d4ff;
  padding: 0;
  color: #9c9c9c;
}

#attitude-container .attitude-wrapper {
  border-top: 1px solid #47d4ff;
  padding: 5px 0px;
}

#attitude-info #pagination-wrapper {
  position: absolute;
 bottom: 0;
 left:50%;
 transform: translateX(-50%);
  display: flex;
  min-width: 25%;
  justify-content: space-between;
}

#pagination-wrapper .btn-prev {
  display: flex;
}

#pagination-wrapper #btn-page-wrapper {
  display: flex;
  margin: 0 10px;
}

#pagination-wrapper .btn-next {
  display: flex;
}

#attitude-info .btn-page {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background-color: white;
  border: 0.5px solid gray;
  color:blue;
  text-align: center;
  font-size: 20px;
  padding: 10px 0;
  margin: 0 5px;
  cursor: pointer;
}

#attitude-info .btn-block {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background-color: white;
  border: 0.5px solid gray;
  text-align: center;
  font-size: 20px;
  padding: 10px 0;
  margin: 0 5px;
  cursor: default;
}

#attitude-info .btn-page:hover {
 background-color: #cacaca; 
}

#attitude-info .selected {
  background-color: #385dff !important;
  color: white !important;
}

#attitude-info .btn-page:active {
 box-shadow: 0 0 5px 2px #385dff;
}
</style>
