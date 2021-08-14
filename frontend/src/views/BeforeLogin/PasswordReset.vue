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

      <!-- 연락처 입력 폼 -->
      <b-form-input
        v-model="userPhone"
        :state="validationPhone"
        type="tel"
        id="textPhone"
        placeholder="연락처"
        size="lg"
      ></b-form-input>
      <!-- 연락처 검증 문자 -->
      <b-form-invalid-feedback :state="validationPhone">
        000-0000-0000의 양식에 맞춰 입력해야합니다
      </b-form-invalid-feedback>

      <!-- 비밀번호 검증 문자 -->
      <b-button block variant="warning" id="resetBtn" @click="certificateForm">비밀번호 재설정</b-button>
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
import axios from 'axios'
import Logo from "@/components/Logo";

export default {
  name: "PasswordReset",
  data: () => ({
    userId: "",
    userName: "",
    userPhone: "",
  }),
  methods: {
    certificateForm: function(event) {
      event.preventDefault();
      var confirmData = {
        username: this.userId,
        name: this.userName,
        phone: this.userPhone,
      }
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/user-confirm/',
        // url: 'http://i5a205.p.ssafy.io:8000/accounts/user-confirm/',
        data: confirmData,
      })
      .then((res) => {
        alert("정보가 확인되었습니다! 비밀번호를 새로 설정해주세요 :)")
        // window.open('/password_change', '_self')
        console.log(res.data)
        this.$router.push({ name:'PasswordChange', params:{'user':res.data} })
      })
      .catch(err => {
        alert(err)
      })
      // if 비정확
      // console.log("정보 재입력")
      if (this.validationPhone) {
        // window.open('/password_change', '_self');
      }
      else {
        alert('전화번호를 재입력하세요');
      } 
    },
  },
  computed: {
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