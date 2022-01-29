import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import VueRouter from 'vue-router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter);

import Login from './views/Login.vue';
import CurrentClients from './views/CurrentClients.vue';
import AllClients from './views/AllClients.vue';
import AddClient from './views/AddClient.vue';
import EditClient from './views/EditClient.vue';

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    { path: '/login', component: Login},
    { path: '/', component: Login},
    { path: '/currentClients', component: CurrentClients},
    { path: '/allClients', component: AllClients},
    { path: '/addClient', component: AddClient},
    { path: '/editClient', component: EditClient}
  ]
});

Vue.prototype.$development = 'http://130.61.111.97:20001/'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
