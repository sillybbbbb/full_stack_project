<template>
    <div class="f-menu" :style="{ width:$store.state.asideWidth }">
        <el-menu :default-active="defaultActive" unique-opened :collapse="isCollapse"  class="border-0 mt-2" @select="handleSelect" :collapse-transition="false">

            <template v-for="(item,index) in asideMenus" :key="index">
                <el-sub-menu v-if="item.child && item.child.length > 0" :index="item.name">
                    <template #title>
                        <el-icon>
                            <component :is="item.icon"></component>
                        </el-icon>
                        <span>{{ item.name }}</span>
                    </template>
                    <el-menu-item v-for="(item2,index2) in item.child" :key="index2" :index="item2.frontpath">
                        <el-icon>
                            <component :is="item2.icon"></component>
                        </el-icon>
                        <span>{{ item2.name }}</span>
                    </el-menu-item>
                </el-sub-menu>

                <el-menu-item v-else :index="item.frontpath">
                    <el-icon>
                         <component :is="item.icon"></component>
                    </el-icon>
                    <span>{{ item.name }}</span>
                </el-menu-item>
            </template>
        </el-menu>
    </div>
</template>
<script setup>
import { computed,ref } from 'vue';
import { useRouter,useRoute ,onBeforeRouteUpdate} from 'vue-router';
import { useStore } from 'vuex';
const router = useRouter()
const store = useStore()
const route = useRoute()

// 默认选中
const defaultActive = ref(route.path)

onBeforeRouteUpdate((to, from) => {
  defaultActive.value = to.path
  
});

// 是否折叠
const isCollapse = computed(()=> !(store.state.asideWidth == '250px'))

//<el-icon><List /></el-icon>
// <el-icon><Tickets /></el-icon>
const asideMenus = [{
    "name": "后台面板",
    "icon": "help",
    "child": [{
        "name": "后台首页",
         "icon": "HomeFilled",
        "frontpath": "/",
    }]
}, {
    "name": "ISSUES管理",
    "icon": "Printer",
    "child": [
        
    {
        "name": "Issue 列表",
        "icon": "Tickets",
        "frontpath": "/issues/list",
    },
    {
        "name":"压测版本统计",
        "icon": "Collection",
        "frontpath": "/issues/stress",
    },
 
    {
        "name": "数据入库",
        "icon": "Notebook",
        "frontpath": "/issues/data",
    },
      
      {
        "name": "数据评测",
        "icon": "DataAnalysis",
        "frontpath": "/issues/data/review",
    },
 
    ]
},
{
    "name": "资产管理",
    "icon": "Monitor",
    "child": [{
        "name": "台架",
        "icon": "Platform",
        "frontpath": "/monitor",
    }]
},

{
    "name": "用户管理",
    "icon": "UserFilled",
    "child": [{
        "name": "人员",
        "icon": "User",
        "frontpath": "/users",
    }]
},{
    "name": "系统设置",
    "icon": "Setting",
    "child": [{
        "name": "系统设置",
         "icon": "Tools",
         "frontpath": "/system",
    }]
},
]


const handleSelect = (e)=>{
    router.push(e)
}
</script>
<style>
.f-menu {
    transition: all 0.2s;
    top: 64px;
    bottom: 0;
    left: 0;
    overflow-y: auto;
    overflow-x: hidden;
    @apply shadow-md fixed bg-light-50;
}
.f-menu::-webkit-scrollbar{
    width: 0px;
}
</style>