import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import Home from './Home.vue'

Vue.use(BootstrapVue);

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

new Vue({
  el: '#app',
  components: {
    home: Home
  },
  render() {
    return <div class='container'>
      <home />
      </div>
  }
})
