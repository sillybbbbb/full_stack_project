<template>
    <el-card shadow="never">
        <template #header>
            <div class="flex justify-between">
                <span class="text-sm">issues 统计</span>
                <div>
                    <el-check-tag v-for="(item, index) in options" :key="index" :checked="current == item.value"
                        style="margin-right: 8px" @click="handleChoose(item.value)">{{ item.text }}</el-check-tag>
                </div>
            </div>
        </template>
        <div ref="el" id="chart" style="width: 100%;height: 300px;"></div>
    </el-card>
</template>
<script setup>
import { ref, onMounted,onBeforeUnmount } from 'vue';
import * as echarts from 'echarts';
import { useResizeObserver } from '@vueuse/core'

import {
    getStatistics1
} from "~/api/index.js"


const current = ref("week")
const options = [
    {
    text:  "3个月",
    value: "quarter"
},{
    text: "近1个月",
    value: "month"
}, {
    text: "近1周",
    value: "week"
}]

const handleChoose = (type) => {
    current.value = type
    // getData()
}


var myChart = null
onMounted(() => {
    var chartDom = document.getElementById('chart');
    myChart = echarts.init(chartDom);

    getData()
})

onBeforeUnmount(()=>{
    if(myChart) echarts.dispose(myChart)
})

let option = null
function getData(){
getStatistics1().then((res) => {
    

      myChart.setOption(
    (option = {
      title: {
        text: 'Beijing AQI',
        left: '1%'
      },
      tooltip: {
        trigger: 'axis'
      },
      grid: {
        left: '5%',
        right: '15%',
        bottom: '10%'
      },
      xAxis: {
        data: res.data.map(function (item) {
          return item[0];
        })
      },
      yAxis: {},
      toolbox: {
        right: 10,
        feature: {
          dataZoom: {
            yAxisIndex: 'none'
          },
          restore: {},
          saveAsImage: {}
        }
      },
      dataZoom: [
        {
          startValue: '2014-06-01'
        },
        {
          type: 'inside'
        }
      ],
      visualMap: {
        top: 50,
        right: 10,
        pieces: [ 
          {
            gt: 200,
            lte: 300,
            color: '#AA069F'
          },
          {
            gt: 300,
            color: '#AC3B2A'
          }
        ],
        outOfRange: {
          color: '#999'
        }
      },
      series: {
        name: 'Beijing AQI',
        type: 'line',
        data: res.data.map(function (item) {
          return item[1];
        }),
        markLine: {
          silent: true,
          lineStyle: {
            color: '#333'
          },
          data: [
            {
              yAxis: 300
            }
          ]
        }
      }
    })
  );
    
});
  option && myChart.setOption(option);

}


const el = ref(null)
useResizeObserver(el, (entries) => myChart.resize())

</script>




