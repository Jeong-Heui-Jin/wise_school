<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">공지사항</h1>

    <div id="noticeForm">
      <div v-if="now_user.usertype===1">
        <button
          id="noticeButton"
          style="text-align: right"
          @click="goNoticeCreate()"
        >
          공지사항 작성
        </button>
      </div>
      <!-- 📗📘📔📙📒📕 -->
      <b-table
        id="noticeTable my-table"
        :hover="true"
        :small="false"
        :borderless="true"
        :fields="fields"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
        :tbody-tr-class="rowClass"
        thead-class="hidden_header"
        @row-clicked="goNoticeView"
      >
        <template #cell(title)="data">
          <div v-if="data.item.is_important === true" id="textNoticeImportant">
            📙 {{ data.item.title }}
          </div>
          <div v-else id="textNotice">📙 {{ data.item.title }}</div>
        </template>
      </b-table>

      <b-pagination
        pills
        id="paginationForm"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>
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
      perPage: 8,
      currentPage: 1,
      fields: [
        {
          key: "title",
          label: "제목",
        },
      ],
      // importantItems: [],
      items: [],
      isImportant: [],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
  methods: {
    setToken: function () {
      this.$store.dispatch("setToken");
    },
    rowClass(item, type) {
      if (!item || type !== "row") return;
      // if (item.status === "awesome") return "table-success";
    },
    getNoticeList: function () {
      axios({
        method: "get",
        url: "http://i5a205.p.ssafy.io:8000/notice/",
        // url: "http://127.0.0.1:8000/notice/",
        headers: this.headers,
      })
        .then((res) => {
          // console.log(res.data);
          // id 기준 내림차순
          res.data.sort(function (a, b) {
            if (a.is_important === b.is_important) {
              if (a.id > b.id) {
                return -1;
              } else {
                return 1;
              }
            } else if (a.is_important) {
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
              "분"; // importantItems, items로 데이터 분리
          }

          for (let i = 0; i < res.data.length; ++i) {
            if (res.data[i].is_important) {
              // console.log(i);
              res.data[i].status = "awesome";
            }
            this.items.push(res.data[i]);
          }
          // this.items = res.data;
          // console.log(this.items);

          // console.log(this.importantItems);
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
    rows() {
      return this.items.length;
    },
    ...mapState(["headers", "now_user"]),
  },
  created: function () {
    this.setToken();
    this.getNoticeList();
    // console.log(this.now_user);
  },
};
</script>

<style>
.hidden_header {
  display: none;
}

#noticeImportant {
  font-weight: bold;
  font-size: 120%;

  /* padding: 10px; */
}

#noticeImportant:link {
  color: rgb(115, 255, 0);
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

#noticeForm {
  position: fixed;
  left: 400px;
  top: 152px;
  max-width: 1000px;
  min-width: 1000px;
  max-height: 600px;
  border-radius: 10px;
  /* padding: 100; */
  /* background-color: white; */
}

#noticeForm #noticeTitle {
  position: fixed;
  top: 10px;
  left: 120px;
  margin-left: 220px;
  margin-top: 20px;
}

#noticeForm #noticeTable {
  position: absolute;
  min-width: 900px;

  /* min-width: 800px;
  border-radius: 10px;
  border: 1px solid; */
}
#noticeForm #textNoticeImportant {
  background-color: #f9f5d8;
  text-align: left;
  line-height: 40px;
  min-height: 40px;
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;
  margin-top: 5px;
}
#noticeForm #textNotice {
  background-color: white;
  text-align: left;
  line-height: 40px;
  min-height: 40px;
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;
  margin-top: 5px;
}

#noticeButton {
  position: absolute;
  top: -30px;
  left: 890px;

  min-width: 100px;

  border-radius: 10px;
  background-color: rgb(193, 243, 187);
}

#noticeForm #paginationForm {
  bottom: 50px;
}
</style>