<template>
  <el-form :inline="true" :model="formInline" class="demo-form-inline">
    <el-form-item label="版">
      <el-select v-model="formInline.user" placeholder="选择版本">
        <el-option label="master" value="master" />
        <el-option label="ad150_CN" value="ad150_CN" />
        <el-option label="ad150_EU" value="ad150_EU" />
        <el-option label="ad141_CN" value="ad141_CN" />
        <el-option label="ad141_EU" value="ad141_EU" />
      </el-select>
    </el-form-item>

    <el-form-item label="场景">
      <el-select v-model="formInline.user" placeholder="选择场景">
        <el-option label="normal" value="normal" />
        <el-option label="parking" value="parking" />
        <el-option label="nop" value="nop" />
      </el-select>
    </el-form-item>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">Query</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

const formInline = reactive({
  user: '',
  region: '',
})

const onSubmit = () => {
  console.log('submit!')
}
</script>