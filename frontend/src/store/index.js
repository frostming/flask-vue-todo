import Vue from 'vue'
import Vuex from 'vuex'
import todos from './todos'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { todos }
})
