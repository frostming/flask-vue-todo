import Vue from 'vue'
import App from './App.vue'
import store from './store'
import VueFlashMessage from 'vue-flash-message';
import VueRouter from 'vue-router'
import router from './router'
Vue.use(VueFlashMessage, {
  messageOptions: {
    timeout: 3000
  }
})
Vue.use(VueRouter)

new Vue({
  store,
  router,
  el: '#app',
  render: h => h(App)
})
