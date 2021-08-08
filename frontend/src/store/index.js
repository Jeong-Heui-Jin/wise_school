import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedMenu: 'Home',
    headers: null,
  },
  mutations: {
    SET_TOKEN: function (state, config) {
      state.headers = config
    }
  },
  actions: {
    setToken: function ({ commit }) {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      commit('SET_TOKEN', config)
      // return config
    },
  },
  modules: {
  }
})
