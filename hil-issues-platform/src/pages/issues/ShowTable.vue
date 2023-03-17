<template>
  <a-table :columns="computedColumns" :data-source="msg.result"></a-table>
</template>

<script>
import { Table } from 'ant-design-vue';

export default {
  name: 'ShowTable',
  components: {
    'a-table': Table
  },
  props: {
    msg: {
      type: Array,     
    }
  },
  computed: {
    computedColumns() {
      if (!this.msg || !this.msg.col_name) {
        return [];
      }
      return this.msg.col_name.map(item => ({ title: item, dataIndex: item }));
    }
  }
}
</script>
