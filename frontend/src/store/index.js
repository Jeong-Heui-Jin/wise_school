import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedMenu: 'Home',
    headers: null,
    selected_homework: null,
    selected_notice: null,
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
  },
  modules: {
  }
})
