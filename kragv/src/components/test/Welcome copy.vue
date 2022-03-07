<template>
  <div :class="{mobileClass:isMobile}">
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     :size='btnSize'
                     @click="showAddDialog">派发运料任务</el-button>
          <el-button type="primary"
                     :size='btnSize'
                     @click="showChargeDialog">派发充电任务</el-button>
          <el-button type="primary"
                     :size='btnSize'
                     @click="showBackFlowAreaDialog">车辆调度</el-button>
        </el-col>
        <el-col class="btnrow2">
          <span>任务单号:</span>
          <el-input class="taskIdSearchInput"
                    clearable
                    placeholder="请输入任务单号"
                    prefix-icon="el-icon-search"
                    @input="taskIdSearchChanged"
                    v-model="taskIdSearch"> </el-input>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="taskStateListPaging"
                border
                highlight-current-row
                :height="tableHeight"
                @current-change="handleCurrentRowChange"
                @sort-change="sortChange">
        <el-table-column label="车号"
                         sortable="custom"
                         prop="AgvId"></el-table-column>
        <el-table-column label="工作区域"
                         sortable="custom"
                         prop="Area"></el-table-column>
        <el-table-column label="任务单号"
                         sortable="custom"
                         prop="TaskId"></el-table-column>
        <el-table-column label="站点清单">
          <template slot-scope="scope">
            {{ scope.row.MarkList ? scope.row.MarkList.join(' , ') : scope.row.MarkList }}
          </template>
        </el-table-column>
        <el-table-column label="站点序号">
          <template slot-scope="scope">
            {{ scope.row.MarkIndex ? scope.row.MarkIndex.join(' , ') : scope.row.MarkIndex }}
          </template>
        </el-table-column>
        <el-table-column label="动作清单">
          <template slot-scope="scope">
            {{ scope.row.ActionList ? scope.row.ActionList.join(' , ') : scope.row.ActionList }}
          </template>
        </el-table-column>
        <el-table-column label="站点时间">
          <template slot-scope="scope">
            {{ scope.row.MarkTime ? scope.row.MarkTime.join(' ，') : scope.row.MarkTime }}
          </template>
        </el-table-column>
        <el-table-column label="任务状态"
                         sortable="custom"
                         prop="TaskStatus"></el-table-column>
        <el-table-column label="挂单时间"
                         sortable="custom"
                         prop="StartTime"></el-table-column>
        <el-table-column label="派发时间"
                         sortable="custom"
                         prop="Task_BeginTime"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="80px"
                         :fixed="delColFix">
          <template slot-scope="scope">
            <el-button type="danger"
                       size="mini"
                       @click="removeById(scope.row.TaskId)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="pagenum"
                     :page-sizes="[10, 20, 50, 100]"
                     :page-size="pagesize"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total"
                     v-if="!isMobile"></el-pagination>

      <!-- 移动端分页 -->
      <el-pagination layout="prev, pager, next"
                     :total="total"
                     small
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     v-if="isMobile">
      </el-pagination>

    </el-card>

    <!-- 新建任务的对话框 -->
    <el-dialog title="派发任务"
               :visible.sync="addDialogVisible"
               :width="handleWidth(30)"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="60px">
        <el-form-item label="区域"
                      prop="SelectTaskOrderArea">
          <el-select v-model="addForm.SelectTaskOrderArea"
                     class="addDialogSelect"
                     filterable
                     @change="taskOrderAreaSelectChanged"
                     placeholder="请选择">
            <el-option v-for="item in taskOrderAreaList"
                       :key="item"
                       :label="item"
                       :value="item"> </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="路线"
                      prop="SelectTaskOrderById">
          <el-select v-model="addForm.SelectTaskOrderById"
                     class="addDialogSelect"
                     filterable
                     :disabled="taskOrderSelectEnable"
                     placeholder="请选择">
            <el-option v-for="item in taskOrderList"
                       :key="item.id"
                       :label="item.TaskName"
                       :value="item.id"> </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addTask">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 充电任务的对话框 -->
    <el-dialog title="派发充电任务"
               :visible.sync="chargeDialogVisible"
               :width="handleWidth(30)"
               @close="chargeDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="chargeFormRef"
               :model="chargeForm"
               :rules="chargeFormRules"
               label-width="70px">
        <el-form-item label="AGV"
                      prop="SelectAgvstateAgv">
          <el-select v-model="chargeForm.SelectAgvstateAgv"
                     class="chargeDialogSelect"
                     filterable
                     @change="agvChargeSelectChanged"
                     placeholder="请选择">
            <el-option v-for="item in agvChargeList"
                       :key="item"
                       :label="item"
                       :value="item"> </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="充电桩"
                      prop="SelectChargeOrderByArea">
          <el-select v-model="chargeForm.SelectChargeOrderByArea"
                     class="chargeDialogSelect"
                     filterable
                     :disabled="agvChargeSelectEnable"
                     placeholder="请选择">
            <el-option v-for="item in agvChargeAreaList"
                       :key="item.id"
                       :label="item.TaskName"
                       :value="item.id"> </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="chargeDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addChargeTask">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 车辆调度的对话框 -->
    <el-dialog title="车辆调度"
               :visible.sync="backFlowAreaDialogVisible"
               :width="handleWidth(30)"
               @close="backFlowAreaDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="backFlowAreaFormRef"
               :model="backFlowAreaForm"
               :rules="backFlowAreaFormRules"
               label-width="70px">
        <el-form-item label="AGV"
                      prop="SelectAgvId">
          <el-select v-model="backFlowAreaForm.SelectAgvId"
                     class="backFlowAreaDialogSelect"
                     filterable
                     @change="agvbackFlowAreaSelectChanged"
                     placeholder="请选择">
            <el-option v-for="item in agvbackFlowList"
                       :key="item"
                       :label="item"
                       :value="item"> </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="区域"
                      prop="SelectAgvArea">
          <el-select v-model="backFlowAreaForm.SelectAgvArea"
                     class="backFlowAreaDialogSelect"
                     filterable
                     :disabled="agvbackFlowAreaSelectEnable"
                     placeholder="请选择">
            <el-option v-for="item in agvbackFlowAreaList"
                       :key="item.id"
                       :label="item"
                       :value="item"> </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="backFlowAreaDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="backFlowAreaChange">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // 任务状态列表
      taskStateList: [],
      // 任务状态列表分页
      taskStateListPaging: [],
      // 处理后要显示的数据
      taskStateListCopy: [],
      // 列表总数
      total: 0,
      // 任务区域
      taskOrderAreaList: [],
      // 任务路线选择框启用状态
      taskOrderSelectEnable: true,
      // 添加表单的显示与隐藏
      addDialogVisible: false,
      // 任务路线
      taskOrderList: [],
      // 添加表单的验证规则对象
      addFormRules: {
        SelectTaskOrderArea: [{ required: true, message: '请输选择任务区域', trigger: 'change' }],
        SelectTaskOrderById: [{ required: true, message: '请输选择任务路线', trigger: 'change' }]
      },
      // 添加表单的表单数据
      addForm: {
        SelectTaskOrderArea: '',
        SelectTaskOrderById: ''
      },

      // 需要充电的AGV
      agvChargeList: [],
      // agv充电区域选择框启用状态
      agvChargeSelectEnable: true,
      // 充电任务表单的显示与隐藏
      chargeDialogVisible: false,
      // 充电区域
      agvChargeAreaList: [],
      // 充电表单的验证规则对象
      chargeFormRules: {
        SelectAgvstateAgv: [{ required: true, message: '请输选择AGV', trigger: 'change' }],
        SelectChargeOrderByArea: [{ required: true, message: '请输选择充电桩', trigger: 'change' }]
      },
      // 充电表单的表单数据
      chargeForm: {
        SelectAgvstateAgv: '',
        SelectChargeOrderByArea: ''
      },

      // 需要车辆调度的AGV
      agvbackFlowList: [],
      // agv车辆调度区域选择框启用状态
      agvbackFlowAreaSelectEnable: true,
      // 车辆调度表单的显示与隐藏
      backFlowAreaDialogVisible: false,
      // 车辆调度区域
      agvbackFlowAreaList: [],
      // 车辆调度表单的验证规则对象
      backFlowAreaFormRules: {
        SelectAgvstateAgv: [{ required: true, message: '请输选择AGV', trigger: 'change' }],
        SelectAgvArea: [{ required: true, message: '请输选择车辆调度桩', trigger: 'change' }]
      },
      // 车辆调度表单的表单数据
      backFlowAreaForm: {
        SelectAgvId: '',
        SelectAgvArea: ''
      },

      // 页码
      pagenum: 1,
      // 分页大小
      pagesize: 10,
      // 动态搜索数据
      taskIdSearch: '',
      // 排序属性
      sortProp: '',
      // 排序命令
      sortOrder: null,
      // 计时器
      timer: null,

      // 选择的行
      currentRow: {},
      // 按钮尺寸
      btnSize: '',
      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      // 删除列固定位置
      delColFix: 'right',
      // 是否是移动端
      isMobile: false
    }
  },
  created () {
    this.getTaskStateList()
    // 定时向服务器发起请求
    this.timer = setInterval(this.getTaskStateList, 1000)
    // 处理移动端大小
    this.handleMobile()
  },
  mounted () { },
  beforeDestroy () {
    clearInterval(this.timer)
    this.timer = null
  },
  methods: {
    // 获取任务状态列表
    async getTaskStateList () {
      const receiveList = await this.$http.post('TaskStateForWeb', { params: [] })
      // console.log(receiveList)
      if (receiveList.status !== 200) {
        return this.$message.error('任务状态列表获取失败！')
      }
      const { data: res } = receiveList
      this.taskStateList = res.rows
      this.handlePaging()
    },
    // 打开添加表单
    async showAddDialog () {
      const receiveList = await this.$http.post('TaskOrderAreaListForWeb')
      if (receiveList.status !== 200) {
        return this.$message.error('任务区域获取失败！')
      }
      const { data: res } = receiveList
      this.taskOrderAreaList = res
      this.addDialogVisible = true
    },
    // 区域选择框，选项发生变化的时候触发
    async taskOrderAreaSelectChanged () {
      const agvSelectLen = this.addForm.SelectTaskOrderArea.length
      if (agvSelectLen === 0) {
        this.addForm.SelectTaskOrderById = ''
        return (this.taskOrderSelectEnable = true)
      }
      this.taskOrderSelectEnable = false
      this.addForm.SelectTaskOrderById = ''
      const receiveList = await this.$http({
        url: 'TaskOrderByAreaForWeb',
        method: 'post',
        headers: {
          'Content-Type': 'application/text;charset=UTF-8;'
        },
        data: this.addForm.SelectTaskOrderArea
      })
      if (receiveList.status !== 200) {
        return this.$message.error('任务路线获取失败！')
      }
      const { data: res } = receiveList
      this.taskOrderList = res
    },
    // 添加任务
    addTask () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const receiveList = await this.$http.get('TaskOrderUpdateForWeb', { params: this.addForm })
        if (receiveList.status !== 200) {
          return this.$message.error('任务派发失败！')
        }
        this.getTaskStateList()
        this.$message.success('任务派发成功！')
        this.addDialogVisible = false
      })
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.taskOrderSelectEnable = true
      this.$refs.addFormRef.resetFields()
    },

    // 打开充电表单
    async showChargeDialog () {
      const receiveList = await this.$http.post('AgvstateByAgvForWeb')
      if (receiveList.status !== 200) {
        return this.$message.error('AGV清单获取失败！')
      }
      const { data: res } = receiveList
      this.agvChargeList = res
      this.chargeDialogVisible = true
    },
    // AGV选择框，选项发生变化的时候触发
    async agvChargeSelectChanged () {
      const agvSelectLen = this.chargeForm.SelectAgvstateAgv.length
      if (agvSelectLen === 0) {
        this.chargeForm.SelectChargeOrderByArea = ''
        return (this.agvChargeSelectEnable = true)
      }
      this.agvChargeSelectEnable = false
      this.chargeForm.SelectChargeOrderByArea = ''
      const receiveList = await this.$http({
        url: 'ChargeOrderByAreaForWeb',
        method: 'post',
        headers: {
          'Content-Type': 'application/text;charset=UTF-8;'
        },
        data: this.chargeForm.SelectAgvstateAgv
      })
      if (receiveList.status !== 200) {
        return this.$message.error('充电桩清单获取失败！')
      }
      const { data: res } = receiveList
      this.agvChargeAreaList = res
    },
    // 添加充电任务
    addChargeTask () {
      this.$refs.chargeFormRef.validate(async valid => {
        if (!valid) return
        const receiveList = await this.$http.get('ChargeOrderUpdateForWeb', { params: this.chargeForm })
        if (receiveList.status !== 200) {
          return this.$message.error('充电任务派发失败！')
        }
        this.getTaskStateList()
        this.$message.success('充电任务派发成功！')
        this.chargeDialogVisible = false
      })
    },
    // 监听充电对话框的关闭事件
    chargeDialogClosed () {
      this.agvChargeSelectEnable = true
      this.$refs.chargeFormRef.resetFields()
    },

    // 显示车辆调度对话框
    async showBackFlowAreaDialog () {
      const receiveList = await this.$http.post('AgvstateByAgvForWeb')
      if (receiveList.status !== 200) {
        return this.$message.error('AGV清单获取失败！')
      }
      const { data: res } = receiveList
      this.agvbackFlowList = res
      this.backFlowAreaDialogVisible = true
    },
    // AGV车辆调度选择框，选项发生变化的时候触发
    async agvbackFlowAreaSelectChanged () {
      const agvSelectLen = this.backFlowAreaForm.SelectAgvId.length
      if (agvSelectLen === 0) {
        this.backFlowAreaForm.SelectAgvArea = ''
        return (this.agvbackFlowAreaSelectEnable = true)
      }
      this.agvbackFlowAreaSelectEnable = false
      this.backFlowAreaForm.SelectAgvArea = ''
      const receiveList = await this.$http({
        url: 'TaskOrderAreaListForWeb',
        method: 'post',
        headers: {
          'Content-Type': 'application/text;charset=UTF-8;'
        }
        // data: this.chargeForm.SelectAgvstateAgv
      })
      if (receiveList.status !== 200) {
        return this.$message.error('区域清单获取失败！')
      }
      const { data: res } = receiveList
      this.agvbackFlowAreaList = res
    },
    // 车辆调度
    backFlowAreaChange () {
      this.$refs.backFlowAreaFormRef.validate(async valid => {
        if (!valid) return
        const receiveList = await this.$http.get('ChangeAgvAreaUpdateForWeb', { params: this.backFlowAreaForm })
        if (receiveList.status !== 200) {
          return this.$message.error('车辆调度失败！')
        }
        this.getTaskStateList()
        this.$message.success('车辆调度成功！')
        this.backFlowAreaDialogVisible = false
      })
    },
    // 监听车辆调度对话框的关闭事件
    backFlowAreaDialogClosed () {
      this.agvbackFlowAreaSelectEnable = true
      this.$refs.backFlowAreaFormRef.resetFields()
    },

    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.pagesize = newSize
      this.handlePaging()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.pagenum = newPage
      this.handlePaging()
    },
    // 分页处理
    handlePaging () {
      const pagenum = this.pagenum
      const pagesize = this.pagesize
      const startIndex = (pagenum - 1) * pagesize
      const endIndex = pagenum * pagesize
      this.handleSort()
      const filterResult = this.taskStateListCopy.filter(x => x.TaskId.indexOf(this.taskIdSearch) !== -1)
      this.total = filterResult.length
      this.taskStateListPaging = filterResult.slice(startIndex, endIndex)
    },
    // 搜索框内容改变触发
    taskIdSearchChanged () {
      this.pagenum = 1
      this.handlePaging()
    },
    // 排序处理函数
    handleSort () {
      const prop = this.sortProp
      const order = this.sortOrder
      this.taskStateListCopy = JSON.parse(JSON.stringify(this.taskStateList))
      if (order == 'descending' && prop !== '') {
        // this.taskStateListCopy.sort((a, b) => new Date(b[prop]) - new Date(a[prop]))
        this.taskStateListCopy.sort((a, b) => this.sortByProp(a[prop], b[prop]))
      } else if (order == 'ascending' && prop !== '') {
        this.taskStateListCopy.sort((a, b) => this.sortByProp(b[prop], a[prop]))
      }
    },
    sortByProp (arg1, arg2) {
      if (arg1 > arg2) {
        return -1
      } else if (arg1 < arg2) {
        return 1
      } else {
        return 0
      }
    },
    // 排序条件发生变化触发
    sortChange (column, prop, order) {
      // console.log(column)
      // console.log(prop)
      // console.log(order)
      this.pagenum = 1
      this.sortProp = column.prop
      this.sortOrder = column.order
      this.handlePaging()
    },

    // 表格选择行时的处理函数
    handleCurrentRowChange (val) {
      this.currentRow = val
    },

    //
    // 根据id，删除对应的用户信息
    async removeById (id) {
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该条任务, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: this.isMobile
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      // const { data: res } = await this.$http.get('DelectMissionFormWeb', sendData)

      const { data: res } = await this.$http({
        url: 'DelectMissionFormWeb',
        method: 'post',
        headers: {
          'Content-Type': 'application/text;charset=UTF-8;'
        },
        data: id
      })

      if (res === 'No') {
        return this.$message.error('任务执行中无法删除！')
      }

      this.$message.success('删除任务成功！')
      this.getTaskStateList()
    },
    // 分辨率改变时，处理控件的宽度
    handleWidth (width) {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        return screenWidth * 0.8 + 'px'
      } else {
        return width + '%'
      }
    },
    // 使用移动端的处理函数
    handleMobile () {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        this.btnSize = 'mini'
        this.delColFix = false
        this.isMobile = true
      }
    }

    //
    //
  },
  computed: {}
}
</script>

<style lang="less" scoped>
.taskIdSearchInput {
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
