<template>
  <div style="font-family: 'Jua', sans-serif">
    <NavSideBar/>
    <NavBar/>
    <h1 id="title">출석 관리</h1>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex'

export default {
  name: 'Attendance',
  components: {
    NavSideBar,
    NavBar
  },
  data: function() {
    return {
      attendances: {},
    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getTeachers: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/student-manage/attendance/',
        headers: this.headers,
      })
        .then((res) => {
          // console.log(res.data)
          this.attendances = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {
    this.setToken()
    this.getTeachers()
  }
}
</script>

<style>

</style>