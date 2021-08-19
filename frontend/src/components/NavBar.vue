<template>
  <div>
    <b-navbar
      id="nav-bar"
      style="font-family: 'Jua', sans-serif"
      toggleable="lg"
      variant="faded"
      type="light"
    >
      <!-- Right aligned nav items -->
      <b-navbar-nav id="right-side" class="ml-auto">
        <img
          id="logo"
          src="@/assets/alarm.png"
          alt="알람_로고"
          @click="goNotification"
        />
        <!-- <img id="logo" src="@/assets/mail.png" alt="편지_로고" /> -->
        <b-button id="button" variant="faded" type="light" size="lg" @click="goMyPage"
          >내 정보 보기</b-button
        >
        <b-button
          id="button"
          variant="faded"
          type="light"
          size="lg"
          @click="logout"
          >로그아웃</b-button
        >
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from 'vuex';

export default {
  beforeCreate: function () {
    // jwt 없으면 login 페이지로 이동
    if (!localStorage.getItem("jwt")) {
      window.open("/login", "_self");
    }
  },
  data() {
    return {
      usertype: 1,
    }
  },
  methods: {
    setUser: function () {
      axios({
        method: 'get',
        url: 'http://i5a205.p.ssafy.io:8000/accounts/profile',
        headers: this.headers,
        })
        .then((res) => {
          this.$store.dispatch('setUser', res.data)
        })
        .catch(err => {
          console.log(err)
      });
    },
    goNotification: function() {
      window.open("/notification", "_self");
    },
    goMyPage: function() {
      if (this.now_user.usertype === 2){
        window.open("/student_info/"+this.now_user.id, "_self");
      } else {
        window.open("/mypage/"+this.now_user.id, "_self");
      }
      
    },
    logout() {
      // 로그아웃
      if (localStorage.getItem("jwt")) {
        // 로컬에 저장된 토큰 삭제
        localStorage.removeItem("jwt");
        window.open("/login", "_self");
      }
    }
  },
   mounted() {
    this.setUser();
    // console.log("여기여기", this.now_user.id)
  },
  computed: {
    ...mapState([
      'now_user'
    ]),
  }
};
</script>


<style>
#nav-bar {
  max-height: 50px;
  width: 100%;
}

#nav-bar #right-side {
  position: absolute;
  min-width: 500px;
  max-width: 500px;
  width: 500px;
  min-height: 60px;
  max-height: 60px;
  height: 60px;
  top: 10px;
  left: 1100px;
}

#nav-bar #button {
  margin-right: 10px;
  min-height: 40px;
  max-height: 40px;
  height: 40px;
  min-width: 60px;
}

#nav-bar #logo {
  margin-top: 5px;
  margin-left: 10px;
  max-height: 35px;
  min-height: 35px;
  height: 40px;
  max-width: 35px;
  min-width: 35px;
  margin-right: 30px;
}
</style>