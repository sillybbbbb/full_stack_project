import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
import { createApp } from 'vue'
import 'xe-utils'
import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'
createApp(App).use(VXETable).mount('#app')
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
