<template>
  <div
    class="
      fixed-top
      d-flex
      align-items-center
      justify-content-center
      background-color
    "
    style="bottom: 0; overflow-y: auto; font-family: 'Jua', sans-serif"
  >
    <Logo />
    <b-form id="resetForm" @submit.stop.prevent>
      <!-- 아이디 -->
      <b-form-input v-model="userId" id="textId" placeholder="아이디" size="lg">
      </b-form-input>

      <!-- 이름 -->
      <b-form-input
        v-model="userName"
        id="textPassword"
        placeholder="이름"
        size="lg"
      >
      </b-form-input>

      <!-- 연락처 -->
      <b-form-input
        v-model="userPhone"
        id="textPhone"
        placeholder="연락처"
        size="lg"
      >
      </b-form-input>

      <!-- 비밀번호 검증 문자 -->
      <b-button block variant="warning" id="resetBtn" href="password_change"
        >비밀번호 재설정</b-button
      >
      <b-row id="link">
        <b-col><b-button variant="link" href="login">로그인</b-button></b-col>
        <b-col>|</b-col>
        <b-col
          ><b-button variant="link" href="service_request"
            >서비스 신청</b-button
          ></b-col
        >
      </b-row>
    </b-form>
  </div>
</template>

<script>
import Logo from "@/components/Logo";
export default {
  name: "PasswordReset",
  data: () => ({
    userId: "",
    userName: "",
    userPhone: "",
  }),
  components: {
    Logo,
  },
};
</script>



<style>
#resetForm {
  min-width: 500px;
  max-height: 350px;
  min-height: 350px;
  background-color: #ccf0ef;
  border-radius: 20px;
}

#resetForm #textId {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#resetForm #textPassword {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#resetForm #textPhone {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#resetForm #resetBtn {
  min-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#resetForm #link {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}
</style>