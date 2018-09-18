<script>
import api from '../api'

export default {
  data () {
    return {
      username: "",
      password: "",
      confirm: "",
    }
  },
  methods: {
    checkForm (e) {
      e.preventDefault()
      const vm = this
      if (this.password !== this.confirm) {
        console.log('Two passwords are different!')
        this.error('Two passwords are different!')
      } else {
        api.register({
          username: this.username,
          password: this.password
        }).then(data => {
          vm.$router.push({ path: '/' }, () => {
            vm.success('Register successfully, please login!')
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
}
</script>

<template>
  <form action="/auth/login" method="post" @submit="checkForm">
    <h2>Register</h2>
    <div class="form-group">
      <label for="username">Username</label>
      <input type="text" id="username" name="username" v-model="username" required>
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" id="password" name="password" v-model="password" required>
    </div>
    <div class="form-group">
      <label for="">Confirm Password</label>
      <input type="password" id="confirm" name="confirm" v-model="confirm" required>
    </div>
    <div class="form-footer">
      <button type="submit" name="submit" class="btn">Submit</button>
      <router-link to="/" class="btn">Return Home</router-link>
    </div>
  </form>
</template>

<style>

</style>
