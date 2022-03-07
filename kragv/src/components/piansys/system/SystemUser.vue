<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>用户</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20">
        <el-col :span="4">
          <el-button type="primary"
                     @click="addDialogVisible = true">添加用户</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="userlist"
                border
                stripe
                height="500">
        <el-table-column label="用户名"
                         prop="username"></el-table-column>
        <el-table-column label="密码"
                         prop="password"></el-table-column>
        <el-table-column label="权限"
                         prop="power"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="250px"
                         fixed="right">
          <template slot-scope="scope">
            <el-button type="primary"
                       size="mini"
                       @click="editFormShow(scope.row)">修改</el-button>
            <el-button type="danger"
                       size="mini"
                       @click="removeById(scope.row.username)">删除</el-button>
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

    <!-- 添加用户的对话框 -->
    <el-dialog title="添加用户"
               :visible.sync="addDialogVisible"
               width="50%"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="90px">
        <el-form-item label="用户名"
                      prop="username">
          <el-input v-model="addForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码"
                      prop="password">
          <el-input v-model="addForm.password"></el-input>
        </el-form-item>
        <el-form-item label="权限"
                      prop="power">
          <el-select v-model="addForm.authorization"
                     placeholder="请选择"
                     clearable>
            <el-option label="管理员"
                       value=0></el-option>
            <el-option label="普通用户"
                       value=1></el-option>
          </el-select>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addUser">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改用户的对话框 -->
    <el-dialog title="修改用户"
               :visible.sync="editDialogVisible"
               width="50%"
               @close="editDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="editFormRef"
               :model="editForm"
               :rules="editFormRules"
               label-width="90px">
        <el-form-item label="用户名"
                      prop="username">
          <el-input v-model="editForm.username"
                    :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="密码"
                      prop="password">
          <el-input v-model="editForm.password"></el-input>
        </el-form-item>
        <el-form-item label="权限"
                      prop="authorization">
          <el-select v-model="editForm.authorization"
                     placeholder="请选择"
                     clearable>
            <el-option label="普通用户"
                       value="guest"></el-option>
            <el-option label="工程师"
                       value="engineer"></el-option>
            <el-option label="管理员"
                       value="admin"></el-option>
          </el-select>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="editUser">确 定</el-button>
      </span>
    </el-dialog>

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
      // 列表
      userlist: {},
      // 列表总数
      total: 0,
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加的表单数据
      addForm: {},
      // 添加表单的验证规则对象
      addFormRules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        authorization: [{ required: true, message: '请选择权限', trigger: 'blur' }]
      },
      // 控制修改窗口的显示与隐藏
      editDialogVisible: false,
      // 修改表单的表单数据
      editForm: {},
      // 修改表单的验证规则对象
      editFormRules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        authorization: [{ required: true, message: '请选择权限', trigger: 'blur' }]
      }

    }
  },
  created () {
    this.getSystemUserList()
  },
  methods: {
    // 获取用户监视列表
    async getSystemUserList () {
      const { data: res } = await this.$http.get('userlist')
      if (res.meta.status !== 200) {
        return this.$message.error('用户列表获取失败！')
      }
      this.userlist = res.data
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getSystemUserList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getSystemUserList()
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 添加用户
    addUser () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/user', this.addForm)
        if (res.meta.status !== 201) {
          return this.$message.error('添加用户失败！')
        }
        this.$message.success('添加用户成功！')
        this.getSystemUserList()
        this.addDialogVisible = false
      })
    },
    // 监听修改对话框的关闭事件
    editDialogClosed () {
      this.$refs.editFormRef.resetFields()
    },
    // 打开修改对话框
    editFormShow (editRow) {
      this.editForm = editRow
      this.editDialogVisible = true
    },
    // 修改用户
    editUser () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/user', this.editForm)
        if (res.meta.status !== 201) {
          return this.$message.error('修改用户失败！')
        }
        this.$message.success('修改用户成功！')
        this.getSystemUserList()
        this.editDialogVisible = false
      })
    },

    // 根据id，删除对应的用户信息
    async removeById (id) {
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      const requestParams = { data: {} }
      requestParams.data.username = id
      const { data: res } = await this.$http.delete('system/user', requestParams)
      if (res.meta.status !== 200) {
        this.$message.error('删除用户失败！')
      }

      this.$message.success('删除用户成功！')
      this.getSystemUserList()
    }
  }
}
</script>

<style lang="less" scoped></style>
