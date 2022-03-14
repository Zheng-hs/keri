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
                     @click="showBindBoxNumDialog">派发任务</el-button>
        </el-col>
        <el-col class="btnrow2">
          <el-button type="primary"
                     @click="addTaskModelDialogVisible= true">保存为模板</el-button>
          <el-button type="primary"
                     @click="clearNodeList">清空</el-button>
          <el-button type="primary"
                     @click="forwardTaskModel">返回</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="nodeList"
                border
                stripe
                :height="tableHeight">
        <el-table-column label="编号"
                         prop="id"></el-table-column>
        <el-table-column label="点位"
                         prop="From"></el-table-column>
        <el-table-column label="动作"
                         prop="action">
          <template slot-scope="scope">
            <template v-if="scope.row.action == 'G'">上料</template>
            <template v-else-if="scope.row.action == 'P'">下料</template>
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
               width="500px"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="80px"
               class="dialogForm">
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="addForm.From"></el-input>
        </el-form-item>
        <el-form-item label="有无动作"
                      prop="actionOrNot">
          <el-switch v-model="addForm.actionOrNot"
                     active-color="#13ce66"
                     inactive-color="#ff4949"
                     @change="handleActionOrNot(addForm.actionOrNot)">
          </el-switch>
        </el-form-item>
        <div v-if="addForm.actionOrNot">
          <el-form-item label="动作"
                        prop="action">
            <el-select v-model="addForm.action"
                       placeholder="请选择"
                       clearable>
              <el-option label="上料"
                         value="G"></el-option>
              <el-option label="下料"
                         value="P"></el-option>
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
            </el-select>
          </el-form-item>

        </div>

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
               width="500px"
               @close="insertDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="insertFormRef"
               :model="insertForm"
               :rules="insertFormRules"
               class="dialogForm"
               label-width="80px">
        <el-form-item label="编号"
                      prop="id">
          <el-input v-model="insertForm.id"></el-input>
        </el-form-item>
        <el-form-item label="点位"
                      prop="From">
          <el-input v-model="insertForm.From"></el-input>
        </el-form-item>
        <el-form-item label="有无动作"
                      prop="actionOrNot">
          <el-switch v-model="insertForm.actionOrNot"
                     active-color="#13ce66"
                     inactive-color="#ff4949"
                     @change="handleActionOrNot(insertForm.actionOrNot)">
          </el-switch>
        </el-form-item>
        <div v-if="insertForm.actionOrNot">
          <el-form-item label="动作"
                        prop="action">
            <el-select v-model="insertForm.action"
                       placeholder="请选择"
                       clearable>
              <el-option label="上料"
                         value="G"></el-option>
              <el-option label="下料"
                         value="P"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="方向"
                        prop="direction">
            <el-select v-model="insertForm.direction"
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
            </el-select>
          </el-form-item>

        </div>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="insertDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="insertNode">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 添加任务模板的对话框 -->
    <el-dialog title="保存任务模板"
               :visible.sync="addTaskModelDialogVisible"
               width="50%"
               @close="addTaskModelDialogClosed">
      <!-- 模板名称 & 备注 -->
      <el-form ref="addTaskModelFormRef"
               :model="addTaskModelForm"
               :rules="addTaskModelFormRules"
               label-width="80px">
        <el-form-item label="模板名称"
                      prop="taskModelName">
          <el-input v-model="addTaskModelForm.taskModelName"></el-input>
        </el-form-item>
        <el-form-item label="备注"
                      prop="remark">
          <el-input type="textarea"
                    v-model="addTaskModelForm.remark"></el-input>
        </el-form-item>
      </el-form>
      <!-- 模板名称 & 备注 -->

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
            1_(_GR21E_000000_100001)
          </el-form-item>
          <el-form-item label="流水线动作"
                        prop="action">
            <el-input type="textarea"
                      v-model="waterLineForm.action"></el-input>
          </el-form-item>
        </template>

      </el-form>
      <!-- 流水线操作 -->
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addTaskModelDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addTaskModel">确 定</el-button>
      </span>
    </el-dialog>
    <!-- 添加任务模板的对话框 -->

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
            1_(_GR21E_000000_100001)
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
      // 控制添加对话框的显示与隐藏
      addDialogVisible: false,
      // 添加表单验证规则对象
      addFormRules: {
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        waitOrNot: [{ required: true, message: '请选择是否等待', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      addFormRulesSource: {
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        waitOrNot: [{ required: true, message: '请选择是否等待', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      // 添加表单数据
      addForm: {
        From: '',
        actionOrNot: true,
        waitOrNot: '',
        action: '',
        direction: '',
        shelf_num: '',
        fork_num: '',
        Transfer_Obj_ID: '',
        boxNum: ''
      },
      // 控制插入对话框的显示与隐藏
      insertDialogVisible: false,
      // 添加表单的验证规则对象
      insertFormRules: {
        id: [{ required: true, message: '请输入编号', trigger: 'blur' }],
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        waitOrNot: [{ required: true, message: '请选择是否等待', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      insertFormRulesSource: {
        id: [{ required: true, message: '请输入编号', trigger: 'blur' }],
        From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        waitOrNot: [{ required: true, message: '请选择是否等待', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
        direction: [{ required: true, message: '请输入方向', trigger: 'blur' }],
        shelf_num: [{ required: true, message: '请输入货架层数', trigger: 'blur' }],
        fork_num: [{ required: true, message: '请输入Fork层数', trigger: 'blur' }],
        Transfer_Obj_ID: [{ required: true, message: '请输入货架类型', trigger: 'blur' }]
      },
      // 添加插入的表单数据
      insertForm: {
        id: '',
        From: '',
        actionOrNot: true,
        waitOrNot: '',
        action: '',
        direction: '',
        shelf_num: '',
        fork_num: '',
        Transfer_Obj_ID: '',
        boxNum: ''
      },
      // 控制bindBoxNum对话框的显示与隐藏
      bindBoxNumDialogVisible: false,

      // 控制添加任务模板对话框的显示与隐藏
      addTaskModelDialogVisible: false,
      // 添加任务模板表单的验证规则对象
      addTaskModelFormRules: {
        taskModelName: [{ required: true, message: '请输入任务模板名称', trigger: 'blur' }]
      },
      // 添加任务模板的表单数据
      addTaskModelForm: {
        taskModelName: '',
        remark: '',
      },

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

      //
      //
      // 提交表单数据
      submitForm: {
        dispatchId: '',
        taskModelName: '',
        actionList: [],
        markList: [],
        remark: ''
      },
      // 表格高度
      tableHeight: window.innerHeight * 0.7,


    }
  },
  computed: {

    // 
  },
  created () { },
  methods: {
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

    handleActionOrNot (actionOrNot) {
      if (actionOrNot) {
        this.addFormRules = this.addFormRulesSource
        this.insertFormRules = this.insertFormRulesSource
      } else {
        this.addFormRules = {
          From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        }
        this.insertFormRules = {
          id: [{ required: true, message: '请输入编号', trigger: 'blur' }],
          From: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        }
      }
    },
    // 校验复位
    formRulesReset () {
      this.addFormRules = this.addFormRulesSource
      this.insertFormRules = this.insertFormRulesSource
    },
    // 添加窗口关闭,触发的函数
    async addDialogClosed () {
      await this.formRulesReset()
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
    async insertDialogClosed () {
      await this.formRulesReset()
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


    // 添加任务模板窗口关闭,触发的函数
    addTaskModelDialogClosed () {
      // this.$refs.addTaskModelFormRef.resetFields()
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
        // return this.$message.info('已取消操作！')
        return this.$message({
          showClose: true,
          message: '已取消操作！',
          type: 'info'
        })
      }

      this.nodeList.splice(id, 1)
      // 重新编排
      for (let i = 0; i < this.nodeList.length; i++) {
        this.nodeList[i].id = i
      }
      // this.$message.success('关键点删除成功！')
      this.$message({
        showClose: true,
        message: '关键点删除成功！',
        type: 'success'
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
    showBindBoxNumDialog () {
      if (this.nodeList.length === 0) {
        // return this.$message.error('任务列表不能为空')
        return this.$message({
          showClose: true,
          message: '任务列表不能为空',
          type: 'error'
        })
      }
      this.bindBoxNumDialogVisible = true
    },

    // 派发任务
    async dispatchMission () {

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
    },

    // 添加任务模板
    addTaskModel () {
      this.$refs.addTaskModelFormRef.validate(async valid => {
        if (!valid) return

        if (this.nodeList.length === 0) {
          // return this.$message.error('任务列表不能为空')
          return this.$message({
            showClose: true,
            message: '任务列表不能为空',
            type: 'error'
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
        const { data: res } = await this.$http.post('/taskModelPlus', subInfo)
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

        this.addTaskModelDialogVisible = false
      })
    },

    // 清空clearNodeList
    clearNodeList () {
      this.nodeList = []
      // this.$message.success('任务列表已清空')
      this.$message({
        showClose: true,
        message: '任务列表已清空',
        type: 'success'
      })
    },
    // 返回任务模板页面
    forwardTaskModel () {
      this.$router.push('taskmodelplus')
    },

    //
  }

}
</script>

<style lang="less" scoped>
#firstRow {
  display: flex;
  justify-content: space-between;
}

.dialogForm {
  .el-select,
  .el-input {
    width: 90%;
  }
}
</style>
