<template>
  <div id="app">
    <flash-message class="myCustomClass"></flash-message>
    <img src="./assets/flask.png">
    <img src="./assets/logo.png">
    <h1>Flask Vue Todo</h1>
    <section class="main">
      <router-view></router-view>
    </section>
    <footer>
      <ul>
        <li><a href="https://github.com/frostming/flask-vue-todo">GitHub</a></li>
        <li>&copy;2018 <a href="https://frostming.com">Frost Ming</a></li>
      </ul>
    </footer>
  </div>
</template>

<script>
require('vue-flash-message/dist/vue-flash-message.min.css');

export default {
  name: 'app',
}
</script>

<style>
* {
  box-sizing: border-box;
}

.main {
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

#app footer {
  margin: 100px auto 0 auto;
  max-width: 600px;
  text-align: right;
  font-size: .95em;
}

#app footer>ul>li {
  display: inline-block;
  padding-right: .5em;
}

footer a {
  color: inherit;
}

footer li + li {
  padding-left: .5em;
  padding-right: 0;
  border-left: 1px solid #e6e6e6;
}

form {
  text-align: left;
}

input[type=text], input[type=password] {
  margin: 10px 0;
  padding: 12px 12px 12px 20px;
  width: 100%;
  border: 1px solid #dddddd;
  box-shadow: 3px 3px 1px rgba(0, 0, 0, 0.06);
}

input[type=text]:focus, input[type=password]:focus, .btn:focus{
  outline: none;
}

.btn {
  text-decoration: none;
  color: white;
  padding: 10px;
  background-color: #42b983;
  border: none;
  font-size: 1em;
  cursor: pointer;
}

.form-footer {
  display: flex;
  justify-content: space-between;
  margin: 10px 0;
}
</style>
