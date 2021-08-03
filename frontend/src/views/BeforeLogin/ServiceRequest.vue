<template>
  <div
    id="requestForm"
    class="fixed-top d-flex align-items-center justify-content-center background-color"
    style="bottom: 0; overflow-y: auto; font-family: 'Jua', sans-serif;"
  >
    <Logo/>
    <b-form 
    id="inputForm"
    @submit.stop.prevent
    >
      <!-- ID 입력 폼 -->
      <div>
      <b-form-input
        v-model="userId"
        :state="validationId"
        id="text"
        placeholder="아이디"
        size="lg"
        label-align="center"
      ></b-form-input>
      <!-- ID 검증 문자 -->
      <b-form-invalid-feedback :state="validationId">
        아이디는 영소문자/숫자로 구성된 최소 7글자, 최대 16글자입니다
      </b-form-invalid-feedback>
      </div>

      <!-- 비밀번호 입력 폼 -->
      <b-form-input
        v-model="userPassword"
        :state="validationPassword"
        type="password"
        id="text"
        placeholder="비밀번호"
        size="lg"
      ></b-form-input>
      <!-- 비밀번호 검증 문자 -->
      <b-form-invalid-feedback :state="validationPassword">
        비밀번호는 영소문자/숫자/특수문자(!@#$%^&*)로 구성된 최소 7글자입니다
      </b-form-invalid-feedback>

      <!-- 비밀번호 확인 입력 폼 -->
      <b-form-input
        v-model="userPasswordCheck"
        :state="validationPasswordCheck"
        type="password"
        id="text"
        placeholder="비밀번호 확인"
        size="lg"
      ></b-form-input>
      <!-- 비밀번호 확인 검증 문자 -->
      <b-form-invalid-feedback :state="validationPasswordCheck">
        비밀번호와 같은 값을 입력해야합니다
      </b-form-invalid-feedback>

      <!-- 연락처 입력 폼 -->
      <b-form-input
        v-model="userPhone"
        :state="validationPhone"
        type="tel"
        id="text"
        placeholder="연락처"
        size="lg"
      ></b-form-input>
      <!-- 연락처 검증 문자 -->
      <b-form-invalid-feedback :state="validationPhone">
        000-0000-0000의 양식에 맞춰 입력해야합니다
      </b-form-invalid-feedback>

      <!-- 학교명 입력 폼 -->
      <b-form-input
        v-model="userSchoolName"
        id="text"
        placeholder="학교명(예시 : OO초등학교)"
        size="lg"
      ></b-form-input>

      <!-- 학교 지역 입력 폼 -->
      <b-form-input
        v-model="userSchoolRegion"
        id="text"
        placeholder="학교 지역(예시 : 서울 광진구/충북 서산)"
        size="lg"
      ></b-form-input>

      <b-row>
        <b-button block variant="warning" id="requestBtn" @click="requestService">서비스 신청</b-button>
      </b-row>
      <b-row id="link">
        <b-col id="linkBtn"><b-button variant="link" href="login">로그인</b-button></b-col>
        <b-col>|</b-col>
        <b-col id="linkBtn"><b-button variant="link" href="password_reset">비밀번호 재설정</b-button></b-col>
      </b-row>
    </b-form>
  </div>
</template>

<script>
import Logo from "@/components/Logo"
export default {
  name: 'ServiceRequest',
  data() {
    return {
      userId: "",
      userPassword: "",
      userPasswordCheck: "",
      userPhone: "",
      userSchoolName: "",
      userSchoolRegion: ""
    };
  },
  methods: {
    requestService() {
      if (!this.validationId) {
        alert('아이디 양식 맞춰주세요');
      }
      else if (!this.validationPassword) {
        alert('비밀번호 양식 맞춰주세요');
      }
      else if (!this.validationPasswordCheck) {
        alert('비밀번호와 같은 값을 입력해주세요');
      }
      else if (!this.validationPhone) {
        alert('전화번호 양식 맞춰주세요');
      }
      else if (this.userSchoolName.length === 0) {
        alert('학교 명을 똑바로 입력해주세요')
      }
      else if (this.userSchoolRegion.length === 0) {
        alert('학교 지역을 똑바로 입력해주세요')
      }
      else {
        alert('서비스 접수 완료');
        window.open('/login', '_self');
      }
    }
  },
  components: {
    Logo
  },
  computed: {
    validationId() {
      if (this.userId.length < 7) return false;
      else if (this.userId.length > 16) return false;
      else {
        for (var i = 0; i < this.userId.length; i++) {
          if (
            !(
              (this.userId[i] >= "a" && this.userId[i] <= "z") ||
              (this.userId[i] >= "0" && this.userId[i] <= "9")
            )
          )
            return false;
        }
        return true;
      }
    },
    validationPassword() {
      if (this.userPassword.length < 7) return false;
      else {
        for (var i = 0; i < this.userPassword.length; i++) {
          if (
            !(
              (this.userPassword[i] >= "a" && this.userPassword[i] <= "z") ||
              (this.userPassword[i] >= "0" && this.userPassword[i] <= "9") ||
              (this.userPassword[i] === "!") ||
              (this.userPassword[i] === "@") ||
              (this.userPassword[i] === "#") ||
              (this.userPassword[i] === "$") ||
              (this.userPassword[i] === "%") ||
              (this.userPassword[i] === "^") ||
              (this.userPassword[i] === "&") ||
              (this.userPassword[i] === "*")
            )
          )
            return false;
        }
        return true;
      }
    },
    validationPasswordCheck() {
      if (this.userPassword === this.userPasswordCheck)
      {
        if (this.userPassword.length < 7) return false;
        else {
          for (var i = 0; i < this.userPassword.length; i++) {
            if (
              !(
                (this.userPassword[i] >= "a" && this.userPassword[i] <= "z") ||
                (this.userPassword[i] >= "0" && this.userPassword[i] <= "9") ||
                (this.userPassword[i] === "!") ||
                (this.userPassword[i] === "@") ||
                (this.userPassword[i] === "#") ||
                (this.userPassword[i] === "$") ||
                (this.userPassword[i] === "%") ||
                (this.userPassword[i] === "^") ||
                (this.userPassword[i] === "&") ||
                (this.userPassword[i] === "*")
              )
            )
              return false;
          }
          return true;
        }
      }
      else
        return false;
    },
    validationPhone() {
      if (this.userPhone.length !== 13)
        return false;
      for (var i = 0; i < this.userPhone.length; i++) {
        if (i == 3 || i == 8) {
          if (this.userPhone[i] !== '-')
            return false;
          else {
            if (this.userPhone[i] < 0 || this.userPhone[i] > 9)
              return false;
          }
        }
      }
      return true;
    }
  },
};
</script>

<style>
#requestForm #inputForm {
  min-width: 500px;
  max-width: 500px;
  max-height: 630px;
  min-height: 630px;
  padding-top: 20px;
  background-color: #ccf0ef;
  border-radius: 20px;
}

#requestForm #inputForm #text {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 15px;
}

#requestForm #inputForm #requestBtn {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 15px;
}

#requestForm #inputForm #link {
  max-width: 400px;
  margin: 0px auto;
  margin-top: 15px;
}

#requestForm #inputForm #linkBtn {
  min-width: 150px;
}
</style>