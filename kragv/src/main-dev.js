import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import 'less-loader'
import './assets/css/global.css'
import './assets/fonts/iconfont.css'
import axios from 'axios'
// import 'element-ui/lib/theme-chalk/display.css'

Vue.config.productionTip = false

// axios.defaults.baseURL = 'http://192.168.43.244:8080/'
// axios.defaults.baseURL = 'http://127.0.0.1:8088'
axios.defaults.baseURL = '/api'

//在main.js设置全局的请求次数，请求的间隙
axios.defaults.retry = 4
axios.defaults.retryDelay = 1000

axios.interceptors.request.use(
  config => {
    config.headers.token = window.sessionStorage.getItem('token')
    return config
  },
  function axiosRetryInterceptor(err) {
    var config = err.config
    // If config does not exist or the retry option is not set, reject
    if (!config || !config.retry) return Promise.reject(err)

    // Set the variable for keeping track of the retry count
    config.__retryCount = config.__retryCount || 0

    // Check if we've maxed out the total number of retries
    if (config.__retryCount >= config.retry) {
      // Reject with the error
      return Promise.reject(err)
    }

    // Increase the retry count
    config.__retryCount += 1

    // Create new promise to handle exponential backoff
    var backoff = new Promise(function(resolve) {
      setTimeout(function() {
        resolve()
      }, config.retryDelay || 1)
    })

    // Return the promise in which recalls axios to retry the request
    return backoff.then(function() {
      return axios(config)
    })
  }
)

axios.interceptors.response.use(config => {
  return config
})

Vue.prototype.$http = axios

Vue.filter('dateFormat', function(originVal) {
  const dt = new Date(originVal)

  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')

  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')

  return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
})

Vue.filter('dateFormat_date', function(originVal) {
  const dt = new Date(originVal)

  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')

  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')

  return `${y}-${m}-${d}`
})

Vue.filter('dateFormat_time', function(originVal) {
  const dt = new Date(originVal)

  const y = dt.getFullYear()
  const m = (dt.getMonth() + 1 + '').padStart(2, '0')
  const d = (dt.getDate() + '').padStart(2, '0')

  const hh = (dt.getHours() + '').padStart(2, '0')
  const mm = (dt.getMinutes() + '').padStart(2, '0')
  const ss = (dt.getSeconds() + '').padStart(2, '0')

  return `${hh}:${mm}:${ss}`
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
