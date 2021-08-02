<template>
  <div style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <h1 id="title">시간표</h1>
    
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

</style>