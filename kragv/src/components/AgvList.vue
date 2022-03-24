<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     @click="agvRegisterOrunRegisterDialogVisible = true">登记/注销</el-button>
          <el-button type="primary"
                     @click="openCheckAllEQ">充电检测</el-button>
          <el-button type="primary"
                     @click="agvSetDialogVisible=true">车体设置</el-button>
          <el-button type="primary"
                     @click="agvUpdateDialogVisible = true">更新车体</el-button>
          <el-button type="primary"
                     @click="agvAlignDialogVisible = true">储位修正</el-button>
        </el-col>
        <el-col class="btnrow2">
          <span>车号:</span>
          <el-input class="searchInput"
                    clearable
                    placeholder="请输入车号号"
                    prefix-icon="el-icon-search"
                    @input="searchInputChange"
                    v-model="agvIdSearch"> </el-input>
        </el-col>
      </el-row>

      <!-- 任务列表 -->
      <el-table :data="agvData.agvList"
                border
                highlight-current-row
                :height="tableHeight">
        <el-table-column label="车号"
                         width='130px'
                         prop="agvId"></el-table-column>
        <el-table-column label="区域"
                         width='130px'
                         prop="agvArea"></el-table-column>
        <el-table-column label="任务状态"
                         width='130px'
                         prop="taskStatus"></el-table-column>
        <el-table-column label="当前任务"
                         prop="taskId"></el-table-column>
        <el-table-column label="车体状态"
                         width='130px'
                         prop="moveStatus"></el-table-column>
        <el-table-column label="停车原因"
                         prop="agvStopReasonS"></el-table-column>
        <el-table-column label="电量"
                         width='130px'
                         prop="batteryLevel"></el-table-column>
        <el-table-column label="通信状态"
                         width='130px'
                         prop="onLine"></el-table-column>
        <el-table-column label="当前点位"
                         width='120px'
                         prop="now"></el-table-column>
        <el-table-column label="速度"
                         width='130px'
                         prop="speed"></el-table-column>
        <el-table-column label="管制状态"
                         width='130px'
                         prop="unBlock"></el-table-column>
        <el-table-column label="最近通讯时间"
                         width='150px'
                         prop="updateTime"></el-table-column>
        <el-table-column label="车体IP地址"
                         width='135px'
                         prop="ipAddress"></el-table-column>
        <el-table-column label="伸缩电机状态"
                         width='110px'
                         prop="forkMotorsStatus"></el-table-column>
        <el-table-column label="拨指电机状态"
                         width='110px'
                         prop="horomerStatus"></el-table-column>
        <el-table-column label="升降电机状态"
                         width='110px'
                         prop="riseFallMotorStatus"></el-table-column>
        <el-table-column label="旋转电机状态"
                         width='110px'
                         prop="rotateMotorsStatus"></el-table-column>

      </el-table>

      <!-- 分页区域 -->
      <el-pagination @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="queryInfo.pagenum"
                     :page-sizes="[10, 20, 50, 100]"
                     :page-size="queryInfo.pagesize"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total"></el-pagination>

      <!-- 登记/注销 -->
      <el-dialog title="登记/注销车辆"
                 :visible.sync="agvRegisterOrunRegisterDialogVisible"
                 width="300px">
        <!-- 内容主体区 -->
        <div id="agvSetDialogButtonArea">
          <el-button type="primary"
                     @click="agvRegisterDialogVisible = true">登记车辆</el-button>
          <el-button type="primary"
                     @click="agvunRegisterDialogVisible = true">注销车辆</el-button>
        </div>
      </el-dialog>
      <!-- 登记/注销 -->

      <!-- 登记车辆 -->
      <el-dialog title="登记车辆"
                 :visible.sync="agvRegisterDialogVisible"
                 width="400px"
                 @close="agvRegisterDialogClosed">
        <!-- 内容主体区 -->
        <el-form ref="agvRegisterFormRef"
                 :model="agvRegisterForm"
                 :rules="agvRegisterFormRules"
                 label-width="60px"
                 class="dialogForm">
          <el-form-item label="AGV"
                        prop="agvId">
            <el-input v-model="agvRegisterForm.agvId"></el-input>
          </el-form-item>
          <el-form-item label="区域"
                        prop="areaId">
            <el-input v-model="agvRegisterForm.areaId"></el-input>
          </el-form-item>

        </el-form>

        <!-- 按键区 -->
        <div slot="footer"
             class="dialog-footer">
          <el-button @click="agvRegisterDialogVisible = false">取 消</el-button>
          <el-button type="primary"
                     @click="registerAgv">确 定</el-button>
        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- 登记车辆 -->

      <!-- 注销车辆 -->
      <el-dialog title="注销车辆"
                 :visible.sync="agvunRegisterDialogVisible"
                 width="400px"
                 @close="agvunRegisterDialogClosed">
        <!-- 内容主体区 -->
        <el-form ref="agvunRegisterFormRef"
                 :model="agvunRegisterForm"
                 :rules="agvunRegisterFormRules"
                 label-width="60px"
                 class="dialogForm">
          <el-form-item label="AGV"
                        prop="agvId">
            <el-input v-model="agvunRegisterForm.agvId"></el-input>
          </el-form-item>

        </el-form>

        <!-- 按键区 -->
        <div slot="footer"
             class="dialog-footer">
          <el-button @click="agvunRegisterDialogVisible = false">取 消</el-button>
          <el-button type="primary"
                     @click="unRegisterAgv">确 定</el-button>
        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- 注销车辆 -->

      <!-- 车体设置的对话框 -->
      <el-dialog title="车体设置"
                 :visible.sync="agvSetDialogVisible"
                 width="400px"
                 @close="agvSetDialogClosed">
        <!-- 内容主体区 -->
        <el-form ref="agvSetFormRef"
                 :model="agvSetForm"
                 :rules="agvSetFormRules"
                 label-width="80px"
                 class="dialogForm">
          <el-form-item label="AGV"
                        prop="agvId">
            <el-select v-model="agvSetForm.agvId"
                       placeholder="请选择"
                       clearable>
              <el-option v-for="agv in agvData.agvList"
                         :key="agv.agvId"
                         :label="agv.agvId"
                         :value="agv.agvId"></el-option>
            </el-select>
          </el-form-item>

        </el-form>

        <!-- 按键区 -->
        <div id="agvSetDialogButtonArea">
          <el-button type="primary"
                     @click="checkOneEQ">充电检测</el-button>
          <el-button type="primary"
                     @click="cancelMission">取消任务</el-button>
          <el-button type="primary"
                     @click="agvReset">复位</el-button>
        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- 车体设置的对话框 -->

      <!-- agv更新对话框 -->
      <el-dialog title="更新车体"
                 :visible.sync="agvUpdateDialogVisible"
                 width="300px">
        <!-- 内容主体区 -->
        <div id="agvSetDialogButtonArea">
          <el-button type="primary"
                     @click="agvMapUpdateDialogOpened">更新车体地图</el-button>
          <el-button type="primary"
                     @click="agvFirmwareUpdateDialogOpened">更新车体固件</el-button>
        </div>
      </el-dialog>
      <!-- agv更新对话框 -->

      <!-- agv地图更新 -->
      <el-dialog title="更新车体地图"
                 :visible.sync="agvMapUpdateDialogVisible"
                 width="690px"
                 @close="agvMapUpdateDialogClosed">
        <!-- 内容主体区 -->
        <div style="padding:20px;">
          <el-upload class="upload-demo"
                     :action=mapFileUrl
                     :limit="1"
                     :on-exceed="handleExceed"
                     :file-list="fileList">
            <el-button size="small"
                       type="primary">点击上传</el-button>
            <div slot="tip"
                 class="el-upload__tip"></div>
          </el-upload>
        </div>
        <!-- 内容主体区 -->

        <!-- 车体选择框 -->
        <div style="padding:20px;">
          <el-transfer filterable
                       :titles="['未选择', '已选择']"
                       filter-placeholder="请输入车体名字"
                       v-model="agvSelectedList"
                       :data="agvWillSelectList">
          </el-transfer>
        </div>
        <!-- 车体选择框 -->

        <!-- 按键区 -->
        <div style="padding-left:20px;">
          <el-button type="primary"
                     @click="uploadMap">更新</el-button>

        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- agv地图更新 -->

      <!-- agv固件更新 -->
      <el-dialog title="更新车体固件"
                 :visible.sync="agvFirmwareUpdateDialogVisible"
                 width="690px"
                 @close="agvFirmwareUpdateDialogClosed">
        <!-- 内容主体区 -->
        <div style="padding:20px;">
          <el-upload class="upload-demo"
                     :action=firmwareFileUrl
                     :limit="1"
                     :on-exceed="handleExceed"
                     :file-list="fileList">
            <el-button size="small"
                       type="primary">点击上传</el-button>
            <div slot="tip"
                 class="el-upload__tip"></div>
          </el-upload>
        </div>
        <!-- 内容主体区 -->

        <!-- 车体选择框 -->
        <div style="padding:20px;">
          <el-transfer filterable
                       :titles="['未选择', '已选择']"
                       filter-placeholder="请输入车体名字"
                       v-model="agvSelectedList"
                       :data="agvWillSelectList">
          </el-transfer>
        </div>
        <!-- 车体选择框 -->

        <!-- 按键区 -->
        <div style="padding-left:20px;">
          <el-button type="primary"
                     @click="uploadFirmware">更新</el-button>

        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- agv固件更新 -->

      <!-- 储位修正对话框 -->
      <el-dialog title="储位修正"
                 :visible.sync="agvAlignDialogVisible"
                 width="500px">
        <!-- 内容主体区 -->
        <div id="agvSetDialogButtonArea">
          <el-button type="primary"
                     @click="agvForkAlignTaskDialogVisible = true">储位修正任务</el-button>
          <el-button type="primary"
                     @click="toAlignFilePage">查看修正文件</el-button>
          <el-button type="primary"
                     @click="agvAlignFileUploadDialogVisible = true">上传修正文件</el-button>
        </div>
      </el-dialog>
      <!-- 储位修正对话框 -->

      <!-- 储位修正任务 -->
      <el-dialog title="储位修正任务"
                 :visible.sync="agvForkAlignTaskDialogVisible"
                 width="400px"
                 @close="agvForkAlignTaskDialogClosed">
        <!-- 内容主体区 -->
        <el-form ref="agvForkAlignTaskFormRef"
                 :model="agvForkAlignTaskForm"
                 :rules="agvForkAlignTaskFormRules"
                 label-width="80px"
                 class="dialogForm">
          <el-form-item label="开始点位"
                        prop="startPoint">
            <el-input v-model="agvForkAlignTaskForm.startPoint"></el-input>
          </el-form-item>
          <el-form-item label="结束点位"
                        prop="endPoint">
            <el-input v-model="agvForkAlignTaskForm.endPoint"></el-input>
          </el-form-item>

        </el-form>

        <!-- 按键区 -->
        <div slot="footer"
             class="dialog-footer">
          <el-button @click="agvForkAlignTaskDialogVisible = false">取 消</el-button>
          <el-button type="primary"
                     @click="dispatchAlignMission">确 定</el-button>
        </div>
        <!-- 按键区 -->

      </el-dialog>
      <!-- 储位修正任务 -->

      <!-- 上传修正文件对话框 -->
      <el-dialog title="上传修正文件"
                 :visible.sync="agvAlignFileUploadDialogVisible"
                 width="500px"
                 @close="agvAlignFileUploadDialogClosed">
        <!-- 内容主体区 -->
        <div style="padding:10px;">
          <el-upload class="upload-demo"
                     :action=agvAlignFileUploadUrl
                     name="files"
                     multiple
                     :file-list="fileList">
            <el-button size="small"
                       type="primary">点击上传</el-button>
            <div slot="tip"
                 class="el-upload__tip"></div>
          </el-upload>
        </div>
        <!-- 内容主体区 -->

      </el-dialog>
      <!-- 上传修正文件对话框 -->

    </el-card>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // 获取列表的参数
      queryInfo: {
        query: {},
        pagenum: 1,
        pagesize: 10
      },
      agvData: {},
      // 列表总数
      total: 0,
      agvIdSearch: '',
      // 计时器
      timer: [],

      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      // 清除timer延时器
      lastBrowseTimeouter: null,
      sendDataSwitch: true,

      // 登记/注销车辆对话框的显示与隐藏
      agvRegisterOrunRegisterDialogVisible: false,

      // 登记车辆对话框的显示与隐藏
      agvRegisterDialogVisible: false,
      // 登记车辆选择的agv
      agvRegisterForm: {
        agvId: "",
        areaId: "",
      },
      // 登记车辆表单的验证规则对象
      agvRegisterFormRules: {
        agvId: [{ required: true, message: '请填写AGV', trigger: 'blur' }],
        areaId: [{ required: true, message: '请填写AGV区域', trigger: 'blur' }],
      },



      // 注销车辆对话框的显示与隐藏
      agvunRegisterDialogVisible: false,
      // 注销车辆填写的agv
      agvunRegisterForm: {
        agvId: "",
      },
      // 注销车辆表单的验证规则对象
      agvunRegisterFormRules: {
        agvId: [{ required: true, message: '请填写AGV', trigger: 'blur' }],
      },


      // 车体设置对话框的显示与隐藏
      agvSetDialogVisible: false,
      // 车体设置选择的agv
      agvSetForm: {
        agvId: ""
      },
      // 车体设置表单的验证规则对象
      agvSetFormRules: {
        agvId: [{ required: true, message: '请选择AGV', trigger: 'blur' }],
      },

      // 车体更新对话框的显示与隐藏
      agvUpdateDialogVisible: false,

      // 地图文件上传地址
      mapFileUrl: this.$http.defaults.baseURL + "/upload/file/map",
      // 固件文件上传地址
      firmwareFileUrl: this.$http.defaults.baseURL + "/upload/file/firmware",
      // 车体地图更新对话框的显示与隐藏
      agvMapUpdateDialogVisible: false,
      // 车体固件更新对话框的显示与隐藏
      agvFirmwareUpdateDialogVisible: false,
      // 文件上传列表
      fileList: [],
      // 未选择agv穿梭框
      agvWillSelectList: [],
      // 选择agv穿梭框
      agvSelectedList: [],


      // 储位修正任务对话框的显示与隐藏
      agvForkAlignTaskDialogVisible: false,
      // 储位修正任务选择的agv
      agvForkAlignTaskForm: {
        startPoint: "",
        endPoint: "",
      },
      // 储位修正任务表单的验证规则对象
      agvForkAlignTaskFormRules: {
        startPoint: [{ required: true, message: '请填写开始点位', trigger: 'blur' }],
        endPoint: [{ required: true, message: '请填写结束点位', trigger: 'blur' }],
      },


      // 储位修正对话框的显示与隐藏
      agvAlignDialogVisible: false,
      // 上传修正文件对话框的显示与隐藏
      agvAlignFileUploadDialogVisible: false,
      // 上传修正文件地址
      agvAlignFileUploadUrl: this.$http.defaults.baseURL + "/upload/file/align",



    }
  },
  created () {
    this.getTaskListRT()
    this.checkDocVis()
  },
  mounted () {

  },
  beforeDestroy () {
    this.cleanTimer()
  },
  methods: {
    // 检测 document visible
    checkDocVis () {
      document.onvisibilitychange = () => {
        // let browseInterval = 1000 * 60 * 30
        let browseInterval = 1000 * 60 * 15

        if (document.visibilityState == 'visible') {
          if (this.lastBrowseTimeouter != null) {
            clearTimeout(this.lastBrowseTimeouter)
            this.lastBrowseTimeouter = null
          }
          if (!this.sendDataSwitch) {
            // window.location.reload()
            this.getTaskListRT()
            this.sendDataSwitch = true
          }
        } else {
          this.lastBrowseTimeouter = setTimeout(() => {
            this.cleanTimer()
            this.sendDataSwitch = false
          }, browseInterval);
        }

      }
    },
    getTaskListRT () {
      this.getAgvState()
      // 定时向服务器发起请求
      this.timer.push(setInterval(this.getAgvState, 10000))
    },
    // 清除timer
    cleanTimer () {
      for (let i = 0; i < this.timer.length; i++) {
        clearInterval(this.timer.pop())
      }
    },
    // 获取任务状态列表
    async getAgvState () {
      const { data: res } = await this.$http.get('getAgvState', { params: this.queryInfo })
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return console.log(res.meta.msg)
      }
      this.agvData = res.data
      this.total = res.data.total
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getAgvState()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getAgvState()
    },
    // 检测搜索栏
    searchInputChange () {
      if (this.agvIdSearch.trim() !== '') {
        this.queryInfo.query.agvId = this.agvIdSearch
      } else {
        this.queryInfo.query = {}
      }
      this.getAgvState()
    },
    // 
    // 打开充电检测
    async openCheckAllEQ () {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将打开充电检测, 是否继续?', '提示', {
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

      const { data: res } = await this.$http.get('/checkAllEQ')
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

    },

    // 登记车体窗体关闭,触发的函数
    async agvRegisterDialogClosed () {
      this.$refs.agvRegisterFormRef.resetFields()
    },



    // 登记agv
    registerAgv () {
      this.$refs.agvRegisterFormRef.validate(async valid => {
        if (!valid) return
        let agvId = this.agvRegisterForm.agvId
        let areaId = this.agvRegisterForm.areaId
        const { data: res } = await this.$http.post(`registerAgv/${agvId}/${areaId}`)

        if (res.meta.status != 200) {
          // return this.$message.error(res.meta.msg)
          return this.$message({
            type: 'error',
            message: res.meta.msg,
            showClose: true
          })
        }
        // this.$message.success(res.meta.msg)
        this.$message({
          type: 'success',
          message: res.meta.msg,
          showClose: true
        })
        this.agvRegisterDialogVisible = false
        this.agvRegisterOrunRegisterDialogVisible = false
      })

    },


    // 注销车体窗体关闭,触发的函数
    async agvunRegisterDialogClosed () {
      this.$refs.agvunRegisterFormRef.resetFields()
    },

    // 注销agv
    unRegisterAgv () {
      this.$refs.agvunRegisterFormRef.validate(async valid => {
        if (!valid) return
        let agvId = this.agvunRegisterForm.agvId
        const { data: res } = await this.$http.delete(`unRegisterAgv/${agvId}`)

        if (res.meta.status != 200) {
          // return this.$message.error(res.meta.msg)
          return this.$message({
            type: 'error',
            message: res.meta.msg,
            showClose: true
          })
        }
        // this.$message.success(res.meta.msg)
        this.$message({
          type: 'success',
          message: res.meta.msg,
          showClose: true
        })
        this.agvunRegisterDialogVisible = false
        this.agvRegisterOrunRegisterDialogVisible = false
      })

    },



    // 车体设置窗体关闭,触发的函数
    async agvSetDialogClosed () {
      this.$refs.agvSetFormRef.resetFields()
    },


    // 车辆设置验证
    agvSetDialogValidate () {
      let validResult = false
      this.$refs.agvSetFormRef.validate(async valid => {
        if (!valid) return
        validResult = true
      })

      return validResult
    },

    // 车辆设置结果处理
    agvSetResultHandler (res) {
      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          type: 'error',
          message: res.meta.msg,
          showClose: true
        })
      }
      // this.$message.success(res.meta.msg)
      this.$message({
        type: 'success',
        message: res.meta.msg,
        showClose: true
      })
      this.agvSetDialogVisible = false
    },

    // 充电检测
    async checkOneEQ () {
      if (!this.agvSetDialogValidate()) return
      let resList = []
      resList.push(this.agvSetForm.agvId)
      const { data: res } = await this.$http.post('checkOneEQ', resList)
      this.agvSetResultHandler(res)
    },

    // 取消任务
    async cancelMission () {
      if (!this.agvSetDialogValidate()) return
      const { data: res } = await this.$http.delete('cancel/agv/' + this.agvSetForm.agvId)
      this.agvSetResultHandler(res)
    },


    // 取消任务
    async agvReset () {
      if (!this.agvSetDialogValidate()) return
      const { data: res } = await this.$http.get('reset/' + this.agvSetForm.agvId)
      this.agvSetResultHandler(res)
    },

    // 生成agv穿梭框数据
    generateAgvWillSelectList () {
      let data = [];
      this.agvData.agvList.forEach(agv => {
        data.push({
          label: agv.agvId,
          key: agv.agvId,
        });
      });
      this.agvWillSelectList = data
    },

    // 车体地图更新窗体关闭,触发的函数
    agvMapUpdateDialogOpened () {
      this.generateAgvWillSelectList()
      this.agvMapUpdateDialogVisible = true
    },

    // 车体地图更新窗体关闭,触发的函数
    agvMapUpdateDialogClosed () {
      this.agvSelectedList = []
      this.agvWillSelectList = []
      this.fileList = []
    },


    // 车体固件更新窗体关闭,触发的函数
    agvFirmwareUpdateDialogOpened () {
      this.generateAgvWillSelectList()
      this.agvFirmwareUpdateDialogVisible = true
    },

    // 车体固件更新窗体关闭,触发的函数
    agvFirmwareUpdateDialogClosed () {
      this.agvSelectedList = []
      this.agvWillSelectList = []
      this.fileList = []
    },

    // 文件上传数量限制
    handleExceed () {
      this.$message({
        type: 'info',
        message: "只能上传一个文件",
        showClose: true
      })
    },
    async upload (url) {
      if (this.agvSelectedList.length == 0) {
        return this.$message({
          type: 'info',
          message: "请选择车体",
          showClose: true
        })
      }
      const { data: res } = await this.$http.post(url, this.agvSelectedList)

      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        this.$message({
          type: 'error',
          message: res.meta.msg,
          showClose: true
        })

        return false
      }
      // this.$message.success(res.meta.msg)
      this.$message({
        type: 'success',
        message: res.meta.msg,
        showClose: true
      })

      return true
    },
    // 更新地图
    async uploadMap () {
      let res = await this.upload("/upload/map")
      if (res == true) {
        this.agvMapUpdateDialogVisible = false
        this.agvUpdateDialogVisible = false
      }

    },
    // 更新更新固件
    async uploadFirmware () {
      let res = await this.upload("/upload/firmware")
      if (res == true) {
        this.agvFirmwareUpdateDialogVisible = false
        this.agvUpdateDialogVisible = false
      }

    },



    // 储位修正任务窗体关闭,触发的函数
    async agvForkAlignTaskDialogClosed () {
      this.$refs.agvForkAlignTaskFormRef.resetFields()

    },
    // 派发储位修正任务
    dispatchAlignMission () {
      this.$refs.agvForkAlignTaskFormRef.validate(async valid => {
        if (!valid) return
        let startPoint = this.agvForkAlignTaskForm.startPoint
        let endPoint = this.agvForkAlignTaskForm.endPoint
        let startcol = Math.floor(startPoint / 100)
        let endcol = Math.floor(endPoint / 100)
        if (startcol !== endcol) {
          return this.$message({
            type: 'error',
            message: "开始点和结束点不是同一个巷道",
            showClose: true
          })
        }

        let markList = []
        let actionList = []
        for (let i = startPoint; i <= endPoint; i++) {
          markList.push(i.toString())
          actionList.push("Get_offset")
        }
        let dispatchId = (new Date()).getTime()

        let task = {}
        task.markList = markList
        task.actionList = actionList
        task.dispatchId = dispatchId

        const { data: res } = await this.$http.post('/dispatchMission', task)
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
        this.agvForkAlignTaskDialogVisible = false
        this.agvAlignDialogVisible = false
      })

    },

    // 查看修正文件
    toAlignFilePage () {
      window.open("/align")
    },
    // 上传修正文件窗体关闭,触发的函数
    agvAlignFileUploadDialogClosed () {
      this.fileList = []
    },




  }

  //
  //
}
</script>

<style lang="less" scoped>
.searchInput {
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

#agvSetDialogButtonArea {
  display: flex;
  justify-content: center;
}
</style>
