<template>
  <div>
    <!-- 面包屑导航区 -->
    <!-- <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/home' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>运行维护</el-breadcrumb-item>
      <el-breadcrumb-item>资源类</el-breadcrumb-item>
      <el-breadcrumb-item>机台</el-breadcrumb-item>
      <el-breadcrumb-item>统计</el-breadcrumb-item>
    </el-breadcrumb> -->

    <!--开始时间-->
    <el-card>
      <div style="font-size:20px;" id="firstcard">
        <span>
          周期开始时间：Tue Jul 14 2020 13:55:30
        </span>
        <span>
          <span>机台 : </span>
          <el-select v-model="portSelect" placeholder="请选择">
            <el-option label="全部" value="0"></el-option>
            <el-option label="1号" value="1"></el-option>
            <el-option label="2号" value="2"></el-option>
          </el-select>
        </span>
      </div>
    </el-card>

    <!-- 卡片视图区 -->
    <el-row :gutter="20">
      <!-- 车体总工时数 -->
      <el-col :span="8">
        <el-card>
          <div slot="header" class="clearfix">
            <span>车体总工时数</span>
          </div>
          <div style="font-size:30px;">9</div>
        </el-card>
      </el-col>
      <!-- 车体正常工作工时 -->
      <el-col :span="8">
        <el-card>
          <div slot="header" class="clearfix">
            <span>车体正常工作工时</span>
          </div>
          <div style="font-size:30px;">8</div>
        </el-card>
      </el-col>
      <!-- 稼动率 -->
      <el-col :span="8">
        <el-card>
          <div slot="header" class="clearfix">
            <span>稼动率</span>
          </div>
          <div style="font-size:30px;">88%</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 错误任务明细表 -->
    <el-card>
      <div slot="header" class="clearfix">
        <span>错误机台明细列表</span>
      </div>

      <!-- 搜索与添加区 -->
      <el-row :gutter="20" class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary" icon="el-icon-printer">导出</el-button>
        </el-col>
        <el-col class="btnrow2">
          <el-button type="primary" icon="el-icon-search" @click="filterDialogVisible = true">筛选</el-button>
          <el-button type="primary" icon="el-icon-circle-close-outline">清除筛选条件</el-button>
        </el-col>
      </el-row>

      <!-- 列表 -->
      <el-table :data="tasklist" border stripe>
        <el-table-column type="index"></el-table-column>
        <el-table-column label="设备名称" prop="missionId"></el-table-column>
        <el-table-column label="硬件版本" prop="missionId"></el-table-column>
        <el-table-column label="固件版本" prop="mobile"></el-table-column>
        <el-table-column label="设备类型(用途）" prop="role_name"></el-table-column>
        <el-table-column label="在线/离线" prop="role_name"></el-table-column>
        <el-table-column label="最近通讯时间" prop="role_name"></el-table-column>
        <el-table-column label="设备动作" prop="role_name"></el-table-column>
        <el-table-column label="动作流程状态" prop="role_name"></el-table-column>
        <el-table-column label="错误" prop="role_name"></el-table-column>
        <el-table-column label="错误码" prop="role_name"></el-table-column>
        <el-table-column label="设备请求" prop="role_name"></el-table-column>
        <el-table-column label="系统命令" prop="role_name"></el-table-column>
        <el-table-column label="任务模板名称" prop="role_name"></el-table-column>
        <el-table-column label="任务编号" prop="role_name"></el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryInfo.pagenum"
        :page-sizes="[1, 2, 5, 10]"
        :page-size="queryInfo.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination>
    </el-card>

    <!-- 筛选表单 -->
    <el-dialog title="添加筛选" :visible.sync="filterDialogVisible" width="50%" @close="filterDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="filterFormRef" :model="filterForm" :rules="filterFormRules" label-width="120px">
        <el-form-item label="设备名称" prop="username">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="硬件版本" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="固件版本" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="设备类型(用途）" prop="password">
          <el-select v-model="agvSelect" placeholder="请选择">
            <el-option label="上下料Port" value="0"></el-option>
            <el-option label="电梯控制" value="1"></el-option>
            <el-option label="风淋门控制" value="2"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="在线/离线" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="最近通讯时间" prop="username">
          <el-date-picker v-model="value3" type="datetimerange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"> </el-date-picker>
        </el-form-item>
        <el-form-item label="设备动作" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="动作流程状态" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="错误" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="错误码" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="设备请求" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="系统命令" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="任务模板名称" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
        <el-form-item label="任务编号" prop="password">
          <el-input v-model="filterForm.username"></el-input>
        </el-form-item>
      </el-form>
      <!-- 底部区 -->
      <span slot="footer" class="dialog-footer">
        <el-button @click="filterDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="filterDialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 获取用户列表的参数
      queryInfo: {
        query: '',
        pagenum: 1,
        pagesize: 10
      },
      tasklist: [],
      total: 0,
      // 机台选择
      portSelect: '0',
      // 筛选框显示与隐藏
      filterDialogVisible: false,
      // 筛选数据
      filterForm: {}
    }
  },
  created () {},
  methods: {
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
    }
  }
}
</script>

<style lang="less" scoped>
#firstcard {
  display: flex;
  justify-content: space-between;
  > span {
    display: flex;
    align-items: center;
    > span {
      padding-right: 20px;
    }
  }
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
</style>
