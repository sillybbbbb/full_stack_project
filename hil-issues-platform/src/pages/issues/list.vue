<template>
  <h1>查询</h1>
     
  <el-form :inline="true" :model="formInline" class="demo-form-inline">
    <el-form-item label="版本" >
    <el-select
      v-model="version_value"
      multiple
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="2"
      placeholder="选择版本"
      style="width: 300px"
      size:large
    >
      <el-option
        v-for="item in versions"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
  </el-form-item>
<el-form-item label="场景">
    <el-select
      v-model="scene_value"
      multiple
      collapse-tags
      collapse-tags-tooltip
      :max-collapse-tags="3"
      placeholder="选择场景"
      size:large
    >
      <el-option
        v-for="item in scene"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />     
    </el-select>
   </el-form-item>
   <el-form-item label="日期">
  <dateSelector ref="dates"></dateSelector>
</el-form-item>
 </el-form>
 <el-form :inline="true" :model="formInline" class="demo-form-inline">
    <el-form-item label="选择查询指标" >
    <MetricSheet v-model="selectedmetric"  placeholder="选择查询指标..." ></MetricSheet>
    <a-button type="primary" @click = "query"> 
            <template #icon><SearchOutlined /></template>
            Search
        </a-button>
    </el-form-item>
    </el-form>
  <!-- </a-space> -->
  <ShowTable :msg= "result"> </ShowTable>
  </template>

  
<script>
import { defineComponent, ref } from 'vue';
import MetricSheet from './metricSheet.vue';
import axios from 'axios';
import ShowTable from './ShowTable.vue';
import dateSelector from './dateSelector.vue';
export default defineComponent({
    data() {
        return {
            classes: ["master", "ad1.5.0-cn", "ad1.4.1-cn", "ad1.5.0-eu", "ad1.4.1-eu"],
            selectedClass: "",
            // metrics: ["app", "network", "framerate", "cpu_mem", "power"],
            selectedmetric: "",
           
            result:[],
            selectedFeatures: [],
            tableData: [],
            columns: [],
            msg:""
        };
    },
    methods: {
        
        query() {
          axios.post('http://localhost:5000/api/query',  {
            
                  version: this.version_value,
                  scene:this.scene_value,
                  startDate:this.dates.value1[0],
                  endDate: this.dates.value1[1],
                  metrics:this.selectedmetric }
          ) .then(response => {
          this.result = response.data;
          })
          .catch(error => { 
            console.error(error)
          })
    }},
    setup() {

        const metrics = ref([]);
        // const selecteddate = ref([])

        const dates = ref([]);
        const versions = ref([
          {label:"master", value:"master_CN"},
          {label: "ad1.5.0-cn",value:"ad1.5.0_CN"},
          {label:"ad1.4.1-cn",value:"ad1.4.1_CN"},
          {label:"ad1.5.0-eu",value:"ad1.5.0_eu"},
          {label: "ad1.4.1-eu",value: "ad1.4.1_eu"} ]);
        const scene = ref([
          {label:"normal", value:"normal"},
          {label: "parking",value:"parking"},
          {label:"nop",value:"nop"}
          ]);

        const maxTagCount = ref(6);
        const maxTagTextLength = ref(10);
      
    
        return {
           
            version_value:ref(['ad1.5.0_CN']),
            scene_value:ref(['normal','nop']),
            versions,
            scene,
            metrics,
            dates,
            maxTagCount,
            maxTagTextLength,
        };
    },
    components: { MetricSheet,ShowTable,dateSelector }
});
</script>