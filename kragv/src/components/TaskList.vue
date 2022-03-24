<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <span>任务类型:</span>
          <el-select v-model="taskType"
                     placeholder="请选择"
                     @change="taskTypeChange">
            <el-option v-for="item in taskTypeOptions"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>
        </el-col>
        <el-col class="btnrow2">
          <span>任务单号:</span>
          <el-input class="searchInput"
                    clearable
                    placeholder="请输入任务单号"
                    prefix-icon="el-icon-search"
                    @input="searchInputChange"
                    v-model="taskIdSearch"> </el-input>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="taskData.taskList"
                border
                highlight-current-row
                :height="tableHeight">
        <el-table-column label="任务单号"
                         prop="taskId"></el-table-column>
        <el-table-column label="任务类型"
                         width="120px"
                         prop="taskType"></el-table-column>
        <el-table-column label="任务状态"
                         width="120px"
                         prop="taskStatus"></el-table-column>
        <el-table-column label="车号"
                         width="120px"
                         prop="agvId"></el-table-column>
        <el-table-column label="区域"
                         width="120px"
                         prop="area"></el-table-column>
        <el-table-column label="站点清单">
          <template slot-scope="scope">
            {{ scope.row.markList ? scope.row.markList.join(' , ') : scope.row.markList }}
          </template>
        </el-table-column>
        <el-table-column label="动作清单">
          <template slot-scope="scope">
            {{ scope.row.actionList ? scope.row.actionList.join(' , ') : scope.row.actionList }}
          </template>
        </el-table-column>
        <el-table-column label="站点时间">
          <template slot-scope="scope">
            {{ scope.row.markTime ? scope.row.markTime.join(' ，') : scope.row.markTime }}
          </template>
        </el-table-column>
        <el-table-column label="挂单时间"
                         prop="startTime"></el-table-column>
        <el-table-column label="派发时间"
                         prop="taskBeginTime"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="100px">
          <template slot-scope="scope">
            <el-button type="danger"
                       size="mini"
                       @click="delTask(scope.row.dispatchId)">删除</el-button>
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
        query: {},
        pagenum: 1,
        pagesize: 10
      },
      taskData: {},
      // 列表总数
      total: 0,
      // RT任务 / 历史任务
      taskType: 'realtime',
      taskTypeOptions: [
        {
          value: 'realtime',
          label: '实时任务'
        },
        {
          value: 'normal',
          label: '已完成任务'
        }
      ],
      taskIdSearch: '',
      // 计时器
      timer: [],

      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      // 清除timer延时器
      lastBrowseTimeouter: null,
      sendDataSwitch: true
    }
  },
  created () {

  },
  mounted () {
    // this.getTaskListRT()
    // this.checkDocVis()
    this.taskTypeChange()
  },
  beforeDestroy () {
    this.cleanTimer()
  },
  methods: {
    // 检测 document visible
    checkDocVis () {
      document.onvisibilitychange = () => {
        // let browseInterval = 1000 * 60 * 30
        let browseInterval = 1000 * 60 * 15

        if (document.visibilityState == 'visible') {
          if (this.lastBrowseTimeouter != null) {
            clearTimeout(this.lastBrowseTimeouter)
            this.lastBrowseTimeouter = null
          }
          if (!this.sendDataSwitch) {
            // window.location.reload()
            this.getTaskListRT()
            this.sendDataSwitch = true
          }
        } else {
          this.lastBrowseTimeouter = setTimeout(() => {
            this.cleanTimer()
            this.sendDataSwitch = false
          }, browseInterval);
        }

      }
    },
    getTaskListRT () {
      this.getMissionList()
      // 定时向服务器发起请求
      this.timer.push(setInterval(this.getMissionList, 10000))
    },
    // 清除timer
    cleanTimer () {
      for (let i = 0; i < this.timer.length; i++) {
        clearInterval(this.timer.pop())
      }
    },
    taskTypeChange () {
      if (this.taskType == 'normal') {
        this.cleanTimer()
        this.getAllMissionList()
      } else {
        this.getTaskListRT()
        this.checkDocVis()
      }
    },
    // 获取任务状态列表
    async getAllMissionList () {
      const { data: res } = await this.$http.get('getAllMissionList', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return console.log(res.meta.msg)
      }
      this.taskData = res.data
      this.total = res.data.total
    },
    // 获取任务状态列表
    async getMissionList () {
      const { data: res } = await this.$http.get('getMissionList', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return console.log(res.meta.msg)
      }
      this.taskData = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      if (this.taskType == 'realtime') {
        this.getMissionList()
      } else {
        this.getAllMissionList()
      }

    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      if (this.taskType == 'realtime') {
        this.getMissionList()
      } else {
        this.getAllMissionList()
      }
    },
    // 检测搜索栏
    searchInputChange () {
      if (this.taskIdSearch.trim() !== '') {
        this.queryInfo.query.taskId = this.taskIdSearch
      } else {
        this.queryInfo.query = {}
      }
      this.getMissionList()
    },
    // 删除任务
    async delTask (dispatchId) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该任务, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        // return this.$message.info('已取消操作！')
        return this.$message({
          showClose: true,
          message: '已取消操作！',
          type: 'info'
        })
      }

      const { data: res } = await this.$http.delete('/cancel/mission/' + dispatchId)
      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          showClose: true,
          message: res.meta.msg,
          type: 'error'
        })
      }
      // this.$message.success(res.meta.msg)
      this.$message({
        showClose: true,
        message: res.meta.msg,
        type: 'success'
      })
      this.getMissionList()
    },
  }

  //
  //
}
</script>

<style lang="less" scoped>
.searchInput {
  width: 200px;
}

.addDialogSelect,
.chargeDialogSelect {
  width: 100%;
}

.mobileClass {
  .el-card {
    box-shadow: 0, 1px, 1px, rgba(0, 0, 0.15) !important;
    margin-top: 5px;
  }

  .el-table {
    margin-top: 5px;
    // font-size: 12px;
  }

  .btnrow {
    display: flex;
    align-items: center;
    // justify-content: space-between;
    flex-direction: column-reverse;
    padding-left: 0;
    padding-right: 0;
  }

  .btnrow1 {
    padding-top: 10px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }

  .btnrow1 > span {
    word-break: keep-all;
    padding-right: 20px;
  }

  .btnrow2 {
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }

  .btnrow2 > span {
    word-break: keep-all;
    padding-right: 20px;
  }
}
</style>
