<template>
  <div id="timetable" style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <!-- 페이지 제목 -->
    <h1 id="title"> {{ timetable.Title }}</h1>
    <b-container id="timetable-content">
      <!-- 요일 -->
      <b-row class="period" >
        <b-col class="subject" style="padding-bottom: 20px;"> </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">월</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">화</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">수</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">목</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">금</b-col>
      </b-row>
      <!-- 과목 -->
      <b-row class="period 1-class" v-if="period >= 1">
        <b-col class="subject">
          1교시
          <div class="time">09:00 ~ 09:40</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
      <b-row class="period 2-class" v-if="period >= 2">
        <b-col class="subject">
          2교시
          <div class="time">09:50 ~ 10:30</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
      <b-row class="period 3-class" v-if="period >= 3">
        <b-col class="subject">
          3교시
          <div class="time">10:40 ~ 11:20</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
      <b-row class="period 4-class" v-if="period >= 4">
        <b-col class="subject">
          4교시
          <div class="time">11:30 ~ 12:10</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
      <b-row class="period 5-class" v-if="period >= 5">
        <b-col class="subject">
          5교시
          <div class="time">13:00 ~ 13:40</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
      <b-row class="period 6-class" v-if="period >= 6">
        <b-col class="subject">
          6교시
          <div class="time">13:50 ~ 14:30</div>
        </b-col>
        <b-col class="subject"><div id="mon"></div></b-col>
        <b-col class="subject"><div id="tue"></div></b-col>
        <b-col class="subject"><div id="wed"></div></b-col>
        <b-col class="subject"><div id="thu"></div></b-col>
        <b-col class="subject"><div id="fri"></div></b-col>
      </b-row>
    </b-container>
    <div id="button-form">
      <button style="background-color: #74a7fe" @click="$router.push('/timetable_change')">수정하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBarTeacher.vue'
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
      period: 0,
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
          console.log(res.data);
          this.period=res.data.details.length;

          for (var i = 0; i < res.data.details.length; i++) {
            const timetableBody = document.getElementsByClassName(res.data.details[i].period+'-class');

            console.log(res.data.details[i].period+'-class');
            console.log(timetableBody[0]);
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
  },
  mounted() {
    this.setToken()
    this.getTimetable()
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {

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

#timetable-content .subject {
  min-width: 40px;
  font-size: 40px;
  text-align: center;
  padding-top: 20px;
  border: 1px solid black;
}

#timetable-content .time {
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