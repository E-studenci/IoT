import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import CurrentClients from '../views/CurrentClients.vue'
import AllClients from '../views/AllClients.vue'
import AddClient from '../views/AddClient.vue'
import EditClient from '../views/EditClient.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
  },
  {
    path: '/addClient',
    name: 'AddClient',
    component: AddClient
  },
  {
    path: '/editClient',
    name: 'EditClient',
    component: EditClient
  },
  {
    path: '/login', 
    redirect: '/'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
