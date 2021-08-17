<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">알림</h1>

    <div id="listForm">
      <div>
        <button
          id="noticeButton"
          style="text-align: right"
          @click="deleteAll()"
        >
          전체 삭제
        </button>
      </div>
      <b-list-group id="groupPosition">
        <!-- 📗📘📔📙📒📕 -->
        <b-list-group-item
          id="textNoticeImportant"
          v-for="(notification, idx) in notifications"
          v-bind:key="idx"
        >
          {{ notification.content }}
          {{ notification.registertime }}
          <b-button @click="deleteNotification(notification)">삭제</b-button>
        </b-list-group-item>
        <!-- <b-list-group-item
          id="textNotice"
          v-for="(item, normal_index) in items"
          v-bind:key="normal_index"
          v-on:click="goNoticeView(item)"
        >
          📙 {{ item.title }}
        </b-list-group-item> -->
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
  name: "Notification",
  data() {
    return {
      perPage: 7,
      currentPage: 1,
      notifications: [],
      userId: 2,
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
    getNotifications: function () {
      axios({
        method: "get",
        // url: `http://i5a205.p.ssafy.io:8000/notice/notification/${this.userId}/`,
        url: `http://127.0.0.1:8000/notice/notification/${this.userId}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data)

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

            var content = res.data[i].content;
            if (content.substring(0,2)==='숙제') {
              res.data[i].content = '📘 ' + content
            } else {
              res.data[i].content = '📙 ' + content
            }
          }

          this.notifications = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteAll: function () {
    },
    deleteNotification: function (notification) {
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/notice/notification/${notification.id}/`,
        // url: `http://127.0.0.1:8000/notice/notification/${notification.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res)
          alert('삭제되었습니다!')
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    ...mapState(["headers", "now_user"]),
  },
  created: function () {
    this.setToken();
    this.getNotifications();
    this.userId = this.now_user.id
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