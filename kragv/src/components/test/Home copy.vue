<template>
  <el-container class="home-container">
    <!-- 头部 -->
    <el-header>
      <div class="header-right">
        <img id="logoImg"
             src="../assets/logo.png" />
      </div>
      <div class="header-center-left"></div>

      <div class="header-center-right">
        <!-- 菜单 -->
        <el-menu class="el-menu-demo"
                 mode="horizontal"
                 router
                 :default-active="activePath"
                 :default-openeds="activeSubmenu">
          <!-- 首页菜单 -->
          <el-menu-item index="/map"
                        @click="saveNavState('/map')">
            <!-- 文本 -->
            <span>首页</span>
          </el-menu-item>

          <!-- 首页菜单 -->
          <el-menu-item index="/tasklist"
                        @click="saveNavState('/tasklist')">
            <!-- 文本 -->
            <span>任务状态</span>
          </el-menu-item>

          <el-menu-item index="/agvlist"
                        @click="saveNavState('/agvlist')">
            <!-- 文本 -->
            <span>车辆状态</span>
          </el-menu-item>

          <el-menu-item index="/taskmodel"
                        @click="saveNavState('/taskmodel')">
            <!-- 文本 -->
            <span>任务派发</span>
          </el-menu-item>

          <el-menu-item index="/user"
                        @click="saveNavState('/user')"
                        v-if="currentAuthority == 0">
            <!-- 文本 -->
            <span>用户管理</span>
          </el-menu-item>

        </el-menu>
        <!-- 菜单 -->
      </div>

      <div class="header-right">

        <!-- 搜索 -->
        <!-- 图标 -->
        <!-- <el-link :underline="false"
                 @click="handleHeaderSearchVisiable"
                 v-if="!isMobile">
          <i class="el-icon-search"></i>
        </el-link> -->
        <!-- 输入框 -->
        <!-- <transition name="slide-fade"
                    v-if="!isMobile">
          <el-input ref="headerSearchRef"
                    v-show="headerSearchVisiable"
                    autofocus="headerSearchVisiable"
                    @blur="headerSearchVisiable = false"
                    placeholder="请输入内容"
                    v-model="headerSearch"
                    class="header-search-input"></el-input>
        </transition> -->

        <!-- 问号 -->
        <el-link :underline="false"
                 v-if="!isMobile">
          <i class="el-icon-question"></i>
        </el-link>

        <!-- 全屏按钮 -->
        <el-link :underline="false"
                 v-if="!isMobile">
          <i class="el-icon-full-screen"
             @click="toggleFullscreen"></i>
        </el-link>

        <!-- 头像下拉框 -->
        <el-dropdown placement="bottom-end">
          <span class="el-dropdown-link">
            <!-- 头像 -->
            <el-avatar> {{ this.currentUser }} </el-avatar>
            <i class="el-icon-caret-bottom"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item icon="el-icon-house"
                              @click.native="avatarToWelcome">首页</el-dropdown-item>
            <!-- <el-dropdown-item disabled>双皮奶</el-dropdown-item> -->
            <el-dropdown-item divided
                              icon="el-icon-right"
                              @click.native="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>

        <!-- <el-button type="info"
                     @click="logout">退出</el-button>
          <i class="el-icon-caret-bottom"></i> -->
      </div>

    </el-header>
    <!-- 主体 -->
    <el-main :class="{mobileClass:isMobile}">
      <router-view></router-view>
    </el-main>
    <!-- <el-footer>
      <div class="foot">
        Copyright &copy; 2020 - FS ATeam Innolux
      </div>

    </el-footer> -->
  </el-container>

</template>

<script>
import screenfull from 'screenfull'

