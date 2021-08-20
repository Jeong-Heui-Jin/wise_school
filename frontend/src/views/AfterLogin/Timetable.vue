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
      <!-- <b-row class="period 1-class" v-if="period >= 1">
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
        <b-col class="subject"><div id="fri"></div></b-col> -->
      <b-row class="period" v-for="detail in timetableDetail" :key="detail.time">
        <b-col class="subject" id="lunch-time" v-if="detail.time==5">
          점심시간
          <div id="time">{{ timetableDetail[3].end }} ~ {{ detail.start }}</div>
        </b-col>

        <div class="w-100"></div>
        <b-col class="subject">
          {{detail.time}}교시
          <div id="time">{{ detail.start }} ~ {{ detail.end }}</div>
        </b-col>
        <b-col class="subject" :class="detail.mon">{{detail.mon}}</b-col>
        <b-col class="subject" :class="detail.tue">{{detail.tue}}</b-col>
        <b-col class="subject" :class="detail.wed">{{detail.wed}}</b-col>
        <b-col class="subject" :class="detail.thu">{{detail.thu}}</b-col>
        <b-col class="subject" :class="detail.fri">{{detail.fri}}</b-col>
      </b-row>      
    </b-container>
    <div id="button-form">
      <button v-if="now_user.usertype===1" style="background-color: #74a7fe" @click="$router.push('/timetable_change')">수정하기</button>
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
      ],
      color:[
        "#D8C8B2",
        "#DDE7E7",
        "#b3a6c9",
        "#F8E77F",
        "#F7B938",
        "#fecdf3",
        "#e3cdfe",
        "#cddefe",
        "#5AC6D0",
        "#defecd",
        "#5DC19B",
        "#C0D84D",
        "#aafdea",
        "#81c199",
        "#9ED6C0",
        "#e5f8ff",
        "#ff7595",
        "#F15B5B",
        "#ffcfb8",
        "#ffd6e2",
        "#fde7f3",
        "#BE577B",
        "#E0709B",
      ],
      subject:[],
      top:0,
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getTimetable: function () {
      axios({
        method: "get",
        // url: 'http://127.0.0.1:8000/classroom/timetable/',
        url: 'http://i5a205.p.ssafy.io:8000/classroom/timetable/',
        headers: this.headers,
      })
        .then((res) => {
          // console.log(res.data);
          // this.period=res.data.details.length;

          // for (var i = 0; i < res.data.details.length; i++) {
          //   const timetableBody = document.getElementsByClassName(res.data.details[i].period+'-class');

          //   console.log(res.data.details[i].period+'-class');
          //   console.log(timetableBody[0]);
          // console.log(res.data)
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
    adjustColor() {
      this.timetableDetail.forEach((detail)=>{
        if(!this.subject[detail.mon]) {
          this.subject[detail.mon]=this.color[this.top%21];
          this.top++;
        }
        if(!this.subject[detail.tue]) {
          this.subject[detail.tue]=this.color[this.top%21];
          this.top++;
        }
        if(!this.subject[detail.wed]) {
          this.subject[detail.wed]=this.color[this.top%21];
          this.top++;
        }
        if(!this.subject[detail.thu]) {
          this.subject[detail.thu]=this.color[this.top%21];
          this.top++;
        }
        if(!this.subject[detail.fri]) {
          this.subject[detail.fri]=this.color[this.top%21];
          this.top++;
        }
      });
      var keys = Object.keys(this.subject)
      keys.forEach((subject)=>{
        document.getElementsByClassName(subject).forEach((el)=>{
          el.style.backgroundColor=this.subject[subject];

        });
      });
    }
  },
  mounted() {
    this.setToken()
    this.getTimetable()
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
      'headers',
      'now_user',
    ]),
  },
  created: function() {

  },
  updated() {
    this.adjustColor();
  },
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
  font-size: 32px;
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

#timetable #time {
  font-size: 16px;
}

#timetable #lunch-time {
  padding:0 !important;
  font-size: 32px;
  background-color: blanchedalmond;
}

</style>