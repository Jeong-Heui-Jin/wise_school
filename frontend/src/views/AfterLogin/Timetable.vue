<template>
  <div id="timetable" style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <!-- 페이지 제목 -->
    <h1 id="title"> {{ timetable.Title }}</h1>
    <b-container id="timetable-content">
      <!-- 요일 -->
      <b-row id="period" >
        <b-col id="subject" style="padding-bottom: 20px;"> </b-col>
        <b-col id="subject" style="padding-bottom: 20px;">월</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">화</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">수</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">목</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">금</b-col>
      </b-row>
      <!-- 과목 -->
      <b-row id="period" v-for="detail in timetableDetail" :key="detail.time">
        <b-col id="subject">
          {{detail.time}}교시
          <div id="time">{{ detail.start }} ~ {{ detail.end }}</div>
        </b-col>
        <b-col id="subject">{{detail.mon}}</b-col>
        <b-col id="subject">{{detail.tue}}</b-col>
        <b-col id="subject">{{detail.wed}}</b-col>
        <b-col id="subject">{{detail.thu}}</b-col>
        <b-col id="subject">{{detail.fri}}</b-col>
      </b-row>
    </b-container>
    <div id="button-form">
      <button style="background-color: #74a7fe" @click="$router.push('/timetable_change')">수정하기</button>
      <button style="background-color: #74a7fe" @click="deleteTimetable">삭제하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBar.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex';

export default {
  name: 'Timetable',
  components: {
    NavSideBar,
    NavBar
  },
  data() {
    return {
      idx: 1,
      timetable: { Title: '1학기 시간표' },
      // 오름 차순 정렬 가정
      timetableDetail : [
        {time : '1', mon: '국어', tue: '체육', wed: '영어', thu: '사회', fri: '수학', start: '09:00', end: '09:50'},
      ]
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getTimetable: function () {
      axios({
        method: "get",
        url: 'http://127.0.0.1:8000/classroom/timetable/',
        // url: 'http://i5a205.p.ssafy.io:8000/classroom/timetable/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
          this.timetable.Title = res.data.title
          this.timetableDetail = res.data.details

          for (let i = 0; i < this.timetableDetail.length; ++i) {
            var start = this.timetableDetail[i].start;
            var end = this.timetableDetail[i].end;

            this.timetableDetail[i].start = start.substring(0, 5)
            this.timetableDetail[i].end = end.substring(0, 5)
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    intToRGB(i) {
        var c = (i & 0x00FFFFFF)
            .toString(16)
            .toUpperCase();

        return "00000".substring(0, 6 - c.length) + c;
    },
    deleteTimetable: function () {
      // axios({
      //   method: "get",
      //   url: 'http://127.0.0.1:8000/classroom/timetable/',
      //   // url: 'http://i5a205.p.ssafy.io:8000/classroom/timetable/',
      //   headers: this.headers,
      // })
      //   .then((res) => {
      //     console.log(res.data)
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    }
  },
  mounted() {
      var arr = [];
      var color = ["lightblue", "lightcyan", "lightgoldenrodyellow", "lightseagreen", "lightyellow", "lightsalmon", "palegreen", "paleturquoise", "papayawhip", "lightpink"];
      const subject = document.querySelectorAll('#subject');

      for (var i = 0; i < this.timetableDetail.length; i++) {
        if (!arr.find(e => e === this.timetableDetail[i].mon)) {
          arr.push(this.timetableDetail[i].mon);
        }
        if(!arr.find(e => e === this.timetableDetail[i].tue)) {
          arr.push(this.timetableDetail[i].tue);
        }
        if(!arr.find(e => e === this.timetableDetail[i].wed)) {
          arr.push(this.timetableDetail[i].wed);
        }
        if(!arr.find(e => e === this.timetableDetail[i].thu)) {
          arr.push(this.timetableDetail[i].thu);
        }
        if(!arr.find(e => e === this.timetableDetail[i].fri)) {
          arr.push(this.timetableDetail[i].fri);
        }
      }
      for (var err = 0; err < arr.length; err++) {
        // console.log(arr[err]);
      } 
      for (var sub = 0; sub < subject.length; sub++) {
        for (var find = 0; find < arr.length; find++) {
          if (subject[sub].textContent === arr[find]) {
            subject[sub].style.backgroundColor = color[find];
            // console.log(color[find]);
            break;
          }
        }
      }
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {
    this.setToken()
    this.getTimetable()
  }
}
</script>

<style>
#timetable-content {
  position: absolute;
  top: 90px;
  left: 350px;
  width: 800px;
  max-width: 800px;
  min-width: 800px;
}

#timetable-content #subject {
  min-width: 40px;
  font-size: 40px;
  text-align: center;
  padding-top: 20px;
  border: 1px solid black;
}

#timetable-content #time {
  font-size: 15px;
}

#timetable #button-form {
  position: absolute;
  top: 90px;
  left: 1200px;
}

#timetable #button-form button {
  width: 130px;
  height: 50px;
  border-radius: 10px;
  margin-bottom: 20px;
  border: 0px;
  font-size: 24px;
}
</style>