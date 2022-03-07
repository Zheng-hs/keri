<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>实时监控</el-breadcrumb-item>
      <el-breadcrumb-item>任务类</el-breadcrumb-item>
      <el-breadcrumb-item>任务列表</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!-- 参数面板卡片视图区 -->
    <el-row :gutter="20">
      <!-- 任务总数 -->
      <el-col :span="8">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#409EFF;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-monitor"></i>
            </div>
            <div class="panelfont">
              <div class="panelfontnum">{{tasklist.missionTotalNum}}</div>
              <div class="panelfontstatus">任务总数</div>
            </div>
          </div>
        </el-card>
      </el-col>
      <!-- 进行中 -->
      <el-col :span="8">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#34bfa3;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-video-play"></i>
            </div>
            <div class="paneltwofont">
              <div class="paneltwofontnum"><span>{{missionDoingPresent}}</span> {{tasklist.missionDoing}} </div>
              <div class="paneltwofontstatus"><span>进行中</span></div>
            </div>
          </div>
        </el-card>
      </el-col>
      <!-- 未派送 -->
      <el-col :span="8">
        <el-card class="parampanel"
                 shadow="always"
                 style="background:#ffba00;">
          <div class="panelcontent">
            <div class="panelicon">
              <i class="el-icon-remove-outline"></i>
            </div>
            <div class="paneltwofont">
              <div class="paneltwofontnum"><span>{{missionToDoPresent}}</span> {{tasklist.missionTodo}} </div>
              <div class="paneltwofontstatus"><span>未派送</span></div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     @click="showAddDialog">添加任务</el-button>
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
      <el-table :data="tasklist.monitormission"
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

    <!-- 新建任务的对话框 -->
    <el-dialog title="新建任务"
               :visible.sync="addDialogVisible"
               width="30%"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="80px">
        <el-form-item label="任务模板"
                      prop="missionFromTo">
          <el-cascader v-model="missionModelSelected"
                       :options="missionModelList"
                       :props="missionModelProps"
                       @change="handleMissionModelChanged"
                       clearable></el-cascader>
        </el-form-item>

        <el-form-item label="货物名"
                      prop="payload">
          <el-input v-model="addForm.payload"></el-input>
        </el-form-item>
        <el-form-item label="车辆"
                      prop="agv">
          <el-input v-model="addForm.agv"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addMission">确 定</el-button>
      </span>
    </el-dialog>

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
      // 添加表单的显示与隐藏
      addDialogVisible: false,
      // 任务模板级联选择器数据
      missionModelList: [],
      // 指定任务模板级联选择器的配置对象
      missionModelProps: {
        value: 'view',
        label: 'view',
        children: 'missionFromToList',
        expandTrigger: 'hover'
      },
      // 选择的任务模板数组
      missionModelSelected: [],
      // 添加表单的验证规则对象
      addFormRules: {
        missionFromTo: [
          { required: true, message: '请输选择任务模板', trigger: 'change' }
        ]
      },
      // 添加表单的表单数据
      addForm: {
        missionFromTo: '',
        payload: '',
        agv: ''
      },
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
      },
      // 计时器
      timer: null
    }
  },
  created () {
    this.getMonitorTaskList()
    // 定时向服务器发起请求
    this.timer = setInterval(this.getMonitorTaskList, 10000)
  },
  mounted () {

  },
  beforeDestroy () {
    clearInterval(this.timer)
    this.timer = null
  },
  methods: {
    // 获取任务监视列表
    async getMonitorTaskList () {
      const { data: res } = await this.$http.get('monitor/mission', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        return this.$message.error('任务监视列表获取失败！')
      }
      this.tasklist = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getMonitorTaskList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getMonitorTaskList()
    },
    // 过滤数据
    getFilter () {
      this.queryInfo.query = this.filterForm
      this.getMonitorTaskList()
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
    // 打开新建任务框
    async showAddDialog () {
      const { data: res } = await this.$http.get('monitor/missionFromTo')
      if (res.meta.status !== 200) {
        return this.$message.error('获取任务模板失败！')
      }
      this.missionModelList = res.data

      this.addDialogVisible = true
    },
    // 任务模板选择框发生改变时，触发这个函数
    handleMissionModelChanged () {
      if (this.missionModelSelected.length == 2) {
        // 已选择的区
        const selectedArea = this.missionModelSelected[0]
        // 已选择的模板
        const selectedModel = this.missionModelSelected[1]
        // 将模板赋值到addForm
        this.addForm.missionFromTo = selectedModel
        // 把该模板的基本信息筛选出来
        const areaList = this.missionModelList.filter(m => m.workAree == selectedArea)
        const missionInfo = areaList[0].missionFromToList.filter(m => m.missionFromTo == selectedModel)
        // 把该模板的基本信息赋值到表单项
        this.addForm.payload = missionInfo[0].payload
        this.addForm.agv = missionInfo[0].agv
      } else {
        this.$refs.addFormRef.resetFields()
        this.missionModelSelected = []
      }
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
      this.missionModelSelected = []
    },
    // 添加任务
    addMission () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('monitor/mission', this.addForm)
        if (res.meta.status !== 201) {
          return this.$message.error('新建任务失败！')
        }
        this.$message.success('新建任务成功！')
        this.getMonitorTaskList()
        this.addDialogVisible = false
      })
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
    },
    /* 小数转百分数 */
    /* Number()数据类型转换，指定截取转换后的小数点后几位(四舍五入) */
    toPercent (point) {
      var str = Number(point * 100).toFixed(0)
      if (isNaN(str)) {
        str = 0
      }
      str += '%'
      return str
    }

  },
  computed: {
    missionDoingPresent () {
      const mNum = parseFloat(this.tasklist.missionTotalNum)
      const mDoing = parseFloat(this.tasklist.missionDoing)
      return this.toPercent(mDoing / mNum)
    },
    missionToDoPresent () {
      const mNum = parseFloat(this.tasklist.missionTotalNum)
      const mTodo = parseFloat(this.tasklist.missionTodo)
      return this.toPercent(mTodo / mNum)
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
}

.paneltwofont {
  // border-radius: 5%;
  body-style {
    padding: '100px';
  }
}

.paneltwofontnum {
  font-size: 40px;
  font-weight: 700;
  color: #eee;
  span {
    font-size: 20px;
    padding-right: 10px;
  }
}

.paneltwofontstatus {
  font-size: 10px;
  font-weight: 700;
  color: #eee;
  span {
    display: flex;
    justify-content: center;
  }
}
</style>
