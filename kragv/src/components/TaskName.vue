<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20" class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary" @click="addDialogVisible = true">新增</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="taskNameList" border highlight-current-row stripe :height="tableHeight">
        <el-table-column label="点位" prop="idInMap"></el-table-column>
        <el-table-column label="功能参数" prop="func"></el-table-column>
        <el-table-column label="可用车辆" prop="agvLimit">
          <template slot-scope="scope">
            {{scope.row.agvLimit.toString()}}
          </template>
        </el-table-column>
        <el-table-column label="可用组" prop="groupLimit" :formatter="stateFormat"></el-table-column>
        <el-table-column label="描述" prop="siteDescription"></el-table-column>
        <el-table-column label="是否受限" prop="limit">
          <template slot-scope="scope">
            {{ scope.row.limit == true ? '是' : '否' }}
          </template>
        </el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="editAction(scope.row)">修改</el-button>
            <el-button type="danger" size="mini" @click="deleteAction(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <!-- <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pagenum"
        :page-sizes="[10, 20, 50, 100]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination> -->
    </el-card>

    <!-- 修改动作的对话框 -->
    <el-dialog title="修改任务名" :visible.sync="dialogVisible" width="630px">
      <el-form ref="taskNameFormRef" :model="taskNameForm" :rules="taskNameFormRules" label-width="100px">
        <el-form-item label="点位" prop="idInMap">
          <el-input v-model="taskNameForm.idInMap"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="siteDescription">
          <el-input v-model="taskNameForm.siteDescription"></el-input>
        </el-form-item>
        <el-form-item label="可用车辆" prop="agvLimit" v-if="taskNameForm.limit==true">
          <el-select v-model="taskNameForm.agvLimit" multiple placeholder="请选择agv">
            <el-option v-for="item in agvList" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="可用组" prop="groupLimit"  v-if="taskNameForm.limit==true">
          <el-select v-model="taskNameForm.groupLimit" multiple placeholder="请选择组">
            <el-option v-for="item in groupList" :key="item.groupId" :label="item.groupName" :value="item.groupId"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="功能参数" prop="func">
          <el-select v-model="taskNameForm.func" placeholder="请选择功能参数">
            <el-option v-for="item in funcList" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否受限" prop="limit">
          <el-switch v-model="taskNameForm.limit" active-color="#13ce66" inactive-color="#ff4949"> </el-switch>
        </el-form-item>
      </el-form>

      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="sumbit">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 新增动作对话框 -->
    <el-dialog title="新增任务名" :visible.sync="addDialogVisible" width="630px" @close="addDialogClosed">
      <el-form ref="addFormRef" :model="addTaskNameForm" :rules="taskNameFormRules" label-width="100px">
        <el-form-item label="点位" prop="idInMap">
          <el-input v-model="addTaskNameForm.idInMap"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="siteDescription">
          <el-input v-model="addTaskNameForm.siteDescription"></el-input>
        </el-form-item>
        <el-form-item label="可用车辆" prop="agvLimit"  v-if="addTaskNameForm.limit==true">
          <el-select v-model="addTaskNameForm.agvLimit" multiple placeholder="请选择agv">
            <el-option v-for="item in agvList" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="可用组" prop="groupLimit" v-if="addTaskNameForm.limit==true">
          <el-select v-model="addTaskNameForm.groupLimit" multiple placeholder="请选择组">
            <el-option v-for="item in groupList" :key="item.groupId" :label="item.groupName" :value="item.groupId"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="功能参数" prop="func">
          <el-select v-model="addTaskNameForm.func" placeholder="请选择功能参数">
            <el-option v-for="item in funcList" :key="item" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否受限" prop="limit">
          <el-switch v-model="addTaskNameForm.limit" active-color="#13ce66" inactive-color="#ff4949"> </el-switch>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addAction">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      taskNameList: [],
      groupList: [],
      dialogVisible: false,
      addDialogVisible: false,
      taskNameForm: {},
      addTaskNameForm: {limit:false,groupLimit:[],agvLimit:[]},
      taskNameFormRules: {
        idInMap: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        siteDescription: [{ required: true, message: '请输入描述', trigger: 'blur' }],
        func: [{ required: true, message: '请选择功能参数', trigger: 'blur' }],
      },
      tableHeight: window.innerHeight * 0.7,
      agvList: [],
      agvLimit: [],
      groupList: [],
      groupLimit: [],
      funcList: [],
      // limit: false
    }
  },
  methods: {
    async getActionList() {
      const { data: res } = await this.$http.get('/worksite/sites')
      if (res.meta.status == 200) {
        this.taskNameList = res.data.worksiteList
      }

      const { data: res1 } = await this.$http.get('/kr3/getTaskArgs')
      if (res.meta.status == 200) {
        this.pointList = res1.data.workSiteList
        this.actionList = res1.data.actionArgsList
        this.agvList = res1.data.agvIdList
        this.groupList = res1.data.groupList
      }

      const { data: res2 } = await this.$http.get('/worksite/func')
      this.funcList = res2.data.funcList
    },
    stateFormat(row, column) {
      const list = []
        row.groupLimit.forEach(v=>{
          this.groupList.forEach(i=> {
            if(i.groupId === v) {
              list.push(i.groupName)
            }
          })
        })
        return list.toString()
    },

    editAction(row) {
      this.dialogVisible = true
      this.taskNameForm = row
    },
    sumbit() {
      this.$refs.taskNameFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/worksite/sites/update', this.taskNameForm)
        if (res.meta.status == 200) {
          this.$message.success('修改成功')
          this.dialogVisible = false
          this.getActionList()
        } else {
          this.$message.error('修改失败')
        }
      })
    },
    // 监听添加用户对话框的关闭事件
    addDialogClosed() {
      this.$refs.addFormRef.resetFields()
    },
    addAction() {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/worksite/sites', this.addTaskNameForm)
        if (res.meta.status == 200) {
          this.$message.success('新增成功')
          this.addDialogVisible = false
          this.getActionList()
        } else {
          this.$message.error('新增失败')
        }
      })
    },
    async deleteAction(id) {
      const confirmResult = await this.$confirm('此操作将删除该任务名, 是否继续?', '提示', {
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
      const { data: res } = await this.$http.delete(`/worksite/sites/${id}`)
      if (res.meta.status == 200) {
        this.$message.success('删除成功')
        this.getActionList()
      } else {
        this.$message.error('删除失败')
      }
    }
  },
  created() {
    this.getActionList()
  }
}
</script>

<style></style>
