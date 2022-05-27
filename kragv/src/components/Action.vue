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
      <el-table :data="actionList" border highlight-current-row stripe :height="tableHeight">
        <el-table-column label="动作参数" prop="actionArgs"></el-table-column>
        <el-table-column label="描述" prop="description"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作" width="230px" fixed="right">
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
    <el-dialog title="修改动作" :visible.sync="dialogVisible" width="630px">
      <el-form ref="actionFormRef" :model="actionForm" :rules="actionFormRules" label-width="100px">
        <el-form-item label="动作参数" prop="actionArgs">
          <el-input v-model="actionForm.actionArgs"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="description">
          <el-input v-model="actionForm.description"></el-input>
        </el-form-item>
      </el-form>

      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="sumbit">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 新增动作对话框 -->
    <el-dialog title="新增动作" :visible.sync="addDialogVisible" width="630px" @close="addDialogClosed">
      <el-form ref="addFormRef" :model="addActionForm" :rules="actionFormRules" label-width="100px">
        <el-form-item label="动作参数" prop="actionArgs">
          <el-input v-model="addActionForm.actionArgs"></el-input>
        </el-form-item>
        <el-form-item label="描述" prop="description">
          <el-input v-model="addActionForm.description"></el-input>
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
      actionList: [],
      dialogVisible: false,
      addDialogVisible: false,
      actionForm: {},
      addActionForm: {},
      actionFormRules: {
        actionName: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        actionArgs: [{ required: true, message: '请输入动作名称', trigger: 'blur' }],
        description: [{ required: true, message: '请输入描述', trigger: 'blur' }]
      },
      tableHeight: window.innerHeight * 0.7
    }
  },
  methods: {
    async getActionList() {
      const { data: res } = await this.$http.get('/action/args')
      if (res.meta.status == 200) {
        this.actionList = res.data.actionArgsList
      }
    },
    editAction(row) {
      this.dialogVisible = true
      this.actionForm = row
    },
    sumbit() {
      this.$refs.actionFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/action/args/update', this.actionForm)
        if (res.meta.status == 200) {
          this.$message.success('修改动作成功')
          this.dialogVisible = false
          this.getActionList()
        } else {
          this.$message.error('修改动作失败')
        }
      })
    },
    // 监听添加用户对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    addAction() {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('/action/args', this.addActionForm)
        if (res.meta.status == 200) {
          this.$message.success('新增动作成功')
          this.addDialogVisible = false
          this.getActionList()
        } else {
          this.$message.error('新增动作失败')
        }
      })
    },
    async deleteAction(id) {
      const confirmResult = await this.$confirm('此操作将删除该动作, 是否继续?', '提示', {
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
      const { data: res } = await this.$http.delete(`/action/args/${id}`)
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
