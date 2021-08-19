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
      <b-row class="period" v-for="detail in timetableDetail" :key="detail.time">
        <b-col class="subject" id="time">
          {{detail.time}}교시
          <div id="term">
            시작
            <input
            type="time"
            class="time-picker-start"
            id="startDate"
            name="trip-start"
            v-model="detail.start"
            /> 
          </div>
          <div id="term">
              종료
              <input
                type="time"
                class='time-picker-end'
                id="endDate"
                name="trip-start"
                v-model="detail.end"
              />
          </div>
        </b-col>
        <b-col class="subject"><b-form-input class="subject-input" id="mon" :value="detail.mon" :class="`${detail.time}`"></b-form-input></b-col>
        <b-col class="subject"><b-form-input class="subject-input" id="tue" :value="detail.tue" :class="`${detail.time}`"></b-form-input></b-col>
        <b-col class="subject"><b-form-input class="subject-input" id="wed" :value="detail.wed" :class="`${detail.time}`"></b-form-input></b-col>
        <b-col class="subject"><b-form-input class="subject-input" id="thu" :value="detail.thu" :class="`${detail.time}`"></b-form-input></b-col>
        <b-col class="subject"><b-form-input class="subject-input" id="fri" :value="detail.fri" :class="`${detail.time}`"></b-form-input></b-col>
        <b-col class="button-field"><button @click="changeTimetableContent" :id="detail.time">수정하기</button></b-col>
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
    this.getTimetable()
    var arr = [];
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
  },
  methods: {
    setToken: function () {
        this.$store.dispatch('setToken')
    },
    changeTimetableContent(e) {
        console.log(e.target.parentElement);
        const day=["mon","tue","wed",'thu','fri'];
        const data={
          start: document.getElementsByClassName('time-picker-start')[Number(e.target.id)-1].value+":00.000000",
          end: document.getElementsByClassName('time-picker-end')[Number(e.target.id)-1].value+":00.000000",
        };
        console.log(document.getElementsByClassName('time-picker-start')[Number(e.target.id)-1].value);
        this.timetableDetail.forEach((detail)=>{
          if(detail.time=== Number(e.target.id)) {
            data.targetId=detail.id;
          }
        });
        document.getElementsByClassName(e.target.id).forEach((el,idx)=>{
          if(!el.value) {
            if(!confirm("빈 칸이 존재합니다. 이대로 수정 할까요?"))
              return;
          }
          data[`${day[idx]}`] = el.value;
        });

        // do update
        // axios update -> id === Period
        axios({
            method: "put",
            url: `http://i5a205.p.ssafy.io:8000/classroom/timetable-detail/${data.targetId}/`,
            headers: this.headers,
            data: {
              time: e.target.id,
              mon: data.mon,
              tue: data.tue,
              wed: data.wed,
              thu: data.thu,
              fri: data.fri,
              end: data.end,
              start: data.start,
            },
        })
        .then(() => {
            alert('수정되었습니다.');
        })
        .catch((err) => {
            console.log(err);
        });
    },
    // 시간표 삭제하기 버튼 함수
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
    },

    // 시간표 제목 바꾸기 버튼 함수
    changeTimetableTitle: function () {
      axios({
          method: "put",
          url: `http://i5a205.p.ssafy.io:8000/classroom/timetable/`,
          headers: this.headers,
          data: {
            id:this.timetable.id,
            title:document.getElementById('timetableTitle').value,
            classroom_id:this.now_user.classroom,
          },
      })
      .then(() => {
          alert('등록되었습니다');
      })
      .catch((err) => {
          console.log(err);
      });
    },
    // 시간표 한 줄 추가
    addTimetable() {
        this.timetableDetail.push({
          id:1,
          mon:"1",
          tue:"1",
          wed:'1',
          thu:'1',
          fri:'1',
          start:"1",
          end:"1",
          time:`${this.timetableDetail.length+1}`,
        })
        // const timetableBody = document.getElementsByClassName(this.timetableDetail.length+'-class');
        // console.log(timetableBody[0].children[1].children[0].value.length);

        // if (timetableBody[0].children[1].children[0].value.length > 0 &&
        //     timetableBody[0].children[2].children[0].value.length > 0 &&
        //     timetableBody[0].children[3].children[0].value.length > 0 &&
        //     timetableBody[0].children[4].children[0].value.length > 0 &&
        //     timetableBody[0].children[5].children[0].value.length > 0) {
        //     if (this.timetableDetail.length <= 5) {
        //         this.timetableDetail.push({Period: this.timetableDetail.length + 1, Monday: '', Tuesday: '', Wednesday: '', Thursday: '', Friday: ''});
        //     }
        //     else {
        //         alert('더 이상 추가할 수 없습니다');
        //     }
        // }
        // else {
        //     alert('빈칸을 채워주세요');
        // }
    },

    getTimetable: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/classroom/timetable/',
        headers: this.headers,
      })
        .then((res) => {
          this.timetable.Title = res.data.title
          this.timetable.id = res.data.id
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
  },
  computed: {
      ...mapState([
          'headers',
          'now_user',
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

#timetable-change #time {
  font-size: 20px;
  padding: 10px;
}

#timetable-change .subject-input {
  font-size: 22px !important;
  text-align: center;
}

#timetable-change .subject {
  font-size: 27px;
}

#timetable-change #term {
  font-size: 10px;
}

#timetable-change .time-picker {
  width:80% !important;
  font-size: 10px;
}
</style>