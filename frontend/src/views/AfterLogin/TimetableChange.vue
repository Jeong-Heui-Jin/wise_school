<template>
  <div id="timetable-change" style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <!-- 페이지 제목 -->
    <div class="d-flex" 
    style="position: absolute; left: 350px; top: 30px; background-color: #e0edd4; border-radius: 20px; min-width: 350px; min-height: 80px; padding-left: 10px;">
        <p style="font-size: 32px; margin-top: auto; margin-bottom: auto; margin-right: 15px;">제목 : </p>
        <b-form-input 
        id="timetableTitle" 
        style="margin-top: auto; margin-bottom: auto; min-width:250px; max-width:250px; max-height: 50px; min-height: 50px; font-size: 20px; background-color: #e0edd4; border: 0px;" 
        placeholder="시간표 제목(수정 희망 시)">
        </b-form-input>
    </div>
    <button
    style="position: absolute; left: 750px;border: 0px; top: 80px; border-radius: 5px; min-width: 80px; min-height: 30px;"
    @click="changeTimetableTitle">
    수정하기</button>
    <b-container class="timetable-change-content">
      <!-- 요일 -->
      <b-row class="period" >
        <b-col class="subject" style="padding-bottom: 20px;"> </b-col>
        <b-col class="subject" style="padding-bottom: 20px;">월</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">화</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">수</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">목</b-col>
        <b-col class="subject" style="padding-bottom: 20px;">금</b-col>
        <b-col></b-col>
      </b-row>
      <!-- 과목 -->
      <b-row class="period 1-class" v-if="timetableDetail.length >= 1">
        <b-col class="subject">
          1교시
          <div class="time">09:00 ~ 09:40</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="1">수정하기</button></b-col>
      </b-row>
      <b-row class="period 2-class" v-if="timetableDetail.length >= 2">
        <b-col class="subject">
          2교시
          <div class="time">09:50 ~ 10:30</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="2">수정하기</button></b-col>
      </b-row>
      <b-row class="period 3-class" v-if="timetableDetail.length >= 3">
        <b-col class="subject">
          3교시
          <div class="time">10:40 ~ 11:20</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="3">수정하기</button></b-col>
      </b-row>
      <b-row class="period 4-class" v-if="timetableDetail.length >= 4">
        <b-col class="subject">
          4교시
          <div class="time">11:30 ~ 12:10</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="4">수정하기</button></b-col>
      </b-row>
      <b-row class="period 5-class" v-if="timetableDetail.length >= 5">
        <b-col class="subject">
          5교시
          <div class="time">13:00 ~ 13:40</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="5">수정하기</button></b-col>
      </b-row>
      <b-row class="period 6-class" v-if="timetableDetail.length >= 6">
        <b-col class="subject">
          6교시
          <div class="time">13:50 ~ 14:30</div>
        </b-col>
        <b-col class="subject"><b-form-input id="mon"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="tue"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="wed"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="thu"></b-form-input></b-col>
        <b-col class="subject"><b-form-input id="fri"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" id="6">수정하기</button></b-col>
      </b-row>
    </b-container>
    
    <div id="button-form">
      <button style="background-color: #74a7fe" @click="$router.push('/timetable')">시간표 보기</button>
      <br/>
      <button style="background-color: #f8fadb" @click="addTimetable">추가하기</button>
        <br/>
      <button style="background-color: #ff8c82" @click="deleteTimeTable">삭제하기</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBar.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex';

