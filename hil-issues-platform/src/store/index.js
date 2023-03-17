import { createStore } from 'vuex'


const store = createStore({
  state() {
      return {
          // 侧边宽度
          asideWidth:"250px"
      }
  },
  mutations: {
      // 展开/缩起侧边
      handleAsideWidth(state){
          state.asideWidth = state.asideWidth == "250px" ? "64px" : "250px"
      }
  },
  actions:{
      
  }
})

export default store