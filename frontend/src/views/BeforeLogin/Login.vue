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
        v-model="userId"
        id="textId"
        placeholder="아이디"
        size="lg"
      ></b-form-input>


      <!-- 비밀번호 입력 폼 -->
      <b-form-input
        v-model="userPassword"
        type="password"
        id="textPassword"
        placeholder="비밀번호"
        size="lg"
      ></b-form-input>
      
      <b-button block variant="warning" id="loginBtn" @click="login()">로그인</b-button>
      <b-row id="link">
        <b-col id="linkBtn"><b-button variant="link" href="password_reset">비밀번호 변경</b-button></b-col>
        <b-col>|</b-col>
        <b-col id="linkBtn"><b-button variant="link" href="service_request">서비스 신청</b-button></b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
import Logo from "@/components/Logo.vue"
export default {
  name: "Login",
  data() {
    return {
      userId: "",
      userPassword: "",
    };
  },
  components: {
    Logo,
  },
  methods: {
    login: function() {
      // 로그인 반환 결과 (0 : 관리자, 1 : 선생님, 2 : 학생)
      window.open('/home')
    }
  }
};
</script>

<style>
#loginForm {
  max-width: 500px;
  min-width: 500px;
  max-height: 250px;
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
