<template>
  <div :class="{mobileClass:isMobile}">
    <el-card>
      <!-- 搜索与添加区 -->
      <el-row :gutter="20"
              class="btnrow">
        <el-col class="btnrow1">
          <el-button type="primary"
                     :size='btnSize'
                     @click="addDialogVisible = true">添加用户</el-button>
        </el-col>
        <el-col class="btnrow2">
          <span>用户名:</span>
          <el-input class="usernameSearchInput"
                    clearable
                    placeholder="请输入用户名"
                    prefix-icon="el-icon-search"
                    @input="usernameSearchChanged"
                    v-model="usernameSearch"> </el-input>
        </el-col>
      </el-row>

      <!-- 用户列表 -->
      <el-table :data="userlistPaging"
                border
                highlight-current-row
                :height="tableHeight"
                @current-change="handleCurrentRowChange"
                @sort-change="sortChange">
        <el-table-column type="index"
                         width="50"></el-table-column>
        <el-table-column label="用户名"
                         sortable="custom"
                         prop="username"></el-table-column>
        <el-table-column label="密码"
                         prop="password"></el-table-column>
        <el-table-column label="权限"
                         sortable="custom"
                         prop="power">
          <template slot-scope="scope">
            {{ scope.row.power == 0 ? '管理员' : '普通用户' }}
          </template>
        </el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="200px">
          <template slot-scope="scope">
            <el-button type="primary"
                       size="mini"
                       @click="showEditDialog(scope.row.id)">修改</el-button>
            <el-button type="danger"
                       size="mini"
                       @click="deleteById(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- 分页区域 -->
      <el-pagination @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="pagenum"
                     :page-sizes="[10, 20, 50, 100]"
                     :page-size="pagesize"
                     layout="total, sizes, prev, pager, next, jumper"
                     :total="total"
                     v-if="!isMobile"></el-pagination>

      <!-- 移动端分页 -->
      <el-pagination layout="prev, pager, next"
                     :total="total"
                     small
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     v-if="isMobile">
      </el-pagination>

    </el-card>

    <!-- 添加用户的对话框 -->
    <el-dialog title="添加用户"
               :visible.sync="addDialogVisible"
               :width="handleWidth(30)"
               @close="addDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="addFormRef"
               :model="addForm"
               :rules="addFormRules"
               label-width="70px">
        <el-form-item label="用户名"
                      prop="username">
          <el-input v-model="addForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码"
                      prop="password">
          <el-input v-model="addForm.password"></el-input>
        </el-form-item>
        <el-form-item label="权限"
                      prop="power">
          <el-select v-model="addForm.power"
                     placeholder="请选择">
            <el-option label="管理员"
                       value=0></el-option>
            <el-option label="普通用户"
                       value=1></el-option>
          </el-select>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="addUser">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改用户的对话框 -->
    <el-dialog title="修改用户"
               :visible.sync="editDialogVisible"
               :width="handleWidth(30)"
               @close="editDialogClosed">
      <!-- 内容主体区 -->
      <el-form ref="editFormRef"
               :model="editForm"
               :rules="editFormRules"
               label-width="70px">
        <el-form-item label="用户名"
                      prop="username">
          <el-input :disabled="true"
                    v-model="editForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码"
                      prop="password">
          <el-input v-model="editForm.password"></el-input>
        </el-form-item>
        <el-form-item label="权限"
                      prop="power">
          <el-select v-model="editForm.power"
                     placeholder="请选择">
            <el-option label="管理员"
                       value=0></el-option>
            <el-option label="普通用户"
                       value=1></el-option>
          </el-select>
        </el-form-item>

      </el-form>
      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="editUser">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  data () {
    return {
      // 用户列表
      userlist: [],
      // 用户列表分页
      userlistPaging: [],
      // 处理后要显示的数据
      userlistCopy: [],
      // 列表总数
      total: 0,
      // 页码
      pagenum: 1,
      // 分页大小
      pagesize: 10,
      // 动态搜索数据
      usernameSearch: '',
      // 排序属性
      sortProp: '',
      // 排序命令
      sortOrder: null,

      // 添加表单的显示与隐藏
      addDialogVisible: false,
      // 添加表单的验证规则对象
      addFormRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 5, message: '用户名不能少于5位', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 5, message: '密码不能少于5位', trigger: 'blur' }
        ],
        power: [{ required: true, message: '请输用户权限', trigger: 'change' }]
      },
      // 添加表单的表单数据
      addForm: {},

      // 修改表单的显示与隐藏
      editDialogVisible: false,
      // 修改表单的验证规则对象
      editFormRules: {
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 5, message: '密码不能少于5位', trigger: 'blur' }
        ],
        power: [{ required: true, message: '请输用户权限', trigger: 'change' }]
      },
      // 修改表单的表单数据
      editForm: {},


      // 选择的行
      currentRow: {},
      //按钮尺寸
      btnSize: '',
      // 表格高度
      tableHeight: window.innerHeight * 0.7,
      // 删除列固定位置
      delColFix: 'right',
      // 是否是移动端
      isMobile: false,
    }
  },
  created () {
    // 处理移动端大小
    this.handleMobile()
  },
  mounted () {
    this.getUserlist()
  },
  methods: {
    // 获取用户列表
    async getUserlist () {
      const { data: res } = await this.$http.get('userlist')
      if (res.meta.status !== 200) {
        return this.$message.error('用户列表获取失败!')
      }
      this.userlist = res.data.userlist
      this.handlePaging()
    },
    // 监听pagesize改变的事件
    handleSizeChange (newSize) {
      // console.log(newSize)
      this.pagesize = newSize
      this.handlePaging()
    },
    // 监听页码值改变的事件
    handleCurrentChange (newPage) {
      // console.log(newPage)
      this.pagenum = newPage
      this.handlePaging()
    },
    // 分页处理
    handlePaging () {
      const pagenum = this.pagenum
      const pagesize = this.pagesize
      const startIndex = (pagenum - 1) * pagesize
      const endIndex = pagenum * pagesize
      this.handleSort()
      const filterResult = this.userlistCopy.filter(x => x.username.indexOf(this.usernameSearch) !== -1)
      this.total = filterResult.length
      this.userlistPaging = filterResult.slice(startIndex, endIndex)
    },
    // 搜索框内容改变触发
    usernameSearchChanged () {
      this.pagenum = 1
      this.handlePaging()
    },
    // 排序处理函数
    handleSort () {
      const prop = this.sortProp
      const order = this.sortOrder
      this.userlistCopy = JSON.parse(JSON.stringify(this.userlist))
      if (order == 'descending' && prop !== '') {
        // this.userlistCopy.sort((a, b) => new Date(b[prop]) - new Date(a[prop]))
        this.userlistCopy.sort((a, b) => this.sortByProp(a[prop], b[prop]))
      } else if (order == 'ascending' && prop !== '') {
        this.userlistCopy.sort((a, b) => this.sortByProp(b[prop], a[prop]))
      }
    },
    sortByProp (arg1, arg2) {
      if (arg1 > arg2) {
        return -1
      } else if (arg1 < arg2) {
        return 1
      } else {
        return 0
      }
    },
    // 排序条件发生变化触发
    sortChange (column, prop, order) {
      // console.log(column)
      // console.log(prop)
      // console.log(order)
      this.pagenum = 1
      this.sortProp = column.prop
      this.sortOrder = column.order
      this.handlePaging()
    },
    // 表格选择行时的处理函数
    handleCurrentRowChange (val) {
      this.currentRow = val
    },
    // 添加用户
    addUser () {
      this.$refs.addFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.post('user', this.addForm)
        if (res.meta.status !== 200) {
          return this.$message.error(res.meta.msg)
        }
        this.getUserlist()
        this.$message.success(res.meta.msg)
        this.addDialogVisible = false
      })
    },
    // 监听添加对话框的关闭事件
    addDialogClosed () {
      this.$refs.addFormRef.resetFields()
    },
    // 打开修改对话框的处理函数
    async showEditDialog (id) {
      const { data: res } = await this.$http.get('user', { params: { id: id } })
      if (res.meta.status !== 200) {
        return this.$message.error('用户获取失败！')
      }
      res.data.user.power = res.data.user.power + ''
      this.editForm = res.data.user

      this.editDialogVisible = true
    },
    // 修改用户
    editUser () {
      this.$refs.editFormRef.validate(async valid => {
        if (!valid) return
        const { data: res } = await this.$http.put('user', this.editForm)
        if (res.meta.status !== 200) {
          return this.$message.error(res.meta.msg)
        }
        this.getUserlist()
        this.$message.success(res.meta.msg)
        this.editDialogVisible = false
      })
    },
    // 监听修改对话框的关闭事件
    editDialogClosed () {
      this.$refs.editFormRef.resetFields()
    },
    // 删除用户
    async deleteById (id) {
      // console.log(id)
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: this.isMobile
      }).catch(err => err)

      // 如果用户确认删除，则返回字符串 confirm
      // 如果用户取消删除，则返回字符串 cancel
      // console.log(confirmResult)
      if (confirmResult !== 'confirm') {
        return this.$message.info('已取消删除')
      }

      const { data: res } = await this.$http.delete('user', { params: { id: id } })
      if (res.meta.status !== 200) {
        return this.$message.error(res.meta.msg)
      }

      this.$message.success('删除用户成功！')
      this.getUserlist()
    },
    // 分辨率改变时，处理控件的宽度
    handleWidth (width) {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        return screenWidth * 0.8 + 'px'
      } else {
        return width + "%"
      }
    },
    // 使用移动端的处理函数
    handleMobile () {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        this.btnSize = 'mini'
        this.delColFix = false
        this.isMobile = true
      }
    }

    // 
    // 
  }
}
</script>

<style lang="less" scoped>
.usernameSearchInput {
  width: 200px;
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
