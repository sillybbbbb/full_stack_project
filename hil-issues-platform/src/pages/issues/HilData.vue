<template>
  <el-form :inline="true" :model="formInline" class="demo-form-inline">
    

    <el-form-item label="版本">
      <el-select v-model="formInline.user" placeholder="选择版本">
        <el-option label="master" value="master" />
        <el-option label="ad1.5.0-CN" value="ad1.5.0_CN" />
        <el-option label="ad1.5.0-EU" value="ad1.5.0_eu" />
        <el-option label="ad1.4.1-CN" value="ad1.4.1_CN" />
        <el-option label="ad1.4.1-eu" value="ad1.4.1_eu" />


      </el-select>
    </el-form-item>
    <el-form-item label="选择日期">
    <el-date-picker
        v-model="date"
        type="date"
        placeholder="Pick a day"
      />
    </el-form-item>
    <el-form-item label="task id">
      <el-input v-model="taskid" placeholder="输入task_id" />
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">入库</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive,ref } from 'vue';
import axios from 'axios';
const taskid = ref('')
const date = ref('')

const formInline = reactive({
  user: [],
  region: '',
})
var result = ref("")
const onSubmit = () => {
  console.log('submit!')
  
  axios.post('http://localhost:5000/api/insert',  {
    
          version: formInline.user,
         
          date:date.value,
          task_id : taskid.value
           }
  ) .then(response => {
  result = response.data;
  })
  .catch(error => { 
    console.error(error)
  })
  
}
</script>