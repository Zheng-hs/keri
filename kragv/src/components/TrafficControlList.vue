<template>
  <div>
    <!-- 卡片视图区 -->
    <el-card>
      <!-- 搜索与添加区 -->
      <!-- <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     @click="freeControlAgvDialogOpen">释放AGV</el-button>

        </el-col>
        <el-col class="btnrow2">
          <div id="searchMapArea">
            <el-input placeholder="请输入搜索内容"
                      v-model="searchContent"
                      id="searchInput"
                      clearable
                      prefix-icon="el-icon-search"
                      @input="searchInputChange">
              <el-select v-model="searchSelect"
                         slot="prepend"
                         @input="searchInputChange"
                         placeholder="请选择">
                <el-option v-for="item in searchOptions"
                           :key="item.value"
                           :label="item.label"
                           :value="item.value">
                </el-option>
              </el-select>
            </el-input>
          </div>
        </el-col>
      </el-row> -->

      <!-- 任务列表 -->
      <el-table :data="receiveData.traffic"
                border
                highlight-current-row
                :height="tableHeight">
        <el-table-column label="AGV名称">
          <template slot-scope="scope">
            {{ scope.row.agvName }}
          </template>
        </el-table-column>
        <el-table-column label="被管制点位">
          <template slot-scope="scope">
            {{ scope.row.bookingList ? scope.row.bookingList.join(' , ') : scope.row.bookingList }}
          </template>
        </el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="150px">
          <template slot-scope="scope">
            <el-button type="danger"
                       size="mini"
                       @click="freeControlArea(scope.row.agvName)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

    </el-card>

    <!-- 释放AGV对话框 -->
    <el-dialog title="释放AGV"
               :visible.sync="freeControlAgvDialogVisible"
               width="400px"
               @close="freeControlAgvDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="freeControlAgvFormRef"
               :model="freeControlAgvForm"
               :rules="freeControlAgvFormRules"
               label-width="90px">

        <el-form-item label="AGV"
                      prop="agvId">
          <el-autocomplete popper-class="my-autocomplete"
                           v-model="freeControlAgvForm.agvId"
                           :fetch-suggestions="querySearch"
                           placeholder="请输入内容"
                           :clearable="true"
                           @select="handleAgvSelect">
            <template slot-scope="props">
              <div class="agvId">{{ props.item.agv }}</div>
              <span class="controlArea">{{ props.item.controlArea }}</span>
            </template>
          </el-autocomplete>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="freeControlAgvDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="freeControlAgv">确 定</el-button>
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
        query: {},
        pagenum: 1,
        pagesize: 10
      },
      searchOptions: [{
        value: 'controlArea',
        label: '交管区域'
      }, {
        value: 'agvId',
        label: '车号'
      }],
      searchSelect: 'controlArea',
      searchContent: '',

      // 控制freeControlAgv窗口的显示与隐藏
      freeControlAgvDialogVisible: false,
      // freeControlAgv表单的表单数据
      freeControlAgvForm: {
        agvId: '',
      },
      // freeControlAgv表单的验证规则对象
      freeControlAgvFormRules: {
        agvId: [{ required: true, message: '请输入/选择AGV', trigger: 'blur' }]
      },
      // 可释放agv
      agvOptions: [],
      receiveData: {},
      // 列表总数
      total: 0,
      taskIdSearch: '',
      // 计时器
      timer: [],

      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      // 清除timer延时器
      lastBrowseTimeouter: null,
      sendDataSwitch: true
    }
  },
  created () {

  },
  mounted () {
    this.getTrafficInfoListRT()
    this.checkDocVis()
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
            this.getTrafficInfoListRT()
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
    getTrafficInfoListRT () {
      this.getTrafficInfoList()
      // 定时向服务器发起请求
      this.timer.push(setInterval(this.getTrafficInfoList, 10000))
    },
    // 清除timer
    cleanTimer () {
      for (let i = 0; i < this.timer.length; i++) {
        clearInterval(this.timer.pop())
      }
    },
    // 获取任务状态列表
    async getTrafficInfoList () {
      const { data: res } = await this.$http.get('/traffic/allLockedArea')
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return console.log(res.meta.msg)
      }
      this.receiveData = res.data
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.queryInfo.pagesize = newSize
      this.getTrafficInfoList()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.queryInfo.pagenum = newPage
      this.getTrafficInfoList()
    },
    // 检测搜索栏
    searchInputChange () {
      if (this.searchContent.trim() !== '') {
        this.queryInfo.query = {}
        if (this.searchSelect == 'controlArea') {
          this.queryInfo.query.controlArea = this.searchContent
        } else if (this.searchSelect == 'agvId') {
          this.queryInfo.query.agvId = this.searchContent
        }
      } else {
        this.queryInfo.query = {}
      }
      this.getTrafficInfoList()
    },
    // 释放交管区
    async freeControlArea (agv) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该信息, 是否继续?', '提示', {
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
          type: 'info',
          message: '已取消操作！',
          showClose: true
        })
      }

      const { data: res } = await this.$http.delete((`/traffic/clear/${agv}`))
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
      this.getTrafficInfoList()
    },
    // 打开 释放AGV dialog
    freeControlAgvDialogOpen () {
      this.agvOptions = []
      this.receiveData.trafficControlList.forEach(tfArea => {
        let agvArr = []
        tfArea.agvEnter.forEach(agv => {
          agvArr.push(agv)
        })
        tfArea.agvWaitEnter.forEach(agv => {
          agvArr.push(agv)
        })
        agvArr.forEach(agv => {
          let temp = { 'agv': agv, 'controlArea': tfArea.controlArea }
          this.agvOptions.push(temp)
        })

      });
      this.freeControlAgvDialogVisible = true
    },
    // 释放agv时，搜索agv
    querySearch (queryString, cb) {
      let agvOptions = this.agvOptions
      let results = queryString ? agvOptions.filter(this.createFilter(queryString)) : agvOptions;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter (queryString) {
      return (agvOptions) => {
        return (agvOptions.agv.toLowerCase().indexOf(queryString.toLowerCase()) !== -1);
      };
    },
    handleAgvSelect (item) {
      this.freeControlAgvForm.agvId = item.agv
    },
    // freeControlAgv
    freeControlAgv () {
      this.$refs.freeControlAgvFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.get('freeControlAgv', { params: this.freeControlAgvForm })
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
        this.freeControlAgvDialogVisible = false
      })

    },
    // 关闭清空
    freeControlAgvDialogClosed () {
      this.$refs.freeControlAgvFormRef.resetFields()
    }

  }

}
</script>

<style lang="less" scoped>
#searchMapArea {
  width: 350px;
  .el-select {
    width: 120px !important;
  }
}

// 释放AGV 提示框
.my-autocomplete {
  li {
    line-height: normal;
    padding: 7px;

    .agvId {
      text-overflow: ellipsis;
      overflow: hidden;
    }
    .controlArea {
      font-size: 12px;
      color: #b4b4b4;
    }

    .highlighted .addr {
      color: #ddd;
    }
  }
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
