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
    <b-form id="changeForm" @submit.stop.prevent>
      <!-- 새 비밀번호 입력 -->
      <b-form-input
        v-model="newPassword"
        type="password"
        id="textNewPassword"
        placeholder="새 비밀번호 입력"
        size="lg"
        :state="validationNewPassword"
      >
      </b-form-input>
      <b-form-invalid-feedback :state="validationNewPassword">
        비밀번호는 영소문자/숫자/특수문자(!,@,#,$,%,^,&,*)로 구성된 7~16글자여야
        합니다.
      </b-form-invalid-feedback>

      <!-- 새 비밀번호 재확인 -->
      <b-form-input
        v-model="checkPassword"
        type="password"
        id="textCheckPassword"
        placeholder="새 비밀번호 입력 확인"
        size="lg"
        :state="validationCheckPassword"
      >
      </b-form-input>
      <b-form-invalid-feedback :state="validationCheckPassword">
        변경한 비밀번호와 같은 값을 입력해야합니다!
      </b-form-invalid-feedback>

      <!-- 비밀번호 검증 문자 -->
      <b-button block variant="warning" id="changeBtn" @click="changePassword()">비밀번호 변경</b-button>
    </b-form>
  </div>
</template>

<script>
import Logo from "@/components/Logo";
export default {
  name: "PasswordChange",
  data: () => ({
    newPassword: "",
    checkPassword: "",
  }),
  components: {
    Logo,
  },
  methods: {
    changePassword: function() {
      window.open("/login", "_self");
    }
  },
  computed: {
    validationNewPassword() {
      if (7 <= this.newPassword.length && this.newPassword.length <= 16) {
        for (var i = 0; i < this.newPassword.length; ++i) {
          if (
            ("a" <= this.newPassword[i] && this.newPassword[i] <= "z") ||
            ("0" <= this.newPassword[i] && this.newPassword[i] <= "9") ||
            this.newPassword[i] === "!" ||
            this.newPassword[i] === "@" ||
            this.newPassword[i] === "#" ||
            this.newPassword[i] === "$" ||
            this.newPassword[i] === "%" ||
            this.newPassword[i] === "^" ||
            this.newPassword[i] === "&" ||
            this.newPassword[i] === "*"
          ) {
            return true;
          }
          return false;
        }
      }
      return false;
    },
    validationCheckPassword() {
      if (this.newPassword === this.checkPassword) {
        if (this.newPassword.length < 7 || 16 < this.newPassword.length) {
          return false;
        }
        return true;
      }
      return false;
    },
  },
};
</script>

<style>
#changeForm {
  max-width: 500px;
  max-height: 250px;
  min-height: 250px;
  background-color: #ccf0ef;
  border-radius: 20px;
}

#changeForm #textNewPassword {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#changeForm #textCheckPassword {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#changeForm #changeBtn {
  min-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}

#changeForm #link {
  min-width: 400px;
  margin: 0px auto;
  margin-top: 20px;
}
</style>