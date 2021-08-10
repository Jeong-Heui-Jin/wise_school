<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">공지사항</h1>

    <div id="listForm">
      <!-- <b-list-group>
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
      </b-list-group> -->
      <b-table
        id="my-table textNotice"
        :hover="true"
        :small="false"
        :borderless="true"
        :items="items"
        :fields="fields"
        :per-page="perPage"
        :current-page="currentPage"
        :tbody-tr-class="rowClass"
      >
        <template #cell(items)="data">
          <b-link v-if="data.items.is_important === true">{{
            data.items
          }}</b-link>
          <b-link v-else>안 중요!</b-link>
        </template>
      </b-table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavSideBar from "@/components/NavSideBarTeacher.vue";
import NavBar from "@/components/NavBar.vue";
import { mapState } from "vuex";

export default {
  name: "Notice",
  data() {
    return {
      perPage: 7,
      currentPage: 1,
      fields: [
        { key: "id", label: "번호" },
        { key: "content", label: "공지사항 제목" },
        { key: "registertime", label: "날짜" },
      ],
      items: [
        // { name: "공지사항 1" },
        // { name: "공지사항 2" },
        // { name: "공지사항 3" },
        // { name: "공지사항 4" },
        // { name: "공지사항 5" },
        // { name: "공지사항 6" },
        // { name: "공지사항 7" },
      ],
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
        // url: "http://i5a205.p.ssafy.io:8000/notice/",
        url: "http://127.0.0.1:8000/notice/",
        headers: this.headers,
      })
        .then((res) => {
          // Print Before
          // for (let i = 0; i < res.data.length; ++i) {
          //   console.log(
          //     "Before :",
          //     "id :",
          //     res.data[i].id,
          //     ", is_important :",
          //     res.data[i].is_important
          //   );
          // }

          // 중요도 우선 & 중요도가 같다면 id 기준 내림차순
          res.data.sort(function (a, b) {
            if (a.is_important === b.is_important) {
              if (a.id > b.id) {
                return -1;
              } else {
                return 1;
              }
            } else {
              if (a.is_important > b.is_important) {
                return -1;
              } else {
                return 1;
              }
            }
          });
          // Print After
          // for (let i = 0; i < res.data.length; ++i) {
          //   console.log(
          //     "After :",
          //     "id :",
          //     res.data[i].id,
          //     ", is_important :",
          //     res.data[i].is_important
          //   );
          // }
          this.items = res.data; // 모든 items의 end 데이터를 가공한다.
          for (let i = 0; i < this.items.length; ++i) {
            var temp = this.items[i].registertime;
            console.log(temp);

            this.items[i].registertime =
              temp.substring(5, 7) +
              "월 " +
              temp.substring(8, 10) +
              "일 " +
              temp.substring(11, 13) +
              "시 " +
              temp.substring(14, 16) +
              "분";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goNoticeCreate: function () {
      window.open("/notice_create", "_self");
    },
    goNoticeView: function () {
      this.$store.dispatch("selectNotice");
      // window.open("/notice_view", "_self")
    },
  },
  computed: {
    ...mapState(["headers"]),
  },
  created: function () {
    this.setToken();
    this.getNoticeList();
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