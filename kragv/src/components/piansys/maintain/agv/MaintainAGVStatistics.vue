<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>运行维护</el-breadcrumb-item>
      <el-breadcrumb-item>任务类</el-breadcrumb-item>
      <el-breadcrumb-item>统计</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!--开始时间-->
    <!-- <el-card id="timecard"
             style="background:#424242;">
      <div>
        <span>
          周期开始时间：Tue Jul 14 2020 13:55:30
        </span>

      </div>
    </el-card> -->

    <!-- 卡片视图区 -->
    <el-row :gutter="20">
      <!-- 任务总数 -->
      <el-col :span="6">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#409EFF;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-monitor"></i>
            </div>
            <div class="panelfont">
              <div class="panelfontnum">{{receiveData.agvWokrhoursBlock.agvWorkhours}}</div>
              <div class="panelfontstatus">车辆总工时</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <!-- 任务完成数 -->
      <el-col :span="6">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#34bfa3;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-circle-check"></i>
            </div>
            <div class="panelfont">
              <div class="panelfontnum">{{receiveData.agvWokrhoursBlock.agvEffectiveWorkhours}}</div>
              <div class="panelfontstatus">车辆有效工时</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <!-- 任务达成率 -->
      <el-col :span="6">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:rgb(179, 127, 235);">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-pie-chart"></i>
            </div>
            <div class="panelfont">
              <div class="panelfontnum">{{receiveData.agvWokrhoursBlock.agvWorkhoursRate}}</div>
              <div class="panelfontstatus">车辆稼动率</div>
            </div>
          </div>
        </el-card>
      </el-col>

      <!-- 周期开始时间 -->
      <el-col :span="6">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#424242;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-time"></i>
            </div>
            <div class="panelfont">
              <div class="panelfontnum"
                   id="timecard">{{receiveData.agvWokrhoursBlock.calTimestamp | dateFormat_date}}</div>
              <div class="panelfontnum"
                   id="timecard">{{receiveData.agvWokrhoursBlock.calTimestamp | dateFormat_time}}</div>
              <div class="panelfontstatus">统计开始时间</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 统计区 -->
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card>
          <div slot="header"
               class="clearfix">
            <span>统计</span>
          </div>
          <!-- 2.为ECharts准备一个具备大小（宽高）的Dom -->
          <div id="main1"
               style="width: 25vw;height:400px;"></div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <div slot="header"
               class="clearfix">
            <span>统计</span>
          </div>
          <!-- 2.为ECharts准备一个具备大小（宽高）的Dom -->
          <div id="main2"
               style="width: 25vw;height:400px;"></div>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <div slot="header"
               class="clearfix">
            <span>统计</span>
          </div>
          <!-- 2.为ECharts准备一个具备大小（宽高）的Dom -->
          <div id="main3"
               style="width: 25vw;height:400px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 错误任务明细表 -->
    <el-card>
      <div slot="header"
           class="clearfix">
        <span>错误任务明细表</span>
      </div>

      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     icon="el-icon-printer">导出</el-button>
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
      <el-table :data="tasklist"
                border
                highlight-current-row
                height="500"
                @current-change="handleCurrentChange"
                @expand-change="expandSelect"
                :row-key="getRowKeys"
                :expand-row-keys="expands">
        <el-table-column type="expand"
                         label="任务进度">
          <template slot-scope="scope"
                    style="left:20%">
            <el-form label-position="left"
                     inline
                     class="demo-table-expand">
              <el-form-item :label="scope.row.missionId + ' - 任务进度'">
                <span>
                  <!-- <div style="height: 300px;"> -->
                  <div style="">
                    <el-steps direction="vertical"
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
                     :page-sizes="[1, 2, 5, 10]"
                     :page-size="queryInfo.pagesize"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total"></el-pagination>
    </el-card>

    <!-- 筛选表单 -->
    <el-dialog title="添加筛选"
               :visible.sync="filterDialogVisible"
               width="50%"
               @close="filterDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="filterFormRef"
               :model="filterForm"
               :rules="filterFormRules"
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
                       value="0"></el-option>
            <el-option label="接受"
                       value="1"></el-option>
            <el-option label="拒绝"
                       value="2"></el-option>
            <el-option label="启动"
                       value="3"></el-option>
            <el-option label="终结"
                       value="4"></el-option>
            <el-option label="取消"
                       value="5"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="任务调度状态"
                      prop="schedulerState">
          <el-select v-model="filterForm.schedulerState"
                     placeholder="请选择"
                     clearable>
            <el-option label="任务绑定到车体"
                       value="0"></el-option>
            <el-option label="没有就绪车体"
                       value="1"></el-option>
            <el-option label="车体无法到达起始点"
                       value="2"></el-option>
            <el-option label="任务没有可匹配的车体类型"
                       value="3"></el-option>
            <el-option label="任务关联车体不可用"
                       value="4"></el-option>
            <el-option label="任务截止时刻不符"
                       value="5"></el-option>
            <el-option label="任务优先级不符"
                       value="6"></el-option>
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
            <el-option label="一级"
                       value="1"></el-option>
            <el-option label="二级"
                       value="2"></el-option>
            <el-option label="三级"
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
                       value="1"></el-option>
            <el-option label="装载中"
                       value="2"></el-option>
            <el-option label="卸载"
                       value="3"></el-option>
            <el-option label="撤销"
                       value="4"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否负载"
                      prop="isLoaded">
          <el-select v-model="filterForm.isLoaded"
                     placeholder="请选择"
                     clearable>
            <el-option label="是"
                       value="true"></el-option>
            <el-option label="否"
                       value="false"></el-option>
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
                          :default-time="['12:00:00', '08:00:00']">
          </el-date-picker>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="filterDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="filterDialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import echarts from 'echarts'

