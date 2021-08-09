<template>
  <div>
    <NavSideBar/>
    <NavBar/>
    <h1>학생 태도 관리</h1>
  </div>
</template>

<script>
import axios from "axios"
import NavSideBar from '@/components/NavSideBarTeacher.vue'
import NavBar from '@/components/NavBar.vue'
import { mapState } from 'vuex'

export default {
  name: 'Attitude',
  components: {
    NavSideBar,
    NavBar
  },
  data: function() {
    return {

    }
  },
  methods: {
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getAttitudes: function () {
      axios({
        method: "get",
        // url: "http://i5a205.p.ssafy.io:8081/homework/list/",
        url: 'http://i5a205.p.ssafy.io:8000/student-manage/note/1/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
          // this.items = res.data
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
    this.getAttitudes()
  }
}
</script>

<style>

</style>