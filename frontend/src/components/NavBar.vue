<template>
    <div>
        <b-navbar id="nav-bar" style="font-family: 'Jua', sans-serif;" class="d-flex row-vw" toggleable="lg" variant="faded" type="light">
            <!-- Right aligned nav items -->
            <b-navbar-nav id="right-side" class="ml-auto">
                <img id="logo" src="@/assets/alarm.png" alt="알람_로고" @click="print">
                <img id="logo" src="@/assets/mail.png" alt="알람_로고">
                <b-button id="button" variant="faded" type="light" size="lg">내 정보 보기</b-button>
                <b-button id="button" variant="faded" type="light" size="lg">로그아웃</b-button>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
export default({
    methods: {
        print() {
            console.log('alarm');
        }
    }
})
</script>


<style>
#nav-bar {
    max-height: 40px;
}

#nav-bar #right-side {
    position: absolute;
    top: 0px;
    right: 10px;
}

#nav-bar #button {
    margin-right: 10px;
    max-height: 40px;
}

#nav-bar #logo {
    margin-top: 5px;
    max-height: 40px;
    max-width: 40px;
    margin-right: 30px;
}

</style>