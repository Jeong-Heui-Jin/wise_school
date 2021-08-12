<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />
  </div>
</template>

<script>
// import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";

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
  computed: {},
  created: function () {},
};
</script>
