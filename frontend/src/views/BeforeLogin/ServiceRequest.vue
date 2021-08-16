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
        v-model="requestForm.username"
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
        v-model="requestForm.password"
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
        v-model="requestForm.password_confirmation"
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
        v-model="requestForm.phone"
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
        v-model="requestForm.school_name"
        id="text"
        placeholder="학교명(예시 : OO초등학교)"
        size="lg"
      ></b-form-input>

      <!-- 학교 지역 입력 폼 -->
      <b-form-input
        v-model="requestForm.area"
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
import axios from 'axios';

export default {
  name: 'ServiceRequest',
  data() {
    return {
      requestForm: {
        username: "",
        password: "",
        password_confirmation: "",
        phone: "",
        school_name: "",
        area: "",
      }
    };
  },
  methods: {
    requestService: function(event) {
      if (!this.validationId) {
        alert('아이디 양식을 맞춰주세요!');
      }
      else if (!this.validationPassword) {
        alert('비밀번호 양식을 맞춰주세요!');
      }
      else if (!this.validationPasswordCheck) {
        alert('비밀번호와 같은 값을 입력해주세요!');
      }
      else if (!this.validationPhone) {
        alert('전화번호 양식을 맞춰주세요.');
      }
      else if (this.userSchoolName.length === 0) {
        alert('학교 명을 똑바로 입력해주세요!')
      }
      else if (this.userSchoolRegion.length === 0) {
        alert('학교 지역을 똑바로 입력해주세요!')
      }
      else {
        event.preventDefault()
        axios({
          method: 'post',
          url: 'http://i5a205.p.ssafy.io:8000/accounts/service-request/',
          data: this.requestForm,
        })
        .then((res) => {
          alert('서비스 접수 완료');
          console.log(res)
          // window.open('/login', '_self');
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
  },
  components: {
    Logo
  },
  computed: {
    validationId() {
      console.log(this.requestForm.username.length);
      if (this.requestForm.username.length < 7) return false;
      else if (this.requestForm.username.length > 16) return false;
      else {
        for (var i = 0; i < this.requestForm.username.length; i++) {
          if (
            !(
              (this.requestForm.username[i] >= "a" && this.requestForm.username[i] <= "z") ||
              (this.requestForm.username[i] >= "0" && this.requestForm.username[i] <= "9")
            )
          )
            return false;
        }
        return true;
      }
    },
    validationPassword() {
      if (this.requestForm.password.length < 7) return false;
      else {
        for (var i = 0; i < this.requestForm.password.length; i++) {
          if (
            !(
              (this.requestForm.password[i] >= "a" && this.requestForm.password[i] <= "z") ||
              (this.requestForm.password[i] >= "0" && this.requestForm.password[i] <= "9") ||
              (this.requestForm.password[i] === "!") ||
              (this.requestForm.password[i] === "@") ||
              (this.requestForm.password[i] === "#") ||
              (this.requestForm.password[i] === "$") ||
              (this.requestForm.password[i] === "%") ||
              (this.requestForm.password[i] === "^") ||
              (this.requestForm.password[i] === "&") ||
              (this.requestForm.password[i] === "*")
            )
          )
            return false;
        }
        return true;
      }
    },
    validationPasswordCheck() {
      if (this.requestForm.password === this.requestForm.password_confirmation)
      {
        if (this.requestForm.password.length < 7) return false;
        else {
          for (var i = 0; i < this.requestForm.password.length; i++) {
            if (
              !(
                (this.requestForm.password[i] >= "a" && this.requestForm.password[i] <= "z") ||
                (this.requestForm.password[i] >= "0" && this.requestForm.password[i] <= "9") ||
                (this.requestForm.password[i] === "!") ||
                (this.requestForm.password[i] === "@") ||
                (this.requestForm.password[i] === "#") ||
                (this.requestForm.password[i] === "$") ||
                (this.requestForm.password[i] === "%") ||
                (this.requestForm.password[i] === "^") ||
                (this.requestForm.password[i] === "&") ||
                (this.requestForm.password[i] === "*")
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
      if (this.requestForm.phone.length !== 13)
        return false;
      for (var i = 0; i < this.requestForm.phone.length; i++) {
        if (i == 3 || i == 8) {
          if (this.requestForm.phone[i] !== '-')
            return false;
          else {
            if (this.requestForm.phone[i] < 0 || this.requestForm.phone[i] > 9)
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