<template>
  <div id="attitude" style="font-family: 'Jua', sans-serif">
    <NavSideBar/>
    <NavBar/>
    <h1 id="title">학생 태도 관리</h1>
    <div id="attitude-content" class="d-flex flex-wrap justify-content-start flex-row">

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavSideBar from '@/components/NavSideBar.vue';
import NavBar from '@/components/NavBar.vue';
import { mapState } from 'vuex';
import Whale from "@/assets/whale.png";
import Beaver from "@/assets/beaver.png";
import Cat from "@/assets/cat.png";
import Elephant from "@/assets/elephant.png";
import Frog from "@/assets/frog.png";
import Koala from "@/assets/koala.png";
import Shark from "@/assets/shark.png";
import Sheep from "@/assets/sheep.png";
import Squirrel from "@/assets/squirrel.png";

export default {
  name: 'Attitude',
  components: {
    NavSideBar,
    NavBar
  },
  data: function() {
    return {
      students: [
        // { name: "김우진", number: "1234" },
        // { name: "목상원", number: "2341" },
        // { name: "정희진", number: "17" },
        // { name: "정명지", number: "45" },
        // { name: "조동윤", number: "984" },
        // { name: "기리보이", number: "123" },
        // { name: "산다라박", number: "3892" },
        // { name: "구창모", number: "1253" },
        // { name: "권지용", number: "8342" },
        // { name: "빈지노", number: "1943" },
      ],
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getMembers: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/accounts/class-members/',
        headers: this.headers,

      })
      .then((res) => {
        res.data.students.forEach((student)=>{
          if(student.usertype === 2){
            this.students.push({
              id:student.id,
              name:student.name,
              number:student.info.number,

            })
          }
        })
        
        this.$nextTick(() => {
          const attitudeBody = document.querySelector("#attitude-content");
          // const imgName = "@/assets/whale.png"

          attitudeBody.innerHTML = this.students
            .map((li) => {
              var img;
              console.log(li)
              if (Number(li.number) % 9 === 0) {
                img = Whale;
              } else if (Number(li.number) % 9 === 1) {
                img = Beaver;
              } else if (Number(li.number) % 9 === 2) {
                img = Cat;
              } else if (Number(li.number) % 9 === 3) {
                img = Elephant;
              } else if (Number(li.number) % 9 === 4) {
                img = Frog;
              } else if (Number(li.number) % 9 === 5) {
                img = Koala;
              } else if (Number(li.number) % 9 === 6) {
                img = Shark;
              } else if (Number(li.number) % 9 === 7) {
                img = Sheep;
              } else {
                img = Squirrel;
              }
              return `
              <div id="card">
                <img src=${img} alt="프로필"/>
                <br/>
                <h3>${li.name}</h3>
                <button onclick="window.open('/attitude_info/${li.number}', '_self')" id="student-button">보기</button>
              </div>`;
            })
            .join("");
        })
      })
      .catch((err) => {
        console.log(err);
      });
    },
    // getAttitudes: function () {
    //   axios({
    //     method: "get",
    //     url: 'http://i5a205.p.ssafy.io:8000/student-manage/note/1/',
    //     headers: this.headers,
    //   })
    //     .then((res) => {
    //       console.log(res.data)
    //       // this.items = res.data
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // }
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {
    this.setToken()
    // this.getAttitudes()
    this.getMembers()
  },
  mounted() {

  }
}
</script>

<style>
#attitude #card img{
  width: 120px;
  height: 120px;
  margin-bottom: 15px;
}

#attitude-content{
  position: absolute;
  left: 350px;
  top: 90px;
}

#attitude-content #card{
  min-width: 200px;
  margin: 20px;
  padding: 30px;
  border-radius: 20px;
  background-color: #e0edd4;
}

#attitude-content button{
  min-width: 100px;
  min-height: 20px;
  border: 0px;
  border-radius: 5px;
  background-color: #fff2d5;
}
</style>