import {createRouter,createWebHashHistory} from 'vue-router'
import Admin from '~/layouts/admin.vue'
import Index from '~/pages/index.vue'
import Login from '~/pages/login.vue'
import HStress from '~/pages/issues/HilStress.vue'
import List from '~/pages/issues/list.vue'
import HData from '~/pages/issues/HilData.vue'
import Review from '~/pages/issues/review.vue'


import User from '~/pages/user.vue'
import Asset from '~/pages/asset.vue'
import Setting from '~/pages/setting.vue'

import NotFound from '~/pages/404.vue'


const routes = [
  {
    path:"/",
    component:Admin,
    children:[{
        path:"/",
        component:Index,
        meta:{
            title:"后台首页"
        }
    },
     
    {
      path:"/issues/stress",
      component:HStress,
      meta:{
          title:"压测版本统计"
      }
    },
     
    {
      path:"/issues/list",
      component:List,
      meta:{
          title:"Issue 问题表"
      }
   },
   {
    path:"/issues/data",
    component:HData,
    meta:{
        title:"数据入库"
    }
  },
  {
    path:"/issues/data/review",
    component:Review,
    meta:{
        title:"数据评测"
    }
  },
    

    { 
      path: '/users', 
      name: 'User',
      component: User,
      meta:{
        title:"用户管理"
    }
    },
    { 
      path: '/monitor', 
      name: 'Asset',
      component: Asset,
      meta:{
        title:"资产管理"
    }
    },
    { 
      path: '/system', 
      name: 'Setting',
      component: Setting,
      meta:{
        title:"系统设置"
    }
    },
  
  ]
  },
  { 
    path: '/login', 
    name: 'Login',
    component: Login,
    meta:{
      title:"登录页"
  }
  },
  
 { 
    path: '/:pathMatch(.*)*', 
    name: 'NotFound',
    component: NotFound 
  },
]

const router = createRouter({
  history:createWebHashHistory(),
  routes

})

export default router