import router from "~/router"
import { 
  showFullLoading,
  hideFullLoading
} from "~/composables/util"

// 全局前置守卫
router.beforeEach(async (to,from,next)=>{
  console.log('全局前置守卫')
  // 显示loading
  showFullLoading()
  // console.log(to.meta.title)
  // // 设置页面标题
  let title = "HIL平台 -" + (to.meta.title ? to.meta.title : "") 
  document.title = title

  next()
})

// 全局后置守卫
router.afterEach((to, from) => hideFullLoading())