<template>
  <div style="font-family: 'Jua', sans-serif;" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="title">학생 정보 확인</h1>

    <!-- 전체 Form -->
    <b-form id="student-info-form">
        <div class="d-flex justify-content-around" style="margin-top: 30px;">
            <img :src="image" style="margin-left: 20px; width: 230px; height: 230px;" alt="학생 프로필 사진"/>
            
            <div id="student-info-text" style="min-width: 500px; background-color: #fff2d5;  border-radius: 10px; padding: 15px; ">
                <div class="d-flex justify-content-between">
                    <p style="margin-top: auto; margin-bottom: auto;">이   름</p>
                    <b-form-input id="student-name"></b-form-input>
                </div>
                <div class="d-flex justify-content-between">
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
                </div>
            </div>
        </div>
        <!-- <div v-if="usertype === 1"> -->
            <button id="student-info-change" type="button" @click="infoChange">수정하기</button>
            <button id="student-info-recovery" type="button" @click="infoRecovery">되돌리기</button>
        <!-- </div> -->
        <!-- 파일 업로드 -->
        <span v-if="imgBtnClick==0">
            <button id="img-change-btn" type="button" @click="updateImgBtn">사진 변경</button>
        </span>
        <span v-else>
            <button id="student-img-change" type="button" @click="infoImgChange">확인</button>
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
        
        <div id="parents-info-form">
            <p style="font-size: 28px; margin-right: auto;">보호자 연락처</p>
            <div style="min-width: 900px; min-height: 200px; background-color: #d6d6d6; border-radius: 20px; padding: 10px;">
                <div id="parent-info-form-graph">
                    <b-row style="min-width: 800px; margin-bottom: 20px; margin-left: 15px;">
                        <b-col cols="2">관계</b-col>
                        <b-col cols="3">이름</b-col>
                        <b-col cols="3">연락처</b-col>
                    </b-row>
                    <div id="parent-info" v-if="parents.length >= 1">
                        <b-row>
                            <b-col cols="2"><input style="min-width:120px; max-width:120px; margin-left:30px;"/></b-col>
                            <b-col cols="3"><input style="min-width:160px; max-width:160px; margin-left:40px;"/></b-col>
                            <b-col cols="3"><input style="min-width:200px; max-width:200px; margin-left:20px;"/></b-col>
                            <b-col cols="1">
                                <button id="parents-1-update" type="button" style="background-color: #d4e3fe; min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-right: 10px; margin-left:30px;" @click="parentInfoUpdate"> 
                                    등록 
                                </button>
                            </b-col>
                            <!-- <b-col v-if="usertype == 1" cols="1"> -->
                            <b-col cols="1">
                                <button id="parents-1-delete" type="button" style="background-color: #ff8c82; min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-left: 40px;" @click="parentInfoDelete"> 
                                    삭제 
                                </button>
                            </b-col>
                        </b-row>
                    </div>
                    <div id="parent-info" v-if="parents.length >= 2">
                        <b-row>
                            <b-col cols="2"><input style="min-width:120px; max-width:120px; margin-left:30px;"/></b-col>
                            <b-col cols="3"><input style="min-width:160px; max-width:160px; margin-left:40px;"/></b-col>
                            <b-col cols="3"><input style="min-width:200px; max-width:200px; margin-left:20px;"/></b-col>
                            <b-col cols="1">
                                <button id="parents-2-update" type="button" style="background-color: #d4e3fe; min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-right: 10px; margin-left:30px;" @click="parentInfoUpdate"> 
                                    등록 
                                </button>
                            </b-col>
                            <b-col cols="1">
                                <button id="parents-2-delete" type="button" style="background-color: #ff8c82; min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-left: 10px; margin-left:40px;" @click="parentInfoDelete"> 
                                    삭제 
                                </button>
                            </b-col>
                        </b-row>
                    </div>
                </div>
                <button type="button" style="width: 80px; height: 35px; border: 0px; border-radius: 10px; margin-top: 10px; margin-left: 10px;" @click="addForm">추가</button>
            </div>
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
    name: "StudentInfo",
    components: {
    NavSideBar,
    NavBar,
    },
    data() {
        return {
            data: '',
            student_id: this.$route.params.id,
            usertype: 0,
            student: { ID: 1234, name: '목상원', number: '16', phone: '010-3542-8554', address: '서울시 강남구 테헤란로 212' },
            parents: [
                { ID: 123, student_id: 1234, relation: '어머니', name: '김다정', phone: '010-1234-5678' },
                { ID: 123, student_id: 1234, relation: '어머니', name: '김다정', phone: '010-1234-5678' },
            ],
            image: '',
            imgBtnClick: 0
        }
    },
    mounted() {
        this.setToken();
        this.getStudentInfo();
    },
    methods: {
        setToken: function () {
            this.$store.dispatch('setToken')
        },
        getStudentInfo: function () {
            axios({
                method: "get",
                url: `http://i5a205.p.ssafy.io:8000/accounts/info/${this.student_id}`,
                headers: this.headers,
            })
            .then((res) => {
                this.data = Object.assign([], res.data);
                console.log(this.data)
                const studentName = document.querySelector('#student-name');
                const studentNumber = document.querySelector('#student-number');
                const studentPhone = document.querySelector('#student-phone');
                const studentAddress = document.querySelector('#student-address');

                studentName.value = this.data.info.name;
                studentNumber.value = this.data.info.info.number;
                studentPhone.value = this.data.info.phone;
                studentAddress.value = this.data.info.info.address;

                this.parents = res.data.info.parents;
                this.usertype = res.data.info.usertype;
                this.image = res.data.info.image;

                const parentInfo = document.querySelectorAll('#parent-info');

                for (var i = 0; i < this.data.info.parents.length; i++) {
                    parentInfo[i].children[0].children[0].children[0].value = this.data.info.parents[i].relation;
                    parentInfo[i].children[0].children[1].children[0].value = this.data.info.parents[i].name;
                    parentInfo[i].children[0].children[2].children[0].value = this.data.info.parents[i].phone;
                }
            })
                .catch((err) => {
                console.log(err);
                });
        },
        // 기존의 정보로 되돌리기
        infoRecovery() {
            const studentName = document.querySelector('#student-name');
            const studentNumber = document.querySelector('#student-number');
            const studentPhone = document.querySelector('#student-phone');
            const studentAddress = document.querySelector('#student-address');

            studentName.value = this.data.name;
            studentNumber.value = this.data.info.number;
            studentPhone.value = this.data.phone;
            studentAddress.value = this.data.info.address;
        },
        // 학생 정보 수정 하기
        infoChange() {
            const studentName = document.querySelector('#student-name');
            const studentNumber = document.querySelector('#student-number');
            const studentPhone = document.querySelector('#student-phone');
            const studentAddress = document.querySelector('#student-address');

            // POST BODY
            let body = { name: studentName.value, number: studentNumber.value, phone: studentPhone.value, address: studentAddress.value };
            console.log(body);
            // axios POST
            axios({
              method: "put",
            //   url: `http://127.0.0.1:8000/accounts/info/${this.student_id}/`,
              url: `http://i5a205.p.ssafy.io:8000/accounts/info/${this.student_id}/`,
              data: body,
              headers: this.headers,
            })
              .then(function(){
                alert('수정되었습니다 :)');
              })
              .catch(function(err){
                console.log(err);
              });
        },
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
            //   url: `http://127.0.0.1:8000/accounts/image-change/${this.student_id}/`,
              url: `http://i5a205.p.ssafy.io:8000/accounts/image-change/${this.student_id}/`,
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
        updateImgBtn() {
            this.imgBtnClick = 1;
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
        parentInfoDelete(e) {
            console.log(this.parents[Number(e.target.id[8]) - 1].id)
            // console.log(e.target.id);
            // console.log(this.parents[Number(e.target.id[8]) - 1].ID);
            // console.log(this.parents[Number(e.target.id[8]) - 1].ID);
            // this.parents.splice(Number(e.target.id[8]) - 1, 1);
            // axios DELETE
            // 해당 this.parents[Number(e.target.id[8]) - 1].ID로 parent Info data delete
            // parents ID -> this.parents[idx].ID

            axios({
              method: "delete",
            //   url: `http://127.0.0.1:8000/accounts/parents/detail/${this.parents[Number(e.target.id[8]) - 1].id}/`,
              url: `http://i5a205.p.ssafy.io:8000/accounts/parents/detail/${this.parents[Number(e.target.id[8]) - 1].id}/`,
              headers: this.headers,
            })
              .then(function(){
                alert('삭제되었습니다 :(');
              })
              .catch(function(err){
                console.log(err);
              });
              this.$router.go();
        },
        parentInfoUpdate(e) {
            if (e.target.parentElement.parentElement.children[0].children[0].value.length > 0 &&
                e.target.parentElement.parentElement.children[1].children[0].value.length > 0 &&
                e.target.parentElement.parentElement.children[2].children[0].value.length > 0) {
                // 처음 등록하는 경우
                if(!this.parents || !this.parents[Number(e.target.id[8]) - 1].ID){
                    // POST
                    var bodyPost = { student_id: this.parents[Number(e.target.id[8]) - 1].student_id, 
                    relation: e.target.parentElement.parentElement.children[0].children[0].value,
                    name: e.target.parentElement.parentElement.children[1].children[0].value,
                    phone: e.target.parentElement.parentElement.children[2].children[0].value};
                    console.log(bodyPost);
                    // POST axios
                    axios({
                        method: "post",
                        // url: `http://127.0.0.1:8000/accounts/parents/${this.student_id}/`,
                        url: `http://i5a205.p.ssafy.io:8000/accounts/parents/${this.student_id}/`,
                        data: bodyPost,
                        headers: this.headers,
                        })
                        .then(function(){
                            alert('등록되었습니다 :)');
                        })
                        .catch(function(err){
                            console.log(err);
                        });
                        this.$router.go();
                }
                // UPDATE 경우
                else {
                    var body = { ID: this.parents[Number(e.target.id[8]) - 1].ID, student_id: this.parents[Number(e.target.id[8]) - 1].student_id, 
                    relation: e.target.parentElement.parentElement.children[0].children[0].value,
                    name: e.target.parentElement.parentElement.children[1].children[0].value,
                    phone: e.target.parentElement.parentElement.children[2].children[0].value};
                    console.log(this.parents[Number(e.target.id[8]) - 1].ID);
                    console.log(body);
                    // axis UPDATE
                    // BODY key -> this.parents[Number(e.target.id[8]) - 1].ID
                    axios({
                        method: "put",
                        // url: `http://127.0.0.1:8000/accounts/parents/detail/${this.parents[Number(e.target.id[8]) - 1].ID}/`,
                        url: `http://i5a205.p.ssafy.io:8000/accounts/parents/${this.student_id}/`,
                        data: bodyPost,
                        headers: this.headers,
                        })
                        .then(function(){
                            alert('수정되었습니다 :)');
                        })
                        .catch(function(err){
                            console.log(err);
                        });

                    this.parents[Number(e.target.id[8]) - 1].relation = e.target.parentElement.parentElement.children[0].children[0].value;
                    this.parents[Number(e.target.id[8]) - 1].name = e.target.parentElement.parentElement.children[1].children[0].value;
                    this.parents[Number(e.target.id[8]) - 1].phone = e.target.parentElement.parentElement.children[2].children[0].value;
                    
                    this.$router.go();
                }
            }
            else {
                alert('빈칸을 채워주세요!');
            }
        },
        addForm() {
            if (this.parents.length <= 1) {
                this.parents.push({ student_id: this.student.ID, relation: '', name: '', phone: ''});
            }
            else {
                alert('더 이상 추가할 수 없습니다');
            }
        }
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
    top: 280px 	!important;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#student-info-form img {
  width: 100%;
  height: 100%;
  /* object-fit: cover; */
  object-fit: fill;
}

#student-info-form #student-img-change {
    position: absolute;
    left: 260px;
    top: 280px 	!important;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#student-info-form #img-change-btn {
    position: absolute;
    left: 150px !important;
    top: 280px 	!important;
    border: 0px;
    background-color: #d4e3fe;
    min-width: 100px;
    min-height: 40px;
    font-size: 20px;
    border-radius: 10px;
}

#student-info-form #img-button {
    position: absolute;
    left: 80px;
    top: 290px 	!important;
    border: 0px;
    /* background-color: #d4e3fe; */
    max-width: 180px;
    max-height: 40px;
    font-size: 15px;
    /* border-radius: 10px; */
    /* background-color: lightgray; */
}

#student-info-form #student-info-recovery {
    position: absolute;
    left: 740px;
    top: 280px 	!important;
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