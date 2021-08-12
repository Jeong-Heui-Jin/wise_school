<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">공지사항</h1>

    <div id="listForm">
      <div>
        <button
          id="noticeButton"
          style="text-align: right"
          @click="goNoticeCreate()"
        >
          공지사항 작성
        </button>
      </div>
      <b-list-group id="groupPosition">
        <!-- 📗📘📔📙📒📕 -->
        <b-list-group-item
          id="textNoticeImportant"
          v-for="(importantItem, import_index) in importantItems"
          v-bind:key="import_index"
          v-on:click="goNoticeView(importantItem)"
        >
          📙 {{ importantItem.title }}
        </b-list-group-item>
        <b-list-group-item
          id="textNotice"
          v-for="(item, normal_index) in items"
          v-bind:key="normal_index"
          v-on:click="goNoticeView(item)"
        >
          📙 {{ item.title }}
        </b-list-group-item>
      </b-list-group>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBar.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "Notice",
  data() {
    return {
      perPage: 7,
      currentPage: 1,
      importantItems: [],
      items: [],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    rowClass(item) {
      if (item.is_important === true) {
        return "table-success";
      }
    },
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    getNoticeList: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/notice/",
        // url: "http://127.0.0.1:8000/notice/",
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data);
          // id 기준 내림차순
          res.data.sort(function (a, b) {
            if (a.id > b.id) {
              return -1;
            } else {
              return 1;
            }
          });

          // registertime print format 변경
          for (let i = 0; i < res.data.length; ++i) {
            var temp = res.data[i].registertime;
            // console.log(temp);

            res.data[i].registertime =
              temp.substring(5, 7) +
              "월 " +
              temp.substring(8, 10) +
              "일 " +
              temp.substring(11, 13) +
              "시 " +
              temp.substring(14, 16) +
              "분";
          }

          // importantItems, items로 데이터 분리
          for (let i = 0; i < res.data.length; ++i) {
            if (res.data[i].is_important) {
              this.importantItems.push(res.data[i]);
            } else {
              this.items.push(res.data[i]);
            }
          }

          console.log(this.importantItems);
          console.log(this.items);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goNoticeCreate: function () {
      window.open("/notice_create", "_self");
    },
    goNoticeView: function (notice) {
      console.log(notice);
      this.$store.dispatch("selectNotice", notice);
      this.$router.push({ name: "NoticeView" });
      // window.open("/notice_view", "_self")
    },
  },
  computed: {
    ...mapState(["headers", "now_user"]),
  },
  created: function () {
    this.setToken();
    this.getNoticeList();
    console.log(this.now_user);
  },
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
  width: 100%;
  height: 100%;
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

#noticeTitle {
  position: absolute;
  left: 22%;
}

#listForm #groupPosition {
  position: absolute;
  min-width: 900px;
  top: 30px;

  /* min-width: 800px;
  border-radius: 10px;
  border: 1px solid; */
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
  top: 20px;
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;
}
#listForm #noticeButton {
  /* margin: 0px auto; */
  /* float: right; */
  position: absolute;
  left: 800px;
  width: 100px;
  border-radius: 10px;
  background-color: rgb(193, 243, 187);
}
</style>