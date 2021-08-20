<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <!-- 작성 Form -->
    <b-form id="noticeViewForm">
      <h1 id="noticeViewTitle">공지 보기</h1>
      <!-- 제목 -->
      <h2 id="sub-title">제목</h2>
      <b-form-input readonly id="titleName" v-model="notice.title">{{
        notice.title
      }}</b-form-input>

      <h2 id="endTitle">등록날짜</h2>
      <b-form-input readonly id="endDate" v-model="notice.registertime">
        {{ notice.registertime }}
      </b-form-input>
      <!-- <input type="date" id="endDate" name="trip-start" /> -->

      <!-- 내용 -->
      <h2 id="content">내용</h2>
      <b-form-textarea
        readonly
        id="contentText"
        plaintext
        v-model="notice.content"
        >{{ notice.content }}</b-form-textarea
      >

      <!-- 이미지 -->
      <div>
        <b-button id="fileBtn" v-b-modal.modal-center>첨부파일</b-button>
        
        <b-modal id="modal-center" scrollable centered no-fade title="첨부 사진"
          size="lg"
        >
          <form ref="form" style="text-align: center;">
            <div v-if="images.length==0">
              첨부파일이 없습니다.
            </div>
            <div v-else>
              <ul>
                <li v-for="image in images" :key="image">
                  <img :src="image">
                </li>
              </ul>
            </div>
          </form>
        </b-modal>
      </div>
      <!-- 취소/수정/삭제 버튼 -->
      <b-button id="cancelBtn" @click="goNotice">목록</b-button>
      <!-- <button id="changeBtn">수정</button> -->
      <button id="deleteBtn" @click="deleteNotice">삭제하기</button>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "NoticeView",
  components: {
    NavSideBar,
    NavBar,
  },
  data: function () {
    return {
      notice: {},
      images:[]
    };
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    getNoticeDetail: function () {
      // const notice = this.selected_notice;
      // console.log(notice_id); // undefined
      axios({
        method: "get",
        // url: `http://127.0.0.1:8000/notice/detail/${this.notice.id}/`,
        url: `http://i5a205.p.ssafy.io:8000/notice/detail/${this.notice.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          // console.log("res.data :", res.data);
          this.notice = res.data;

          // 모든 notice의 registertime 데이터를 가공한다.
          var temp = this.notice.registertime;
          // console.log(temp);
          for(let i=0;i<this.notice.noticefile_set.length;i++){
            this.images.push(this.notice.noticefile_set[i].image);
          }

          this.notice.registertime =
            temp.substring(5, 7) +
            "월 " +
            temp.substring(8, 10) +
            "일 " +
            temp.substring(11, 13) +
            "시 " +
            temp.substring(14, 16) +
            "분";
          // console.log("this.notice :", this.notice);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goNotice: function () {
      this.$router.push({ name: "Notice" });
    },
    deleteNotice: function (e) {
      // console.log(this.notice.id)
      e.preventDefault();
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/notice/${this.notice.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Notice" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(["headers", "selected_notice"]),
  },
  created: function () {
    this.setToken();
    this.notice = this.selected_notice;
    for(let i=0;i<this.notice.noticefile_set.length;i++){
      this.images.push(this.notice.noticefile_set[i].image);
    }
  },
};
</script>

<style>
#noticeViewForm {
  position: fixed;

  width: 1100px;
  height: 600px;

  top: 112px;
  left: 370px;

  background-color: #e0edd4;
  border-radius: 10px;

  font-size: 160%;
}

#noticeViewForm #noticeViewTitle {
  position: fixed;
  top: 10px;
  left: 120px;
  margin-left: 220px;
  margin-top: 20px;
}

#noticeViewForm #sub-title {
  position: absolute;
  left: 100px;
  top: 70px;
}

#noticeViewForm #titleName {
  position: absolute;
  left: 250px;
  top: 60px;

  width: 700px;
  font-size: 100%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeViewForm #endTitle {
  position: absolute;
  left: 100px;
  top: 135px;
}

#noticeViewForm #endDate {
  position: absolute;
  left: 250px;
  top: 135px;

  width: 700px;
  font-size: 90%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeViewForm #content {
  position: absolute;
  left: 100px;
  top: 200px;
}

#noticeViewForm #contentText {
  position: absolute;
  left: 250px;
  top: 200px;

  max-width: 700px;
  min-width: 700px;
  max-height: 300px;
  min-height: 300px;

  padding: 10px;

  font-size: 80%;

  background-color: rgb(248, 236, 196);
  border-radius: 10px;
}

#noticeViewForm #cancelBtn {
  position: absolute;
  top: 530px;
  left: 650px;

  border-radius: 12px;
  border: 0px;
  /* color: red;
  background-color: #fcb6b6; */
  color: rgb(0, 87, 46);
  background-color: #b6e0fc;

  min-width: 11%;
}

#noticeViewForm #fileBtn {
  position: absolute;
  top: 530px;
  left: 350px;

  border-radius: 12px;
  border: 0px;
  color: rgb(0, 87, 46);
  background-color: #b6e0fc;

  min-width: 11%;
}

#noticeViewForm #changeBtn {
  position: absolute;
  top: 17px;
  left: 965px;

  border-radius: 7px;
  border: 0px;
  color: rgb(190, 140, 32);
  background-color: rgb(249, 249, 252);

  font-size: 60%;

  min-width: 5%;
}

#noticeViewForm #deleteBtn {
  position: absolute;
  top: 17px;
  left: 980px;

  border-radius: 7px;
  border: 0px;
  /* color: rgb(190, 140, 32); */
  /* background-color: rgb(249, 249, 252); */
  background-color: #fcb6b6;
  color: white;
  font-size: 60%;
  vertical-align: auto;

  width: 70px;
  height: 35px;
}
</style>