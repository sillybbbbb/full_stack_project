<template>
  <el-table :data="tableData"  height="500" style="width: 100%">

    <el-table-column prop="date" label="Date" width="100"  align="center" sortable />

     <el-table-column label="HIL压测版本报告信息 - 统计表 ( -- 正常触发 )"  align="center">
     
       
      <el-table-column label="maser" align="center">
        <el-table-column prop="Mnormal" label="normal" width="100" />
        <el-table-column prop="Mparking" label="parking" width="100" />
        <el-table-column prop="Mnop" label="nop" width="100" />
      </el-table-column>

      <el-table-column label="AD141_CN" align="center">
        <el-table-column prop="AD141CNnormal" label="normal" width="100" />
        <el-table-column prop="AD141CNparking" label="parking" width="100" />
        <el-table-column prop="AD141CNnop" label="nop"  width="100" />
      
      </el-table-column>
        <el-table-column label="AD141_EU" align="center">
        <el-table-column prop="AD141EUnormal" label="normal" width="100" />
        <el-table-column prop="AD141EUparking" label="parking" width="100" />
      </el-table-column>

   <el-table-column label="AD150_CN" align="center">
        <el-table-column prop="AD150CNnormal" label="normal" width="100" />
        <el-table-column prop="AD150CNparking" label="parking" width="100" />
        <el-table-column prop="AD150CNnop" label="nop" width="100" />
    </el-table-column>

     <el-table-column label="AD150_EU" align="center">
        <el-table-column prop="AD150EUnormal" label="normal" width="100" />
        <el-table-column prop="AD150EUparking" label="parking" width="100" />
   
    </el-table-column>


    </el-table-column>
        
        <el-table-column fixed="right" label="操作" width="80">
          <template #default>
            <el-button link type="primary" size="small" @click="dialogFormVisible = true" >编辑</el-button>

          </template>
        </el-table-column>



     
  </el-table>

     <el-dialog v-model="dialogFormVisible" title="版本报告信息统计">
        <el-form :model="form">

          <el-form-item label="日期" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off" />
          </el-form-item>

          <el-form-item label="master版本" :label-width="formLabelWidth">
            <div class="flex">
              normal :<el-input v-model="form.name" autocomplete="off" />
              parking: <el-input v-model="form.name" autocomplete="off" />
              nop: <el-input v-model="form.name" autocomplete="off" />
            </div>

            
          </el-form-item>


          <el-form-item label="AD141_CN" :label-width="formLabelWidth">

             <div class="flex  h-[35px]">
              normal :<el-input v-model="form.name" autocomplete="off" />
              parking: <el-input v-model="form.name" autocomplete="off" />
              nop: <el-input v-model="form.name" autocomplete="off" />
            </div>

          </el-form-item>

          <el-form-item label="AD141_EU" :label-width="formLabelWidth">
             <div class="flex  h-[35px]">
              normal :<el-input v-model="form.name" autocomplete="off" />
              parking: <el-input v-model="form.name" autocomplete="off" />
            </div>
            
          </el-form-item>
          <el-form-item label="AD150_CN" :label-width="formLabelWidth">
             <div class="flex  h-[35px] mr-10">
              normal :<el-input v-model="form.name" autocomplete="off" />
              parking: <el-input v-model="form.name" autocomplete="off" />
              nop: <el-input v-model="form.name" autocomplete="off" />
            </div>
          </el-form-item>

           <el-form-item label="AD150_EU" :label-width="formLabelWidth">
             <div class="flex  h-[35px]">
              normal :<el-input v-model="form.name" autocomplete="off" />
              parking: <el-input v-model="form.name" autocomplete="off" />
            
            </div>
          </el-form-item>
          
        </el-form>

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          确认
        </el-button>
      </span>
    </template>
  </el-dialog>

</template>

<script  setup>

import { reactive, ref } from 'vue'
const dialogTableVisible = ref(false)
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'

const form = reactive({
  name: '',
  region: '',
  date1: '',
  date2: '',
  delivery: false,
  type: [],
  resource: '',
  desc: '',
})

const tableData = [
  {
    date: '2023-03-14',
    Mnormal: '台架问题',
    Mparking: '台架问题',
    Mnop: 'oms_app发生coredump',

    AD141CNnormal:"--",
    AD141CNparking:"--",
    AD141CNnop:"未触发",

    AD141EUnormal:"--",
    AD141EUparking:"--",

    AD150CNnormal:"arg_app发生coredump",
    AD150CNparking:"--",
    AD150CNnop:"arg_app发生coredump",

    AD150EUnormal:"台架问题",
    AD150EUparking:"台架问题",
   
  },
 {
    date: '2023-03-13',
    Mnormal: '台架问题',
    Mparking: '台架问题',
    Mnop: 'oms_app发生coredump',

    AD141CNnormal:"--",
    AD141CNparking:"--",
    AD141CNnop:"未触发",

    AD141EUnormal:"--",
    AD141EUparking:"--",

    AD150CNnormal:"arg_app发生coredump",
    AD150CNparking:"--",
    AD150CNnop:"arg_app发生coredump",

    AD150EUnormal:"台架问题",
    AD150EUparking:"台架问题",
   
  },
 {
    date: '2023-03-12',
    Mnormal: '台架问题',
    Mparking: '台架问题',
    Mnop: 'oms_app发生coredump',

    AD141CNnormal:"--",
    AD141CNparking:"--",
    AD141CNnop:"未触发",

    AD141EUnormal:"--",
    AD141EUparking:"--",

    AD150CNnormal:"arg_app发生coredump",
    AD150CNparking:"--",
    AD150CNnop:"arg_app发生coredump",

    AD150EUnormal:"台架问题",
    AD150EUparking:"台架问题",
   
  },
  
]
</script>