export default {
  data () {
    return {
      // 左侧菜单数据
      menulist: [],

      isCollapse: false,
      // 被激活的链接地址
      activePath: '',
      // 被激活子菜单
      activeSubmenu: [],
      // 折叠图标
      collapseIcon: 'el-icon-s-fold',
      // 是否全屏
      isFullscreen: false,
      // 头部搜索输入框显示与隐藏
      headerSearchVisiable: false,
      // 搜索框内容
      headerSearch: '',
      // 是否移动端
      isMobile: false
    }
  },
  created () {
    // this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
    this.handleMobile()
  },
  methods: {
    // 判断是否移动端
    handleMobile () {
      if (window.innerWidth < 1024) {
        this.isCollapse = true
        this.isMobile = true
      }
    },
    // 登出
    logout () {
      window.sessionStorage.clear()
      this.$router.push('/login')
    },
    // async getMenuList() {
    //   const { data: res } = await this.$http.get('menus')
    //   if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
    //   this.menulist = res.data
    //   console.log(res)
    // },
    // 点击按钮切换菜单的折叠与展开
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
      if (this.isCollapse) {
        this.collapseIcon = 'el-icon-s-unfold'
      } else {
        this.collapseIcon = 'el-icon-s-fold'
      }
    },
    saveNavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    },
    // 头像框首页
    avatarToWelcome () {
      this.saveNavState('/welcome')
      this.$router.push('/welcome')
    },
    // 全屏按钮
    toggleFullscreen () {
      screenfull.toggle()
    },
    /**
     * 全屏事件
     */
    screenfull () {
      if (!screenfull.enabled) {
        this.$message({
          message: 'Your browser does not work',
          type: 'warning'
        })
        return false
      }
      screenfull.toggle()
      this.isFullscreen = true
    },
    /**
     * 是否全屏并按键ESC键的方法
     */
    checkFull () {
      var isFull = document.fullscreenEnabled || window.fullScreen || document.webkitIsFullScreen || document.msFullscreenEnabled
      // to fix : false || undefined == undefined
      if (isFull === undefined) {
        isFull = false
      }
      return isFull
    },
    // 控制搜索框的显示与隐藏
    async handleHeaderSearchVisiable () {
      // let wait = ms => new Promise(resolve => setTimeout(resolve, ms))
      this.headerSearchVisiable = !this.headerSearchVisiable
      // console.log(this.headerSearchVisiable)
      // 如果方法不生效，可能是input元素还没有渲染出来，可通过setTimeout等待一下
      if (this.headerSearchVisiable) {
        const _this = this
        setTimeout(function () {
          _this.$refs.headerSearchRef.focus()
        }, 1)
      }
    }
  },
  computed: {
    currentUser () {
      return window.sessionStorage.getItem('currentUser')
    },
    currentAuthority () {
      return window.sessionStorage.getItem('power')
    }

  },
  mounted () {
    window.onresize = () => {
      // 全屏下监控是否按键了ESC
      if (!this.checkFull()) {
        // 全屏下按键esc后要执行的动作
        this.isFullscreen = false
      }
    }
  }
}
</script>

<style lang="less" scoped>
.mobileClass {
  padding: 0px;
  margin: 0px;
}

.home-container {
  height: 100%;
  // background-color: #001529;
}

.el-header {
  // background-color: #373d41;
  // background-color: #fff;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  // color: #666;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    // span {
    //   margin-left: 15px;
    //   margin-right: 30px;
    // }
    // img {
    //   width: 15%;
    //   height: 15%;
    //   border-radius: 50%;
    //   display: flex;
    //   align-items: center;
    //   margin-left: 10px;
    // }
  }
}

#logoImg {
  // width: 80%;
  // height: 15%;
  // border-radius: 50%;
  padding: 10px;
  display: flex;
  align-items: center;
  // margin-left: 15px;
  display: inline-block;
  height: 50px;
  vertical-align: middle;
  transition: height 0.2s;
}

.header-title {
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-main {
  // background-color: #eee;
  background-color: #e5e5f0;
}

.iconfont {
  margin-right: 10px;
}

// 中部导航栏
.header-center-left {
  width: 30%;
}

// 头部--右侧
.header-right {
  // display: flex;
  // align-items: center;
  margin-left: 0;
  margin-right: 0;

  .header-search-input {
    padding-right: 10px;
  }

  .el-dropdown-link {
    display: flex;
    justify-content: space-between;
    padding-right: 0;
    padding-left: 10px;
    margin-left: 0 !important;
    margin-right: 0 !important;
    .el-avatar {
      margin-left: 0 !important;
      margin-right: 0 !important;
    }

    i {
      padding-left: 0px;
      padding-right: 0px;
      display: flex;
      align-items: flex-end;
    }
  }

  i {
    font-size: 25px;
    font-weight: 500;
    padding-right: 5px;
  }

  .el-icon-caret-bottom {
    font-size: 10px;
  }

  > div span[data-v-8dc7cce2] {
    margin-left: 0px;
    margin-right: 0px;
  }

  .el-avatar {
    color: #fff;
    background-color: rgb(64, 158, 255);
  }
}

//搜索框动画
/* 可以设置不同的进入和离开动画 */
/* 设置持续时间和动画函数 */
.slide-fade-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}

.foot {
  color: rgb(108, 117, 125) !important;
  text-align: center !important;
}
</style>
