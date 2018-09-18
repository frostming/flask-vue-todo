import todoApi from '../../api'

export const types = {
  ADD_TODO: 'addTodo',
  REMOVE_TODO: 'removeTodo',
  TOGGLE_TODO: 'toggleTodo',
  EDIT_TODO: 'editTodo',
  GET_TODOS: 'getTodos'
}

export default {
  [types.ADD_TODO] ({commit}, text) {
    const todo = {text, done: false}
    const vm = this
    return todoApi.addTodo(todo).then(data => {
      commit('addTodo', data.todo)
    }).catch(e => {
      vm.error(e.response.data.description)
    })
  },
  [types.REMOVE_TODO] ({commit}, todo) {
    commit('removeTodo', todo)
    const vm = this
    return todoApi.removeTodo(todo).catch(e => {
      vm.error(e.response.data.description)
    })
  },
  [types.TOGGLE_TODO] ({commit}, todo) {
    commit('editTodo', {todo, done:!todo.done})
    const vm = this
    return todoApi.editTodo(todo).catch(e => {
      vm.error(e.response.data.description)
    })
  },
  [types.EDIT_TODO] ({commit}, {todo, value}) {
    commit('editTodo', {todo, text:value})
    const vm = this
    return todoApi.editTodo(todo).catch(e => {
      vm.error(e.response.data.description)
    })
  },
  [types.GET_TODOS] ({commit}) {
    const vm = this
    return todoApi.getTodos().then(data => {
      commit('setTodos', data)
    }).catch(e => {
      vm.error(e.response.data.description)
    })
  }
}
