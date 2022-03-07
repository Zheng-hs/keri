<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>AGV</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20">
        <el-col :span="4">
          <el-button type="primary"
                     @click="addDialogVisible = true">添加AGV</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="agvlist.agvlist"
                border
                stripe
                height="500">
        <el-table-column label="agv名称"
                         prop="agvName"></el-table-column>
        <el-table-column label="安全电量"
                         prop="batterySoc"></el-table-column>
        <el-table-column label="agv类型"
                         prop="vehicleType"></el-table-column>
        <el-table-column label="地图分区"
                         prop="workArea"></el-table-column>
        <el-table-column label="启用/禁用"
                         prop="enable"></el-table-column>
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
                       @click="removeById(scope.row.agvName)">删除</el-button>
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

    <!-- 添加AGV的对话框 -->
    <el-dialog title="添加AGV"
               :visible.sync="addDialogVisible"
               width="50%"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="90px">
        <el-form-item label="agv名称"
                      prop="agvName">
          <el-input v-model="addForm.agvName"></el-input>
        </el-form-item>
        <el-form-item label="安全电量"
                      prop="batterySoc">
          <el-input v-model="addForm.batterySoc"></el-input>
        </el-form-item>
        <el-form-item label="agv类型"
                      prop="vehicleType">
          <el-input v-model="addForm.vehicleType"></el-input>
        </el-form-item>
        <el-form-item label="地图分区"
                      prop="workArea">
          <el-input v-model="addForm.workArea"></el-input>
        </el-form-item>
        <el-form-item label="启用/禁用"
                      prop="enable">
          <el-select v-model="addForm.enable"
                     placeholder="请选择"
                     clearable>
            <el-option label="启用"
                       value="启用"></el-option>
            <el-option label="禁用"
                       value="禁用"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addAgv">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改AGV的对话框 -->
    <el-dialog title="修改AGV"
               :visible.sync="editDialogVisible"
               width="50%"
               @close="editDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="editFormRef"
               :model="editForm"
               :rules="editFormRules"
               label-width="90px">
        <el-form-item label="agv名称"
                      prop="agvName">
          <el-input v-model="editForm.agvName"
                    :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="安全电量"
                      prop="batterySoc">
          <el-input v-model="editForm.batterySoc"></el-input>
        </el-form-item>
        <el-form-item label="agv类型"
                      prop="vehicleType">
          <el-input v-model="editForm.vehicleType"></el-input>
        </el-form-item>
        <el-form-item label="地图分区"
                      prop="workArea">
          <el-input v-model="editForm.workArea"></el-input>
        </el-form-item>
        <el-form-item label="启用/禁用"
                      prop="enable">
          <el-select v-model="editForm.enable"
                     placeholder="请选择"
                     clearable>
            <el-option label="启用"
                       value="启用"></el-option>
            <el-option label="禁用"
                       value="禁用"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="editAgv">确 定</el-button>
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
      agvlist: {},
      // 列表总数
      total: 0,
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加的表单数据
      addForm: {},
      // 添加表单的验证规则对象
      addFormRules: {
        agvName: [{ required: true, message: '请输入agv名称', trigger: 'blur' }],
        batterySoc: [{ required: true, message: '请输入安全电量', trigger: 'blur' }],
        vehicleType: [{ required: true, message: '请输入agv类型', trigger: 'blur' }],
        workArea: [{ required: true, message: '请输入地图分区', trigger: 'blur' }],
        enable: [{ required: true, message: '请选择agv的启用/禁用', trigger: 'blur' }]
      },
      // 控制修改窗口的显示与隐藏
      editDialogVisible: false,
      // 修改表单的表单数据
      editForm: {},
      // 修改表单的验证规则对象
      editFormRules: {
        agvName: [{ required: true, message: '请输入agv名称', trigger: 'blur' }],
        batterySoc: [{ required: true, message: '请输入安全电量', trigger: 'blur' }],
        vehicleType: [{ required: true, message: '请输入agv类型', trigger: 'blur' }],
        workArea: [{ required: true, message: '请输入地图分区', trigger: 'blur' }],
        enable: [{ required: true, message: '请选择agv的启用/禁用', trigger: 'blur' }]
      }

    }
  },
  created () {
    this.getSystemAGVList()
  },
  methods: {
    // 获取AGV监视列表
    async getSystemAGVList () {
      const { data: res } = await this.$http.get('system/agv', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('AGV列表获取失败！')
      }
      this.agvlist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getSystemAGVList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getSystemAGVList()
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 添加AGV
    addAgv () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/agv', this.addForm)
        if (res.meta.status !== 201) {
          return this.$message.error('添加AGV失败！')
        }
        this.$message.success('添加AGV成功！')
        this.getSystemAGVList()
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
    // 修改AGV
    editAgv () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('system/agv', this.editForm)
        if (res.meta.status !== 201) {
          return this.$message.error('修改AGV失败！')
        }
        this.$message.success('修改AGV成功！')
        this.getSystemAGVList()
        this.editDialogVisible = false
      })
    },

    // 根据id，删除对应的AGV信息
    async removeById (id) {
      // console.log(id)
      // 弹框提示AGV是否删除信息
      const confirmResult = await this.$confirm('此操作将永久删除该AGV, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果AGV确认删除，则返回字符串 confirm
      // 如果AGV取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      const requestParams = { data: {} }
      requestParams.data.agvName = id
      const { data: res } = await this.$http.delete('system/agv', requestParams)
      if (res.meta.status !== 200) {
        this.$message.error('删除AGV失败！')
      }

      this.$message.success('删除AGV成功！')
      this.getSystemAGVList()
    }
  }
}
</script>

<style lang="less" scoped></style>
