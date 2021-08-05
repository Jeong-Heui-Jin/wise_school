<template>
    <div>
        <b-navbar id="nav-bar" style="font-family: 'Jua', sans-serif;" toggleable="lg" variant="faded" type="light">
            <!-- Right aligned nav items -->
            <b-navbar-nav id="right-side" class="ml-auto">
                <img id="logo" src="@/assets/alarm.png" alt="알람_로고" @click="print">
                <img id="logo" src="@/assets/mail.png" alt="알람_로고">
                <b-button id="button" variant="faded" type="light" size="lg">내 정보 보기</b-button>
                <b-button id="button" variant="faded" type="light" size="lg" @click="logout">로그아웃</b-button>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
export default({
    methods: {
        print() {
            console.log('alarm');
        },
        logout() {
            // 로그아웃
            if(localStorage.getItem('jwt')){
                // 로컬에 저장된 토큰 삭제
                localStorage.removeItem('jwt');
                window.open('/login', '_self');
            }
        },
    }
})
</script>


<style>
#nav-bar {
    max-height: 50px;
    width: 100%;
}

#nav-bar #right-side {
    position: absolute;
    min-width: 500px;
    max-width: 500px;
    width: 500px;
    min-height: 60px;
    max-height: 60px;
    height: 60px;
    top: 0px;
    left: 1000px;
}

#nav-bar #button {
    margin-right: 10px;
    min-height: 40px;
    max-height: 40px;
    height: 40px;
    min-width: 60px;
}

#nav-bar #logo {
    margin-top: 5px;
    max-height: 40px;
    min-height: 40px;
    height: 40px;
    max-width: 40px;
    min-width: 40px;
    margin-right: 30px;
}

</style>