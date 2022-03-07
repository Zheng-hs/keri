<template>
  <el-container class="home-container">
    <!-- 左侧 -->
    <el-aside :width="isCollapse ? '64px' : '200px'">
      <!-- <div class="toggle-button"
           @click="toggleCollapse">|||</div> -->
      <img id="logoImg"
           v-show="!isCollapse"
           src="../../assets/logo.png" />
      <!-- <div class="aside-icon">
        <span v-if="!isCollapse">物流互联系统</span>
      </div> -->
      <!-- 侧边栏菜单区域 -->
      <!-- <el-menu background-color="#333744"
               text-color="#fff"
               active-text-color="#409eff"
               :unique-opened="true"
               :collapse="isCollapse"
               :collapse-transition="false"
               router
               :default-active="activePath"> -->
      <el-menu background-color="#00152A"
               text-color="rgba(255,255,255,0.65)"
               active-text-color="#fff"
               :unique-opened="true"
               :collapse="isCollapse"
               :collapse-transition="false"
               router
               :default-active="activePath"
               :default-openeds="activeSubmenu">
        <!-- 首页菜单 -->
        <!-- 首页菜单 -->
        <el-menu-item index="/admin/map"
                      @click="saveNavState('/admin/map')">
          <!-- 图标 -->
          <i class="el-icon-house"></i>
          <!-- 文本 -->
          <span>首页</span>
        </el-menu-item>

        <!-- 车辆状态 -->
        <el-menu-item index="/admin/agvlist"
                      @click="saveNavState('/admin/agvlist')">
          <!-- 图标 -->
          <i class="el-icon-odometer"></i>
          <!-- 文本 -->
          <span>车辆状态</span>
        </el-menu-item>

        <!-- 任务状态 -->
        <el-menu-item index="/admin/tasklist"
                      @click="saveNavState('/admin/tasklist')">
          <!-- 图标 -->
          <i class="el-icon-notebook-1"></i>
          <!-- 文本 -->
          <span>任务状态</span>
        </el-menu-item>

        <!-- 交管状态 -->
        <el-menu-item index="/admin/trafficcontrollist"
                      @click="saveNavState('/admin/trafficcontrollist')">
          <!-- 图标 -->
          <i class="el-icon-coordinate"></i>
          <!-- 文本 -->
          <span>交管状态</span>
        </el-menu-item>

        <el-menu-item index="/admin/taskmodel"
                      @click="saveNavState('/admin/taskmodel')">
          <!-- 图标 -->
          <i class="el-icon-set-up"></i>
          <!-- 文本 -->
          <span>任务派发</span>
        </el-menu-item>

        <el-menu-item index="/admin/user"
                      @click="saveNavState('/admin/user')"
                      v-if="currentAuthority == 99">
          <!-- 文本 -->
          <span>用户管理</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <!-- 头部 -->
      <el-header>
        <div>
          <!-- 图标 -->
          <i :class="collapseIcon"
             @click="toggleCollapse"
             style="font-size: 40px;cursor: pointer;"></i>
          <!-- <div class="aside-icon">
            <span v-if="!isCollapse">物流互联系统</span>
            <span>物流互联系统</span>
          </div> -->
          <div class="header-title">
            <span>AGV Control System</span>
          </div>
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
                   v-if="!isMobile"
                   @click="sysInfoDrawerOpen"
                   :before-close="sysInfoDrawerClose">
            <el-badge :is-dot="sysInfoAlarm">
              <i class="el-icon-message-solid"></i>
            </el-badge>
          </el-link>

          <!-- 信息 -->
          <el-link :underline="false"
                   @click="userTipsVisible=true"
                   v-if="!isMobile">
            <i class="el-icon-info"></i>
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

      <!-- 系统告警信息栏 -->
      <template>
        <el-drawer title="消息"
                   :visible.sync="sysInfoDrawerVisible"
                   :direction="sysInfoDrawerDirection">
          <el-card>
            <el-table :data="systemInfoCardData"
                      stripe
                      :show-header="false"
                      :height="sysInfoHeight"
                      style="width: 100%">
              <!-- <el-table-column prop="time"
                             label="时间">
            </el-table-column>
            <el-table-column prop="info"
                             label="系统信息">
            </el-table-column> -->
              <el-table-column label="动作清单">
                <template slot-scope="scope">
                  <p>{{ scope.row.time}} : </p>
                  <p style="font-size:15px;">{{ scope.row.info}}</p>
                </template>
              </el-table-column>
            </el-table>
          </el-card>
        </el-drawer>
      </template>
      <!-- 系统告警信息栏 -->

      <!-- 用户手册 -->
      <el-dialog title="操作提示"
                 :visible.sync="userTipsVisible"
                 width="60%">
        <!-- 内容主体区 -->
        <el-carousel height="60vh"
                     indicator-position="outside">
          <el-carousel-item interval=5
                            v-for="item in userTipsImgUrlList"
                            :key="item">
            <el-image :src="item"
                      style=" height: 100%;"
                      fit="contain">
              <div slot="error"
                   class="image-slot">
                <i class="el-icon-picture-outline"></i>
              </div>
            </el-image>
          </el-carousel-item>
        </el-carousel>
        <!-- 内容主体区 -->
      </el-dialog>
      <!-- 用户手册 -->

      <!-- 右侧主体 -->
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
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
      isMobile: false,
      sysInfoDrawerVisible: false,
      sysInfoDrawerDirection: 'rtl',
      // sysInfo height
      sysInfoHeight: window.innerHeight * 0.8,
      systemInfoCardData: [{
        time: '',
        info: ''
      }],
      systemInfoCardDataHistory: [{
        time: '',
        info: ''
      }],
      // 信息提示红点
      sysInfoAlarm: false,
      // 公告栏计时器
      sysInfotimer: null,
      // 公告栏计时器
      sysInfoAlarmtimer: null,
      // 用户tips显示与隐藏
      userTipsVisible: false,
      userTipsImgUrlList: [
        require('../../assets/tipImg/tip01.jpg'),
        require('../../assets/tipImg/tip02.jpg'),
        require('../../assets/tipImg/tip03.jpg'),
        require('../../assets/tipImg/tip04.jpg'),
        require('../../assets/tipImg/tip05.jpg'),
      ],

    }
  },
  created () {
    // this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
    this.handleMobile()
  },
  beforeDestroy () {
    this.cleanTimer()
  },
  mounted () {
    window.onresize = () => {
      // 全屏下监控是否按键了ESC
      if (!this.checkFull()) {
        // 全屏下按键esc后要执行的动作
        this.isFullscreen = false
      }
    }
    this.sysInfoAlarmInit()
  },
  methods: {
    cleanTimer () {
      clearInterval(this.sysInfotimer)
      this.sysInfotimer = null
      clearInterval(this.sysInfoAlarmtimer)
      this.sysInfoAlarmtimer = null
    },
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
      this.saveNavState('/admin/map')
      this.$router.push('/admin/map')
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
    },
    // Alarm红点提示
    async setSysInfoAlarmRed () {
      const { data: res } = await this.$http.get('getSystemInfo')
      if (res.meta.status == 200) {
        let systemInfo = window.sessionStorage.getItem('systemInfo')

        if (this.sysInfoDrawerVisible == false && JSON.stringify(res.data.systemInfo) != systemInfo) {
          this.sysInfoAlarm = true
        } else {
          this.sysInfoAlarm = false
        }
        this.systemInfoCardData = res.data.systemInfo
      }

    },
    // 告警红点初始化
    sysInfoAlarmInit () {
      this.setSysInfoAlarmRed()
      this.sysInfoAlarmtimer = setInterval(this.setSysInfoAlarmRed, 1000 * 20);
    },
    // 获取公告栏信息
    async getSystemInfo () {
      if (this.sysInfoDrawerVisible == false) return
      const { data: res } = await this.$http.get('getSystemInfo')
      if (res.meta.status == 200) {
        this.systemInfoCardData = res.data.systemInfo
        // this.systemInfoCardDataHistory = res.data.systemInfo
        window.sessionStorage.setItem('systemInfo', JSON.stringify(res.data.systemInfo))
      }

    },
    // 消息栏打开
    sysInfoDrawerOpen () {
      this.sysInfoDrawerVisible = true
      this.sysInfoAlarm = false
      this.getSystemInfo()
      this.sysInfotimer = setInterval(this.getSystemInfo, 1000)
    },
    // 消息栏关闭
    sysInfoDrawerClose () {
      clearInterval(this.sysInfotimer)
      this.sysInfotimer = null
    },

  },
  computed: {
    currentUser () {
      return window.sessionStorage.getItem('currentUser')
    },
    currentAuthority () {
      return window.sessionStorage.getItem('power')
    }

  },
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
  // background-color: #001529;
}

