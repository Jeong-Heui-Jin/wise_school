<template>
  <div style="font-family: 'Jua', sans-serif" variant="light">
    <NavSideBar />
    <NavBar />

    <h1 id="title">알림</h1>

    <div id="notificationForm">
      <div>
        <button id="notificationBtn" @click="deleteAll">전체 삭제</button>
      </div>
      <!-- 📗📘📔📙📒📕 -->
      <!-- previous version -->
      <!-- <b-list-group id="groupPosition">
        <b-list-group-item
          id="textNotification my-table"
          v-for="(notification, idx) in notifications"
          v-bind:key="idx"
          class="d-flex justify-content-between align-items-center"
        >
          <div>
            {{ notification.content }}
          </div>
          <div>
            {{ notification.registertime }}
            <b-button @click="deleteNotification(notification)">삭제</b-button>
          </div>
        </b-list-group-item>
      </b-list-group> -->

      <b-table
        id="textNotification my-table"
        :hover="true"
        :small="false"
        :borderless="true"
        :fields="fields"
        :items="notifications"
        :per-page="perPage"
        :current-page="currentPage"
        thead-class="hidden_header"
      >
        <template #cell(content)="data">
          <div id="textNotification">
            <a id="alignLeft">{{ data.item.content }}</a
            ><button id="deleteBtn" @click="deleteNotification(data.item)">
              삭제
            </button>
          </div>
        </template>
      </b-table>

      <!-- Pagination -->
      <b-pagination
        id="paginationForm"
        pills
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
  name: "Notification",
  data() {
    return {
      perPage: 8,
      currentPage: 1,
      fields: [{ key: "content", label: "알림" }],
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
        url: `http://i5a205.p.ssafy.io:8000/notice/notification/${this.userId}/`,
        // url: `http://127.0.0.1:8000/notice/notification/${this.userId}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res.data);

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
            if (content.substring(0, 2) === "숙제") {
              res.data[i].content = "📘 " + content;
            } else {
              res.data[i].content = "📙 " + content;
            }
          }

          this.notifications = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteAll: function () {
      console.log("deleteAll function call", this.userId);
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/notice/notification/${this.userId}`,
        // url: `http://127.0.0.1:8000/notice/notification/${this.userId}`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res);
          alert("전체삭제되었습니다!");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteNotification: function (notification) {
      console.log(notification);
      axios({
        method: "delete",
        url: `http://i5a205.p.ssafy.io:8000/notice/notification_detail/${notification.id}/`,
        // url: `http://127.0.0.1:8000/notice/notification_detail/${notification.id}/`,
        headers: this.headers,
      })
        .then((res) => {
          console.log(res);
          alert("삭제되었습니다!");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  computed: {
    rows() {
      return this.notifications.length;
    },
    ...mapState(["headers", "now_user"]),
  },
  created: function () {
    this.setToken();
    this.userId = this.now_user.id;
    this.getNotifications();
  },
};
</script>

<style>
#alignLeft {
  float: left;
}

#deleteBtn {
  position: absolute;
  /* left: 850px; */
  left: 930px;
  font-size: 110%;

  width: 55px;
  height: 33px;
  line-height: 35px;
  border-radius: 5px;

  background-color: rgb(253, 155, 142);
}

#notificationForm {
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

#noticeTitle {
  position: absolute;
  left: 22%;
}

#notificationForm #groupPosition {
  position: absolute;
  min-width: 900px;
  top: 30px;
}
#notificationForm #textNotification {
  background-color: #f9f5d8;
  text-align: left;
  line-height: 40px;
  min-height: 40px;
  min-width: 800px;
  border-radius: 10px;
  border: 1px solid;

  display: flex;
  align-items: center; /* 수직 정렬 */
  flex-direction: row; /* default: row */

  margin-top: 5px;
}

#notificationForm #notificationBtn {
  position: absolute;

  top: -20px;
  left: 917px;

  border-radius: 10px;
  background-color: rgb(193, 243, 187);
}

#notificationForm #paginationForm {
  bottom: 50px;
}
</style>