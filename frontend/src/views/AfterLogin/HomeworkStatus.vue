<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1>안녕</h1>
  </div>
</template>

<script>
// import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "HomeworkStatus",
  data: function () {
    return {
      perPage: 10,
      currentPage: 1,
      fields: [],
      items: [],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {},
  computed: {
    ...mapState(["infomation_homework"]),
  },
  created: function () {
    this.setToken();
  },
};
</script>
