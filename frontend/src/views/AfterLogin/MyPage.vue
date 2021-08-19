<template>
  <div style="font-family: 'Jua', sans-serif;" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="title">내 정보 </h1>

    <!-- 전체 Form -->
    <b-form id="student-info-form">
        <div class="d-flex justify-content-around" style="margin-top: 30px;">
            <img :src="image" style="margin-left: 30px; max-width: 200px;" alt="학생사진"/>
            
            <div id="student-info-text" style="min-width: 500px; background-color: #fff2d5;  border-radius: 10px; padding: 15px; ">
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">이   름</p>
                    <b-form-input id="name"></b-form-input>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">I D</p>
                    <b-form-input id="username"></b-form-input>
                </div>
                <!-- <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">학급번호</p>
                    <b-form-input id="student-number"></b-form-input>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">전화번호</p>
                    <b-form-input id="student-phone"></b-form-input>
                </div>
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">주   소</p>
                    <b-form-input id="student-address"></b-form-input>
                </div> -->
            </div>
        </div>
        <!-- 파일 업로드 -->
        <span id="fileUploadTitle" style="font-size: 20px">사진 변경</span>
        <p>
            <input
                type="file"
                id="files"
                ref="files"
                accept="image/*"
                v-on:change="upload"
                enctype="multipart/form-data"
            />
        </p>
        
        <div v-if="usertype == 1">
            <button id="student-info-change" type="button" @click="infoImgChange">수정하기</button>
            <button id="student-info-recovery" type="button" @click="infoRecovery">되돌리기</button>
        </div>
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
            name: "",
            student: { ID: 1234, name: '목상원', number: '16', phone: '010-3542-8554', address: '서울시 강남구 테헤란로 212' },
            image: ''
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
                console.log(this.data);
                const name = document.querySelector('#name');
                const username = document.querySelector('#username');

                name.value = this.data.name;
                this.name = this.data.name;
                username.value = this.data.username;

                this.usertype = res.data.usertype;
                this.image = res.data.image;
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
            console.log("form", formData);

            this.image = this.$refs.files.files[0];
           
            // axios Put
            axios({
              method: "put",
              url: `http://127.0.0.1:8000/accounts/info/${this.user_id}/`,
            //   url: `http://i5a205.p.ssafy.io:8000/accounts/info/${this.user_id}/`,
              data: formData,
              headers: {
                  "Authorization": this.headers.Authorization,
                  "Content-Type": "multipart/form-data"
              }
            })
              .then(function(){
                alert('프로필 이미지 수정되었습니다 :)');
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
    },
    computed: {
        ...mapState([
            'headers'
        ]),
    },
};
</script>

<style>
#student-info-form {
    position: absolute;
    left: 350px;
    top: 100px;
    min-width: 1000px;
    min-height: 650px;
    background-color: #e0edd4;
    border-radius: 20px;
}

#student-info-form p{
    min-width: 100px;
    min-height: 20px;
    vertical-align: middle;
}

#student-info-text div{
    margin-bottom: 10px; 
}

#student-info-form #student-info-change {
    position: absolute;
    left: 510px;
    top: 280px;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#student-info-form #student-info-recovery {
    position: absolute;
    left: 740px;
    top: 280px;
    border: 0px;
    background-color: #ff8c82;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#parents-info-form {
    position: absolute;
    left: 35px;
    top: 350px;
}

#parent-info {
    margin-bottom: 15px;
}

#parent-info input {
    text-align: center;
}

#parent-info-form-graph input {
    border: 0px;
    border-radius: 3px;
    min-height: 35px;
    margin-left: 10px;
}
</style>