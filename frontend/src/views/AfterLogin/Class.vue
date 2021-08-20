<template>
  <div id="class" style="font-family: 'Jua', sans-serif">
    <NavBar />
    <NavSideBar />

    <h1 id="title">우리반 친구들</h1>

    <div id="teacher" class="d-flex">
      <img :src="teacher.image" id="teacher-img" alt="프로필" />
      <div id="teacher-form">
        <h3 id="class-num" style="font-size: 24px">{{ teacher.class }}</h3>
        <div class="d-flex">
          <h2 id="teacher-name" style="font-size: 36px">{{ teacher.name }}</h2>
          <h3 id="teacher-title" style="font-size: 30px">담임 선생님</h3>
        </div>
        <h3 id="call" style="font-size: 30px">
          전화 번호 : {{ teacher.number }}
        </h3>
      </div>
      <!-- <button id="teacher-button" href="#">메시지 보내기</button> -->
    </div>
    <div
      id="content"
      class="d-flex flex-wrap justify-content-start flex-row"
    ></div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBar.vue';
import NavBar from "@/components/NavBar.vue";
import { mapState } from 'vuex'

export default {
  name: "Class",
  data: function () {
    return {
      teacher: {
        name: "유재석",
        number: "02-123-4567",
        class: "2학년 2반",
        image:''
      },
      students: [],
      usertype: 2,
    };
  },

  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMembers: function () {
      axios({
        method: "get",
        // url: 'http://127.0.0.1:8000/accounts/class-members/',
        url: 'http://i5a205.p.ssafy.io:8000/accounts/class-members/',
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res.data);
          this.teacher.name = res.data.teacher.name
          this.teacher.number = res.data.teacher.phone
          this.teacher.image = res.data.teacher.image
          this.teacher.class = String(res.data.classroom.grade)[0] + "학년 " + String(res.data.classroom.grade)[2] + "반"

          this.students = Object.assign([], res.data.students);
          const cardBody = document.querySelector("#content");

          cardBody.innerHTML = this.students
          .map((li) => {
            var img;

            img = li.image;

            if (this.usertype == 1) {
              return `
              <div id="card">
                <h3>${li.name}</h3>
                <img id="img" src=${img} alt="프로필"/>
                <br/>
                <div class="d-flex" id="button-field" style="text-align: center">
                  <button onclick="window.open('/student_info/${li.id}', '_self')" id="student-button">학생정보</button>
                  <!-- <button href="#" id="message-button">메시지 보내기</button> -->
                </div>
              </div>`;
            } else {
                return `
              <div id="card">
                <h3>${li.name}</h3>
                <img id="img" src=${img} alt="프로필"/>
                <br/>
                <div class="d-flex" id="button-field">
                  <!--<button href="#" id="message-button" style="margin-left:43px;">메시지 보내기</button> -->
                </div>
              </div>`;
            }
          })
          .join("");
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  created: function() {
    this.usertype = this.now_user.usertype
    this.getMembers()
  },
  components: {
    NavSideBar,
    NavBar,
  },
  computed: {
    ...mapState([
      'headers',
      'now_user',
    ]),
  },
};
</script>

<style>
#title {
  position: absolute;
  top: 30px;
  left: 350px;
  font-size: 36px;
  min-width: 200px;
}

#class #teacher {
  position: absolute;
  top: 90px;
  left: 360px;
  background-color: #ccf0ef;
  border-radius: 30px;
  min-width: 1000px;
  min-height: 200px;
  padding: 30px;
}

#class #teacher-img {
  width: 150px;
  height: 150px;
  margin-right: 30px;
}

#class #teacher-button {
  position: absolute;
  left: 800px;
  border-radius: 10px;
  min-width: 120px;
  min-height: 50px;
  border: 0;
}

#class #teacher-form {
  min-width: 50%;
}

#class #class-num {
  margin-right: 80%;
  margin-bottom: 10px;
  width: 200px;
}

#class #teacher-name {
  margin-right: 30px;
  margin-bottom: 20px;
  width: 200px;
}

#class #call {
  width: 500px;
  margin-top: 15px;
  text-align: left;
  margin-left: 20px;
}

#class #teacher-title {
  margin-top: 7px;
  width: 200px;
}

#class #content {
  position: absolute;
  top: 300px;
  left: 350px;
  min-width: 1200px;
}

#class #card {
  margin: 30px;
  min-width: 200px;
  min-height: 200px;
  border-radius: 15px;
  padding: 10px;
}

#class #img {
  width: 120px;
  height: 120px;
  margin-bottom: 15px;
}

/* #class #button-field {

} */

#class #message-button {
  border-radius: 10px;
  min-width: 60px;
  min-height: 30px;
  border: 0;
  margin-left: 10px;
}

#class #student-button {
  position: absolute;
  border-radius: 10px;
  min-width: 60px;
  min-height: 30px;
  border: 0;
  margin-left: 60px;
}
</style>