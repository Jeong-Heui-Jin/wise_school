<template>
  <div>
    <NavSideBar/>
    <NavBar/>
    <h1>학생 태도 관리</h1>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Attitude',
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>

</style>