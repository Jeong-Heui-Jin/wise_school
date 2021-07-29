<template>
  <div>
    <NavSideBar />
    <NavBar />
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "NoticeCreate",
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
</style>