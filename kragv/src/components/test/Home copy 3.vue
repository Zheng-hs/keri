<template>
  <el-container class="home-container">
    <!-- 左侧 -->
    <el-aside :width="isCollapse ? '64px' : '200px'">
      <!-- <div class="toggle-button"
           @click="toggleCollapse">|||</div> -->
      <div class="aside-icon">
        <img src="../assets/logo.png" />
        <span v-if="!isCollapse">物流互联系统</span>
      </div>
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
          <template slot="title">
            <!-- 图标 -->
            <i class="el-icon-s-home"></i>
            <!-- 文本 -->
            <span>首页</span>
          </template>
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
        <el-submenu index="2">
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
        <el-submenu index="3">
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
             style="font-size: 40px;"></i>
        </div>

        <div>
          <span>{{ this.currentUser }}</span>
          <el-button type="info"
                     @click="logout">退出</el-button>
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
export default {
  data () {
    return {
      // 左侧菜单数据
      menulist: [],
      iconObj: {
        125: 'iconfont icon-user',
        103: 'iconfont icon-tijikongjian',
        101: 'iconfont icon-shangpin',
        102: 'iconfont icon-danju',
        145: 'iconfont icon-baobiao'
      },
      isCollapse: false,
      // 被激活的链接地址
      activePath: '',
      // 被激活子菜单
      activeSubmenu: [],
      // 折叠图标
      collapseIcon: 'el-icon-s-fold'
    }
  },
  created () {
    // this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
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
    }
  },
  computed: {
    currentUser () {
      return window.sessionStorage.getItem('currentUser')
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

.aside-icon {
  display: flex;
  align-items: center;
  padding-top: 20px;
  padding-bottom: 10px;
  span {
    margin-left: 15px;
    margin-right: 30px;
    display: inline-block;
    height: 32px;
    margin: 0 0 0 12px;
    color: #fff;
    font-weight: 600;
    font-size: 18px;
    line-height: 32px;
    vertical-align: middle;
    animation: fade-in;
    animation-duration: 0.2s;
  }
  img {
    width: 32px;
    // height: 15%;
    // border-radius: 50%;
    display: flex;
    align-items: center;
    margin-left: 15px;
    display: inline-block;
    height: 32px;
    vertical-align: middle;
    transition: height 0.2s;
  }
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
  background-color: #eee;
  // background-color: #bebebe;
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
</style>