export default {
  data () {
    return {
      // 获取用户列表的参数
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      },
      // 请求数据集
      receiveData: {
        agvWokrhoursBlock: {
          agvWorkhours: 0,
          agvEffectiveWorkhours: 0,
          agvWorkhoursRate: 0,
          calTimestamp: 0
        }

      },

      tasklist: [
        { missionId: 1, role_name: '金克拉' },
        { missionId: 2, role_name: '金克拉' },
        { missionId: 3, role_name: '金克拉' },
        { missionId: 4, role_name: '金克拉' },
        { missionId: 5, role_name: '金克拉' },
        { missionId: 6, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' },
        { missionId: 1, role_name: '金克拉' }
      ],
      total: 0,
      // 任务编号选择
      taskSelect: '0',
      // 筛选框显示与隐藏
      filterDialogVisible: false,
      // 筛选数据
      filterForm: {},
      // 统计图数据
      option: {
        xAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line'
          }
        ]
      },
      //
      // 选择的行
      currentRow: null,
      selectedMissionId: '',
      // 展开行的 key 值
      expands: [],
      // 返回每行的key
      getRowKeys (row) {
        return row.missionId
      },
      // test时间
      value3: '',
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
      }
      //

      //
      //
    }
  },
  created () {
    this.getStatisticsList()
  },
  mounted () {
    // 3.基于准备好的dom，初始化echarts实例
    var myChart1 = echarts.init(document.getElementById('main1'))
    var myChart2 = echarts.init(document.getElementById('main2'))
    var myChart3 = echarts.init(document.getElementById('main3'))

    // const { data: res } = await this.$http.get('reports/type/1')

    // if (res.meta.status !== 200) {
    //   return this.$message.error('获取折线图数据失败！')
    // }

    // // 4.准备数据和配置项
    // const result = _.merge(res.data, this.options)

    // 5.展示数据
    myChart1.setOption(this.option)
    myChart2.setOption(this.option)
    myChart3.setOption(this.option)
  },
  methods: {
    // 接收统计数据
    async getStatisticsList () {
      const { data: res } = await this.$http.get('maintain/agvstatistics', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('统计数据获取失败！')
      }
      this.receiveData = res.data
      this.total = res.data.total
    },

    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getUserList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getUserList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getUserList()
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 表格选择行时的处理函数
    handleCurrentChange (val) {
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
    },
    // // test 刷数据
    // setList () {
    //   this.tasklist = [
    //     { missionId: 1, role_name: '金克拉' },
    //     { missionId: 2, role_name: '56789' },
    //     { missionId: 3, role_name: '金克拉' },
    //     { missionId: 4, role_name: '金克拉' },
    //     { missionId: 5, role_name: '金克拉' }
    //   ]
    // },
    // 清除筛选项
    cleanFilter () {
      // this.$refs.filterFormRef.resetFields()
      this.filterForm = {}
      return this.$message.success('清除成功')
    }
  }
}
</script>

<style lang="less" scoped>
#timecard {
  text-align: center;
  font-size: 20px;
  font-weight: 700;
  color: #eee;
}

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

.panelcontent {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.panelcontent,
.panelicon {
  font-size: 40px;
  font-weight: 700;
  color: #eee;
}

.panelcontent,
.panelfont {
  font-size: 40px;
  font-weight: 700;
  color: #666;
}

.parampanel {
  // border-radius: 5%;
  body-style {
    padding: '100px';
  }
}

.panelfontnum {
  font-size: 40px;
  font-weight: 700;
  color: #eee;
}

.panelfontstatus {
  font-size: 10px;
  font-weight: 700;
  color: #eee;
  text-align: center;
}
</style>
