<template>
  <div>
    <el-card>
      <el-row :gutter="20" class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary" @click="dialogVisible = true">新增</el-button>
        </el-col>
      </el-row>
      <el-table :data="lineActionList" border>
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-table :data="props.row.ruleList" border>
              <el-table-column prop="startPoint" label="起点"></el-table-column>
              <el-table-column prop="endPoint" label="终点"></el-table-column>
              <el-table-column prop="action" label="动作">
                <template slot-scope="scope">
                  {{ scope.row.action | formatterEmployment }}
                </template>
              </el-table-column>
              <el-table-column prop="index" label="线段顺序"></el-table-column>
              <el-table-column prop="id" label="线段ID"></el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <el-table-column prop="id" label="动作规则ID"> </el-table-column>
        <el-table-column prop="remark" label="动作规则名"> </el-table-column>
        <el-table-column prop="strategy" label="动作限制" :formatter="formatterEmployment1"> </el-table-column>
        <el-table-column label="操作" width="100px">
          <template slot-scope="scope">
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="deleteAction(scope.row.id)"></el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="block">
        <el-pagination :current-page="pagenum" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper"
          :total="total" @size-change="handleSizeChange" @current-change="handleCurrentChange" />
      </div>
    </el-card>
    <el-dialog :title="title" :visible.sync="dialogVisible" width="70%" @close="closeDialog">

      <!-- <el-col :gutter="20">
        <el-row :span="6">
            <div class="input_name">动作规则名:</div>
            <el-input class="input_body" v-model="remark" placeholder="请填写规则名"></el-input>
        </el-row>
        <el-row :span="6">
            <div>请选择动作限制：</div>
            <el-select v-model="condition" filterable placeholder="请选择动作限制">
              <el-option v-for="item in conditionList" :key="item.args" :label="item.description" :value="item.args"> </el-option>
            </el-select>
        </el-row>
      </el-col> -->
      <el-form :inline="true" style="margin-left:5px">
        <el-form-item label="动作规则名">
          <el-input class="input_body" v-model="remark" placeholder="请填写规则名"></el-input>
        </el-form-item>
        <el-form-item label="请选择动作限制">
          <el-select v-model="strategy" filterable placeholder="请选择动作限制">
              <el-option v-for="item in conditionList" :key="item.args" :label="item.description" :value="item.args"> </el-option>
            </el-select>
        </el-form-item>
      </el-form>

      <div class="line" v-for="(i, index) in actions" :key="index">
        <div class="line-left">
          <div class="line1">
            <div>请选择线段：</div>
            <el-select v-model="actions[index].id" filterable placeholder="请选择线段" @change="chooseLine(actions[index].id, index)">
              <el-option v-for="item in lineList" :key="item.pathId" :label="item.name" :value="item.pathId"> </el-option>
            </el-select>
          </div>
        </div>
        <div class="line-right">
          <div>请选择动作:</div>
          <div class="line2">
            <el-select v-model="actions[index].action" placeholder="请选择动作">
              <el-option v-for="item in actionList" :key="item.id" :label="item.description" :value="item.actionArgs"> </el-option>
            </el-select>
          </div>
        </div>
      </div>
      <el-button class="add_btn" type="primary" icon="el-icon-circle-plus-outline" @click="addPoint"></el-button>
      <el-button type="danger" icon="el-icon-remove-outline" @click="delPoint"></el-button>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="add">新增</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
