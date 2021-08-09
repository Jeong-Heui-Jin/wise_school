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
    <b-container id="timetable-change-content">
      <!-- 요일 -->
      <b-row id="period" >
        <b-col id="subject" style="padding-bottom: 20px;"> </b-col>
        <b-col id="subject" style="padding-bottom: 20px;">월</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">화</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">수</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">목</b-col>
        <b-col id="subject" style="padding-bottom: 20px;">금</b-col>
        <b-col></b-col>
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
        <b-col id="subject"><b-form-input 
        style="margin-top: auto; margin-bottom: auto; min-width:100px; max-width:140px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;" 
        v-model="detail.Monday">
        </b-form-input></b-col>
        <b-col id="subject"><b-form-input 
        style="margin-top: auto; margin-bottom: auto; min-width:100px; max-width:140px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;" 
        v-model="detail.Tuesday">
        </b-form-input></b-col>
        <b-col id="subject"><b-form-input 
        style="margin-top: auto; margin-bottom: auto; min-width:100px; max-width:140px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;" 
        v-model="detail.Wednesday">
        </b-form-input></b-col>
        <b-col id="subject"><b-form-input 
        style="margin-top: auto; margin-bottom: auto; min-width:100px; max-width:140px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;" 
        v-model="detail.Thursday">
        </b-form-input></b-col>
        <b-col id="subject"><b-form-input 
        style="margin-top: auto; margin-bottom: auto; min-width:100px; max-width:140px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;" 
        v-model="detail.Friday">
        </b-form-input></b-col>
        <b-col style="margin-top: auto;"><button
        style="border: 0px; border-radius: 5px; min-width: 80px; min-height: 30px;"
        @click="changeTimetableContent()">
        수정하기</button></b-col>
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
// import axios from "axios";
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'
// import { mapState } from 'vuex';

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
      ]
    }
  },
  methods: {
    // getTimetable: function () {
    //   axios({
    //     method: "get",
    //     // url: "http://i5a205.p.ssafy.io:8000/homework/list/",
    //     url: 'http://127.0.0.1:8000/classroom/timetable/1/',
    //     // headers: this.headers,
    //     // data: this.createValue,
    //   })
    //     .then((res) => {
    //       console.log(res)
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
    // 
    changeTimetableContent() {
        console.log('HI');
        // console.log(e.Target);
    },
    // 시간표 삭제하기 버튼 함수
    deleteTimeTable() {

    },

    // 시간표 제목 바꾸기 버튼 함수
    changeTimetableTitle() {

    },
    addTimetable() {
        // const parentInfo = document.querySelectorAll('#parent-info');

        // if (parentInfo.length === 2) {
        //     alert('더 이상 추가할 수 없습니다');
        // }
        // else {
            //             <div id="time" v-if="detail.Period === '1'">09:00 ~ 09:40</div>
            // <div id="time" v-else-if="detail.Period === '2'">09:50 ~ 10:30</div>
            // <div id="time" v-else-if="detail.Period === '3'">10:40 ~ 11:20</div>
            // <div id="time" v-else-if="detail.Period === '4'">11:30 ~ 12:10</div>
            // <div id="time" v-else-if="detail.Period === '5'">13:00 ~ 13:40</div>
            // <div id="time" v-else-if="detail.Period === '6'">13:50 ~ 14:30</div>
        const timetableGraph = document.getElementById('timetable-change-content');

        timetableGraph.insertAdjacentHTML('beforeend', `
            <b-row id="period">
                <b-col id="subject" style="min-width: 100px; font-size: 32px; text-align: center; padding-top: 20px; border: 1px solid black; min-height: 80px;">
                교시
                </b-col>
                <b-col id="subject"><input 
                style="margin-top: auto; margin-bottom: auto; min-width:120px; max-width:120px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;"/>
                </b-col>
                <b-col id="subject"><input 
                style="margin-top: auto; margin-bottom: auto; min-width:120px; max-width:120px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;"/>
                </b-col>
                <b-col id="subject"><input 
                style="margin-top: auto; margin-bottom: auto; min-width:120px; max-width:120px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;"/>
                </b-col>
                <b-col id="subject"><input 
                style="margin-top: auto; margin-bottom: auto; min-width:120px; max-width:120px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;"/>
                </b-col>
                <b-col id="subject"><input 
                style="margin-top: auto; margin-bottom: auto; min-width:120px; max-width:120px; max-height: 60px; min-height: 60px; font-size: 32px; border: 0px;"/>
                </b-col>
                <b-col style="margin-top: auto;">
                <button onclick="changeTimetableContent()" style="border: 0px; border-radius: 5px; min-width: 80px; min-height: 30px;">
                수정하기</button></b-col>
            </b-row>`);
    },
  }
};
</script>

<style>
#timetable-change-content {
  position: absolute;
  top: 150px;
  left: 350px;
  width: 800px;
  max-width: 900px;
  min-width: 900px;
}

#timetable-change-content #subject {
  min-width: 100px;
  font-size: 32px;
  text-align: center;
  padding-top: 20px;
  border: 1px solid black;
}

#timetable-change-content #time {
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
</style>