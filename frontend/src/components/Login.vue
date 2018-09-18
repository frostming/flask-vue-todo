<script>
import api from '../api'

export default {
  data () {
    return {
      username: "",
      password: "",
      remember: false
    }
  },
  methods: {
    checkForm (e) {
      e.preventDefault()
      const vm = this
      api.login({
        username: this.username,
        password: this.password,
        remember: this.remember
      }).then(data => {
        vm.$router.push({ path: '/' }, () => {
          vm.success('Logged in successfully!')
        })
      }).catch(e => {
        let errors = e.response.data.message
        for (let key in errors) {
          errors[key].forEach(e => {vm.error(`${key}: ${e}`)})
        }
      })
    }
  }
}
</script>

<template>
  <form action="/auth/login" method="post" @submit="checkForm">
    <h2>Login</h2>
    <div class="form-group">
      <label for="username">Username</label>
      <input type="text" id="username" name="username" v-model="username" required>
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" id="password" name="password" v-model="password" required>
    </div>
    <div class="form-group">
      <label for="remember">
        <input type="checkbox" id="remember" name="remember" v-model="remember">
        Remember Me
      </label>
    </div>
    <div class="form-footer">
      <button type="submit" name="submit" class="btn">Submit</button>
      <router-link to="/" class="btn">Return Home</router-link>
    </div>
  </form>
</template>

<style>
</style>
