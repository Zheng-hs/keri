<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>运行维护</el-breadcrumb-item>
      <el-breadcrumb-item>任务类</el-breadcrumb-item>
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
                     @click="cleanFilter">清除筛选条件</el-button>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="tasklist.maintainmissionhistory"
                border
                highlight-current-row
                height="500"
                @current-change="handleCurrentRowChange"
                @expand-change="expandSelect"
                :row-key="getRowKeys"
                :expand-row-keys="expands">
        <el-table-column type="expand"
                         label="任务进度">
          <template slot-scope="scope">
            <el-form label-position="left"
                     inline
                     class="demo-table-expand"
                     style="padding-left:50px">
              <el-form-item :label="scope.row.missionId + ' - 任务进度'">
                <span>
                  <!-- <div style="height: 300px;"> -->
                  <div style="">
                    <el-steps direction="vertical"
                              finish-status="success"
                              :active="scope.row.missionProcess">
                      <el-step v-for="(item, i) in scope.row.missionMilestoneList"
                               :key="i"
                               :title="item.title"
                               :description="item.description"></el-step>
                    </el-steps>
                  </div>
                </span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="任务编号"
                         prop="missionId"
                         fixed></el-table-column>
        <el-table-column label="开始时刻"
                         prop="startTime"></el-table-column>
        <el-table-column label="结束时刻"
                         prop="endTime"></el-table-column>
        <el-table-column label="导航状态"
                         prop="navigationState"></el-table-column>
        <el-table-column label="任务调度状态"
                         prop="schedulerState"></el-table-column>
        <el-table-column label="任务组ID"
                         prop="missionGroupId"></el-table-column>
        <el-table-column label="任务优先级"
                         prop="priority"></el-table-column>
        <el-table-column label="任务绑定车辆"
                         prop="assigneTo"></el-table-column>
        <el-table-column label="负载状态"
                         prop="payloadStatus"></el-table-column>
        <el-table-column label="是否负载"
                         prop="isLoaded"></el-table-column>
        <el-table-column label="装载货物名称"
                         prop="payload"></el-table-column>
        <el-table-column label="创建者"
                         prop="creater"></el-table-column>
        <el-table-column label="业务分类"
                         prop="businessType"></el-table-column>
        <el-table-column label="工作区"
                         prop="workArea"></el-table-column>
        <el-table-column label="最近状态变更时间"
                         prop="missionTimestamp"></el-table-column>
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
               label-width="130px"
               fixed>
        <el-form-item label="任务编号"
                      prop="missionId">
          <el-input v-model="filterForm.missionId"></el-input>
        </el-form-item>
        <el-form-item label="开始时刻"
                      prop="startTime">
          <el-date-picker v-model="filterForm.startTime"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          type="datetime"
                          placeholder="选择日期时间"
                          align="right"
                          :picker-options="pickerOptions"> </el-date-picker>
        </el-form-item>
        <el-form-item label="结束时刻"
                      prop="endTime">
          <el-date-picker v-model="filterForm.endTime"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          type="datetime"
                          placeholder="选择日期时间"
                          align="right"
                          :picker-options="pickerOptions"> </el-date-picker>
        </el-form-item>
        <el-form-item label="导航状态"
                      prop="navigationState">
          <el-select v-model="filterForm.navigationState"
                     placeholder="请选择"
                     clearable>
            <el-option label="收到"
                       value="收到"></el-option>
            <el-option label="接受"
                       value="接受"></el-option>
            <el-option label="拒绝"
                       value="拒绝"></el-option>
            <el-option label="启动"
                       value="启动"></el-option>
            <el-option label="终结"
                       value="终结"></el-option>
            <el-option label="取消"
                       value="取消"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务调度状态"
                      prop="schedulerState">
          <el-select v-model="filterForm.schedulerState"
                     placeholder="请选择"
                     clearable>
            <el-option label="任务绑定到车体"
                       value="任务绑定到车体"></el-option>
            <el-option label="没有就绪车体"
                       value="没有就绪车体"></el-option>
            <el-option label="车体无法到达起始点"
                       value="车体无法到达起始点"></el-option>
            <el-option label="任务没有可匹配的车体类型"
                       value="任务没有可匹配的车体类型"></el-option>
            <el-option label="任务关联车体不可用"
                       value="任务关联车体不可用"></el-option>
            <el-option label="任务截止时刻不符"
                       value="任务截止时刻不符"></el-option>
            <el-option label="任务优先级不符"
                       value="任务优先级不符"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务组ID"
                      prop="missionGroupId">
          <el-input v-model="filterForm.missionGroupId"></el-input>
        </el-form-item>
        <el-form-item label="任务优先级"
                      prop="priority">
          <el-select v-model="filterForm.priority"
                     placeholder="请选择"
                     clearable>
            <el-option label="1"
                       value="1"></el-option>
            <el-option label="2"
                       value="2"></el-option>
            <el-option label="3"
                       value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务绑定车辆"
                      prop="assigneTo">
          <el-input v-model="filterForm.assigneTo"></el-input>
        </el-form-item>
        <el-form-item label="负载状态"
                      prop="payloadStatus">
          <el-select v-model="filterForm.payloadStatus"
                     placeholder="请选择"
                     clearable>
            <el-option label="等待装载"
                       value="等待装载"></el-option>
            <el-option label="装载中"
                       value="装载中"></el-option>
            <el-option label="卸载"
                       value="卸载"></el-option>
            <el-option label="撤销"
                       value="撤销"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否负载"
                      prop="isLoaded">
          <el-select v-model="filterForm.isLoaded"
                     placeholder="请选择"
                     clearable>
            <el-option label="是"
                       value="是"></el-option>
            <el-option label="否"
                       value="否"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="装载货物名称"
                      prop="payload">
          <el-input v-model="filterForm.payload"></el-input>
        </el-form-item>
        <el-form-item label="创建者"
                      prop="creater">
          <el-input v-model="filterForm.creater"></el-input>
        </el-form-item>
        <el-form-item label="业务分类"
                      prop="businessType">
          <el-input v-model="filterForm.businessType"></el-input>
        </el-form-item>
        <el-form-item label="工作区"
                      prop="workArea">
          <el-input v-model="filterForm.creater"></el-input>
        </el-form-item>
        <el-form-item label="最近状态变更时间"
                      prop="missionTimestampStart">
          <el-date-picker v-model="filterForm.missionTimestampStart"
                          value-format="yyyy-MM-dd HH:mm:ss"
                          type="datetimerange"
                          align="right"
                          start-placeholder="开始日期"
                          end-placeholder="结束日期"
                          :default-time="['12:00:00', '08:00:00']"
                          :picker-options="pickerOptions2">
          </el-date-picker>
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
      // 任务列表
      tasklist: [],
      // 列表总数
      total: 0,
      // 筛选框显示与隐藏
      filterDialogVisible: false,
      // 筛选数据
      filterForm: {},

      // 选择的行
      currentRow: {},
      // 选择行的任务id
      selectedMissionId: '',
      // 展开行的 key 值
      expands: [],
      // 返回每行的key
      getRowKeys (row) {
        return row.missionId
      },

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
    this.getHistoryTaskList()
  },
  mounted () {

  },
  beforeDestroy () {
  },
  methods: {
    // 获取任务监视列表
    async getHistoryTaskList () {
      const { data: res } = await this.$http.get('maintain/mission/history', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('任务历史列表获取失败！')
      }
      this.tasklist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getHistoryTaskList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getHistoryTaskList()
    },
    // 过滤数据
    getFilter () {
      this.queryInfo.query = this.filterForm
      this.getHistoryTaskList()
      this.filterDialogVisible = false
    },
    // 清除筛选项
    cleanFilter () {
      // 这条会卡死
      // this.$refs.filterFormRef.resetFields()
      this.filterForm = {}
      this.getFilter()
      return this.$message.success('清除成功')
    },
    // 表格选择行时的处理函数
    handleCurrentRowChange (val) {
      this.currentRow = val
      this.selectedMissionId = val.missionId
    },
    // 折叠面板每次只能展开一行
    expandSelect (row, expandedRows) {
      // row 当前行详细信息
      // expandedRows 已展开行的详细信息
      var that = this
      if (expandedRows.length) {
        that.expands = []
        if (row) {
          that.expands.push(row.missionId)
        }
      } else {
        that.expands = []
      }
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
