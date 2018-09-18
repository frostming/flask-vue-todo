<script>
import Login from './Login.vue'
import Register from './Register.vue'
import Todo from './Todo.vue'
import api from '../api'

export default {
  components: { Todo },
  data () {
    return {
      isLoggedIn: false
    }
  },
  mounted() {
    const vm = this
    api.getSession().then(resp => {
      vm.isLoggedIn = true
    })
  },
  watch: {
    isLoggedIn (val) {
      this.$store.dispatch('getTodos')
    }
  }
}
</script>

<template>
  <Todo v-if="isLoggedIn"></Todo>
  <div v-else class="auth">
    <router-link to="/login" class="btn">Login</router-link>
    <router-link to="/register" class="btn">Register</router-link>
  </div>
</template>

<style>
.btn {
  text-decoration: none;
  color: white;
  padding: 10px;
  background-color: #42b983;
}

</style>
