<template>
  <div class="login_container"
       ref="loginContainerRef">
    <div class="login_box">
      <!-- 头像 -->
      <div class="avatar_box">
        <img src="../assets/agvLogo.jpg" />
      </div>
      <!-- 表单   -->
      <el-form ref="loginFormRef"
               :model="loginForm"
               :rules="loginFormRules"
               label-width="0px"
               class="login_form">
        <!-- 用户名 -->
        <el-form-item prop="username">
          <el-input v-model="loginForm.username"
                    prefix-icon="iconfont icon-user"></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item prop="password">
          <el-input v-model="loginForm.password"
                    prefix-icon="iconfont icon-3702mima"
                    type="password"></el-input>
        </el-form-item>
        <!-- 按钮区 -->
        <el-form-item class="btns">
          <el-button type="primary"
                     @click="login">登陆</el-button>
          <el-button type="info"
                     @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      loginFormRules: {
        username: [{ required: true, message: '请输入登陆名称', trigger: 'blur' }],
        password: [{ required: true, message: '请输入登陆密码', trigger: 'blur' }]
      },
      userList: {
        admin: {
          username: 'admin',
          password: '123456',
          power: '0'
        },
        guest: {
          username: 'guest',
          password: '123456',
          power: '1'
        },
      }
    }
  },
  created () {
    this.turnToMobileLogin()
  },
  methods: {
    turnToMobileLogin () {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        this.$router.push('/mobileLogin')
      }
    },
    // 重置登录表单
    resetLoginForm () {
      //   console.log(this)
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(async vaild => {
        // console.log(vaild)
        if (!vaild) return

        // const { data: res } = await this.$http.post('login', this.loginForm)
        // console.log(res)
        // if (res.meta.status !== 200) return this.$message.error(res.meta.msg)

        // this.$message.success('登录成功')

        // window.sessionStorage.setItem('token', res.data.user)
        // window.sessionStorage.setItem('power', res.data.user.power + '')
        // window.sessionStorage.setItem('currentUser', res.data.user.username)
        // window.sessionStorage.setItem('activePath', '/welcome')
        if (this.userList[this.loginForm.username] == null || this.userList[this.loginForm.username].password != this.loginForm.password) {
          console.log(this.userList[this.loginForm.username])
          console.log(this.userList[this.loginForm.username].password)
          return this.$message.error('账户或密码错误')
        }

        window.sessionStorage.setItem('token', this.userList[this.loginForm.username].username)
        window.sessionStorage.setItem('power', this.userList[this.loginForm.username].power)
        window.sessionStorage.setItem('currentUser', this.userList[this.loginForm.username].username)
        window.sessionStorage.setItem('activePath', '/map')

        this.$router.push('/home')
      })
    }
  }
}
</script>

<style lang="less" scoped>
.login_container {
  background: #2b4b6b;
  height: 100%;
}

.login_title {
  color: #fff;
  font-size: 50px;
  position: absolute;
  left: 50%;
  top: 20%;
  transform: translate(-50%, -50%);
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);

  .avatar_box {
    height: 130px;
    width: 130px;
    border: solid 1px #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10 #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.btns {
  display: flex;
  justify-content: flex-end;
}
</style>