.el-header {
  // background-color: #373d41;
  background-color: #fff;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #666;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
      margin-right: 30px;
    }
    img {
      width: 15%;
      height: 15%;
      border-radius: 50%;
      display: flex;
      align-items: center;
      margin-left: 10px;
    }
  }
}

#logoImg {
  width: 80%;
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

// .aside-icon {
//   display: flex;
//   align-items: center;
//   padding-top: 20px;
//   padding-bottom: 10px;
//   justify-content: center;
//   span {
//     margin-left: 15px;
//     margin-right: 30px;
//     display: inline-block;
//     display: flex;
//     align-items: center;
//     height: 32px;
//     margin: 0 0 0 12px;
//     color: #000;
//     font-weight: 600;
//     font-size: 25px;
//     line-height: 32px;
//     vertical-align: middle;
//     animation: fade-in;
//     animation-duration: 0.2s;
//   }
//   img {
//     width: 50px;
//     // height: 15%;
//     // border-radius: 50%;
//     display: flex;
//     align-items: center;
//     margin-left: 15px;
//     display: inline-block;
//     height: 32px;
//     vertical-align: middle;
//     transition: height 0.2s;
//   }
// }

.header-title {
  display: flex;
  align-items: center;
  justify-content: center;
}

.el-aside {
  // background-color: #333744;
  background-color: #00152a;

  .el-menu {
    border-right: none;
  }
}

// 激活菜单颜色
.el-menu-item.is-active {
  background-color: #1373cc !important;
}

// 鼠标滑过菜单的颜色
// .el-menu-item :hover {
//   color: #fff;
//   background-color: hotpink !important;
// }

// 鼠标滑过菜单的字体颜色
.el-menu-item:hover i,
.el-menu-item:hover span {
  color: #fff !important;
}

// 鼠标滑过菜单背景颜色
// .el-menu-item:hover {
//   background-color: #333744 !important;
// }

// 鼠标滑过子菜单的字体颜色
.el-submenu__title:hover i,
.el-submenu__title:hover span,
.el-submenu__title:hover .el-submenu__icon-arrow {
  color: #fff !important;
}

// .el-submenu__icon-arrow {
//   background-color: #fff !important;
// }

.el-main {
  // background-color: #eee;
  background-color: #e5e5f0;
}

.iconfont {
  margin-right: 10px;
}

.toggle-button {
  background-color: #4a5064;
  // background-color: #666;
  color: #fff;
  text-align: center;
  font-size: 10px;
  line-height: 24px;
  letter-spacing: 0.2em; //当前字体大小乘以0.2
  cursor: pointer;
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
    // padding-right: 5px;
  }

  .el-link {
    padding-right: 15px;
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
</style>