export default {
  name: 'TimetableChange',
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
      ],
    }
  },
  mounted() {
    //   
    //   처음에 한번만 axios로 timetableDetail에 데이터 받아와주세용!
    // 

      for (var i = 0; i < this.timetableDetail.length; i++) {
          const classBody = document.getElementsByClassName(this.timetableDetail[i].Period + '-class');

          classBody[0].children[1].children[0].value=this.timetableDetail[i].Monday;
          classBody[0].children[2].children[0].value=this.timetableDetail[i].Tuesday;
          classBody[0].children[3].children[0].value=this.timetableDetail[i].Wednesday;
          classBody[0].children[4].children[0].value=this.timetableDetail[i].Thursday;
          classBody[0].children[5].children[0].value=this.timetableDetail[i].Friday;
      }
  },
  methods: {
    setToken: function () {
        this.$store.dispatch('setToken')
    },
    changeTimetableContent(e) {
        console.log(e.target.id);
        // console.log(e.target.parentElement.parentElement.children[1].children[0]);
        if (e.target.parentElement.parentElement.children[1].children[0].value.length <= 0) {
            alert('빈칸이 존재합니다')
        } 
        else if (e.target.parentElement.parentElement.children[2].children[0].value.length <= 0) {
            alert('빈칸이 존재합니다')
        } 
        else if (e.target.parentElement.parentElement.children[3].children[0].value.length <= 0) {
            alert('빈칸이 존재합니다')
        } 
        else if (e.target.parentElement.parentElement.children[4].children[0].value.length <= 0) {
            alert('빈칸이 존재합니다')
        } 
        else if (e.target.parentElement.parentElement.children[5].children[0].value.length <= 0) {
            alert('빈칸이 존재합니다')
        } 
        else {
            // do update
            // axios update -> id === Period
            axios({
                method: "put",
                url: `http://i5a205.p.ssafy.io:8000/classroom/timetable-detail/${e.id}/`,
                headers: this.headers,
                data: {},
            })
                .then((res) => {
                    console.log(res.data)
                    alert('수정되었습니다.');
                })
                .catch((err) => {
                    console.log(err);
                });
        }
    },
    // 시간표 삭제하기 버튼 함수
    deleteTimeTable() {
        
    },

    // 시간표 제목 바꾸기 버튼 함수
    changeTimetableTitle: function () {
      // axios({
      //     method: "put",
      //     url: `http://i5a205.p.ssafy.io:8000/classroom/timetable/`,
      //     headers: this.headers,
      //     data: {},
      // })
      //     .then((res) => {
      //         console.log(res.data)
      //         alert('등록되었습니다');
      //     })
      //     .catch((err) => {
      //         console.log(err);
      //     });
    },
    // 시간표 한 줄 추가
    addTimetable() {
        const timetableBody = document.getElementsByClassName(this.timetableDetail.length+'-class');
        console.log(timetableBody[0].children[1].children[0].value.length);

        if (timetableBody[0].children[1].children[0].value.length > 0 &&
            timetableBody[0].children[2].children[0].value.length > 0 &&
            timetableBody[0].children[3].children[0].value.length > 0 &&
            timetableBody[0].children[4].children[0].value.length > 0 &&
            timetableBody[0].children[5].children[0].value.length > 0) {
            if (this.timetableDetail.length <= 5) {
                this.timetableDetail.push({Period: this.timetableDetail.length + 1, Monday: '', Tuesday: '', Wednesday: '', Thursday: '', Friday: ''});
            }
            else {
                alert('더 이상 추가할 수 없습니다');
            }
        }
        else {
            alert('빈칸을 채워주세요');
        }
    },
  },
  computed: {
      ...mapState([
          'headers'
      ]),
  },
  created: function() {
      this.setToken()
  }
};
</script>

<style>
.timetable-change-content {
  position: absolute;
  top: 150px;
  left: 350px;
  max-width: 800px;
  min-width: 800px;
  width: 800px;
}

.timetable-change-content .subject {
  min-width: 130px;
  max-width: 130px;
  font-size: 32px;
  text-align: center;
  padding-top: 20px;
  border: 1px solid black;
}

.timetable-change-content .time {
  font-size: 15px;
}

#timetable-change #button-form {
  position: absolute;
  top: 150px;
  left: 1250px;
}

#timetable-change #button-form button {
  width: 130px;
  height: 50px;
  border-radius: 10px;
  margin-bottom: 20px;
  border: 0px;
  font-size: 24px;
}

#timetable-change .subject #mon{
    margin-top: auto; 
    margin-bottom: auto; 
    min-width:100px; 
    max-width:100px; 
    max-height: 60px; 
    min-height: 60px; 
    font-size: 32px; 
    border: 0px;
}
#timetable-change .subject #tue{
    margin-top: auto; 
    margin-bottom: auto; 
    min-width:100px; 
    max-width:100px; 
    max-height: 60px; 
    min-height: 60px; 
    font-size: 32px; 
    border: 0px;
}
#timetable-change .subject #wed{
    margin-top: auto; 
    margin-bottom: auto; 
    min-width:100px; 
    max-width:100px; 
    max-height: 60px; 
    min-height: 60px; 
    font-size: 32px; 
    border: 0px;
}
#timetable-change .subject #thu{
    margin-top: auto; 
    margin-bottom: auto; 
    min-width:100px; 
    max-width:100px; 
    max-height: 60px; 
    min-height: 60px; 
    font-size: 32px; 
    border: 0px;
}
#timetable-change .subject #fri{
    margin-top: auto; 
    margin-bottom: auto; 
    min-width:100px; 
    max-width:100px; 
    max-height: 60px; 
    min-height: 60px; 
    font-size: 32px; 
    border: 0px;
}

#timetable-change .period .button-field{
    margin-top: auto;
    min-width: 80px;
    max-width: 80px;
}

#timetable-change .period button{
    border: 0px;
    border-radius: 5px;
    min-width: 80px;
    min-height: 30px;
}
</style>