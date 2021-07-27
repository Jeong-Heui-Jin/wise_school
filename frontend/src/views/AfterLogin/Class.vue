<template>
  <div id="class" style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>

    <h1 id="title">우리반 친구들</h1>

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
          <button href="#" id="button">메시지 보내기</b-button>
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
  left: 22%;
}

#class #content {
  position: absolute;
  top: 10%;
  left: 22%;
  min-width: 78%;
}

#class #card {
  margin: 30px;
  min-width: 200px;
  min-height: 200px;
}

#class #img {
  width: 120px;
  height: 120px;
  margin-bottom: 15px;
}

#class #button {
  border-radius: 5px;
  min-width: 60px;
  min-height: 30px;
  border: 0;
}
</style>