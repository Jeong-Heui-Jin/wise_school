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
      <b-row id="period" v-for="detail in timetableDetail" :key="detail.Period">
        <b-col id="subject">
          {{detail.Period}}교시
          <div id="time" v-if="detail.Period === '1'">09:00 ~ 09:40</div>
          <div id="time" v-else-if="detail.Period === '2'">09:50 ~ 10:30</div>
          <div id="time" v-else-if="detail.Period === '3'">10:40 ~ 11:20</div>
          <div id="time" v-else-if="detail.Period === '4'">11:30 ~ 12:10</div>
          <div id="time" v-else-if="detail.Period === '5'">13:00 ~ 13:40</div>
          <div id="time" v-else-if="detail.Period === '6'">13:50 ~ 14:30</div>
        </b-col>
        <b-col id="subject">{{detail.Monday}}</b-col>
        <b-col id="subject">{{detail.Tuesday}}</b-col>
        <b-col id="subject">{{detail.Wednesday}}</b-col>
        <b-col id="subject">{{detail.Thursday}}</b-col>
        <b-col id="subject">{{detail.Friday}}</b-col>
      </b-row>
    </b-container>
    <div id="button-form">
      <button style="background-color: #74a7fe" @click="$router.push('/timetable_change')">수정하기</button>
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
        {Period : '1', Monday: '국어', Tuesday: '체육', Wednesday: '영어', Thursday: '사회', Friday: '수학'},
        {Period : '2', Monday: '수학', Tuesday: '영어', Wednesday: '체육', Thursday: '국어', Friday: '과학'},
        {Period : '3', Monday: '음악', Tuesday: '국어', Wednesday: '국어', Thursday: '수학', Friday: '도덕'},
        {Period : '4', Monday: '과학', Tuesday: '과학', Wednesday: '음악', Thursday: '체육', Friday: '미술'},
        {Period : '5', Monday: '사회', Tuesday: '사회', Wednesday: '창체', Thursday: '체육', Friday: '국어'},
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
        url: 'http://i5a205.p.ssafy.io:8000/classroom/timetable/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
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
  },
  mounted() {
      var arr = [];
      var color = ["lightblue", "lightcyan", "lightgoldenrodyellow", "lightseagreen", "lightyellow", "lightsalmon", "palegreen", "paleturquoise", "papayawhip", "lightpink"];
      const subject = document.querySelectorAll('#subject');

      for (var i = 0; i < this.timetableDetail.length; i++) {
        if (!arr.find(e => e === this.timetableDetail[i].Monday)) {
          arr.push(this.timetableDetail[i].Monday);
        }
        if(!arr.find(e => e === this.timetableDetail[i].Tuesday)) {
          arr.push(this.timetableDetail[i].Tuesday);
        }
        if(!arr.find(e => e === this.timetableDetail[i].Wednesday)) {
          arr.push(this.timetableDetail[i].Wednesday);
        }
        if(!arr.find(e => e === this.timetableDetail[i].Thursday)) {
          arr.push(this.timetableDetail[i].Thursday);
        }
        if(!arr.find(e => e === this.timetableDetail[i].Friday)) {
          arr.push(this.timetableDetail[i].Friday);
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