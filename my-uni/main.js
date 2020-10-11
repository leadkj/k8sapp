import Vue from 'vue'
import App from './App'
import {myRequest} from './util/api.js'

Vue.prototype.$myRequest = myRequest  //挂在方法到全局，方便调用
Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
