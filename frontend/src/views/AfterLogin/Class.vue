<template>
  <div style="font-family: 'Jua', sans-serif;">
    <NavSideBar/>
    <NavBar/>
    <h1 id="">우리반 친구들</h1>
  </div>
</template>

<script>
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Class',
  components: {
    NavSideBar,
    NavBar
  },
}
</script>

<style>

</style>