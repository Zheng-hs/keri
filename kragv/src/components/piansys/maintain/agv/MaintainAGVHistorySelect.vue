<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>运行维护</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>AGV</el-breadcrumb-item>
      <el-breadcrumb-item>历史查询</el-breadcrumb-item>
    </el-breadcrumb> -->

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
      <el-table :data="agvlist.agvlist"
                border
                highlight-current-row
                height="500"
                @current-change="handleCurrentRowChange">
        <el-table-column label="车名"
                         prop="agvName"
                         fixed></el-table-column>
        <el-table-column label="是否载货中"
                         prop="isLoad"></el-table-column>
        <el-table-column label="任务模板名称"
                         prop="misssionFromTo"></el-table-column>
        <el-table-column label="组任务编号"
                         prop="missionGroupId"></el-table-column>
        <el-table-column label="车辆状态"
                         prop="operatingState"></el-table-column>
        <el-table-column label="最近通讯时间"
                         prop="agvTimestamp"></el-table-column>
        <!-- <el-table-column label="当前任务导航点列表" prop="path"></el-table-column> -->
        <el-table-column label="车体动作"
                         prop="agvAction"></el-table-column>
        <el-table-column label="车体坐标"
                         prop="locationXYZ"></el-table-column>
        <el-table-column label="车体角度"
                         prop="locationTheta"></el-table-column>
        <!-- <el-table-column label="地图编号" prop="mapId"></el-table-column>
        <el-table-column label="地图分区编号" prop="group"></el-table-column> -->
        <el-table-column label="最新点位"
                         prop="currentNode"></el-table-column>
        <!-- <el-table-column label="任务进度" prop="role_name"></el-table-column>
        <el-table-column label="任务信息" prop="role_name"></el-table-column> -->
        <el-table-column label="连线检查"
                         prop="agvConnection"></el-table-column>
        <el-table-column label="电池电压"
                         prop="batteryVol"></el-table-column>
        <el-table-column label="电池电量"
                         prop="batterySoc"></el-table-column>
        <el-table-column label="电池最高温度"
                         prop="batteryTem"></el-table-column>
        <el-table-column label="错误"
                         prop="agvErrors"></el-table-column>
        <el-table-column label="错误码"
                         prop="agvErrorCode"></el-table-column>
        <el-table-column label="车辆类型"
                         prop="vehicleType"></el-table-column>
        <el-table-column label="车体上传信息"
                         prop="messages"></el-table-column>
        <el-table-column label="车体工作区"
                         prop="workArea"></el-table-column>
        <el-table-column label="对接设备名"
                         prop="eqName"></el-table-column>
        <el-table-column label="对接设备动作"
                         prop="eqAction"></el-table-column>
        <el-table-column label="对接设备错误"
                         prop="eqErrors"></el-table-column>
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
        <el-form-item label="车名"
                      prop="agvName">
          <el-input v-model="filterForm.agvName"></el-input>
        </el-form-item>
        <el-form-item label="是否载货中"
                      prop="isLoad">
          <el-select v-model="filterForm.isLoad"
                     placeholder="请选择"
                     clearable>
            <el-option label="是"
                       value="是"></el-option>
            <el-option label="否"
                       value="否"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务模板名称"
                      prop="misssionFromTo">
          <el-input v-model="filterForm.misssionFromTo"></el-input>
        </el-form-item>
        <el-form-item label="组任务编号"
                      prop="missionGroupId">
          <el-input v-model="filterForm.missionGroupId"></el-input>
        </el-form-item>
        <el-form-item label="车辆状态"
                      prop="operatingState">
          <el-select v-model="filterForm.operatingState"
                     placeholder="请选择"
                     clearable>
            <el-option label="未插入"
                       value="未插入"></el-option>
            <el-option label="就绪"
                       value="就绪"></el-option>
            <el-option label="任务中"
                       value="任务中"></el-option>
            <el-option label="不可用"
                       value="不可用"></el-option>
            <el-option label="暂停"
                       value="暂停"></el-option>
            <el-option label="休眠/巡游"
                       value="休眠/巡游"></el-option>
            <el-option label="错误"
                       value="错误"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="最近通讯时间"
                      prop="agvTimestamp">
          <el-date-picker v-model="filterForm.agvTimestamp"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          type="datetimerange"
                          align="right"
                          start-placeholder="开始日期"
                          end-placeholder="结束日期"
                          :picker-options="pickerOptions2"
                          :default-time="['12:00:00', '08:00:00']">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="车体动作"
                      prop="agvAction">
          <el-input v-model="filterForm.agvAction"></el-input>
        </el-form-item>
        <el-form-item label="车体坐标"
                      prop="locationXYZ">
          <el-input v-model="filterForm.locationXYZ"></el-input>
        </el-form-item>
        <el-form-item label="车体角度"
                      prop="locationTheta">
          <el-input v-model="filterForm.locationTheta"></el-input>
        </el-form-item>
        <el-form-item label="最新点位"
                      prop="currentNode">
          <el-input v-model="filterForm.currentNode"></el-input>
        </el-form-item>
        <el-form-item label="连线检查"
                      prop="agvConnection">
          <el-input v-model="filterForm.agvConnection"></el-input>
        </el-form-item>
        <el-form-item label="电池电压"
                      prop="batteryVol">
          <el-input v-model="filterForm.batteryVol"></el-input>
        </el-form-item>
        <el-form-item label="电池电量"
                      prop="batterySoc">
          <el-input v-model="filterForm.batterySoc"></el-input>
        </el-form-item>
        <el-form-item label="电池最高温度"
                      prop="batteryTem">
          <el-input v-model="filterForm.batteryTem"></el-input>
        </el-form-item>
        <el-form-item label="错误"
                      prop="agvErrors">
          <el-input v-model="filterForm.agvErrors"></el-input>
        </el-form-item>
        <el-form-item label="错误码"
                      prop="agvErrorCode">
          <el-input v-model="filterForm.agvErrorCode"></el-input>
        </el-form-item>
        <el-form-item label="车辆类型"
                      prop="vehicleType">
          <el-input v-model="filterForm.vehicleType"></el-input>
        </el-form-item>
        <el-form-item label="车体上传信息"
                      prop="messages">
          <el-input v-model="filterForm.messages"></el-input>
        </el-form-item>
        <el-form-item label="车体工作区"
                      prop="workArea">
          <el-input v-model="filterForm.workArea"></el-input>
        </el-form-item>
        <el-form-item label="对接设备名"
                      prop="eqName">
          <el-input v-model="filterForm.eqName"></el-input>
        </el-form-item>
        <el-form-item label="对接设备动作"
                      prop="eqAction">
          <el-input v-model="filterForm.eqAction"></el-input>
        </el-form-item>
        <el-form-item label="对接设备错误"
                      prop="eqErrors">
          <el-input v-model="filterForm.eqErrors"></el-input>
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
      // AGV列表
      agvlist: {},
      // agv列表总数
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
      }

      //
    }
  },
  created () {
    this.getHistoryAGVList()
  },
  mounted () {

  },
  beforeDestroy () {
  },
  methods: {
    // 获取AGV监视列表
    async getHistoryAGVList () {
      const { data: res } = await this.$http.get('maintain/agv/history', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('AGV历史列表获取失败！')
      }
      this.agvlist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getHistoryAGVList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getHistoryAGVList()
    },
    // 过滤数据
    getFilter () {
      this.queryInfo.query = this.filterForm
      this.getHistoryAGVList()
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
      this.selectedRowId = val.agvName
      // 有数据再启用，现在默认
      // this.carclass = val.vehicleType
      // this.carclassSrc = require(`../../assets/carimg/${this.carclass}.jpg`)
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
