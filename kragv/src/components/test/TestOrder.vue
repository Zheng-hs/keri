<template>
  <div>
    <el-table :data="tableData"
              style="width: 100%"
              :default-sort="{ prop: 'date', order: 'descending' }"
              @sort-change="sortthiscolumn">
      <el-table-column prop="date"
                       label="日期"
                       sortable="custom"
                       width="180"> </el-table-column>
      <el-table-column prop="name"
                       label="姓名"
                       sortable="custom"
                       width="180"> </el-table-column>
      <el-table-column prop="address"
                       label="地址"
                       :formatter="formatter"> </el-table-column>
      <el-table-column prop="wr"
                       label="写"
                       :formatter="formatter">
        <template slot-scope="scope">
          <el-input v-model="scope.row.wr"></el-input>
        </template>

      </el-table-column>
    </el-table>

    <br />

    <div id="testiconout">
      <div id="testicon">
        <i class="el-icon-monitor"></i>
        <span>adsfsa</span>
      </div>
    </div>

    <div>
      <el-date-picker v-model="valuetime"
                      value-format="yyyy-MM-dd HH:mm:ss"
                      type="datetimerange"
                      range-separator="至"
                      start-placeholder="开始日期"
                      end-placeholder="结束日期"> </el-date-picker>
    </div>

    <el-card style="width: 40%;">
      <el-table :data="tableData"
                style="width: 100%;"
                height='10%'>
        <el-table-column prop="date"
                         style="width: 100%"
                         min-width='800px'
                         label="日期">
          <template>
            <el-steps :active="5"
                      finish-status="success">
              <el-step title="步骤1"
                       description="这是一段很长很长很长的描述性文字"></el-step>
              <el-step title="步骤2"
                       description="这是一段很长很长很长的描述性文字"></el-step>
              <el-step title="步骤3"
                       description="这是一段很长很长很长的描述性文字"></el-step>
              <el-step title="步骤4"
                       description="这是一段很长很长很长的描述性文字"></el-step>
              <el-step title="步骤1"
                       description="这是一段很长很长很长的描述性文字"></el-step>
              <el-step title="步骤2"
                       description="这是一段很长很长很长的描述性文字"></el-step>
            </el-steps>
          </template>
        </el-table-column>

      </el-table>
    </el-card>

    <el-button @click="clickButt">???</el-button>
    <el-button @click="clickButt">{{showFont()}}</el-button>

    <iframe src="./static/点位+车v4.0/mapAGV.html"
            width="100%"
            height="500vh"
            scrolling='no'
            frameborder='0'></iframe>
    <v-html-panel url.asyc="../assets/aaa.html"></v-html-panel>

  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [
        {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄',
          wr: ''
        },
        {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1517 弄',
          wr: ''
        },
        {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1519 弄',
          wr: ''
        },
        {
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1516 弄',
          wr: ''
        }
      ],
      valuetime: []
    }
  },
  methods: {
    formatter (row, column) {
      return row.address
    },
    sortthiscolumn (column) {
      console.log(column)
    },
    clickButt () {
      this.$message.success('123')
    },
    showFont () {
      return '撒范德萨'
    }
  }
}
</script>

<style lang="less" scoped>
#testicon {
  font-size: 200%;
  font-weight: 700;
  color: red;
}

#testiconout:hover i,
#testiconout:hover span {
  color: blue !important;
}
</style>
