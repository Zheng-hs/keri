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
            {{missionDataSplit(scope.row.missionData,'pointId')}}
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
      <!-- 流水线操作 -->
      <el-form ref="waterLineFormRef"
               :model="waterLineForm"
               :rules="waterLineFormRules"
               label-width="100px">
        <el-form-item label="有无流水线"
                      prop="actionOrNot">
          <el-switch v-model="waterLineForm.waterLineOrNot"
                     active-color="#13ce66"
                     inactive-color="#ff4949"
                     @change="handleWaterLineOrNot(waterLineForm.waterLineOrNot)">
          </el-switch>
        </el-form-item>
        <template v-if="waterLineForm.waterLineOrNot">
          <el-form-item label="上料/下料"
                        prop="inOrOut">
            <el-select v-model="waterLineForm.inOrOut"
                       placeholder="请选择"
                       clearable>
              <el-option label="上料"
                         value="G"></el-option>
              <el-option label="下料"
                         value="P"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="流水线点位"
                        prop="point">
            <el-input v-model="waterLineForm.point"></el-input>
          </el-form-item>

          <el-form-item label="友情提示">
            1_(_GR21E_000000_000000)
          </el-form-item>
          <el-form-item label="流水线动作"
                        prop="action">
            <el-input type="textarea"
                      v-model="waterLineForm.action"></el-input>
          </el-form-item>
        </template>

      </el-form>
      <!-- 流水线操作 -->

      <!-- 箱号绑定 -->
      <el-table :data="nodeList"
                border
                stripe
                height="350px">
        <el-table-column label="编号"
                         prop="id"></el-table-column>
        <el-table-column label="点位"
                         prop="From"></el-table-column>
        <el-table-column label="动作"
                         prop="action">
          <template slot-scope="scope">
            <template v-if="scope.row.action == 'G'">上料</template>
            <template v-else-if="scope.row.action == 'P'">下料</template>
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
      <!-- 箱号绑定 -->

      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="bindBoxNumDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="dispatchMission">派 发</el-button>
      </span>
    </el-dialog>
    <!-- 任务派发的对话框 -->

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

      // 流水线表单
      waterLineForm: {
        waterLineOrNot: false,
        inOrOut: '',
        point: '',
        action: ''
      },
      // 流水线表单的验证规则对象
      waterLineFormRules: {
      },
      waterLineFormRulesSource: {
        inOrOut: [{ required: true, message: '请选择上料/下料', trigger: 'blur' }],
        point: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
      },

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
      const { data: res } = await this.$http.get('taskModelPlus', { params: this.queryInfo })
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
    handleWaterLineOrNot (waterLineOrNot) {
      if (waterLineOrNot) {
        this.waterLineFormRules = this.waterLineFormRulesSource
      } else {
        this.waterLineFormRules = {}
        // this.waterLineForm = {
        //   waterLineOrNot: false,
        //   inOrOut: '',
        //   point: '',
        //   action: ''
        // }
      }
    },
    // 任务列表参数拆解
    missionDataSplit (missionData, needParam) {
      try {
        let tempArr = []
        missionData.forEach(item => {
          tempArr.push(item[needParam])
        });
        return tempArr.join('，')
      } catch (error) {
        return ''
      }
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
      this.$router.push('taskmodeladdplus')
    },

    // 跳转到编辑页面
    turnToEditTaskModel (rowData) {
      let isAdmin = this.isAdminPage()
      if (isAdmin) {
        this.$router.push({ name: 'adminTaskModelEdit', path: 'taskmodeledit', params: { rowData: rowData } })
      } else {
        this.$router.push({ name: 'taskModelEditPlus', path: 'taskmodeleditplus', params: { rowData: rowData } })
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
      const { data: res } = await this.$http.delete('taskModelPlus', { params: { id: rowData.taskModelId } })
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
      let actionList = taskData.missionData
      if (!actionList) return
      this.addTaskModelForm.taskModelName = taskData.taskModelName
      this.addTaskModelForm.remark = taskData.remark

      if (taskData.inPoint || taskData.outPoint) {
        this.waterLineForm.waterLineOrNot = true
        if (taskData.inPoint) {
          this.waterLineForm.inOrOut = "G"
          this.waterLineForm.point = taskData.inPoint
          this.waterLineForm.action = taskData.inAction
        } else {
          this.waterLineForm.inOrOut = "P"
          this.waterLineForm.point = taskData.outPoint
          this.waterLineForm.action = taskData.outAction
        }
      }

      actionList.forEach((act, index) => {
        let nodeRow = {}
        if (act == '') {
          nodeRow.boxNum = ''
          nodeRow.From = ''
          nodeRow.direction = ''
          nodeRow.action = ''
          nodeRow.shelf_num = ''
          nodeRow.actionOrNot = false
          this.nodeList.push(nodeRow)
          return
        }

        nodeRow.boxNum = act.itemNum
        nodeRow.From = act.pointId
        nodeRow.direction = act.lr
        nodeRow.action = act.gp
        nodeRow.shelf_num = act.floorNum
        if (act.gp) {
          nodeRow.actionOrNot = true
        } else {
          nodeRow.actionOrNot = false
        }
        this.nodeList.push(nodeRow)

      })

      this.nodeList.forEach((node, index) => {
        node.id = index
      })
    },
    // 报文格式编码
    submitMsgEncode () {
      let subInfo = {}
      subInfo.dispatchId = (new Date()).getTime() + Math.ceil(Math.random() * 1000000)
      let missionData = []
      this.nodeList.forEach(node => {
        let temp = {}
        temp.itemNum = node.boxNum
        temp.pointId = node.From
        temp.lr = node.direction
        temp.gp = node.action
        temp.floorNum = node.shelf_num
        missionData.push(temp)
      })
      subInfo.missionData = missionData
      if (this.waterLineForm.waterLineOrNot) {
        if (this.waterLineForm.inOrOut == "G") {
          subInfo.inPoint = this.waterLineForm.point
          subInfo.inAction = this.waterLineForm.action
        } else {
          subInfo.outPoint = this.waterLineForm.point
          subInfo.outAction = this.waterLineForm.action
        }
        subInfo.guide = "WCS"
      }
      subInfo.taskModelName = this.addTaskModelForm.taskModelName
      subInfo.remark = this.addTaskModelForm.remark
      return subInfo
    },
    // 箱号绑定框打开
    showBindBoxNumDialog (rowData) {
      if (rowData.missionData.length === 0) {
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
      const confirmResult = await this.$confirm('此操作将提交任务, 是否继续?', '提示', {
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

      if (this.waterLineForm.waterLineOrNot) {
        let res = false
        this.$refs.waterLineFormRef.validate(valid => {
          res = valid
        })
        if (!res) return
      }


      let subInfo = this.submitMsgEncode()

      const { data: res } = await this.$http.post('/dispatchMissionPlus', subInfo)
      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          type: 'error',
          message: res.meta.msg,
          showClose: true
        })
      }
      this.bindBoxNumDialogVisible = false
      // this.$message.success(res.meta.msg)
      this.$message({
        showClose: true,
        message: res.meta.msg,
        type: 'success'
      })
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
