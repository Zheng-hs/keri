<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 任务列表 -->
      <el-table :data="groupList" border highlight-current-row stripe :height="tableHeight">
        <el-table-column label="" type="index"></el-table-column>
        <el-table-column label="组名称" prop="groupName"></el-table-column>
        <el-table-column label="组内车辆" prop="agvList">
          <template slot-scope="scope">
            {{ scope.row.agvList.toString() }}
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      groupList: [],
      tableHeight: window.innerHeight * 0.7
    }
  },
  methods: {
    async getGroupList() {
      const { data: res } = await this.$http.get('/getGroup')
      if (res.meta.status == 200) {
        this.groupList = res.data.groupList
      }
    }
  },
  created() {
    this.getGroupList()
  }
}
</script>

<style lang="less" scoped>

</style>
