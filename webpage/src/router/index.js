import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import CurrentClients from '../views/CurrentClients.vue'
import AllClients from '../views/AllClients.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/currentClients',
    name: 'CurrentClients',
    component: CurrentClients
  },
  {
    path: '/allClients',
    name: 'AllClients',
    component: AllClients
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
