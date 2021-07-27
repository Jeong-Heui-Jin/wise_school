<template>
  <div>
    <NavSideBarStudent/>
  </div>
  
</template>

<script>
import NavSideBarStudent from '@/components/NavSideBarStudent.vue'
export default {
  name: 'HomeStudent',
  components: {
    NavSideBarStudent,
  },
  created: function () {
    //this.$router.push({ name: 'Login' })
  }
}
</script>

<style>
</style>