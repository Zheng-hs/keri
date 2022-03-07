<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>系统设置</el-breadcrumb-item>
      <el-breadcrumb-item>任务类</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/systemtaskmodel' }">任务模板</el-breadcrumb-item>
      <el-breadcrumb-item>任务模板添加</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>

      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     @click="addDialogVisible = true">添加关键点</el-button>
          <el-button type="primary"
                     @click="insertDialogVisible = true">插入关键点</el-button>
          <el-button type="primary"
                     @click="submitDialogVisible = true">提交</el-button>
        </el-col>
        <el-col class="btnrow2">
          <el-button type="primary"
                     @click="forwardTaskModel">返回</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="nodeList"
                border
                stripe
                height="500">
        <el-table-column label="组内编号"
                         prop="nodeSn"></el-table-column>
        <el-table-column label="任务关键节点名称"
                         prop="node"></el-table-column>
        <el-table-column label="节点动作"
                         prop="action"></el-table-column>
        <el-table-column label="业务类型"
                         prop="bussinessType"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="100px">
          <template slot-scope="scope">
            <el-button type="danger"
                       size="mini"
                       @click="delNode(scope.row.nodeSn)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 添加点位的对话框 -->
    <el-dialog title="添加关键节点"
               :visible.sync="addDialogVisible"
               width="50%"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="80px">
        <el-form-item label="节点名称"
                      prop="node">
          <el-input v-model="addForm.node"></el-input>
        </el-form-item>
        <el-form-item label="节点动作"
                      prop="action">
          <el-input v-model="addForm.action"></el-input>
        </el-form-item>
        <el-form-item label="业务类型"
                      prop="bussinessType">
          <el-input v-model="addForm.bussinessType"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addNode">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 插入点位的对话框 -->
    <el-dialog title="插入关键点"
               :visible.sync="insertDialogVisible"
               width="50%"
               @close="insertDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="insertFormRef"
               :model="insertForm"
               :rules="insertFormRules"
               label-width="80px">
        <el-form-item label="组内编号"
                      prop="nodeSn">
          <el-input v-model="insertForm.nodeSn"></el-input>
        </el-form-item>
        <el-form-item label="节点名称"
                      prop="node">
          <el-input v-model="insertForm.node"></el-input>
        </el-form-item>
        <el-form-item label="节点动作"
                      prop="action">
          <el-input v-model="insertForm.action"></el-input>
        </el-form-item>
        <el-form-item label="业务类型"
                      prop="bussinessType">
          <el-input v-model="insertForm.bussinessType"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="insertDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="insertNode">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 提交对话框 -->
    <el-dialog title="提交任务模板"
               :visible.sync="submitDialogVisible"
               width="50%">
      <!-- 内容主体区 -->
      <el-form ref="submitFormRef"
               :model="submitForm"
               :rules="submitFormRules"
               label-width="80px">
        <el-form-item label="模板组名"
                      prop="groupName">
          <el-input v-model="submitForm.groupName"
                    :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="工作区"
                      prop="workArea">
          <el-input v-model="submitForm.workArea"></el-input>
        </el-form-item>
        <el-form-item label="默认AGV"
                      prop="agvDefault">
          <el-input v-model="submitForm.agvDefault"></el-input>
        </el-form-item>
        <el-form-item label="默认货物"
                      prop="payloadDefault">
          <el-input v-model="submitForm.payloadDefault"></el-input>
        </el-form-item>
        <el-form-item label="业务注释"
                      prop="content">
          <el-input v-model="submitForm.content"></el-input>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="submitDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="submitMissionModel">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  data () {
    return {
      receiveFromTo: {},
      // 列表数据
      nodeList: [],
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加表单验证规则对象
      addFormRules: {
        node: [{ required: true, message: '请输入节点名称', trigger: 'blur' }],
        action: [{ required: true, message: '请输入节点动作', trigger: 'blur' }],
        bussinessType: [{ required: true, message: '请输入业务类型', trigger: 'blur' }]
      },
      // 添加表单数据
      addForm: {},
      // 控制插入对话框的显示与隐藏
      insertDialogVisible: false,
      // 添加表单的验证规则对象
      insertFormRules: {
        nodeSn: [{ required: true, message: '请输入组内编号', trigger: 'blur' }],
        node: [{ required: true, message: '请输入节点名称', trigger: 'blur' }],
        action: [{ required: true, message: '请输入节点动作', trigger: 'blur' }],
        bussinessType: [{ required: true, message: '请输入业务类型', trigger: 'blur' }]
      },
      // 添加插入的表单数据
      insertForm: {},
      // 提交对话框的显示与隐藏
      submitDialogVisible: false,
      // 提交表单的验证规则对象
      submitFormRules: {
        groupName: [{ required: true, message: '请输入模板组名', trigger: 'blur' }],
        workArea: [{ required: true, message: '请输入工作区', trigger: 'blur' }]
      },
      // 提交表单数据
      submitForm: {
        nodeList: []
      }

    }
  },
  created () {
    this.getReceiveFromTo()
  },
  mounted () {
  },
  methods: {
    // 获取选择行参数
    getReceiveFromTo () {
      this.receiveFromTo = this.$route.params.editData
      this.submitForm = this.receiveFromTo
      this.nodeList = this.submitForm.nodeList
    },

    // 添加窗口关闭,触发的函数
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 添加点位到列表
    addNode () {
      // 深拷贝添加表单
      const p = JSON.parse(JSON.stringify(this.addForm))
      // 拿到组内编号
      p.nodeSn = this.nodeList.length
      // 添加到末尾
      this.nodeList.push(p)
      this.addDialogVisible = false
    },
    // 插入窗口关闭,触发的函数
    insertDialogClosed () {
      this.$refs.insertFormRef.resetFields()
    },
    // 插入点位到列表
    insertNode () {
      const p = JSON.parse(JSON.stringify(this.insertForm))
      // 插入点位
      this.nodeList.splice(p.nodeSn, 0, p)
      // 重新编排组内编号
      for (let i = 0; i < this.nodeList.length; i++) {
        this.nodeList[i].nodeSn = i
      }
      this.insertDialogVisible = false
    },
    // 删除点位
    async delNode (id) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该关键点, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消操作！')
      }

      this.nodeList.splice(id, 1)
      // 重新编排
      for (let i = 0; i < this.nodeList.length; i++) {
        this.nodeList[i].nodeSn = i
      }
      this.$message.success('关键点删除成功！')
    },
    // 返回任务模板页面
    forwardTaskModel () {
      this.$router.push('/systemtaskmodel')
    },
    // 提交任务模板
    submitMissionModel () {
      this.$refs.submitFormRef.validate(async valid => {
        if (!valid) return
        this.submitForm.nodeList = this.nodeList
        const { data: res } = await this.$http.post('system/fromtoModel', this.submitForm)
        if (res.meta.status !== 201) {
          return this.$message.error('添加模板失败！')
        }
        this.$message.success('添加模板成功！')
        this.$router.push('/systemtaskmodel')
      })
    }

    //
  }

}
</script>

<style lang="less" scoped>
#firstRow {
  display: flex;
  justify-content: space-between;
}
</style>
