<template>
  <div id="class" style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>

    <h1 id="title">우리반 친구들</h1>

    <div id="teacher" class="d-flex">
      <img id="teacher-img" src="@/assets/owl.png" alt="프로필"/>
      <div id="teacher-form">
        <h3 id="class-num">{{teacher.class}}</h3>
        <div class="d-flex">
          <h2 id="teacher-name">{{teacher.name}}</h2>
          <h3 id="teacher-title">담임 선생님</h3>
        </div>
        <h3 id="call">전화 번호 : {{teacher.number}}</h3>
      </div>
      <button id="teacher-button" href="#">메시지 보내기</button>
    </div>
    <div id="content" class="d-flex flex-wrap justify-content-start flex-row">
    </div>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'
import Whale from '@/assets/whale.png'
import Beaver from '@/assets/beaver.png'
import Cat from '@/assets/cat.png'
import Elephant from '@/assets/elephant.png'
import Frog from '@/assets/frog.png'
import Koala from '@/assets/koala.png'
// import Owl from '@/assets/owl.png'
import Shark from '@/assets/shark.png'
import Sheep from '@/assets/sheep.png'
import Squirrel from '@/assets/squirrel.png'

export default {
  name: 'Class',
  data() {
    return{
      teacher: {
        name: '유재석',
        number: '02-123-4567',
        class: '2학년 2반'
      },
      students: [
        {name: '김우진', number: '1234'}, 
        {name: '목상원', number: '2341'}, 
        {name: '정희진', number: '17'}, 
        {name: '정명지', number: '45'}, 
        {name: '조동윤', number: '984'}, 
        {name: '기리보이', number: '123'}, 
        {name: '산다라박', number: '3892'}, 
        {name: '구창모', number: '1253'}, 
        {name: '권지용', number: '8342'},
        {name: '빈지노', number: '1943'}
      ]
    }
  },

  created() {
    this.$nextTick(() => {
      const cardBody = document.querySelector('#content');
      // const imgName = "@/assets/whale.png"

      cardBody.innerHTML = this.students.map((li) => {
        var img;

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
            <h3>${li.name}</h3>
            <img id="img" src=${img} alt="프로필"/>
            <br/>
            <div class="d-flex" id="button-field">
              <button href="#" id="student-button">학생정보</button>
              <button href="#" id="message-button">메시지 보내기</button>
            </div>
          </div>`;
      }).join("");
    });
  },
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>
#title {
  position: absolute;
  left: 350px;
}

#class #teacher {
  position: absolute;
  top: 90px;
  left: 24%;
  background-color: #ccf0ef;
  border-radius: 30px;
  min-width: 70%;
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
  right: 10%;
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
  left: 22%;
  min-width: 78%;
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
  border-radius: 10px;
  min-width: 60px;
  min-height: 30px;
  border: 0;
  margin-left: 12px;
}
</style>