<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">공지사항</h1>

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
          </div> </b-list-group
        ><b-list-group-item
          id="textNoticeImportant"
          v-for="(important_item, index) in important_items"
          v-bind:key="index"
        >
          <a id="noticeImportant" href="/notice"
            >🎈 {{ important_item.name }}</a
          >
        </b-list-group-item>
        <b-list-group-item
          id="textNotice"
          v-for="(item, index) in items"
          v-bind:key="index"
        >
          <a id="notice" href="/notice" v-if="index % 6 === 0"
            >📕 {{ item.name }}</a
          >
          <a id="notice" href="/notice" v-else-if="index % 6 === 1"
            >📗 {{ item.name }}</a
          >
          <a id="notice" href="/notice" v-else-if="index % 6 === 2"
            >📘 {{ item.name }}</a
          >
          <a id="notice" href="/notice" v-else-if="index % 6 === 3"
            >📔 {{ item.name }}</a
          >
          <a id="notice" href="/notice" v-else-if="index % 6 === 4"
            >📙 {{ item.name }}</a
          >
          <a id="notice" href="/notice" v-else-if="index % 6 === 5"
            >📒 {{ item.name }}</a
          >
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from 'vuex'

export default {
  name: "Notice",
  data() {
    return {
      perPage: 7,
      currentPage: 1,
      important_items: [
        { name: "중요 공지사항 1" },
        { name: "중요 공지사항 2" },
        { name: "중요 공지사항 3" },
        { name: "중요 공지사항 4" },
      ],
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
    setToken: function () {
      this.$store.dispatch('setToken')
    },
    getNoticeList: function () {
      axios({
        method: "get",
        url: 'http://i5a205.p.ssafy.io:8000/notice/',
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goNoticeCreate: function () {
      window.open("/notice_create", "_self");
    },
    goNoticeView: function () {
      this.$store.dispatch('selectNotice')
      // window.open("/notice_view", "_self")
    }
  },
  computed: {
    ...mapState([
      'headers'
    ]),
  },
  created: function() {
    this.setToken()
    this.getNoticeList()
  }
};
</script>

<style>
#noticeImportant {
  font-weight: bold;
  font-size: 120%;

  /* padding: 10px; */
}

#noticeImportant:link {
  color: red;
  text-decoration: none;
}

#noticeImportant:visited {
  color: black;
  text-decoration: none;
}

#noticeImportant:hover {
  color: dodgerblue;
  text-decoration: underline;
}

#notice {
  font-size: 120%;
}

#notice:link {
  color: red;
  text-decoration: none;
}

#notice:visited {
  color: black;
  text-decoration: none;
}

#notice:hover {
  color: rgb(255, 207, 94);
  text-decoration: underline;
}

#listForm {
  position: fixed;
  left: 500px;
  top: 90px;
  max-width: 900px;
  min-width: 900px;
  max-height: 60%;
  min-height: 60%;
  border-radius: 10px;
  /* padding: 100; */
  background-color: white;
}

#listForm #textNoticeImportant {
  background-color: #f9f5d8;
  text-align: left;
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;
  margin-top: 20px;
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