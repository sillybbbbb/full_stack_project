
<template>
    <div>
       
        <el-row :gutter="20">
            <el-col :span="6" :offset="0">
                <IndexChart/>
            </el-col>
            <el-col :span="6" :offset="0">
                <IndexChart/>
            </el-col>
            <el-col :span="6" :offset="0">
                <IndexChart/>
            </el-col>
            <el-col :span="6" :offset="0">
                <IndexChart/>
            </el-col>
            
        </el-row>
        
   
    </div>
</template>

<script setup>

import IndexChart from "~/components/IndexChart.vue";


</script >
