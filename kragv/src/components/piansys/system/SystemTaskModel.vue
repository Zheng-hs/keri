<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>系统设置</el-breadcrumb-item>
      <el-breadcrumb-item>任务类</el-breadcrumb-item>
      <el-breadcrumb-item>任务模板</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>

      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col :span="4">
          <el-button type="primary"
                     @click="goAddPage">添加模板</el-button>
        </el-col>
      </el-row>

      <!-- 列表 -->
      <el-table :data="modellist.fromtoModellist"
                border
                height="500">
        <el-table-column label="模板组名"
                         prop="groupName"></el-table-column>
        <el-table-column label="工作区"
                         prop="workArea"></el-table-column>
        <el-table-column label="默认AGV"
                         prop="agvDefault"></el-table-column>
        <el-table-column label="默认货物"
                         prop="payloadDefault"></el-table-column>
        <el-table-column label="业务注释"
                         prop="content"></el-table-column>
        <el-table-column label="更新日期"
                         prop="timestamp"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="200px"
                         fixed="right">
          <template slot-scope="scope">
            <el-button type="primary"
                       size="mini"
                       @click="turnToEditFromToModel(scope.row)">修改</el-button>
            <el-button type="danger"
                       size="mini"
                       @click="delFromToModel(scope.row.groupName)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="queryInfo.pagenum"
                     :page-sizes="[10, 20, 50, 100]"
                     :page-size="queryInfo.pagesize"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total"></el-pagination>
    </el-card>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // 获取列表的参数
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      },
      // 任务列表
      modellist: [],
      // 列表总数
      total: 0

      //

    }
  },
  created () {
    this.getSystemFromtoModelList()
  },
  mounted () {

  },
  beforeDestroy () {
  },
  methods: {
    // 获取AGV监视列表
    async getSystemFromtoModelList () {
      const { data: res } = await this.$http.get('system/fromtoModel', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('任务模板列表获取失败！')
      }
      this.modellist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getSystemFromtoModelList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getSystemFromtoModelList()
    },
    // 跳转到添加页面
    goAddPage () {
      this.$router.push('systemtaskmodel/add')
    },

    // 任务模板删除
    async delFromToModel (id) {
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将该任务模板删除, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消操作！')
      }

      const sendData = {}
      sendData.groupName = id
      const { data: res } = await this.$http.delete('system/fromtoModel/', { data: sendData })
      if (res.meta.status !== 200) {
        return this.$message.error('任务模板删除失败！')
      }

      this.$message.success('任务模板删除成功！')
      this.getSystemFromtoModelList()
    },

    // 跳转到修改页面
    turnToEditFromToModel (rowData) {
      this.$router.push({ name: 'editModel', path: '/systemtaskmodel/edit', params: { editData: rowData } })
    }

  }
}
</script>

<style lang="less" scoped></style>
