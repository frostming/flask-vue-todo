<script>
  import TodoItem from './TodoItem.vue'

  const filters = {
    all: todos => todos,
    undone: todos => todos.filter(todo => !todo.done),
    completed: todos => todos.filter(todo => todo.done)
  }

  export default {
    components: { TodoItem },
    data() {
      return {
        visibility: 'all',
        filters
      }
    },
    computed: {
      todos () {
        return this.$store.state.todos
      },
      visibleTodos () {
        return filters[this.visibility](this.todos)
      }
    },
    methods: {
      addTodo(e) {
        const text = e.target.value
        if (text.trim()) {
          this.$store.dispatch('addTodo', text)
        }
        e.target.value = ''
      }
    },
    filters: {
      capitalize: s => s.charAt(0).toUpperCase() + s.slice(1)
    }
  }
</script>

<template>
  <div id="todo">
    <input placeholder="What needs to be done?"
          id="todo-input"
          @keyup.enter="addTodo">
    <ul class="nav">
      <li v-for="(val, key) in filters" :key="key">
        <a class="nav-link" :class="{active: visibility === key}"
           href="javascript:void(0)"
           @click="visibility = key">{{ key|capitalize }}</a>
      </li>
    </ul>
    <ul class="todo-list">
      <TodoItem v-for="(item, index) in visibleTodos" :key="index" :todo="item"/>
    </ul>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}
#todo-input {
  margin: 10px 0;
  padding: 12px 12px 12px 20px;
  font-size: 1.5em;
  width: 100%;
  border: 1px solid #dddddd;
  box-shadow: 3px 3px 1px rgba(0, 0, 0, 0.06);
}
#todo-input:focus {
  outline: none;
}
.nav-link {
  padding: 8px;
  box-sizing: border-box;
  color: #2c3e50;
  text-decoration: none;
}
.nav-link:hover{
  border-bottom: 3px solid #42b983;
}
.nav-link.active {
  color: #42b983;
  font-weight: bold;
  border-bottom: 3px solid #42b983;
}
ul {
  list-style-type: none;
  padding: 0;
}
.nav>li {
  display: inline-block;
  margin: 0 10px;
}
</style>
