<template>
  <div>
    <NavSideBar/>
    <NavBar/>
    <h1>숙제 관리</h1>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Homework',
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>

</style>