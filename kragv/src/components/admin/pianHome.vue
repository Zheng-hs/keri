<template>
  <el-container class="home-container">
    <!-- 左侧 -->
    <el-aside :width="isCollapse ? '64px' : '200px'">
      <!-- <div class="toggle-button"
           @click="toggleCollapse">|||</div> -->
      <img id="logoImg"
           src="../assets/logo.png" />
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
        <el-menu-item index="/welcome"
                      @click="saveNavState('/welcome')">
          <!-- 图标 -->
          <i class="el-icon-house"></i>
          <!-- 文本 -->
          <span>首页</span>
        </el-menu-item>

        <!-- 实时监视 -->
        <!--  一级菜单 -->
        <el-submenu index="1">
          <!-- 一级菜单模板区 -->
          <template slot="title">
            <!-- 图标 -->
            <i class="el-icon-monitor"></i>
            <!-- 文本 -->
            <span>实时监视</span>
          </template>

          <!-- 任务 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">任务类</template>
            <!-- 监视 -->
            <!--  三级菜单 -->
            <el-menu-item index="/monitortask"
                          @click="saveNavState('/monitortask')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-notebook-1"></i>
                <!-- 文本 -->
                <span>任务列表</span>
              </template>
            </el-menu-item>
          </el-menu-item-group>

          <!-- 资源类 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">资源类</template>
            <!-- AGV -->
            <!--  三级菜单 -->
            <el-menu-item index="/monitoragv"
                          @click="saveNavState('/monitoragv')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-coordinate"></i>
                <!-- 文本 -->
                <span>AGV</span>
              </template>
            </el-menu-item>
            <!-- 机台 -->
            <!--  三级菜单 -->
            <el-menu-item index="/monitorport"
                          @click="saveNavState('/monitorport')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-odometer"></i>
                <!-- 文本 -->
                <span>机台</span>
              </template>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>

        <!-- 运行维护 -->
        <!-- 一级菜单 -->
        <el-submenu index="2"
                    v-if="currentAuthority == 'engineer' || currentAuthority == 'admin'">
          <!-- 一级菜单模板区 -->
          <template slot="title">
            <!-- 图标 -->
            <i class="el-icon-set-up"></i>
            <!-- 文本 -->
            <span>运行维护</span>
          </template>

          <!-- 任务类 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">任务类</template>
            <el-submenu index="2-1">
              <!-- 二级菜单模板区 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-notebook-1"></i>
                <!-- 文本 -->
                <span>任务</span>
              </template>
              <!-- 实时控制 -->
              <!--  三级菜单 -->
              <el-menu-item index="/maintaintaskcontrol"
                            @click="saveNavState('/maintaintaskcontrol')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-mouse"></i>
                  <!-- 文本 -->
                  <span>实时控制</span>
                </template>
              </el-menu-item>
              <!-- 历史查询 -->
              <!--  三级菜单 -->
              <el-menu-item index="/maintaintaskhistoryselect"
                            @click="saveNavState('/maintaintaskhistoryselect')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-notebook-2"></i>
                  <!-- 文本 -->
                  <span>历史查询</span>
                </template>
              </el-menu-item>
              <!-- 统计 -->
              <!--  三级菜单 -->
              <el-menu-item index="/maintaintaskstatistics"
                            @click="saveNavState('/maintaintaskstatistics')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-s-data"></i>
                  <!-- 文本 -->
                  <span>统计</span>
                </template>
              </el-menu-item>
            </el-submenu>
          </el-menu-item-group>

          <!-- 运维资源类 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">资源类</template>
            <!-- 运维agv -->
            <!-- 三级菜单 -->
            <el-submenu index="2-2-1">
              <!-- 三级菜单模板区 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-coordinate"></i>
                <!-- 文本 -->
                <span>AGV</span>
              </template>
              <!-- AGV实时控制 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainagvcontrol"
                            @click="saveNavState('/maintainagvcontrol')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-mouse"></i>
                  <!-- 文本 -->
                  <span>实时控制</span>
                </template>
              </el-menu-item>
              <!-- AGV历史查询 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainagvhistoryselect"
                            @click="saveNavState('/maintainagvhistoryselect')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-notebook-2"></i>
                  <!-- 文本 -->
                  <span>历史查询</span>
                </template>
              </el-menu-item>
              <!-- AGV统计 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainagvstatistics"
                            @click="saveNavState('/maintainagvstatistics')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-s-data"></i>
                  <!-- 文本 -->
                  <span>统计</span>
                </template>
              </el-menu-item>
            </el-submenu>

            <!-- 运维机台 -->
            <!-- 三级菜单 -->
            <el-submenu index="2-2-2">
              <!-- 三级菜单模板区 -->
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-odometer"></i>
                <!-- 文本 -->
                <span>机台</span>
              </template>
              <!-- 机台实时控制 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainportcontrol"
                            @click="saveNavState('/maintainportcontrol')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-mouse"></i>
                  <!-- 文本 -->
                  <span>实时控制</span>
                </template>
              </el-menu-item>
              <!-- 机台历史查询 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainporthistoryselect"
                            @click="saveNavState('/maintainporthistoryselect')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-notebook-2"></i>
                  <!-- 文本 -->
                  <span>历史查询</span>
                </template>
              </el-menu-item>
              <!-- 机台统计 -->
              <!--  四级菜单 -->
              <el-menu-item index="/maintainportstatistics"
                            @click="saveNavState('/maintainportstatistics')">
                <template slot="title">
                  <!-- 图标 -->
                  <i class="el-icon-s-data"></i>
                  <!-- 文本 -->
                  <span>统计</span>
                </template>
              </el-menu-item>
            </el-submenu>
          </el-menu-item-group>
        </el-submenu>

        <!-- 系统设置 -->
        <!-- 一级菜单 -->
        <el-submenu index="3"
                    v-if="currentAuthority == 'admin'">
          <!-- 一级菜单模板区 -->
          <template slot="title">
            <!-- 图标 -->
            <i class="el-icon-setting"></i>
            <!-- 文本 -->
            <span>系统设置</span>
          </template>

          <!-- 系统设置任务类 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">任务类</template>
            <!-- 模板 -->
            <!--  三级菜单 -->
            <el-menu-item index="/systemtaskmodel"
                          @click="saveNavState('/systemtaskmodel')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-notebook-1"></i>
                <!-- 文本 -->
                <span>任务模板</span>
              </template>
            </el-menu-item>
          </el-menu-item-group>

          <!-- 系统设置资源类 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">资源类</template>
            <!-- 系统AGV -->
            <!--  三级菜单 -->
            <el-menu-item index="/systemagv"
                          @click="saveNavState('/systemagv')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-coordinate"></i>
                <!-- 文本 -->
                <span>AGV</span>
              </template>
            </el-menu-item>
            <!-- 系统机台 -->
            <!--  三级菜单 -->
            <el-menu-item index="/systemport"
                          @click="saveNavState('/systemport')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-odometer"></i>
                <!-- 文本 -->
                <span>机台</span>
              </template>
            </el-menu-item>
          </el-menu-item-group>

          <!-- 系统设置用户管理 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">用户管理</template>
            <!-- 系统AGV -->
            <!--  三级菜单 -->
            <el-menu-item index="/systemuser"
                          @click="saveNavState('/systemuser')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-user"></i>
                <!-- 文本 -->
                <span>用户列表</span>
              </template>
            </el-menu-item>
          </el-menu-item-group>

          <!-- 系统设置仪表盘 -->
          <!-- 二级菜单 -->
          <el-menu-item-group>
            <template slot="title">统计分析</template>
            <!-- 系统AGV -->
            <!--  三级菜单 -->
            <el-menu-item index="/dashboard"
                          @click="saveNavState('/dashboard')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-odometer"></i>
                <!-- 文本 -->
                <span>仪表盘1</span>
              </template>
            </el-menu-item>

            <!--  三级菜单 -->
            <el-menu-item index="/dashboardagv"
                          @click="saveNavState('/dashboardagv')">
              <template slot="title">
                <!-- 图标 -->
                <i class="el-icon-odometer"></i>
                <!-- 文本 -->
                <span>仪表盘2</span>
              </template>
            </el-menu-item>

          </el-menu-item-group>
        </el-submenu>
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
            <span>物流互联系统</span>
          </div>
        </div>

        <div class="header-right">
          <!-- 搜索 -->
          <!-- 图标 -->
          <el-link :underline="false"
                   @click="handleHeaderSearchVisiable">
            <i class="el-icon-search"></i>
          </el-link>
          <!-- 输入框 -->
          <transition name="slide-fade">
            <el-input ref="headerSearchRef"
                      v-show="headerSearchVisiable"
                      autofocus="headerSearchVisiable"
                      @blur="headerSearchVisiable = false"
                      placeholder="请输入内容"
                      v-model="headerSearch"
                      class="header-search-input"></el-input>
          </transition>

          <!-- 问号 -->
          <el-link :underline="false">
            <i class="el-icon-question"></i>
          </el-link>

          <!-- 全屏按钮 -->
          <el-link :underline="false">
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
              <!-- <el-dropdown-item divided
                                icon="el-icon-odometer"
                                @click.native="toDashboard">仪表盘</el-dropdown-item> -->
              <el-dropdown-item divided
                                icon="el-icon-odometer"
                                @click.native="toDashboardAgv">仪表盘</el-dropdown-item>
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
      headerSearch: ''
    }
  },
  created () {
    // this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    // 跳转到仪表盘
    toDashboard () {
      this.$router.push('/dashboard')
    },
    // 跳转到agv仪表盘
    toDashboardAgv () {
      this.$router.push('/dashboardagv')
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
      if (window.sessionStorage.getItem('status') == 499) {
        this.$message.info('登陆已失效，请重新登陆！')
        window.sessionStorage.clear()
        return
      }
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
        let _this = this
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
      return window.sessionStorage.getItem('authority')
    },

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
</style>
