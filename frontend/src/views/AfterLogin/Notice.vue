<template>
  <div>
    <NavSideBar/>
    <NavBar/>
    <h1>공지사항</h1>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Notice',
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>

</style>