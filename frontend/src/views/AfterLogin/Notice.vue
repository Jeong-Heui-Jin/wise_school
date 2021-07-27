<template>
  <div
    class="fixed-top d-flex align-items-center justify-content-center"
    style="bottom: 0; overflow-y: auto; font-family: 'Jua', sans-serif"
    variant="light"
  >
    <NavSideBar />
    <NavBar />
    <div id="backgroundForm">
      <div id="listForm">
        <!-- 일반 리스트 태그로는 개행이 안됨 -->
        <!-- <ul>
        <li v-for="(notice, index) in noticeList" v-bind:key="index">
          {{ index }}{{ notice.name }}
        </li>
      </ul> -->
        <b-list-group>
          <b-list-group id="textNotice">
            <div>
              <span id="noticeTitle" style="text-align: left">공지사항</span
              ><button id="noticeButton" style="text-align: right">
                공지사항 작성
              </button>
            </div>
          </b-list-group>
          <b-list-group-item
            id="textNotice"
            v-for="(item, index) in items"
            v-bind:key="index"
          >
            <router-link id="notice" to="/notice" v-if="index % 6 === 0"
              >📕 {{ item.name }}</router-link
            >
            <router-link to="/notice" v-else-if="index % 6 === 1"
              >📗 {{ item.name }}</router-link
            >
            <router-link to="/notice" v-else-if="index % 6 === 2"
              >📘 {{ item.name }}</router-link
            >
            <router-link to="/notice" v-else-if="index % 6 === 3"
              >📔 {{ item.name }}</router-link
            >
            <router-link to="/notice" v-else-if="index % 6 === 4"
              >📙 {{ item.name }}</router-link
            >
            <router-link to="/notice" v-else-if="index % 6 === 5"
              >📒 {{ item.name }}</router-link
            >
          </b-list-group-item>
        </b-list-group>

        <!-- 설정 -->
        <!-- <b-table over :fields="fields" :items="items">
        <template colspan="1" #cell(index)="data">
          {{ data.index + 1 }}
        </template>
        <template style="text-align: 'left'" #cell(name)="data">
          {{ data.value }}
        </template>
      </b-table> -->
        <!-- <b-table-simple hover small caption-top responsive>
        <b-thead head-variant="dark">
          <b-tr>
            <b-th colspan="1">Country</b-th>
            <b-th colspan="3">City</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="(item, index) in items" v-bind:key="index">
            <b-th colspan="1">{{ index }}</b-th>
            <b-td colspan="9">{{ item.name }}</b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple> -->
      </div>
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
        { name: "공지사항 8" },
        { name: "공지사항 9" },
      ],
    };
  },
  components: {
    NavSideBar,
    NavBar,
  },
};
</script>

<style>
#listForm {
  max-width: 900px;
  min-width: 900px;
  max-height: 100%;
  min-height: 100%;
  margin: 0px auto;
  border-radius: 10px;
  padding: 100;
  background-color: white;
}

#listForm #textNotice {
  text-align: left;
  max-width: 800px;
  min-width: 800px;
  margin: 0px auto;
  border-radius: 10px;
}

#listForm #textNotice #notice {
  border: 1px solid;
}

#noticeTitle {
  font-size: 200%;
  display: inline-block;
}

#noticeButton {
  display: flex;
  align-items: center;
  margin: 0px auto;
  float: right;
  border-radius: 10px;
  background-color: rgb(245, 183, 102);
}
</style>