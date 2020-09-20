import Vue from 'vue'
import App from './App.vue'
// import  from 'bootstrap-vue'
import { VBTogglePlugin, BootstrapVue } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(VBTogglePlugin)
Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
