import Vue from 'vue'
import Router from 'vue-router'
import home from '@/pages/Home'
import news from '@/pages/News'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/news',
      name: 'news',
      component: news
    }
  ]
})
