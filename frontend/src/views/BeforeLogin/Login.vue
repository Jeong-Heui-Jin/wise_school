<template>
  <div
    class="fixed-top d-flex align-items-center justify-content-center background-color"
    style="bottom: 0; overflow-y: auto; font-family: 'Jua', sans-serif;"
  >
    <Logo/>
    <b-form 
    id="loginForm"
    @submit.stop.prevent
    >
      <!-- ID 입력 폼 -->
      <b-form-input
        v-model="loginCredentials.username"
        id="textId"
        placeholder="아이디"
        size="lg"
      ></b-form-input>
      <p style="color: red; text-align: left; padding: 0.2rem 0 0 3.2rem; margin: 0px;" id="error" v-if="isIdNull"> {{idMessage}} </p>
      <!-- 비밀번호 입력 폼 -->
      <b-form-input
        v-model="loginCredentials.password"
        type="password"
        id="textPassword"
        placeholder="비밀번호"
        size="lg"
        @keypress.enter="login"
      ></b-form-input>
      <p style="color: red; text-align: left; padding: 0.2rem 0 0 3.2rem; margin: 0px;" id="error" v-if="isPasswordNull"> {{passwordMessage}} </p>
      
      <b-button block variant="warning" id="loginBtn" @click="login">로그인</b-button>
      <b-row id="link">
        <b-col id="linkBtn"><b-button variant="link" href="password_reset">비밀번호 재설정</b-button></b-col>
        <b-col>|</b-col>
        <b-col id="linkBtn"><b-button variant="link" href="service_request">서비스 신청</b-button></b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'
import Logo from "@/components/Logo.vue"

export default {
  name: "Login",
  data() {
    return {
      loginCredentials: {
        username: "",
        password: "",
      },
      isIdNull:false,
      isPasswordNull:false,
      idMessage:"아이디를 입력해주세요",
      passwordMessage:"비밀번호를 입력해주세요",
    };
  },
  components: {
    Logo,
  },
  methods: {
    login: function(event) {
      event.preventDefault()

      // 아이디 입력칸이 비어있으면 알림
      if(!this.loginCredentials.username){
        this.isIdNull=true;
        this.isPasswordNull=false;
        return;
      } else {
        this.isIdNull=false;

        // 비밀번호 입력칸이 비어있으면 알림
        if(!this.loginCredentials.password){
          this.isPasswordNull=true;
          return;
        } else {
          this.isPasswordNull = false;
        }
      }
      
      axios({
        method: 'post',
        url: 'http://i5a205.p.ssafy.io:8000/accounts/login/',
        data: this.loginCredentials,
      })
      .then((res) => {
        localStorage.setItem('jwt', res.data.token)
        window.open('/home', '_self')
      })
      .catch(err => {
        alert("로그인에 실패했습니다.")
        console.log(err)
      })

      // 로그인 반환 결과 (0 : 관리자, 1 : 선생님, 2 : 학생)
      // if (this.userId === 'admin1234' && this.userPassword === '1q2w3e4r!') {
      //   window.open('/home', '_self');
      // }
      // else {
      //   alert('로그인 실패');
      // }
    },
    isLogin: function() {
      // 로그인 되어있다면
      if(localStorage.getItem('jwt')){
          // 로컬에 저장된 토큰 삭제
          window.open('/home', '_self');
      }
    },
  },
  created: function() {
    this.isLogin();
    console.log(localStorage.getItem('jwt'));
  }
};
</script>

<style>
#loginForm {
  max-width: 500px;
  min-width: 500px;

  min-height: 250px;
  background-color: #ccf0ef;
  border-radius: 20px;
}

#loginForm #textId {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#loginForm #textPassword {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#loginForm #loginBtn {
  min-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#loginForm #link {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#loginForm #linkBtn {
  min-width: 150px;
}
</style>
