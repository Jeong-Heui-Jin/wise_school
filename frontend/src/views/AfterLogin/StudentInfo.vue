<template>
  <div style="font-family: 'Jua', sans-serif;" variant="light">
    <!-- left/top navbar -->
    <NavSideBar />
    <NavBar />

    <h1 id="title">학생 정보 확인</h1>

    <!-- 전체 Form -->
    <b-form id="student-info-form">
        <div class="d-flex justify-content-around" style="margin-top: 30px;">
            <img src="@/assets/sheep.png" style="max-width: 200px;" alt="학생사진"/>
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
        <button id="student-info-change" type="button" @click="infoChange">수정하기</button>
        <button id="student-info-recovery" type="button" @click="infoRecovery">되돌리기</button>
        <div id="parents-info-form">
            <p style="font-size: 28px; margin-right: auto;">비상 연락망</p>
            <div style="min-width: 900px; min-height: 200px; background-color: #d6d6d6; border-radius: 20px; padding: 10px;">
                <div id="parent-info-form-graph">
                    <b-row style="min-width: 800px; margin-bottom: 20px;">
                        <b-col cols="2">관계</b-col>
                        <b-col cols="3">이름</b-col>
                        <b-col cols="3">연락처</b-col>
                    </b-row>
                    <div id="parent-info" v-for="parent in parents" :key="parent.Relation">
                        <b-row>
                            <b-col><input style="min-width:120px; max-width:120px; margin-right: 20px;" v-model="parent.Relation"/></b-col>
                            <b-col><input style="min-width:160px; max-width:160px; margin-right: 20px;" v-model="parent.Name"/></b-col>
                            <b-col><input style="min-width:200px; max-width:200px; margin-right: 30px;" v-model="parent.Phone"/></b-col>
                            <b-col><button type="button" style="min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px;" @click="parentInfoDelete"> 삭제 </button></b-col>
                        </b-row>
                    </div>
                </div>
                <button type="button" style="min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-top: 10px; margin-left: 330px;" @click="parentInfoUpdate">수정</button>
                <button type="button" style="min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-top: 10px; margin-left: 10px;" @click="addForm">추가</button>
            </div>
        </div>
    </b-form>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";

export default {
    name: "StudentInfo",
    components: {
    NavSideBar,
    NavBar,
    },
    data() {
        return {
            student: { Name: '목상원', Number: '16', Phone: '010-3542-8554', Address: '서울시 강남구 테헤란로 212' },
            parents: [
                { Relation: '어머니', Name: '김다정', Phone: '010-1234-5678' }
            ]
        }
    },
    mounted() {
        const studentName = document.querySelector('#student-name');
        const studentNumber = document.querySelector('#student-number');
        const studentPhone = document.querySelector('#student-phone');
        const studentAddress = document.querySelector('#student-address');

        studentName.value = this.student.Name;
        studentNumber.value = this.student.Number;
        studentPhone.value = this.student.Phone;
        studentAddress.value = this.student.Address;
    },
    methods: {
        infoRecovery() {
            const studentName = document.querySelector('#student-name');
            const studentNumber = document.querySelector('#student-number');
            const studentPhone = document.querySelector('#student-phone');
            const studentAddress = document.querySelector('#student-address');

            studentName.value = this.student.Name;
            studentNumber.value = this.student.Number;
            studentPhone.value = this.student.Phone;
            studentAddress.value = this.student.Address;
        },
        infoChange() {
            // 실제로 페이지가 로드 될 때 다시 data 값을 가져오기 때문에 갱신되지 않음
            // 백엔드와 연동해야 동작이 가능해짐
            const studentName = document.querySelector('#student-name');
            const studentNumber = document.querySelector('#student-number');
            const studentPhone = document.querySelector('#student-phone');
            const studentAddress = document.querySelector('#student-address');

            this.student.Name = studentName.value;
            this.student.Number = studentNumber.value;
            this.student.Phone = studentPhone.value;
            this.student.Address = studentAddress.value;
            // alert('Connecting Backend...');
        },
        parentInfoDelete(e) {
            // removeItem(e.currentTarget.parentElement.parentElement.children[0].children[0].value, this.parents.Relation)
            // this.parents = this.parents.fillter(info => info.Relation !== e.currentTarget.parentElement.parentElement.children[0].children[0].value);
            // for (var i = 0; i < this.parents.length; i++) {

            //     if (this.parents[i].Relation === e.currentTarget.parentElement.parentElement.children[0].children[0].value) {
            //         this.parents.this.parents[i]
            //     }
            // }
            e.currentTarget.parentElement.parentElement.parentElement.removeChild(e.currentTarget.parentElement.parentElement);
        },
        parentInfoUpdate() {
            this.parents = [];
            const parentInfo = document.querySelectorAll('#parent-info');

            for (var i = 0; i < parentInfo.length; i++) {
                this.parents.push({ Relation: parentInfo[i].children[0].children[0].children[0].value, Name: parentInfo[i].children[0].children[1].children[0].value, 
                Phone: parentInfo[i].children[0].children[2].children[0].value})
                // parents.push({ Relation: parentInfo[i].children, Name: '김다정', Phone: '010-1234-5678' })
            }
            const parentInfoAddtion = document.querySelector('.addition-form');
            parentInfoAddtion.parentElement.removeChild(parentInfoAddtion);
            
        },
        addForm() {
            const parentInfo = document.querySelectorAll('#parent-info');

            if (parentInfo.length === 2) {
                alert('더 이상 추가할 수 없습니다');
            }
            else {
                const parentInfoFormGraph = document.querySelector('#parent-info-form-graph');
                console.log('add');
                parentInfoFormGraph.insertAdjacentHTML('beforeend', `
                    <div id="parent-info" class="addition-form">
                        <b-row>
                            <b-col cols="2"><input style="min-width:120px; max-width:120px; margin-right: 73px;"/></b-col>
                            <b-col cols="3"><input style="min-width:160px; max-width:160px; margin-right: 45px;"/></b-col>
                            <b-col cols="4"><input style="min-width:200px; max-width:200px; margin-right: 108px;"/></b-col>
                            <b-col><button type="button" style="min-width: 80px; min-height: 35px; border: 0px; border-radius: 10px; margin-right: 32px;" onclick="parentInfoDelete(e)"> 삭제 </button></b-col>
                        </b-row>
                    </div>
                `);
            }
        }
    }
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
    left: 40px;
    top: 350px;
}

#parent-info {
    margin-bottom: 10px;
}

#parent-info-form-graph input {
    border: 0px;
    border-radius: 3px;
    min-height: 35px;
}
</style>