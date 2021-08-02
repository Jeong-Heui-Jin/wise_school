<template>
  <div style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <h1 id="title">시간표</h1>
    <b-container class="bv-example-row">
      <b-row id="timetable">
        <b-col> </b-col>
        <b-col>월</b-col>
        <b-col>화</b-col>
        <b-col>수</b-col>
        <b-col>목</b-col>
        <b-col>금</b-col>
        <div></div>
        <b-col>1교시</b-col>
        <b-col>국어</b-col>
        <b-col>수학</b-col>
        <b-col>사회</b-col>
        <b-col>과학</b-col>
        <b-col>영어</b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Timetable',
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>
#timetable {
  position: absolute;
  top: 90px;
  left: 23%;
  width: 1060px;
  height: 650px;
  background-color: aqua;
}

#timetable b-col {
  
}

</style>