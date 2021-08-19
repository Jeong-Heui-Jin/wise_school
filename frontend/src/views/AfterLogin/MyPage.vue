<template>
  <div style="font-family: 'Jua', sans-serif;" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="title">내 정보 </h1>

    <!-- 전체 Form -->
    <b-form id="user-info-form">
        <div class="d-flex justify-content-around" style="margin-top: 180px;">
            <img :src="image" style="margin-left: 40px; max-width: 260px; max-height: 260px;" alt="프로필 사진"/>
            
            <div id="user-info-text" style="min-width: 500px; max-height: 230px; background-color: #fff2d5; border-radius: 10px; padding: 10px; padding-top: 20px">
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">이   름</p>
                    <b-form-input id="name" v-model="userValue.name">{{userValue.name}}</b-form-input>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">I D</p>
                    <b-form-input id="username"></b-form-input>
                    <button style="font-size:12px; background-color:#d4e3fe;" type="button" @click="passwordChange">비밀번호 변경</button>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">담당학급</p>
                    <b-form-input id="userclass" v-model="userValue.class_num">{{userValue.class_num}}</b-form-input>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">전화번호</p>
                    <b-form-input id="phone-number" v-model="userValue.phone">{{userValue.phone}}</b-form-input>
                </div>
            </div>
        </div>
    
        <div v-if="usertype == 1">
            <button id="user-info-change" type="button" @click="infoChange">수정하기</button>
            <button id="user-info-recovery" type="button" @click="infoRecovery">변경취소</button>
        </div>

        <!-- 파일 업로드 -->
        <span v-if="imgBtnClick==0">
            <button id="img-change-btn" type="button" @click="updateImgBtn">사진 변경</button>
        </span>
        <span v-else>
            <button id="user-img-change" type="button" @click="infoImgChange">확인</button>
            <p>
                <input
                    type="file"
                    id="img-button"
                    ref="files"
                    accept="image/*"
                    v-on:change="upload"
                    enctype="multipart/form-data"
                />
            </p>
        </span>
    </b-form>
    
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from 'vuex'

export default {
    name: "MyPage",
    components: {
    NavSideBar,
    NavBar,
    },
    data() {
        return {
            data: '',
            user_id: this.$route.params.id,
            usertype: 1,
            userValue: {  
                name: '',
                phone: '',
                class_num: ''
            },
            image: '',
            imgBtnClick: 0
        }
    },
    mounted() {
        this.setToken();
        this.getUserInfo();
    },
    methods: {
        setToken: function () {
            this.$store.dispatch('setToken')
        },
        getUserInfo: function () {
            axios({
                method: "get",
                url: `http://i5a205.p.ssafy.io:8000/accounts/info/${this.user_id}`,
                headers: this.headers,
            })
            .then((res) => {
                this.data = Object.assign([], res.data);
                // console.log(this.data);
                const name = document.querySelector('#name');
                const username = document.querySelector('#username');
                const phone_number = document.querySelector('#phone-number');

                name.value = this.data.info.name;
                username.value = this.data.info.username;
                phone_number.value = this.data.info.phone;
                
                this.userValue.name = this.data.info.name;
                name.value = this.data.info.name;
                this.userValue.class_num = String(res.data.class_num)[0] + "학년 " + String(res.data.class_num)[2] + "반";
                
                this.userValue.phone = this.data.info.phone;

                this.usertype = res.data.info.usertype;
                this.image = res.data.info.image;
                const userclass = document.querySelector('#userclass');
                userclass.value = String(res.data.class_num)[0] + "학년 " + String(res.data.class_num)[2] + "반";
                
            })
            .catch((err) => {
                console.log(err);
            });
        },
        // 기존의 정보로 되돌리기
        infoRecovery() {
            const name = document.querySelector('#name');
            const username = document.querySelector('#username');
            
            name.value = this.data.name;
            username.value = this.data.username;
            this.image = this.data.image;
        },
        // 프로필 이미지 수정 하기
        infoImgChange() {
            
            this.image = this.$refs.files.files[0];
            var formData = new FormData();
            formData.append("files", this.image);
            for (var i = 0; i < this.image.length; i++) {
              formData.append("files", this.image[i]);
            }
           
            // axios Put
            axios({
              method: "put",
            //   url: `http://127.0.0.1:8000/accounts/image-change/${this.user_id}/`,
              url: `http://i5a205.p.ssafy.io:8000/accounts/image-change/${this.user_id}/`,
              data: formData,
              headers: {
                  "Authorization": this.headers.Authorization,
                  "Content-Type": "multipart/form-data"
              }
            })
              .then(function(){
                alert('프로필 이미지 수정되었습니다 :)');
                this.imgBtnClick = 0;
              })
              .catch(function(err){
                console.log(err);
              });
            this.$router.go();
        },
        upload(e) {
            let file = e.target.files;
            let reader = new FileReader();

            reader.readAsDataURL(file[0]);
            reader.onload = e => {
                // console.log(e.target.result);
                this.image = e.target.result;
            }
        },
        updateImgBtn() {
            this.imgBtnClick = 1;
        },
        infoChange() {  
            const name = document.querySelector('#name');
            const phone_number = document.querySelector('#phone-number');
            const userclass = document.querySelector('#userclass');

            // POST BODY
            let body = { name: name.value, phone: phone_number.value, classroom: userclass.value};
            console.log(body);
            // axios PUT
            axios({
              method: "put",
            //   url: `http://127.0.0.1:8000/accounts/info/${this.user_id}/`,
              url: `http://i5a205.p.ssafy.io:8000/accounts/info/${this.user_id}/`,
              data: body,
              headers: this.headers,
            })
              .then(function(){
                alert('수정되었습니다 :)');
              })
              .catch(function(err){
                console.log(err);
              });
            // this.$router.go();
        },
        passwordChange() {  
            const username = document.querySelector('#username');
            username.value = this.data.username;
            this.$router.push({ name:'PasswordChange', params:{'user':{username: username.value, id: this.user_id}} })
        },


    },
    computed: {
        ...mapState([
            'headers'
        ]),
    },
};
</script>

<style>
#user-info-form {
    position: absolute;
    left: 350px;
    top: 100px;
    min-width: 1000px;
    min-height: 650px;
    background-color: #e0edd4;
    border-radius: 20px;
}

#user-info-form p{
    min-width: 100px;
    min-height: 20px;
    vertical-align: middle;
}

#user-info-text div{
    margin-bottom: 10px; 
}

#user-info-form #user-info-change {
    position: absolute;
    left: 560px;
    top: 450px;
    border: 0px;
    background-color: #87acf1;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#user-info-form img {
  width: 100%;
  height: 100%;
  /* object-fit: cover; */
  object-fit: fill;
}

#user-info-form #user-img-change {
    position: absolute;
    left: 260px;
    top: 450px;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#user-info-form #img-change-btn {
    position: absolute;
    left: 170px;
    top: 450px;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#user-info-form #img-button {
    position: absolute;
    left: 80px;
    top: 460px;
    border: 0px;
    /* background-color: #d4e3fe; */
    max-width: 180px;
    max-height: 40px;
    font-size: 15px;
    /* border-radius: 10px; */
    /* background-color: lightgray; */
}

#user-info-form #user-info-recovery {
    position: absolute;
    left: 720px;
    top: 450px;
    border: 0px;
    background-color: #ff8c82;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}


</style>