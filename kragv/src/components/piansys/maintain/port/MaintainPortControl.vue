<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>运行维护</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>机台</el-breadcrumb-item>
      <el-breadcrumb-item>实时控制</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <span>机台名称</span>
          <span>
            <el-input placeholder="任务编号"
                      class="btnrowinput"
                      style="width:150px"
                      v-model="selectedRowId"
                      :disabled="true"
                      resize="none"> </el-input>
          </span>
          <el-button type="primary"
                     @click="portStopControl(selectedRowId)">停机</el-button>
          <el-button type="primary"
                     @click="portRestorationControl(selectedRowId)">复位</el-button>
        </el-col>
        <el-col class="btnrow2">
          <el-button type="primary"
                     icon="el-icon-search"
                     @click="filterDialogVisible = true">筛选</el-button>
          <el-button type="primary"
                     icon="el-icon-circle-close-outline"
                     @click="clearFilter">清除筛选条件</el-button>
        </el-col>
      </el-row>

      <!-- 列表 -->
      <el-table :data="portlist.portlist"
                border
                highlight-current-row
                height="500"
                @current-change="handleCurrentRowChange">
        <el-table-column label="设备名称"
                         prop="eqName"
                         fixed></el-table-column>
        <el-table-column label="硬件版本"
                         prop="hardwareVer"></el-table-column>
        <el-table-column label="固件版本"
                         prop="firmwareVer"></el-table-column>
        <el-table-column label="设备类型(用途）"
                         prop="eqType"></el-table-column>
        <el-table-column label="设备在线/离线"
                         prop="eqConnection"></el-table-column>
        <el-table-column label="最近通讯时间"
                         prop="eqTimestamp"></el-table-column>
        <el-table-column label="设备动作"
                         prop="eqAction"></el-table-column>
        <el-table-column label="动作流程状态"
                         prop="actionProcessInfo"></el-table-column>
        <el-table-column label="错误"
                         prop="eqErrors"></el-table-column>
        <el-table-column label="错误码"
                         prop="eqErrorCode"></el-table-column>
        <el-table-column label="任务模板名称"
                         prop="missionFromTo"></el-table-column>
        <el-table-column label="设备绑定点位"
                         prop="bindingNode"></el-table-column>
        <el-table-column label="任务编号"
                         prop="missionGroupId"></el-table-column>
        <el-table-column label="车辆名称"
                         prop="agvName"></el-table-column>
        <el-table-column label="对接车辆的状态"
                         prop="operationgState"></el-table-column>
        <el-table-column label="对接车辆的电量"
                         prop="batterySoc"></el-table-column>
        <el-table-column label="车辆动作"
                         prop="agvAction"></el-table-column>
        <el-table-column label="车辆在线/离线"
                         prop="agvConnection"></el-table-column>
        <el-table-column label="车辆错误"
                         prop="agvErrors"></el-table-column>
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

    <!-- 筛选表单 -->
    <el-dialog title="添加筛选"
               :visible.sync="filterDialogVisible"
               width="50%">
      <!-- 内容主体区 -->
      <el-form ref="filterFormRef"
               :model="filterForm"
               label-width="120px">
        <el-form-item label="设备名称"
                      prop="eqEame">
          <el-input v-model="filterForm.eqEame"></el-input>
        </el-form-item>
        <el-form-item label="硬件版本"
                      prop="hardwareVer">
          <el-input v-model="filterForm.hardwareVer"></el-input>
        </el-form-item>
        <el-form-item label="固件版本"
                      prop="firmwareVer">
          <el-input v-model="filterForm.firmwareVer"></el-input>
        </el-form-item>
        <el-form-item label="设备类型(用途）"
                      prop="eqType">
          <el-select v-model="filterForm.eqType"
                     placeholder="请选择"
                     clearable>
            <el-option label="上下料Port"
                       value="上下料Port"></el-option>
            <el-option label="电梯控制"
                       value="电梯控制"></el-option>
            <el-option label="风淋门控制"
                       value="风淋门控制"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="设备在线/离线"
                      prop="eqConnection">
          <el-select v-model="filterForm.eqConnection"
                     placeholder="请选择"
                     clearable>
            <el-option label="在线"
                       value="在线"></el-option>
            <el-option label="离线"
                       value="离线"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="最近通讯时间"
                      prop="eqTimestamp">
          <el-date-picker v-model="filterForm.eqTimestamp"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          type="datetimerange"
                          align="right"
                          start-placeholder="开始日期"
                          end-placeholder="结束日期"
                          :picker-options="pickerOptions2"
                          :default-time="['12:00:00', '08:00:00']">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="设备动作"
                      prop="eqAction">
          <el-input v-model="filterForm.eqAction"></el-input>
        </el-form-item>
        <el-form-item label="动作流程状态"
                      prop="actionProcessInfo">
          <el-input v-model="filterForm.actionProcessInfo"></el-input>
        </el-form-item>
        <el-form-item label="错误"
                      prop="eqErrors">
          <el-input v-model="filterForm.eqErrors"></el-input>
        </el-form-item>
        <el-form-item label="错误码"
                      prop="eqErrorCode">
          <el-input v-model="filterForm.eqErrorCode"></el-input>
        </el-form-item>
        <el-form-item label="任务模板名称"
                      prop="missionFromTo">
          <el-input v-model="filterForm.missionFromTo"></el-input>
        </el-form-item>
        <el-form-item label="设备绑定点位"
                      prop="bindingNode">
          <el-input v-model="filterForm.bindingNode"></el-input>
        </el-form-item>
        <el-form-item label="任务编号"
                      prop="missionGroupId">
          <el-input v-model="filterForm.missionGroupId"></el-input>
        </el-form-item>
        <el-form-item label="车辆名称"
                      prop="agvName">
          <el-input v-model="filterForm.agvName"></el-input>
        </el-form-item>
        <el-form-item label="对接车辆的状态"
                      prop="operationgState">
          <el-input v-model="filterForm.operationgState"></el-input>
        </el-form-item>
        <el-form-item label="对接车辆的电量"
                      prop="batterySoc">
          <el-input v-model="filterForm.batterySoc"></el-input>
        </el-form-item>
        <el-form-item label="车辆动作"
                      prop="agvAction">
          <el-input v-model="filterForm.agvAction"></el-input>
        </el-form-item>
        <el-form-item label="车辆在线/离线"
                      prop="agvConnection">
          <el-select v-model="filterForm.agvConnection"
                     placeholder="请选择"
                     clearable>
            <el-option label="在线"
                       value="在线"></el-option>
            <el-option label="离线"
                       value="离线"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="车辆错误"
                      prop="agvErrors">
          <el-input v-model="filterForm.agvErrors"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="filterDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="getFilter">确 定</el-button>
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
      // 机台列表
      portlist: [],
      // 列表总数
      total: 0,
      // 筛选框显示与隐藏
      filterDialogVisible: false,
      // 筛选数据
      filterForm: {},

      // 选择的行
      currentRow: {},
      // 选择行的id
      selectedRowId: '',

      // 日期选择框快捷日期
      pickerOptions: {
        shortcuts: [
          {
            text: '今天',
            onClick (picker) {
              picker.$emit('pick', new Date())
            }
          },
          {
            text: '昨天',
            onClick (picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24)
              picker.$emit('pick', date)
            }
          },
          {
            text: '一周前',
            onClick (picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
              picker.$emit('pick', date)
            }
          }
        ]
      },
      // 日期范围选择框快捷日期
      pickerOptions2: {
        shortcuts: [{
          text: '最近一周',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近一个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近三个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
            picker.$emit('pick', [start, end])
          }
        }]
      },

      // 计时器
      timer: null
    }
  },
  created () {
    // 获取机台监视列表
    this.getMonitorPortList()
    // 定时向服务器发起请求
    this.timer = setInterval(this.getMonitorPortList, 10000)
  },
  mounted () {

  },
  beforeDestroy () {
    clearInterval(this.timer)
    this.timer = null
  },
  methods: {
    // 获取机台监视列表
    async getMonitorPortList () {
      const { data: res } = await this.$http.get('monitor/port', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('AGV监视列表获取失败！')
      }
      this.portlist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getMonitorPortList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getMonitorPortList()
    },
    // 过滤数据
    getFilter () {
      this.queryInfo.query = this.filterForm
      this.getMonitorPortList()
      this.filterDialogVisible = false
    },
    // 清除筛选项
    clearFilter () {
      this.filterForm = {}
      this.getFilter()
      return this.$message.success('清除成功')
    },

    // 表格选择行时的处理函数
    handleCurrentRowChange (val) {
      this.currentRow = val
      this.selectedRowId = val.eqName
      // 有数据再启用，现在默认
      // this.carclass = val.vehicleType
      // this.carclassSrc = require(`../../assets/carimg/${this.carclass}.jpg`)
    },

    // 机台停止
    async portStopControl (id) {
      if (id === '') {
        return this.$message.info('请选择机台！')
      }
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将停止机台, 是否继续?', '提示', {
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

      const controlParams = {}
      controlParams.eqId = id
      controlParams.cmd = 'Stop'
      const { data: res } = await this.$http.post('maintain/portcontrol/', controlParams)
      if (res.meta.status !== 200) {
        this.$message.error('机台停止失败！')
      }

      this.$message.success('机台停止成功！')
      this.getMonitorPortList()
    },
    // 机台复位
    async portRestorationControl (id) {
      if (id === '') {
        return this.$message.info('请选择机台！')
      }
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将复位机台, 是否继续?', '提示', {
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

      const controlParams = {}
      controlParams.eqId = id
      controlParams.cmd = 'Reset'
      const { data: res } = await this.$http.post('maintain/portcontrol/', controlParams)
      if (res.meta.status !== 200) {
        this.$message.error('机台复位失败！')
      }

      this.$message.success('机台复位成功！')
      this.getMonitorPortList()
    }

  }
}
</script>

<style lang="less" scoped>
#firstrow {
  display: flex;
  align-items: center;

  div {
    display: flex;
    justify-content: space-between;
    align-items: center;
    span {
      padding: 5px;
    }
  }
}
</style>
