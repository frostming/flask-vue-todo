<script>
  import { mapActions } from 'vuex'

  export default {
    props: ['todo'],
    data () {
      return {
        editing: false
      }
    },
    methods: mapActions(['toggleTodo', 'removeTodo'])
  }
</script>

<template>
  <li class="todo-item" :class="{complete: todo.done}">
    <div class="view">
      <label class="todo-label">
        <input type="checkbox"
               class="checkbox"
               @change="toggleTodo(todo)"
               :checked="todo.done">
          {{ todo.text }}
      </label>
      <button class="remove-item" @click="removeTodo(todo)"><i class="fa fa-times"></i></button>
    </div>
  </li>
</template>

<style>
.todo-item {
  font-size: 1.5em;
  text-align: left;
  padding: 5px 0;
}
.todo-item:hover {
  background: #f7f7f7;
}
.todo-item:hover .remove-item, .todo-item:hover .edit-item {
  display: block;
}
.complete .todo-label {
  position: relative;
  text-decoration: line-through;
  cursor: pointer;
}
.checkbox {
  position: relative;
  cursor: pointer;
  margin-right: 2.5em;
  -webkit-appearance: none;
  top: -0.375em;
}
.checkbox:focus {
  outline: none;
}
.checkbox::before {
  transition: all 0.3s ease-in-out;
  content: "";
  position: absolute;
  left: 0;
  top: -0.875em;
  z-index: 1;
  width: 1.5em;
  height: 1.5em;
  border: 2px solid #f2f2f2;
}
.checkbox:checked::before {
  transform: rotate(-45deg);
  height: 0.75em;
  border-color: #42b983;
  border-top-style: none;
  border-right-style: none;
}
.remove-item, .edit-item {
  -webkit-appearance: none;
  float: right;
  font-size: 1.1em;
  background: none;
  border: none;
  cursor: pointer;
  margin-top: -2px;
  display: none;
}
.remove-item:focus {
  outline: none;
}
</style>
