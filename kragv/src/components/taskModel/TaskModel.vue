<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20" class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary" @click="openDialog">下发任务</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="taskModelData" border highlight-current-row :height="tableHeight">
        <el-table-column  type="index"  width="50"></el-table-column>
        <el-table-column label="任务模板名" prop="templateName"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="showBindBoxNumDialog(scope.row)">派发</el-button>
            <el-button type="primary" size="mini" @click="turnToEditTaskModel(scope.row)">修改</el-button>
            <el-button type="danger" size="mini" @click="delTaskModel(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <el-dialog :title="title" :visible.sync="dialogVisible" width="70%" @close="closeDialog">
      <el-dialog width="30%" title="请填写模板名称" :visible.sync="innerVisible" append-to-body>
        <el-input v-model="templateName"></el-input>
        <span slot="footer" class="dialog-footer">
          <el-button @click="innerVisible = false">取 消</el-button>
          <el-button type="primary" @click="saveModel">确 定</el-button>
        </span>
      </el-dialog>
      <el-row class="row1" :gutter="20" v-if="editShow">
        <el-col :span="5">
          <el-select v-model="select" placeholder="请选择">
            <el-option v-for="item in selectList" :key="item.value" :label="item.name" :value="item.value"> </el-option>
          </el-select>
        </el-col>
        <el-col v-if="select === 'groupId'" :span="5">
          <el-select v-model="groupId" placeholder="请选择组">
            <el-option v-for="item in groupList" :key="item.groupId" :label="item.groupName" :value="item.groupId"> </el-option>
          </el-select>
        </el-col>
        <el-col v-if="select === 'agvId'" :span="5">
          <el-select v-model="agvId" placeholder="请选择agv">
            <el-option v-for="item in agvList" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-col>
      </el-row>
      <el-row :gutter="20" v-else>
        <el-col :span="6">
          <el-input v-model="templateName"></el-input>
        </el-col>
      </el-row>
      <div class="line" v-for="(i, index) in actions" :key="index">
        <div class="line-left">

        <el-radio v-model="checked" :label="index" @change="choose">
          <div class="line1">
            <div>请选择站点：</div>
            <el-select v-model="actions[index].point" filterable placeholder="请选择站点">
              <el-option v-for="item in pointList" :key="item.workSiteId" :label="item.description" :value="item.workSiteId"> </el-option>
            </el-select>
          </div>
        </el-radio>
        </div>
        <div class="line-right">
          <div class="actions">请选择动作:</div>
          <div class="line2">
            <el-select v-model="actions[index].cmdList[index1]" placeholder="请选择动作" @change="val => chageValue(val, index1, index)" v-for="(tag, index1) in actions[index].cmdList" :key="index1">
              <el-option v-for="item in actionList" :key="item.actionDescription" :label="item.actionDescription" :value="item.id"> </el-option>
            </el-select>
            <el-button type="primary" icon="el-icon-circle-plus-outline" @click="addAction(index)"></el-button>
            <el-button type="danger" icon="el-icon-remove-outline" @click="delAction(index)"></el-button>
          </div>
        </div>
      </div>
        <el-button class="add_btn" type="primary" icon="el-icon-circle-plus-outline" @click="addPoint"></el-button>
        <el-button type="danger" icon="el-icon-remove-outline" @click="delPoint"></el-button>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="openName" v-if="addModel">保存为模板</el-button>
        <el-button type="primary" @click="openName" v-if="editShow1">另存为模板</el-button>
        <el-button type="primary" @click="sendTask" v-if="editShow">下 发</el-button>
        <el-button type="primary" @click="editModel" v-else>保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nodeList: [],
      checked: '',
      // 控制bindBoxNum对话框的显示与隐藏
      bindBoxNumDialogVisible: false,
      dialogVisible: false,
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
      taskModelData: [],
      // 列表总数
      total: 0,
      modelNameSearch: '',
      // 计时器
      timer: null,
      title: '任务下发',
      addModel: true,

      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      actionArgsList: [],
      pointList: [],
      actionList: [],
      groupId: '',
      agvId: '',
      actions: [
        {
          point: '',
          cmdList: ['']
        }
      ],
      workSiteId: '',
      actionName: '',
      actionForm: {
        point: '',
        cmdList: ['']
      },
      j: 0,
      groupList: [],
      selectList: [
        {
          name: 'agv',
          value: 'agvId'
        },
        {
          name: '组',
          value: 'groupId'
        }
      ],
      select: '',
      agvList: [],
      editShow: true,
      editShow1: false,
      templateName: '',
      innerVisible: false,
      modelId: ''
    }
  },
  created() {},
  mounted() {
    this.getTaskModel()
  },
  beforeDestroy() {},
  methods: {
    async openDialog() {
      this.title = '任务下发'
      this.editShow = true
      this.editShow1 = false
      this.addModel = true
      this.dialogVisible = true
    },
    choose(i) {
      this.j = i
    },
    addAction(j) {
      this.actions[j].cmdList.push('')
    },
    delAction(j) {
      this.actions[j].cmdList.pop()
    },
    addPoint() {
      this.actions.splice(this.j + 1, 0, {
        point: '',
        cmdList: ['']
      })
    },
    delPoint() {
      this.actions.splice(this.j, 1)
    },
    chageValue(value, index, j) {
      this.actions[j].cmdList[index] = value
    },
    async sendTask() {
      if (this.select === '' || this.actions[0].point === '' || this.actions[0].cmdList[0] === '') {
        this.$message.info('请填写完整')
      } else {
        const yy = new Date().getFullYear()
        const mm = new Date().getMonth() + 1
        const dd = new Date().getDate()
        const hh = new Date().getHours() < 10 ? '0' + new Date().getHours() : new Date().getHours()
        const mf = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes()
        const ss = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds()
        if (this.select === 'agvId') {
          const { data: res } = await this.$http.post('/kr3/recvLiftTaskFromExternal', {
            dispatchId: yy + '' + mm + '' + dd + '' + hh + '' + mf + '' + ss,
            action: this.actions,
            agvId: this.agvId
          })
          if (res.meta.status == 200) {
            this.$message.success('任务下发成功')
            this.actions = [
              {
                point: '',
                cmdList: ['']
              }
            ]
            this.select = ''
            this.groupId = ''
            this.agvId = ''
            this.templateName = ''
            this.dialogVisible = false
          }
        } else {
          const { data: res } = await this.$http.post('/kr3/recvLiftTaskFromExternal', {
            dispatchId: yy + '' + mm + '' + dd + '' + hh + '' + mf + '' + ss,
            action: this.actions,
            groupId: parseInt(this.groupId)
          })
          if (res.meta.status == 200) {
            this.$message.success('任务下发成功')
            this.actions = [
              {
                point: '',
                cmdList: ['']
              }
            ]
            this.select = ''
            this.groupId = ''
            this.agvId = ''
            this.templateName = ''
            this.dialogVisible = false
          }
        }
      }
    },
    async editModel() {
      const { data: res } = await this.$http.post('/templates/task/update', {
        templateName: this.templateName,
        action: this.actions,
        id: this.modelId
      })
      if (res.meta.status == 200) {
        this.$message.success('修改模板成功')
        this.dialogVisible = false
        this.actions = [
          {
            point: '',
            cmdList: ['']
          }
        ]
        this.select = ''
        this.groupId = ''
        this.agvId = ''
        this.templateName = ''
        this.getTaskModel()
      } else {
        this.$message.error('修改模板失败')
      }
    },
    async saveModel() {
      if (this.templateName === '') {
        this.$message.info('请填写模板名')
      } else {
        const { data: res } = await this.$http.post('/templates/task', {
          templateName: this.templateName,
          action: this.actions
        })
        if (res.meta.status == 200) {
          this.$message.success('新增任务模板成功')
          this.innerVisible = false
          this.dialogVisible = false
          this.actions = [
            {
              point: '',
              cmdList: ['']
            }
          ]
          this.select = ''
          this.groupId = ''
          this.agvId = ''
          this.templateName = ''
          this.getTaskModel()
        } else {
          this.$message.error('新增模板失败')
        }
      }
    },
    closeDialog() {
      this.actions = [
        {
          point: '',
          cmdList: ['']
        }
      ]
      this.select = ''
      this.groupId = ''
      this.agvId = ''
      this.templateName = ''
      this.dialogVisible = false
    },
    // 获取任务状态列表
    async getTaskModel() {
      const { data: res } = await this.$http.get('/templates/task')
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          showClose: true,
          message: res.meta.msg,
          type: 'error'
        })
      }
      this.taskModelData = res.data.templateList
      const { data: res1 } = await this.$http.get('/kr3/getTaskArgs')
      if (res1.meta.status == 200) {
        this.pointList = res1.data.workSiteList
        this.actionList = res1.data.actionArgsList
        this.agvList = res1.data.agvIdList
        this.groupList = res1.data.groupList
      }
    },
    openName() {
      if (this.actions[0].point === '' || this.actions[0].cmdList[0] === '') {
        this.$message.info('请填写完整')
      } else {
        this.innerVisible = true
      }
    },
    // 判断是否admin page
    isAdminPage() {
      let path = window.location.href
      if (path.indexOf('admin') != -1) {
        return true
      } else {
        return false
      }
    },
    // 跳转到添加页面
    goAddPage() {
      this.$router.push('taskmodeladd')
    },

    // 跳转到编辑页面
    turnToEditTaskModel(row) {
      this.title = '修改任务模板'
      this.editShow = false
      this.editShow1 = true
      this.addModel = false
      this.templateName = row.templateName
      this.modelId = row.id
      this.actions = row.action
      this.dialogVisible = true
    },
    // 删除模板
    async delTaskModel(row) {
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

      const { data: res } = await this.$http.delete(`/templates/task/${row.id}`)
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
    // 箱号绑定框打开
    showBindBoxNumDialog(row) {
      this.title = '下发任务'
      this.editShow = true
      this.editShow1 = false
      this.addModel = false
      this.templateName = row.templateName
      this.modelId = row.id
      this.actions = row.action
      this.dialogVisible = true
    },
    // 任务派发
    async dispatchMission(taskModel) {
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
    }

    //
    //
    //
  }

  //
  //
}
</script>

<style lang="less" scoped>
.row1 {
  margin: 5px;
}
.el-radio {
  display: flex;
}
/deep/.el-dialog__body {
  overflow: scroll;
  overflow-x: hidden;
  height: 500px;
}
/deep/ .el-radio__input {
  display: flex;
  align-items: center;
}
.line {
  display: flex;
  align-items: center;
  .line-left {
    flex: 1;
  }
  .line-right {
    flex: 3;
    display: flex;
    align-items: center;
  }
  .actions {
    margin-right: 10px;
    flex: 1;
  }
  .line1 {
    margin: 5px;
    display: flex;
    align-items: center;
    div {
      margin-right: 10px;
    }
  }
  .line2 {
    flex: 8;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    .el-select {
      margin: 5px;
    }
  }
}
.add_btn {
  margin: 5px;
}
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
