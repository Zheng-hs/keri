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
                     @click="addNullDialogVisible = true">添加非凡点</el-button>
          <el-button type="primary"
                     @click="insertNullDialogVisible = true">插入非凡点</el-button>
          <el-button type="primary"
                     @click="submitMissionModel">提交</el-button>
        </el-col>
        <el-col class="btnrow2">
          <el-button type="primary"
                     @click="addTaskModelDialogVisible= true">保存</el-button>
          <el-button type="primary"
                     @click="forwardTaskModel">清空</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="nodeList"
                border
                stripe
                height="500">
        <el-table-column label="编号"
                         prop="id"></el-table-column>
        <el-table-column label="点位"
                         prop="From"></el-table-column>
        <el-table-column label="动作"
                         prop="action">
          <template slot-scope="scope">
            <template v-if="scope.row.action == 'Get'">上料</template>
            <template v-else-if="scope.row.action == 'Put'">下料</template>
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

        <el-table-column label="货架类型"
                         prop="Transfer_Obj_ID">
          <template slot-scope="scope">
            <template v-if="scope.row.Transfer_Obj_ID == 'Rack'">普通货架</template>
            <template v-else-if="scope.row.Transfer_Obj_ID == 'Express'">快递柜</template>
          </template>
        </el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="100px">
          <template slot-scope="scope">
            <el-button type="danger"
                       size="mini"
                       @click="delNode(scope.row.id)">删除</el-button>
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
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="addForm.From"></el-input>
        </el-form-item>
        <el-form-item label="动作"
                      prop="action">
          <el-select v-model="addForm.action"
                     placeholder="请选择"
                     clearable>
            <el-option label="上料"
                       value="Get"></el-option>
            <el-option label="下料"
                       value="Put"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="方向"
                      prop="direction">
          <el-select v-model="addForm.direction"
                     placeholder="请选择"
                     clearable>
            <el-option label="左"
                       value="L"></el-option>
            <el-option label="右"
                       value="R"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="货架层数"
                      prop="shelf_num">
          <el-select v-model="addForm.shelf_num"
                     placeholder="请选择"
                     clearable>
            <el-option label="1"
                       value="1"></el-option>
            <el-option label="2"
                       value="2"></el-option>
            <el-option label="3"
                       value="3"></el-option>
            <el-option label="4"
                       value="4"></el-option>
            <el-option label="5"
                       value="5"></el-option>
            <el-option label="6"
                       value="6"></el-option>
            <el-option label="7"
                       value="7"></el-option>
            <el-option label="8"
                       value="8"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Fork层数"
                      prop="fork_num">
          <el-select v-model="addForm.fork_num"
                     placeholder="请选择"
                     clearable>
            <el-option label="1"
                       value="1"></el-option>
            <el-option label="2"
                       value="2"></el-option>
            <el-option label="3"
                       value="3"></el-option>
            <el-option label="4"
                       value="4"></el-option>
            <el-option label="5"
                       value="5"></el-option>
            <el-option label="6"
                       value="6"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="货架类型"
                      prop="Transfer_Obj_ID">
          <el-select v-model="addForm.Transfer_Obj_ID"
                     placeholder="请选择"
                     clearable>
            <el-option label="快递柜"
                       value="Express"></el-option>
            <el-option label="普通货架"
                       value="Rack"></el-option>
          </el-select>
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
        <el-form-item label="编号"
                      prop="id">
          <el-input v-model="insertForm.id"></el-input>
        </el-form-item>
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="insertForm.From"></el-input>
        </el-form-item>
        <el-form-item label="动作"
                      prop="action">
          <el-select v-model="insertForm.action"
                     placeholder="请选择"
                     clearable>
            <el-option label="上料"
                       value="Get"></el-option>
            <el-option label="下料"
                       value="Put"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="方向"
                      prop="direction">
          <el-select v-model="insertForm.direction"
                     placeholder="请选择"
                     clearable>
            <el-option label="左"
                       value="R"></el-option>
            <el-option label="右"
                       value="L"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="货架层数"
                      prop="shelf_num">
          <el-select v-model="insertForm.shelf_num"
                     placeholder="请选择"
                     clearable>
            <el-option label="1"
                       value="1"></el-option>
            <el-option label="2"
                       value="2"></el-option>
            <el-option label="3"
                       value="3"></el-option>
            <el-option label="4"
                       value="4"></el-option>
            <el-option label="5"
                       value="5"></el-option>
            <el-option label="6"
                       value="6"></el-option>
            <el-option label="7"
                       value="7"></el-option>
            <el-option label="8"
                       value="8"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Fork层数"
                      prop="fork_num">
          <el-select v-model="insertForm.fork_num"
                     placeholder="请选择"
                     clearable>
            <el-option label="1"
                       value="1"></el-option>
            <el-option label="2"
                       value="2"></el-option>
            <el-option label="3"
                       value="3"></el-option>
            <el-option label="4"
                       value="4"></el-option>
            <el-option label="5"
                       value="5"></el-option>
            <el-option label="6"
                       value="6"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="货架类型"
                      prop="Transfer_Obj_ID">
          <el-select v-model="insertForm.Transfer_Obj_ID"
                     placeholder="请选择"
                     clearable>
            <el-option label="快递柜"
                       value="Express"></el-option>
            <el-option label="普通货架"
                       value="Rack"></el-option>
          </el-select>
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

    <!-- 任务模板的对话框 -->
    <el-dialog title="添加非凡节点"
               :visible.sync="addNullDialogVisible"
               width="50%"
               @close="addNullDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addNullFormRef"
               :model="addNullForm"
               :rules="addNullFormRules"
               label-width="80px">
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="addNullForm.From"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addNullDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addNullNode">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 插入点位的对话框 -->
    <el-dialog title="插入关键点"
               :visible.sync="insertNullDialogVisible"
               width="50%"
               @close="insertNullDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="insertNullFormRef"
               :model="insertNullForm"
               :rules="insertNullFormRules"
               label-width="80px">
        <el-form-item label="编号"
                      prop="id">
          <el-input v-model="insertNullForm.id"></el-input>
        </el-form-item>
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="insertNullForm.From"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="insertNullDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="insertNullNode">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 添加任务模板的对话框 -->
    <el-dialog title="保存任务模板"
               :visible.sync="addTaskModelDialogVisible"
               width="50%"
               @close="addTaskModelDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addTaskModelFormRef"
               :model="addTaskModelForm"
               :rules="addTaskModelFormRules"
               label-width="80px">
        <el-form-item label="名称"
                      prop="taskName">
          <el-input v-model="addTaskModelForm.taskName"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addTaskModelDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addTaskModel">确 定</el-button>
      </span>
    </el-dialog>

    <!--  -->
    <!--  -->
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
          <el-input v-model="submitForm.groupName"></el-input>
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
      nodeList: [],
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加表单验证规则对象
      addFormRules: {
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      // 添加表单数据
      addForm: {},
      // 控制插入对话框的显示与隐藏
      insertDialogVisible: false,
      // 添加表单的验证规则对象
      insertFormRules: {
        id: [{ required: true, message: '请输入编号', trigger: 'blur' }],
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      // 添加插入的表单数据
      insertForm: {},

      // 控制添加对话框的显示与隐藏
      addNullDialogVisible: false,
      // 添加表单验证规则对象
      addNullFormRules: {
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }]
      },
      // 添加表单数据
      addNullForm: {},
      // 控制插入空对话框的显示与隐藏
      insertNullDialogVisible: false,
      // 添加表单的验证规则对象
      insertNullFormRules: {
        id: [{ required: true, message: '请输入编号', trigger: 'blur' }],
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }]
      },
      // 添加插入空的表单数据
      insertNullForm: {},

      // 控制添加任务模板对话框的显示与隐藏
      addTaskModelDialogVisible: false,
      // 添加任务模板表单的验证规则对象
      addTaskModelFormRules: {
        taskName: [{ required: true, message: '请输入任务模板名称', trigger: 'blur' }]
      },
      // 添加任务模板的表单数据
      addTaskModelForm: {},

      //
      //
      // 提交对话框的显示与隐藏
      submitDialogVisible: false,
      // 提交表单的验证规则对象
      submitFormRules: {
        groupName: [{ required: true, message: '请输入模板组名', trigger: 'blur' }],
        workArea: [{ required: true, message: '请输入工作区', trigger: 'blur' }]
      },
      // 提交表单数据
      submitForm: {
        AgvCommandList: [],
        AGV_ID: '',
        Dispatch_ID: '0',
        LINE_ID: 'ASRS'

      }

    }
  },
  created () { },
  methods: {
    // 添加窗口关闭,触发的函数
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 添加点位到列表
    addNode () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return

        // 深拷贝添加表单
        const p = JSON.parse(JSON.stringify(this.addForm))
        // 拿到组内编号
        p.id = this.nodeList.length
        // 添加到末尾
        this.nodeList.push(p)
        this.addDialogVisible = false
      })
    },
    // 插入窗口关闭,触发的函数
    insertDialogClosed () {
      this.$refs.insertFormRef.resetFields()
    },
    // 插入点位到列表
    insertNode () {
      this.$refs.insertFormRef.validate(async valid => {
        if (!valid) return

        const p = JSON.parse(JSON.stringify(this.insertForm))
        // 插入点位
        this.nodeList.splice(p.id, 0, p)
        // 重新编排组内编号
        for (let i = 0; i < this.nodeList.length; i++) {
          this.nodeList[i].id = i
        }
        this.insertDialogVisible = false
      })
    },

    // 添加空点位窗口关闭,触发的函数
    addNullDialogClosed () {
      this.$refs.addNullFormRef.resetFields()
    },
    // 添加点位到列表
    addNullNode () {
      this.$refs.addNullFormRef.validate(async valid => {
        if (!valid) return

        // 深拷贝添加表单
        const p = JSON.parse(JSON.stringify(this.addNullForm))
        // 拿到组内编号
        p.id = this.nodeList.length
        // 添加到末尾
        this.nodeList.push(p)
        this.addNullDialogVisible = false
      })
    },
    // 插入空点位窗口关闭,触发的函数
    insertNullDialogClosed () {
      this.$refs.insertNullFormRef.resetFields()
    },
    // 插入空点位点位到列表
    insertNullNode () {
      this.$refs.insertNullFormRef.validate(async valid => {
        if (!valid) return

        const p = JSON.parse(JSON.stringify(this.insertNullForm))
        // 插入空点位点位
        this.nodeList.splice(p.id, 0, p)
        // 重新编排组内编号
        for (let i = 0; i < this.nodeList.length; i++) {
          this.nodeList[i].id = i
        }
        this.insertNullDialogVisible = false
      })
    },

    // 添加任务模板窗口关闭,触发的函数
    addTaskModelDialogClosed () {
      this.$refs.addTaskModelFormRef.resetFields()
    },
    // 添加任务模板
    addTaskModel () {
      this.$refs.addTaskModelFormRef.validate(async valid => {
        if (!valid) return

        if (this.nodeList.length === 0) {
          return this.$message.error('任务列表不能为空')
        }

        this.submitForm.AGV_ID = this.addTaskModelForm.taskName
        this.submitForm.Dispatch_ID = (new Date()).getTime()
        this.submitForm.AgvCommandList = []

        this.nodeList.forEach(node => {
          const agvAct = {}
          agvAct.CARRIER_ID = node.action + '_' + node.direction + '_0' + node.shelf_num + '_0' + node.fork_num
          agvAct.Destination = ''
          agvAct.From = node.From
          agvAct.MTRL_ID = ''
          agvAct.SETTING_CODE = ''
          agvAct.SLOT_CNT = ''
          agvAct.Sequence = '1'
          agvAct.Transfer_Obj_ID = node.Transfer_Obj_ID + ''
          this.submitForm.AgvCommandList.push(agvAct)
        })

        const { data: res } = await this.$http.post('/taskorderlist', this.submitForm)
        if (res.meta.status !== 200) {
          return this.$message.error('添加失败！')
        }
        this.$message.success(res.meta.msg)

        this.addTaskModelDialogVisible = false
      })
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
        this.nodeList[i].id = i
      }
      this.$message.success('关键点删除成功！')
    },
    // 返回任务模板页面
    forwardTaskModel () {
      this.nodeList = []
      this.$message.success('打卡下班')
    },
    // 提交任务模板
    async submitMissionModel () {
      if (this.nodeList.length === 0) {
        return this.$message.error('任务列表不能为空')
      }

      this.submitForm.Dispatch_ID = (new Date()).getTime()
      this.submitForm.AgvCommandList = []

      this.nodeList.forEach(node => {
        const agvAct = {}
        agvAct.CARRIER_ID = node.action + '_' + node.direction + '_0' + node.shelf_num + '_0' + node.fork_num
        agvAct.Destination = ''
        agvAct.From = node.From
        agvAct.MTRL_ID = ''
        agvAct.SETTING_CODE = ''
        agvAct.SLOT_CNT = ''
        agvAct.Sequence = '1'
        agvAct.Transfer_Obj_ID = node.Transfer_Obj_ID + ''
        this.submitForm.AgvCommandList.push(agvAct)
      })

      const { data: res } = await this.$http.post('/QrAgvCommandInfo', this.submitForm)
      if (res.Return_Code !== '1') {
        return this.$message.error('添加失败！')
      }
      this.$message.success('添加成功！')
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
