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
      <el-table :data="groupList" border highlight-current-row stripe :height="tableHeight">
        <el-table-column label="组名称" prop="groupName"></el-table-column>
        <el-table-column label="车数量" prop="groupLimit"></el-table-column>
        <el-table-column label="区域策略参数" prop="areaStrategyEnum"></el-table-column>
        <el-table-column label="充电策略参数" prop="chargeStrategyEnum"></el-table-column>
        <el-table-column label="任务派发策略参数" prop="taskDispatchStrategyEnum"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作" width="230px" fixed="right">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="editAction(scope.row)">修改</el-button>
            <el-button type="danger" size="mini" @click="deleteAction(scope.row.groupId)">删除</el-button>
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
    <el-dialog title="修改工作组" :visible.sync="dialogVisible" width="50%">
      <el-form ref="groupFormRef" :model="groupForm" :rules="groupFormRules" label-width="150px">
        <el-form-item label="组名称" prop="groupName">
          <el-input v-model="groupForm.groupName"></el-input>
        </el-form-item>
        <el-form-item label="车数量" prop="groupLimit">
          <el-input v-model="groupForm.groupLimit"></el-input>
        </el-form-item>
        <el-form-item label="区域策略参数" prop="areaStrategyEnum">
          <el-select v-model="groupForm.areaStrategyEnum" placeholder="请选择区域策略参数">
            <el-option v-for="(item,index) in areaStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="充电策略参数" prop="chargeStrategyEnum">
          <el-select v-model="groupForm.chargeStrategyEnum" placeholder="请选择充电策略参数">
            <el-option v-for="(item,index) in chargeStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务派发策略参数" prop="taskDispatchStrategyEnum">
          <el-select v-model="groupForm.taskDispatchStrategyEnum" placeholder="请选择任务派发策略参数">
            <el-option v-for="(item,index) in taskStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
      </el-form>

      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="sumbit">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 新增动作对话框 -->
    <el-dialog title="新增工作组" :visible.sync="addDialogVisible" width="50%" @close="addDialogClosed">
      <el-form ref="addFormRef" :model="addGroupForm" :rules="groupFormRules" label-width="150px">
        <el-form-item label="组名称" prop="groupName">
          <el-input v-model="addGroupForm.groupName"></el-input>
        </el-form-item>
        <el-form-item label="车数量" prop="groupLimit">
          <el-input v-model="addGroupForm.groupLimit"></el-input>
        </el-form-item>
        <el-form-item label="区域策略参数" prop="areaStrategyEnum">
          <el-select v-model="addGroupForm.areaStrategyEnum" placeholder="请选择区域策略参数">
            <el-option v-for="(item,index) in areaStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="充电策略参数" prop="chargeStrategyEnum">
          <el-select v-model="addGroupForm.chargeStrategyEnum" placeholder="请选择充电策略参数">
            <el-option v-for="(item,index) in chargeStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务派发策略参数" prop="taskDispatchStrategyEnum">
          <el-select v-model="addGroupForm.taskDispatchStrategyEnum" placeholder="请选择任务派发策略参数">
            <el-option v-for="(item,index) in taskStrategyList" :key="index" :label="item" :value="item"> </el-option>
          </el-select>
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
      groupList: [],
      dialogVisible: false,
      addDialogVisible: false,
      groupForm: {},
      addGroupForm: {},
      groupFormRules: {
        groupLimit: [{ required: true, message: '请输入车数量', trigger: 'blur' }],
        areaStrategyEnum: [{ required: true, message: '请选择区域策略参数', trigger: 'blur' }],
        taskDispatchStrategyEnum: [{ required: true, message: '请选择任务派发策略参数', trigger: 'blur' }],
        chargeStrategyEnum: [{ required: true, message: '请选择充电策略参数', trigger: 'blur' }]
      },
      tableHeight: window.innerHeight * 0.7,
      taskStrategyList: [],
      chargeStrategyList:[],
      areaStrategyList: []
    }
  },
  methods: {
    async getGroupList() {
      const { data: res } = await this.$http.get('/group/groups')
      if (res.meta.status == 200) {
        this.groupList = res.data.groupList
      }
      const {data: res3} = await this.$http.get('/group/task')
      this.taskStrategyList = res3.data.taskStrategyList
      const {data: res1} = await this.$http.get('/group/charge')
      this.chargeStrategyList = res1.data.chargeStrategyList
      const {data: res2} = await this.$http.get('/group/area')
      this.areaStrategyList = res2.data.areaStrategyList
    },
    async editAction(row) {
      this.dialogVisible = true
      this.groupForm = row
    },
    sumbit() {
      this.$refs.groupFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/group/groups/update', this.groupForm)
        if (res.meta.status == 200) {
          this.$message.success('修改成功')
          this.dialogVisible = false
          this.getGroupList()
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
        const { data: res } = await this.$http.post('/group/groups', this.addGroupForm)
        if (res.meta.status == 200) {
          this.$message.success('新增成功')
          this.addDialogVisible = false
          this.getGroupList()
        } else {
          this.$message.error('新增失败')
        }
      })
    },
    async deleteAction(groupId) {
      const confirmResult = await this.$confirm('此操作将删除该工作组, 是否继续?', '提示', {
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
      const { data: res } = await this.$http.delete(`/group/groups/${groupId}`)
      if (res.meta.status == 200) {
        this.$message.success('删除成功')
        this.getGroupList()
      } else {
        this.$message.error('删除失败')
      }
    }
  },
  created() {
    this.getGroupList()
  }
}
</script>

<style lang="less" scoped>
/deep/.el-select {
    width: 100%;
}
</style>