let self = null
export default {
  filters: {
    formatterEmployment(value) {
      const obj = self.actionList.find((item) =>{
        item.actionArgs === value
      })
      return obj ? obj.description : value
    },
    formatterEmployment1(cellValue) {
      const obj = self.conditionList.find((item) => item.args === cellValue)
      return obj ? obj.description : cellValue
    }
  },
  data() {
    return {
      lineActionList: [],
      actionList: [],
      conditionList: [],
      strategy: '',
      pagenum: 1,
      pagesize: 20,
      total: 0,
      lineList: [],
      title: '新增地图动作规则',
      dialogVisible: false,
      remark: '',
      actions: [
        {
          id: '',
          action: '',
          index: 0,
          startPoint: '',
          endPoint: '',
        },
      ],
      j: 0,
      checked: '',
      // 所有要合并的数量（一行一行的开始）
      spanAll: [],
      titleData: [
        {
          name: 'remark',
          label: '名称',
        },
        {
          name: 'condition',
          label: '',
        },
        {
          name: 'action',
          label: 'ID',
        },
        {
          name: 'index',
          label: 'ID',
        },
        {
          name: 'lindId',
          label: '线段',
        },
        {
          name: 'startPoint',
          label: '起点',
        },
        {
          name: 'endPoint',
          label: '终点',
        },
        {
          name: 'ruleId',
          label: '',
        },
      ],
    }
  },
  beforeCreate() {
    self = this
  },
  mounted() {
    this.getLine()
    this.getAction()
  },
  methods: {
    async getAction() {
      const { data: res } = await this.$http.post(`/mapAction/rulePage?pageNum=${this.pagenum}&pageSize=${this.pagesize}`)
      if (res.meta.status == 200) {
        this.lineActionList = res.data.mapRule
        this.total = res.data.total
      }
    },
    async getLine() {
      const { data: res } = await this.$http.get('/mapAction/getAllPath')
      if (res.meta.status === 200) {
        this.lineList = res.data.path
      }

      const { data: res1 } = await this.$http.get('/action/args')
      if (res1.meta.status == 200) {
        this.actionList = res1.data.actionArgsList
      }

      const { data: res2 } = await this.$http.get('/mapAction/getActionConditionStrategy')
      if (res2.meta.status == 200) {
        this.conditionList = res2.data.conditionList
      }
    },
    addPoint() {
      this.actions.push({
        id: '',
        action: '',
        index: this.actions.length,
        startPoint: '',
        endPoint: '',
      })
    },
    delPoint() {
      this.actions.pop()
    },
    formatterEmployment(row, column, cellValue) {
      const obj = this.actionList.find((item) => item.actionArgs === cellValue)
      return obj ? obj.description : cellValue
    },
    formatterEmployment1(row, column, cellValue) {
      const obj = this.conditionList.find((item) => item.args === cellValue)
      return obj ? obj.description : cellValue
    },
    chooseLine(val, index) {
      this.lineList.forEach((line) => {
        if (line.pathId === val) {
          this.actions[index].startPoint = line.sourcePoint
          this.actions[index].endPoint = line.destinationPoint
        }
      })
    },
    handleSizeChange(newSize) {
      this.pagesize = newSize
      this.getAction()
    },
    handleCurrentChange(newPage) {
      this.pagenum = newPage
      this.getAction()
    },
    closeDialog() {
      this.actions = [
        {
          id: '',
          action: '',
          index: 0,
          startPoint: '',
          endPoint: '',
        },
      ]
      this.remark = ''
      this.dialogVisible = false
    },
    async add() {
      const { data: res } = await this.$http.post('/mapAction/addRule', {
        remark: this.remark,
        strategy: this.strategy,
        ruleList: this.actions,
      })

      if (res.meta.status == 200) {
        this.$message.success('新增成功')
        this.getAction()
        this.dialogVisible = false
      }
    },
    async deleteAction(id) {
      const confirmResult = await this.$confirm('此操作将永久删除该动作规则, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).catch((err) => err)

      // 如果用户确认删除，则返回字符串confirm
      // 如果用户取消删除，则返回字符串cancel
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }
      const { data: res } = await this.$http.post(`/mapAction/deleteRule?groupId=${id}`)
      if (res.meta.status == 200) {
        this.$message.success('删除成功')
        this.getAction()
      }
    },
    getSpanNum(curName) {
      const data = this.lineActionList
      const spanArry = []
      let pos = 0
      data.forEach((val, i) => {
        if (i === 0) {
          spanArry.push(1)
          pos = 0
        } else {
          // 判断当前列数据与下一行的该列数据是否相同
          if (data[i][curName] === data[i - 1][curName]) {
            // 每一列每一行的合并数量
            spanArry[pos] += 1
            spanArry.push(0)
          } else {
            spanArry.push(1)
            pos = i
          }
        }
      })
      // 把合并数据放入spanAll里面
      this.spanAll.push(spanArry)
    },

    // 合并行
    objectSpanMethod({ row, column, rowIndex, columnIndex }) {
      // 得到行合并的数据
      const rowNum = this.spanAll[columnIndex][rowIndex]
      // 列合并
      const colNum = rowNum > 0 ? 1 : 0
      // 当前位置的行合并和列合并数据
      if (columnIndex === 0) {
        return {
          rowspan: rowNum,
          colspan: colNum,
        }
      }
      if (columnIndex === 1) {
        return {
          rowspan: rowNum,
          colspan: colNum,
        }
      }
      if (columnIndex === 7) {
        return {
          rowspan: rowNum,
          colspan: colNum,
        }
      }
    },
  },
}
</script>

<style lang="less" scoped>
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
.dialog_header {
  display: flex;
  align-items: center;
  width: 31%;
  margin: 10px;
  .input_name {
    width: 40%;
  }
  // .input_body {
  //   flex: 4;
  // }
}
.line {
  display: flex;
  align-items: center;
  .line-left {
    flex: 3;
  }
  .line-right {
    flex: 4;
    display: flex;
    align-items: center;
  }
  .actions {
    margin-right: 10px;
    // flex: 1;
  }
  .line1 {
    margin: 5px;
    display: flex;
    align-items: center;
    div {
      margin-right: 10px;
      // width: 30%;
    }
  }
  .line2 {
    flex: 10;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    .el-select {
      margin: 5px;
    }
  }
}
.el-radio {
  display: flex;
}
/deep/ .el-radio__input {
  display: flex;
  align-items: center;
}
</style>