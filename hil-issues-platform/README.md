# Vue 3 + Vite

1. vite安装  https://cn.vitejs.dev/guide/#overview
2. vite构建项目 https://cn.vuejs.org/guide/scaling-up/tooling.html#project-scaffolding
      npm init vite@latest hil-issues-platform -- --template vue
3. 插件 volar  vue3 sni  windicss

4. element plus 引入 https://element-plus.gitee.io/zh-CN/component/button.html#%E5%9F%BA%E7%A1%80%E7%94%A8%E6%B3%95

 npm install element-plus --save
 5. windi css 引入  https://cn.windicss.org/
 npm i -D vite-plugin-windicss windicss

 6. vue Router   https://router.vuejs.org/zh/
 npm install vue-router@4

7. 设置src别名 
 import path from 'path'
export default defineConfig({
  resolve:{
    alias:{
      "~":path.resolve(__dirname,'src')
    }
  },
  plugins: [vue(),WindiCSS(),],
})

8. 图标安装
npm install @element-plus/icons-vue

9. axios安装
    npm install axios
10. 跨域解决 配置vite.config server
11. vueuse 使用 https://vueuse.org/
    cookie安装：
    npm i @vueuse/core
    npm i @vueuse/integrations
    npm i universal-cookie

11.  状态管理 vuex https://vuex.vuejs.org/zh/guide/
    npm install vuex@next --save
12. npm i nprogress  全局loading

13. npm install echarts
https://echarts.apache.org/zh/index.html