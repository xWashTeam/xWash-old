// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import axios from 'axios'
import router from './router'
import vueLoading from 'vue-loading-template'
import VueTouch from 'vue-touch'
import {Notification} from 'element-ui'
axios.defaults.timeout = 300;
axios.interceptors.request.use(function (config) {
  // Do something before request is sent
  return config;
}, function (error) {
  // Do something with request error
  console.log(error.message);
  return Promise.reject(error);
});
axios.interceptors.response.use(response => {
  return response
}, err => {
    if(err.message == 'timeout of 5000ms exceeded'){
        return {code : 10,message:'请求超时'}
    }else{
        return {code :500, message:'网络连接失败，请稍后重试'}
    }
})

Vue.prototype.$notify = Notification;
Vue.config.productionTip = false
Vue.use(vueLoading)
Vue.use(VueTouch, {name: 'v-touch'})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
