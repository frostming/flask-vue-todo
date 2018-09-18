import axios from 'axios'


const mockTodos = [
  {id: 1, text: 'Item 1', done: false},
  {id: 2, text: 'Item 2', done: true}
]

const mockRequest = ()=>{
  return new Promise((resolve, reject)=>{
    setTimeout(()=>{
      Math.random() < 0.85 ? resolve(mockTodos) : reject(new Error("Get Todo list error!"))
    }, 100)
  })
}

const api = axios.create({
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content')}
})

export default {
  getTodos () {
    return api.get('/todos').then(response => response.data)
  },
  addTodo (todo) {
    return api.post('/todo', todo).then(response => response.data)
  },
  removeTodo (todo) {
    return api.delete('/todo/' + todo.id).then(response => response.data)
  },
  editTodo (todo) {
    return api.put('/todo/' + todo.id, todo).then(response => response.data)
  },
  login({username, password, remember}) {
    return api.post('/auth/login', {username, password, remember}).then(response => response.data)
  },
  logout() {
    return api.get('/auth/logout').then(response => response.data)
  },
  register({username, password}) {
    return api.post('/auth/register', {username, password}).then(response => response.data)
  },
  getSession() {
    return api.get('/auth/session').then(response => response.data)
  }
}
