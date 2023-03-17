<template> 
        
        <el-date-picker
          v-model="value1"
          type="daterange"
          range-separator="To"
          start-placeholder="Start date"
          end-placeholder="End date"
          :size="size"
        />  
  </template>
  
  <script lang="ts" setup>
  import {ref, defineExpose } from 'vue'
  
  const size = ref<'default' | 'large' | 'small'>('default')
  
  const value1 = ref('')
  defineExpose({value1})
  </script>
  
  <style scoped>
  .demo-date-picker {
    display: flex;
    width: 100%;
    padding: 0;
    flex-wrap: wrap;
  }
  
  .demo-date-picker .block {
    padding: 30px 0;
    text-align: center;
    border-right: solid 1px var(--el-border-color);
    flex: 1;
  }
  
  .demo-date-picker .block:last-child {
    border-right: none;
  }
  
  .demo-date-picker .demonstration {
    display: block;
    color: var(--el-text-color-secondary);
    font-size: 14px;
    margin-bottom: 20px;
  }
  </style>
  