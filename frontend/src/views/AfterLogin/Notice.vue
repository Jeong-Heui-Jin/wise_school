<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="noticeTitle">공지사항</h1>

    <div id="listForm">
      <b-list-group>
        <b-list-group>
          <div>
            <button
              id="noticeButton"
              style="text-align: right"
              @click="goNoticeCreate()"
            >
              공지사항 작성
            </button>
          </div>
        </b-list-group>
        <b-list-group-item
          id="textNotice"
          v-for="(item, index) in items"
          v-bind:key="index"
        >
          <a href="/notice" v-if="index % 6 === 0">📕 {{ item.name }}</a>
          <a href="/notice" v-else-if="index % 6 === 1">📗 {{ item.name }}</a>
          <a href="/notice" v-else-if="index % 6 === 2">📘 {{ item.name }}</a>
          <a href="/notice" v-else-if="index % 6 === 3">📔 {{ item.name }}</a>
          <a href="/notice" v-else-if="index % 6 === 4">📙 {{ item.name }}</a>
          <a href="/notice" v-else-if="index % 6 === 5">📒 {{ item.name }}</a>
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
export default {
  name: "Notice",
  data() {
    return {
      fields: [{ key: "name", label: "wa" }],
      items: [
        { name: "공지사항 1" },
        { name: "공지사항 2" },
        { name: "공지사항 3" },
        { name: "공지사항 4" },
        { name: "공지사항 5" },
        { name: "공지사항 6" },
        { name: "공지사항 7" },
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    goNoticeCreate: function () {
      window.open("/notice_create", "_self");
    },
  },
};
</script>

<style>
a {
  font-size: 120%;
}

a:link {
  color: red;
  text-decoration: none;
}

a:visited {
  color: black;
  text-decoration: none;
}

a:hover {
  color: rgb(255, 207, 94);
  text-decoration: underline;
}

#listForm {
  max-width: 900px;
  min-width: 900px;
  max-height: 60%;
  min-height: 60%;
  margin: 0px auto;
  border-radius: 10px;
  /* padding: 100; */
  background-color: white;
}

#listForm {
  position: absolute;
  top: 90px;
  left: 22%;
}

#listForm #textNotice {
  text-align: left;
  /* margin: 0px auto; */
  /* max-width: 800px; */
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;
  margin-top: 20px;
}

#noticeTitle {
  position: absolute;
  left: 22%;
}

#noticeButton {
  /* margin: 0px auto; */
  float: right;
  border-radius: 10px;
  background-color: rgb(193, 243, 187);
}
</style>