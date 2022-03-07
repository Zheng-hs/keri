<template>
  <div>
    <el-card body-style="width:500px">
      <TaskList></TaskList>
    </el-card>
    <el-card body-style="width:500px">
      <Map></Map>
    </el-card>
  </div>
</template>

<script>
import TaskList from '../TaskList.vue'
import TestOrder from './TestOrder.vue'
import Map from '../Map.vue'

export default {

  components: { TaskList, Map },
  mounted () {
    this.prt()
    this.prt1()
  },
  data () {
    return {

    }
  },
  methods: {
    prt () {
      TestOrder.data.aaa = 123456
      console.log(TestOrder.methods.showFont())
    },
    prt1 () {
      console.log(TestOrder.data.aaa)
    }
  }

}
</script>

<style lang="less" scoped>
</style>