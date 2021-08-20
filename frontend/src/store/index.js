import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    selectedMenu: 'Home',
    headers: null,
    selected_homework: null,
    selected_notice: null,
    selected_attitude: null,
    selected_submited_homework: null,
    now_user: null,
    information_homework:null,
    user_class: null
  },
  mutations: {
    SET_TOKEN: function (state, config) {
      state.headers = config
    },
    SELECT_HOMEWORK: function (state, homework) {
      state.selected_homework = homework
    },
    SELECT_NOTICE: function (state, notice) {
      state.selected_notice = notice
    },
    SELECT_ATTITUDE: function (state, attitude) {
      state.selected_attitude = attitude
    },
    SELECT_SUBMITED_HOMEWORK: function (state, homeworkInfo) {
      state.selected_submited_homework = homeworkInfo
    },
    SET_USER: function (state, user) {
      state.now_user = user
    },
    SELECT_INFO_HOMEWORK:function(state, info_homework){
      state.information_homework = info_homework;
    },
    SET_USER_CLASS: function (state, class_id) {
      state.user_class = class_id
    },
  },
  actions: {
    setToken: function ({ commit }) {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      commit('SET_TOKEN', config)
    },
    selectHomework: function ({ commit }, homework) {
      commit('SELECT_HOMEWORK', homework)
    },
    selectNotice: function ({ commit }, notice) {
      commit('SELECT_NOTICE', notice)
    },
    selectAttitude: function ({ commit }, attitude) {
      commit('SELECT_ATTITUDE', attitude)
    },
    selectSubmitedHomework: function ({ commit }, homeworkInfo) {
      commit('SELECT_SUBMITED_HOMEWORK', homeworkInfo)
    },
    setUser: function ({ commit }, user) {
      commit('SET_USER', user)
    },
    selectInfoHomework:function({commit}, info_homework){
      commit('SELECT_INFO_HOMEWORK', info_homework);
    },
    setUserClass: function ({ commit }, class_id) {
      commit('SET_USER_CLASS', class_id)
    },
  },
  modules: {
  }
})
