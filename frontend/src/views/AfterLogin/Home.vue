<template>
  <div>
    <!-- 백엔드와 연동하여 권한을 확인한 후 해당 페이지를 띄워줄 예정 -->
    <div v-if="authority==='0'"><NavSideBarAdmin/></div>
    <div v-else-if="authority==='1'"><NavSideBarTeacher/></div>
    <div v-else><NavSideBarStudent/></div>
  </div>
  
</template>

<script>
import NavSideBarAdmin from '@/components/NavSideBarAdmin.vue'
import NavSideBarTeacher from '@/components/NavSideBarTeacher.vue'
import NavSideBarStudent from '@/components/NavSideBarStudent.vue'

export default {
  name: 'Home',
  data() {
    return {
      authority: '1',
    }
  },
  mounted() {
    // console.log(this.$route.params.authority);
    // this.authority = this.$route.params.authority;
  },
  components: {
    NavSideBarAdmin,
    NavSideBarTeacher,
    NavSideBarStudent,
  },
  created: function () {
    //this.$router.push({ name: 'Login' })
  }
}
</script>

<style>
</style>