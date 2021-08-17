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
    now_user: null,
    infomation_homework:null,
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
    SET_USER: function (state, user) {
      state.now_user = user
    },
    SELECT_INFO_HOMEWORK:function(state, info_homework){
      state.infomation_homework = info_homework;
    }
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
    setUser: function ({ commit }, user) {
      commit('SET_USER', user)
    },
    selectInfoHomework:function({commit}, info_homework){
      commit('SELECT_INFO_HOMEWORK', info_homework);
    }
  },
  modules: {
  }
})
