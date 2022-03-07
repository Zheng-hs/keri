<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>机台</el-breadcrumb-item>
    </el-breadcrumb> -->

    <el-row :gutter="20"
            class="parampanel">
      <el-card class="headercard">
        <!-- 机台图片 -->
        <img id="carimg"
             :src="carclassSrc" />

        <el-col :span="12"
                class="parampanelside">
          <!-- 卡片视图区 -->
          <div class="parampanelsideleft">
            <el-card style="background:#34bfa3;">
              <div>设备名称 {{ currentRow.agvName }}</div>
              <div>硬件版本：{{ currentRow.hardwareVer }}</div>
              <div>固件版本：{{ currentRow.firmwareVer }}</div>
              <div>设备类型：{{ currentRow.eqType }}</div>
              <div>任务模板名称：{{ currentRow.missionFromTo }}</div>
              <div>设备绑定点位：{{ currentRow.bindingNode }}</div>
              <div>任务编号：{{ currentRow.missionGroupId }}</div>
            </el-card>

            <el-card style="background:#34bfa3;">
              <div>设备在线/离线：{{ currentRow.eqConnection }}</div>
              <div>最近通讯时间：{{ currentRow.eqTimestamp }}</div>
              <div>设备动作: {{ currentRow.eqAction }}</div>
              <div>动作流程状态: {{ currentRow.actionProcessInfo }}</div>
            </el-card>
            <!-- <el-card style="background:rgb(255, 156, 110);"><span>载货状态：载货中</span></el-card> -->
            <!-- <el-card style="background:#409EFF;"><span></span></el-card> -->
            <!-- <el-card style="background:rgb(179, 127, 235);"><span>车辆状态：任务中</span></el-card>
            <el-card style="background:rgb(179, 127, 235);"><span>最新点位：156，458</span></el-card> -->
          </div>
        </el-col>

        <el-col :span="12"
                class="parampanelside">
          <!-- 卡片视图区 -->
          <div class="parampanelsideright">
            <el-card style="background:#34bfa3;">
              <div>车辆名称：{{ currentRow.agvName }}</div>
              <div>对接车辆的状态：{{ currentRow.operationgState }}</div>
              <div>对接车辆的电量：{{ currentRow.batterySoc }}</div>
              <div>车辆动作：{{ currentRow.agvAction }}</div>
              <div>车辆在线/离线：{{ currentRow.agvConnection }}</div>
            </el-card>
            <el-card style="background:#34bfa3;">
              <div>错误: {{ currentRow.eqErrors }}</div>
              <div>错误码：{{ currentRow.eqErrorCode }}</div>
              <div>车辆错误：{{ currentRow.agvErrors }}</div>
            </el-card>
            <!-- <el-card style="background:#34bfa3;"><span>电池电压：24V</span></el-card>
            <el-card style="background:#34bfa3;"><span>电池电量：3000 mAh</span></el-card>
            <el-card style="background:#409EFF;"><span>任务进度：60%</span></el-card>
            <el-card style="background:#ffba00;"><span>错误: 暂无</span></el-card>
            <el-card style="background:#ffba00;"><span>错误码：暂无</span></el-card> -->
          </div>
        </el-col>
      </el-card>
    </el-row>

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <!-- <el-button type="primary" @click="addDialogVisible = true">添加任务</el-button> -->
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
      // 选择行车体类型
      carclass: 'agvImg1',
      // 车体图片
      carclassSrc: require('../../assets/carimg/agvImg1.jpg'),

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
    }
  }
}
</script>

<style lang="less" scoped>
.panelcardtitle {
  display: flex;
  justify-content: center;
  color: rgba(0, 0, 0, 0.45);
  font-size: 20px;
  font-weight: 700;
}

.panelcontent {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.panelcontent,
.panelicon {
  font-size: 40px;
  font-weight: 700;
  color: rgba(0, 0, 0, 0.45);
}

.panelcontent,
.panelfont {
  font-size: 15px;
  font-weight: 700;
  color: #666;
}

.headercard {
  // background-color: #eee;
  padding-top: 0%;
  padding-bottom: 3%;
}

.parampanelside {
  padding: 0px;
  padding-bottom: 0%;
  height: 100%;
  font-size: 20px;
  font-weight: 700;
  display: flex;
  flex-direction: column;
  // span {
  //   color: #fff;
  // }
  .el-card {
    height: 300px;
  }
}

.parampanelsideleft {
  text-align: left;
}

.parampanelsideright {
  text-align: right;
}

#carimg {
  width: 480px;
  height: 480px;
  // border: solid 1px #eee;
  border-radius: 50%;
  padding: 20px;
  // box-shadow: 0 0 10 #eee;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  z-index: 5;
}
</style>
