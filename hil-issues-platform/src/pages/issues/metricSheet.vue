<template>
    <div>
 
     
      <el-select v-model="selectedForm" @change="onFormChange" placeholder="请选择表单" >
        <el-option value="app_proc" >app_proc</el-option>
        <el-option value="cpu_mem">cpu_mem</el-option>
        <el-option value="network">network</el-option>
        <el-option value="perception_framerate">perception_framerate</el-option>
        <el-option value="power">power</el-option>
      </el-select>

 
 
      <el-select v-if="selectedForm === 'app_proc'" v-model="app0" @change="onMetricChange0"  placeholder="SOC">
        <el-option value="1" label="s1"></el-option>
        <el-option value="2" label="s2"></el-option>
        <el-option value="3" label="s3"></el-option>
        <el-option value="4" label="s4"></el-option>
        </el-select>

        <el-select v-if="selectedForm === 'app_proc'" v-model="app1" @change="onMetricChange1"  placeholder="app_name">
          <el-option v-for="option in app_names" :lable = "option" :value="option" :key="option"/>
        </el-select>

        <el-select v-if="selectedForm === 'app_proc'" v-model="app2" @change="onMetricChange2"  placeholder="cpu/mem">
        <el-option value="cpu" label="cpu"></el-option>
        <el-option value="mem" label="mem"></el-option>
       
        </el-select>


              
   
      <!-- <el-form-item v-if="selectedForm === 'cpu_mem'" > -->
        <el-select v-if="selectedForm === 'cpu_mem'" v-model="cpu0" @change="onMetricChange0" placeholder="SOC" >
          <el-option label="s1" value="1"></el-option>
          <el-option label="s2" value="2"></el-option>
          <el-option label="s3" value="3"></el-option>
          <el-option label="s4" value="4"></el-option>
        </el-select>
      <!-- </el-form-item> -->

      <!-- <el-form-item v-if="selectedForm === 'cpu_mem'" > -->
        <el-select v-if="selectedForm === 'cpu_mem'" v-model="cpu1" @change="onMetricChange1" placeholder="category" >
          <el-option value="cpu">cpu</el-option>
          <el-option value="gpu">gpu</el-option>
          <el-option value="ram">ram</el-option>
        </el-select>
      <!-- </el-form-item> -->


          
        
      <el-select v-if="selectedForm === 'network'"  v-model="net0" @change="onMetricChange0" placeholder="SOC">
        <el-option label="s1" value="1"></el-option>
        <el-option label="s2" value="2"></el-option>
        <el-option label="s3" value="3"></el-option>
        <el-option label="s4" value="4"></el-option>
      </el-select>
  
    
      <el-select v-if="selectedForm === 'network'"  v-model="net1" @change="onMetricChange1" placeholder="指标" >
        <el-option label="can0" value="can0"></el-option>
        <el-option label="can1" value="can1"></el-option>
        <el-option label="eth0" value="eth0"></el-option>
        <el-option label="eth1" value="eth1"></el-option>
        <el-option label="eth1.10" value="eth1.10"></el-option>
        <el-option label="eth1.20" value="eth1.20"></el-option>
        <el-option label="eth1.30" value="eth1.30"></el-option>
        <el-option label="eth1.40" value="eth1.40"></el-option>
        <el-option label="eth1.50" value="eth1.50"></el-option>
        <el-option label="lo" value="lo"></el-option>
      </el-select>


        <el-select v-if="selectedForm === 'perception_framerate'" v-model="pf0" @change="onMetricChange0"  placeholder="指标" style="width: 400px">
         <el-option v-for="option in fp_options" :lable = "option" :value="option" :key="option"/>
        </el-select>
        <el-select v-if="selectedForm === 'power'"  v-model="power0" @change="onMetricChange0" placeholder="SOC">
        <el-option label="s1" value="1"></el-option>
        <el-option label="s2" value="2"></el-option>
        <el-option label="s3" value="3"></el-option>
        <el-option label="s4" value="4"></el-option>
      </el-select>
    </div>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';

  export default defineComponent({
    data() {
      return {
            selectedForm: '',
            fp_options :['common_perception_perception_objects_prod','common_perception_vision_road_detection','common_perception_vision_feature_flag_prod','common_perception_vision_perception_objects_prod','common_perception_od_output_adb','common_perception_od_output_adp','common_perception_od_output_prod','common_perception_od_output_lidar_prod','common_perception_svc_perception_prod','common_perception_svc_nn_output','coapp_common_perception_perception_objects','coapp_common_perception_vision_road_detection','coapp_common_perception_od_output'],
        // selectedMetric:[0,0,0,0,0],
            app_names :[
            "adhmi","arb_app","arg_app","can_app","coapp_proxy_tx","control","ehy_app","fcts_app","fota-server","gnss_imu_servic","hw_manager","launcher","param_server","planner","position_app","radar_app","rel_loc_app","someip_endpoint","sysmon_app","trace_control_a","worldmodel","cdm_app","coapp_proxy_rx","dds_record","desensitization","lidar_dlb","lidar_recorder","map_loc_app","cdm_eco_app","diagnose_app","dlb_app","dms_app","lidar_ctrl","lidar_fltmgr","parking_env_app","parking_plannin","parking_process","coapp_mgr","co_arg_app"
            ]
      }
    },
    
   
  
    methods: {
        onFormChange(value){
            this.selectedForm = value;
            this.selectedMetric[0] = value;
        },
        onMetricChange0(value) {
        this.selectedMetric[1] = value;
        this.$emit('update:modelValue', this.selectedMetric)
      },
      onMetricChange1(value) {
        this.selectedMetric[2] = value;
        this.$emit('update:modelValue', this.selectedMetric);
      },
        onMetricChange2(value) {
        this.selectedMetric[3] = value;
        this.$emit('update:modelValue', this.selectedMetric)
      },
      onMetricChange3(value) {
        this.selectedMetric[4] = value;
        this.$emit('update:modelValue', this.selectedMetric)

      }
    },
    emits: ['update:modelValue'],

    setup(){
    var selectedMetric =  ref([0,0,0,0,0]);
    const net0 = ref('');
    const net1 = ref('');
    const pf0 = ref('');
    const cpu0 = ref('');
    const cpu1 = ref('');
    const power0 = ref('');
    const power1 = ref('');
    const app0=ref('');
    const app1 = ref('');
    const app2 = ref('')
     // const emit = defineEmits(['change'])
    //  const clickChild=()=>{
      
    //    //传递给父组件
    //    context.emit('sonHandler',selectedMetric)}
 
       
    //  const onFormChange = (value)=> {
    //     // 处理表单选择器选项的变化
    //     this.selectedForm = value;
    //     selectedMetric.value[0] = value; 
    //     context.emit('sonHandler',selectedMetric)
        
    //   };
    //   const onMetricChange0 = (value)=> {
    //     selectedMetric.value[1] = value;
    //     context.emit('sonHandler',selectedMetric)

    //   };
    //   const onMetricChange1 = (value)=> {
    //     selectedMetric.value[2] = value;
    //     context.emit('sonHandler',selectedMetric)

    //   };

      return {
        selectedMetric,
        net0,
        net1,
        power0,
        power1,
        app0,
        app1,
        app2,
        pf0,
        cpu0,
        cpu1
       };
     
    },
  })
  </script>
  