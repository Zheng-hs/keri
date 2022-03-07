<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     @click="goAddPage">新增</el-button>
        </el-col>
        <el-col class="btnrow2">
          <span>任务模板名:</span>
          <el-input class="searchInput"
                    clearable
                    placeholder="请输入任务模板名"
                    prefix-icon="el-icon-search"
                    @input="searchInputChange"
                    v-model="modelNameSearch"> </el-input>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="taskModelData.taskModelList"
                border
                highlight-current-row
                :height="tableHeight">
        <el-table-column label="任务模板名"
                         width="260px"
                         prop="taskModelName"></el-table-column>
        <el-table-column label="点位">
          <template slot-scope="scope">
            {{scope.row.markList ? scope.row.markList.join(' , '):scope.row.markList}}
          </template>
        </el-table-column>
        <el-table-column label="备注"
                         prop="remark"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="230px"
                         fixed="right">
          <template slot-scope="scope">
            <el-button type="primary"
                       size="mini"
                       @click="showBindBoxNumDialog(scope.row)">派发</el-button>
            <el-button type="primary"
                       size="mini"
                       @click="turnToEditTaskModel(scope.row)">修改</el-button>
            <el-button type="danger"
                       size="mini"
                       @click="delTaskModel(scope.row)">删除</el-button>
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

    <!-- 任务派发的对话框 -->
    <el-dialog title="箱号绑定"
               :visible.sync="bindBoxNumDialogVisible"
               width="630px">
      <!-- content -->
      <el-table :data="nodeList"
                border
                stripe
                height="450px">
        <el-table-column label="编号"
                         prop="id"></el-table-column>
        <el-table-column label="点位"
                         prop="From"></el-table-column>
        <el-table-column label="动作"
                         prop="action">
          <template slot-scope="scope">
            <template v-if="scope.row.action == 'Get'">上料</template>
            <template v-else-if="scope.row.action == 'Put'">下料</template>
            <template v-else>无</template>
          </template>
        </el-table-column>
        <el-table-column label="方向"
                         prop="direction">
          <template slot-scope="scope">
            <template v-if="scope.row.direction == 'R'">右</template>
            <template v-else-if="scope.row.direction == 'L'">左</template>
          </template>
        </el-table-column>
        <el-table-column label="货架层数"
                         prop="shelf_num"></el-table-column>
        <el-table-column label="Fork层数"
                         prop="fork_num"></el-table-column>

        <el-table-column label="箱号"
                         prop="boxNum"
                         width="100px">
          <template slot-scope="scope">
            <template v-if="scope.row.actionOrNot">
              <el-input size="mini"
                        v-model="scope.row.boxNum"></el-input>
            </template>
            <template v-else>
              <el-input size="mini"
                        :disabled="true"
                        v-model="scope.row.boxNum"></el-input>
            </template>

          </template>

        </el-table-column>

      </el-table>
      <!-- content -->

      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="bindBoxNumDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="dispatchMission">派 发</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  data () {
    return {
      nodeList: [],
      // 控制bindBoxNum对话框的显示与隐藏
      bindBoxNumDialogVisible: false,
      // 凑数
      addTaskModelForm: {},
      // 派发表单
      submitForm: {},
      // 获取列表的参数
      queryInfo: {
        query: {},
        pagenum: 1,
        pagesize: 10
      },
      taskModelData: {},
      // 列表总数
      total: 0,
      modelNameSearch: '',
      // 计时器
      timer: null,

      // 表格高度
      tableHeight: window.innerHeight * 0.7,
    }
  },
  created () {
  },
  mounted () {
    this.getTaskModel()
  },
  beforeDestroy () {
  },
  methods: {
    // 获取任务状态列表
    async getTaskModel () {
      const { data: res } = await this.$http.get('taskModel', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          showClose: true,
          message: res.meta.msg,
          type: 'error'
        })
      }
      this.taskModelData = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getTaskModel()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getTaskModel()
    },
    // 检测搜索栏
    searchInputChange () {
      if (this.modelNameSearch !== '') {
        this.queryInfo.query.taskModelName = this.modelNameSearch
      } else {
        this.queryInfo.query = {}
      }
      this.getTaskModel()
    },
    // 判断是否admin page
    isAdminPage () {
      let path = window.location.href
      if (path.indexOf('admin') != -1) {
        return true
      } else {
        return false
      }
    },
    // 跳转到添加页面
    goAddPage () {
      this.$router.push('taskmodeladd')
    },

    // 跳转到编辑页面
    turnToEditTaskModel (rowData) {
      let isAdmin = this.isAdminPage()
      if (isAdmin) {
        this.$router.push({ name: 'adminTaskModelEdit', path: 'taskmodeledit', params: { rowData: rowData } })
      } else {
        this.$router.push({ name: 'taskModelEdit', path: 'taskmodeledit', params: { rowData: rowData } })
      }

    },
    // 删除模板
    async delTaskModel (rowData) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该模板, 是否继续?', '提示', {
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

      const { data: res } = await this.$http.delete('taskModel', { params: { id: rowData.id } })
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
      this.getTaskModel()
    },
    // nodeList解码
    nodeListDecode (taskData) {
      let actionList = taskData.actionList
      if (!actionList) return
      let markList = taskData.markList
      this.addTaskModelForm.taskModelName = taskData.taskModelName
      this.addTaskModelForm.remark = taskData.remark

      actionList.forEach((act, index) => {
        if (act == '') {
          let nodeRow = {}
          nodeRow.From = markList[index]
          nodeRow.action = ''
          nodeRow.direction = ''
          nodeRow.shelf_num = ''
          nodeRow.fork_num = ''
          nodeRow.Transfer_Obj_ID = ''
          nodeRow.actionOrNot = false
          nodeRow.boxNum = ''
          nodeRow.waitOrNot = ''
          this.nodeList.push(nodeRow)
          return
        }

        let waitOrNot = act.substring(act.indexOf('(') - 1, act.indexOf('('))
        let actNum = Number(act.substring(0, act.indexOf('(') - 1))
        let actList = act.substring(act.indexOf('(') + 1, act.indexOf(')')).split(',')
        for (let i = 0; i < actNum; i++) {
          let nodeRow = {}
          nodeRow.From = markList[index]
          let action = ''
          let direction = actList[i].substring(2, 3)
          let shelf_num = actList[i].substring(3, 4)
          let fork_num = actList[i].substring(4, 5)
          let Transfer_Obj_ID = ''
          if (actList[i].substring(1, 2) == 'G') {
            action = 'Get'
          } else if (actList[i].substring(1, 2) == 'P') {
            action = 'Put'
          }
          if (actList[i].substring(5, 6) == 'E') {
            Transfer_Obj_ID = 'Express'
          } else if (actList[i].substring(5, 6) == 'R') {
            Transfer_Obj_ID = 'Rack'
          }

          nodeRow.waitOrNot = waitOrNot
          nodeRow.action = action
          nodeRow.direction = direction
          nodeRow.shelf_num = shelf_num
          nodeRow.fork_num = fork_num
          nodeRow.Transfer_Obj_ID = Transfer_Obj_ID
          nodeRow.actionOrNot = true
          nodeRow.boxNum = ''
          this.nodeList.push(nodeRow)
        }
      })

      this.nodeList.forEach((node, index) => {
        node.id = index
      })
    },
    // 报文格式编码
    submitMsgEncode () {
      this.submitForm = {
        dispatchId: '',
        taskModelName: '',
        actionList: [],
        markList: [],
        remark: ''
      }

      this.submitForm.dispatchId = (new Date()).getTime()

      this.nodeList.forEach(node => {
        let nodeWait = node.waitOrNot
        let nodeAct = node.action.substring(0, 1)
        let nodeDirection = node.direction
        let nodeShelf_num = node.shelf_num
        let nodeFork_num = node.fork_num
        let nodeShelfCate = node.Transfer_Obj_ID.substring(0, 1)
        let nodeBoxNum = node.boxNum == '' ? '999999' : node.boxNum
        let actCommand = '_' + nodeAct + nodeDirection + nodeShelf_num + nodeFork_num + nodeShelfCate + '_000000_' + nodeBoxNum
        let markListLen = this.submitForm.markList.length
        if (markListLen == 0) {
          this.submitForm.markList.push(node.From)
          let actCommandRes = ''
          if (node.actionOrNot) {
            actCommandRes = '1' + nodeWait + '(' + actCommand + ')'
          }
          this.submitForm.actionList.push(actCommandRes)
        } else {
          let lastPoint = this.submitForm.markList[markListLen - 1]
          if (node.From == lastPoint) {
            // 后空
            if (!node.actionOrNot) return
            let lastActCommand = this.submitForm.actionList[markListLen - 1]
            // 前空
            if (lastActCommand.trim() == '') {
              let actCommandRes = '1' + nodeWait + '(' + actCommand + ')'
              this.submitForm.actionList[markListLen - 1] = actCommandRes
            } else {
              let lastWait = lastActCommand.substring(lastActCommand.indexOf('(') - 1, lastActCommand.indexOf('('))
              if (nodeWait == 'W') {
                lastWait = 'W'
              }
              let lastActNum = Number(lastActCommand.substring(0, lastActCommand.indexOf('(') - 1))
              let lastAct = lastActCommand.substring(lastActCommand.indexOf('(') + 1, lastActCommand.indexOf(')'))
              let actCommandRes = (lastActNum + 1) + lastWait + '(' + lastAct + ',' + actCommand + ')'
              this.submitForm.actionList[markListLen - 1] = actCommandRes
            }

          } else {
            this.submitForm.markList.push(node.From)
            let actCommandRes = ''
            if (node.actionOrNot) {
              actCommandRes = '1' + nodeWait + '(' + actCommand + ')'
            }
            this.submitForm.actionList.push(actCommandRes)
          }

        }
      })
    },
    // 箱号绑定框打开
    showBindBoxNumDialog (rowData) {
      if (rowData.actionList.length === 0) {
        // return this.$message.error('任务列表不能为空')
        return this.$message({
          showClose: true,
          message: '任务列表不能为空',
          type: 'error'
        })

      }
      this.nodeList = []
      this.submitForm = {}
      this.nodeListDecode(rowData)
      this.bindBoxNumDialogVisible = true
    },
    // 任务派发
    async dispatchMission (taskModel) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将派发该任务, 是否继续?', '提示', {
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

      if (this.nodeList.length === 0) {
        // return this.$message.error('任务列表不能为空')
        return this.$message({
          showClose: true,
          message: '任务列表不能为空',
          type: 'error'
        })
      }

      this.submitMsgEncode()
      const { data: res } = await this.$http.post('/dispatchMission', this.submitForm)
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
      this.bindBoxNumDialogVisible = false
      this.getTaskModel()

    },
    // 
    // 
  },


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
