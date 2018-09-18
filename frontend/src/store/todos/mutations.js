export default {
  addTodo (state, todo) {
    state.push(todo)
  },

  removeTodo (state, todo) {
    state.splice(state.indexOf(todo), 1)
  },

  editTodo (state, { todo, text = todo.text, done = todo.done }) {
    todo.text = text
    todo.done = done
  },

  setTodos (state, todos) {
    state.splice(0, state.length, ...todos)
  }
}
