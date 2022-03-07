<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>机台</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20">
        <el-col :span="4">
          <el-button type="primary"
                     @click="addDialogVisible = true">添加机台</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="portlist.portlist"
                border
                stripe
                height="500">
        <el-table-column label="设备名称"
                         prop="eqName"></el-table-column>
        <el-table-column label="设备类型"
                         prop="eqType"></el-table-column>
        <el-table-column label="任务模板名称"
                         prop="missionFromTo"></el-table-column>
        <el-table-column label="设备地标节点"
                         prop="bindingNode"></el-table-column>
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
                       @click="removeById(scope.row.eqName)">删除</el-button>
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

    <!-- 添加机台的对话框 -->
    <el-dialog title="添加机台"
               :visible.sync="addDialogVisible"
               width="50%"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="120px">
        <el-form-item label="设备名称"
                      prop="eqName">
          <el-input v-model="addForm.eqName"></el-input>
        </el-form-item>
        <el-form-item label="设备类型"
                      prop="eqType">
          <el-input v-model="addForm.eqType"></el-input>
        </el-form-item>
        <el-form-item label="任务模板名称"
                      prop="missionFromTo">
          <el-input v-model="addForm.missionFromTo"></el-input>
        </el-form-item>
        <el-form-item label="设备地标节点"
                      prop="bindingNode">
          <el-input v-model="addForm.bindingNode"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addPort">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改机台的对话框 -->
    <el-dialog title="修改机台"
               :visible.sync="editDialogVisible"
               width="50%"
               @close="editDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="editFormRef"
               :model="editForm"
               :rules="editFormRules"
               label-width="120px">
        <el-form-item label="设备名称"
                      prop="eqName">
          <el-input v-model="editForm.eqName"
                    :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="设备类型"
                      prop="eqType">
          <el-input v-model="editForm.eqType"></el-input>
        </el-form-item>
        <el-form-item label="任务模板名称"
                      prop="missionFromTo">
          <el-input v-model="editForm.missionFromTo"></el-input>
        </el-form-item>
        <el-form-item label="设备地标节点"
                      prop="bindingNode">
          <el-input v-model="editForm.bindingNode"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="editPort">确 定</el-button>
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
      portlist: {},
      // 列表总数
      total: 0,
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加的表单数据
      addForm: {},
      // 添加表单的验证规则对象
      addFormRules: {
        eqName: [{ required: true, message: '请输入设备名称', trigger: 'blur' }],
        eqType: [{ required: true, message: '请输入设备类型', trigger: 'blur' }],
        missionFromTo: [{ required: true, message: '请输入任务模板名称', trigger: 'blur' }],
        bindingNode: [{ required: true, message: '请输入设备地标节点', trigger: 'blur' }]
      },
      // 控制修改窗口的显示与隐藏
      editDialogVisible: false,
      // 修改表单的表单数据
      editForm: {},
      // 修改表单的验证规则对象
      editFormRules: {
        eqName: [{ required: true, message: '请输入设备名称', trigger: 'blur' }],
        eqType: [{ required: true, message: '请输入设备类型', trigger: 'blur' }],
        missionFromTo: [{ required: true, message: '请输入任务模板名称', trigger: 'blur' }],
        bindingNode: [{ required: true, message: '请输入设备地标节点', trigger: 'blur' }]
      }

    }
  },
  created () {
    this.getSystemPortList()
  },
  methods: {
    // 获取AGV监视列表
    async getSystemPortList () {
      const { data: res } = await this.$http.get('system/port', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('机台列表获取失败！')
      }
      this.portlist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getSystemPortList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getSystemPortList()
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 添加AGV
    addPort () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/port', this.addForm)
        if (res.meta.status !== 201) {
          return this.$message.error('添加机台失败！')
        }
        this.$message.success('添加机台成功！')
        this.getSystemPortList()
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
    // 修改机台
    editPort () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/port', this.editForm)
        if (res.meta.status !== 201) {
          return this.$message.error('修改机台失败！')
        }
        this.$message.success('修改机台成功！')
        this.getSystemPortList()
        this.editDialogVisible = false
      })
    },

    // 根据id，删除对应的机台信息
    async removeById (id) {
      // console.log(id)
      // 弹框提示机台是否删除信息
      const confirmResult = await this.$confirm('此操作将永久删除该机台, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果机台确认删除，则返回字符串 confirm
      // 如果机台取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      const requestParams = { data: {} }
      requestParams.data.eqName = id
      const { data: res } = await this.$http.delete('system/port', requestParams)
      if (res.meta.status !== 200) {
        this.$message.error('删除机台失败！')
      }

      this.$message.success('删除机台成功！')
      this.getSystemPortList()
    }
  }
}
</script>

<style lang="less" scoped></style>
