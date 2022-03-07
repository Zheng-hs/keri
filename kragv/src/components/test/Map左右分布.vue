<template>
  <el-row :gutter="20">
    <el-col>
      <el-card id="mapCard"
               v-loading="loading">
        <!-- 地图 -->
        <svg xmlns="http://www.w3.org/2000/svg"
             viewBox="0 0 800.0 600.0"
             id="svgMap"
             :height="mapHeight"
             width="100%"></svg>

        <!-- 搜索框 -->
        <div id="searchMapArea"
             style="margin-top: 15px;">
          <el-input placeholder="请输入内容"
                    v-model="searchContent"
                    id="searchInput">
            <el-select v-model="searchSelect"
                       slot="prepend"
                       placeholder="请选择">
              <el-option v-for="item in searchOptions"
                         :key="item.value"
                         :label="item.label"
                         :value="item.value">
              </el-option>
            </el-select>
            <el-button slot="append"
                       icon="el-icon-search"
                       @click="locateSearchObject"></el-button>
          </el-input>
        </div>

        <!-- agv信息面板 -->
        <template v-if="agvInfoCardVissble">
          <el-card class="box-card"
                   id="agvInfoCard"
                   body-style="">
            <!-- 头部 -->
            <div slot="header"
                 class="clearfix">
              <span>{{agvClicked}}</span>
              <el-button size="medium"
                         :plain="true"
                         @click="agvInfoCardClose"
                         style="float: right; padding: 3px 0; font-size:10px;">
                <i class="el-icon-close"></i>
              </el-button>
            </div>
            <!-- 内容 -->
            <template>
              <el-carousel :interval="10000"
                           height="350px"
                           indicator-position="none"
                           :autoplay="false">
                <!-- 上线 + 电量 -->
                <el-carousel-item>
                  <div class="mainPlate">
                    <el-row :gutter="24">
                      <el-col :span="12"
                              class="mainPlateCol">
                        <!-- 在线状态 -->
                        <el-card body-style="padding-top: 10px;padding-bottom: 10px;">
                          <div id="onlineTitle"
                               class="mainCardTitle">连接状态</div>
                          <div>
                            <el-result :icon="agvClickedInfo.onLine=='on'?'success':'info'"
                                       :sub-title="agvClickedInfo.onLine=='on'?'在线':'离线'">
                            </el-result>
                          </div>

                        </el-card>
                        <!-- 在线状态 -->

                        <!-- 速度 -->
                        <el-card>
                          <div class="mainCardTitle">速度</div>
                          <div>
                            <el-progress :color="colors"
                                         type="dashboard"
                                         :width="80"
                                         :percentage="handleSpeedDashboard(agvClickedInfo.speed)"
                                         :format="speedDashboardFormat">

                            </el-progress>
                          </div>

                        </el-card>
                        <!-- 速度 -->

                      </el-col>
                      <el-col :span="12"
                              class="mainPlateCol">
                        <!-- 电量 -->
                        <el-card body-style="padding-top: 10px;padding-bottom: 10px;">
                          <div class="mainCardTitle">电量</div>
                          <div>
                            <el-progress :color="agvClickedInfo.batteryLevel >=30?'rgb(19, 206, 102)':'rgb(255, 73, 73)'"
                                         type="circle"
                                         :width="80"
                                         :percentage="agvClickedInfo.batteryLevel">
                            </el-progress>
                          </div>

                        </el-card>
                        <!-- 电量 -->

                        <!-- 车体状态 -->
                        <el-card>
                          <div class="mainCardTitle">运动状态</div>
                          <div>
                            <el-progress :color="agvClickedInfo.moveStatus =='Run'?'#67C23A':'#E6A23C'"
                                         type="circle"
                                         :width="80"
                                         :percentage="100"
                                         :format="moveStatusDashboardFormat">

                            </el-progress>
                          </div>

                        </el-card>
                        <!-- 车体状态 -->

                      </el-col>
                    </el-row>

                  </div>

                  <!-- <el-progress :class="agvClickedInfo.batteryLevel >=30?'batteryGreen':'batteryRed'"
                             type="circle"
                             :percentage="agvClickedInfo.batteryLevel">
                </el-progress> -->
                </el-carousel-item>
                <!-- 上线 + 电量 -->
                <!-- 装箱情况 + 卡号 -->
                <el-carousel-item>
                  <div class="mainPlate">
                    <el-row :gutter="24">
                      <el-col :span="12"
                              class="mainPlateCol">
                        <el-card>
                          <div class="mainCardTitle">装箱情况</div>
                          <div class="forkLayer">
                            <div v-for=" (item,i) in agvForkLayer"
                                 :key='i'>
                              <el-tag :color="item==0?'#909399':'#303133'">
                                <div class="forkLayerFont">插槽 - {{6-i}} </div>
                                <div class="agvBoxNumFont">{{agvBoxNum[i]==0?'无料号':agvBoxNum[i]}}</div>
                              </el-tag>

                            </div>

                          </div>
                        </el-card>
                      </el-col>
                      <el-col :span="12"
                              class="mainPlateCol">
                        <!-- 车辆区域 -->
                        <el-card body-style="padding-top: 10px;padding-bottom: 10px;">
                          <div class="mainCardTitle">所属区域</div>
                          <div class="rectContent">
                            <!-- <el-tag effect="plain">
                              {{ agvClickedInfo.agvArea }}
                            </el-tag> -->
                            <el-progress color="#67C23A"
                                         type="circle"
                                         :width="80"
                                         :percentage="100"
                                         :format="agvAreaDashboardFormat">

                            </el-progress>
                          </div>

                        </el-card>
                        <!-- 车辆区域 -->
                        <!-- 当前卡号 -->
                        <el-card>
                          <div class="mainCardTitle">当前位置</div>
                          <div class="plateCardNum">
                            <div>
                              <el-progress :color="agvClickedInfo.now !='0'?'#409EFF':'#E6A23C'"
                                           type="circle"
                                           :width="80"
                                           :percentage="100"
                                           :format="cardNowStatusDashboardFormat">

                              </el-progress>
                            </div>
                          </div>
                        </el-card>
                        <!-- 当前卡号 -->

                      </el-col>
                    </el-row>
                  </div>

                </el-carousel-item>
                <!-- 装箱情况 + 卡号 -->
                <!--  -->
                <!-- 详细数据 -->
                <el-carousel-item>
                  <template>
                    <el-table :data="agvInfoCardData"
                              stripe
                              :show-header="false"
                              max-height='400px'
                              style="width: 100%">
                      <el-table-column prop="agvValue"
                                       label="参数名"
                                       width="130">
                      </el-table-column>
                      <el-table-column prop="agvKey"
                                       label="参数"
                                       width="110">
                      </el-table-column>
                    </el-table>
                  </template>
                </el-carousel-item>

                <!-- 详细数据 -->
              </el-carousel>
            </template>

            <!-- 内容 -->
          </el-card>
        </template>
        <!-- agv信息面板 -->

        <!-- agv左侧信息面板 -->
        <template v-if="agvLeftInfoCardVisible">
          <el-card class="box-card"
                   id="agvLeftInfoCard">
            <!-- 头部 -->
            <div slot="header"
                 class="clearfix">
              <span>{{agvClicked}} 任务进度</span>
              <el-button size="medium"
                         :plain="true"
                         @click="agvLeftInfoCardClose"
                         style="float: right; padding: 3px 0; font-size:10px;">
                <i class="el-icon-close"></i>
              </el-button>

            </div>
            <!-- 内容 -->
            <template>

              <el-table :data="taskScheduleCardData"
                        stripe
                        :show-header="false"
                        style="width: 100%"
                        max-height='400px'>
                <el-table-column style="width: 100%"
                                 label="任务进度">
                  <template slot-scope="scope">

                    <template v-if="scope.row.taskActionList.length ==0">
                      <el-result icon="info"
                                 title="信息提示"
                                 subTitle="AGV空闲中">
                        <template slot="extra">

                        </template>
                      </el-result>
                    </template>
                    <template v-else>
                      {{scope.row.taskId}}
                      <el-steps :active="scope.row.taskActionIndex"
                                direction="vertical"
                                finish-status="success">
                        <el-step v-for="(item , i) in scope.row.taskActionList"
                                 :key='i'
                                 :title="item.pointId.toString()"
                                 :description="translateAction(item) "></el-step>
                      </el-steps>
                    </template>

                  </template>
                </el-table-column>
              </el-table>
            </template>
            <!-- 内容 -->
          </el-card>
        </template>
        <!-- agv左侧信息面板 -->

        <!-- 地图放大缩小按钮 -->
        <div id="btn-area">
          <el-button id="scale-up"
                     size='mini'
                     @click="svgPanZoomScaleUp"
                     icon="el-icon-plus"></el-button>

          <div></div>
          <el-button id="scale-down"
                     @click="svgPanZoomScaleDown"
                     size='mini'
                     icon="el-icon-minus"></el-button>

          <div></div>
          <el-button id="reset-btn"
                     @click="svgPanZoomReset"
                     size='mini'
                     icon="el-icon-location-outline"></el-button>

        </div>
        <!-- 地图放大缩小按钮 -->

        <!-- 左下角菜单功能按钮区 -->
        <div class="menuBtnArea"
             @click="menuBtnVisible = !menuBtnVisible">

          <el-button id="menuBtn"
                     circle
                     icon="el-icon-menu"></el-button>

          <template v-if="menuBtnVisible">
            <!-- 任务派发 -->
            <el-tooltip effect="dark"
                        content="任务派发"
                        placement="top">
              <transition name="slide-fade">
                <el-button @click="getTaskModel"
                           circle
                           icon="el-icon-notebook-1"></el-button>
              </transition>
            </el-tooltip>
            <!-- 任务派发 -->
            <!-- 充电检测 -->
            <el-tooltip effect="dark"
                        content="充电检测"
                        placement="top">
              <transition name="slide-fade">
                <el-button @click="openCheckAllEQ"
                           circle
                           icon="el-icon-set-up"></el-button>

              </transition>
            </el-tooltip>
            <!-- 充电检测 -->
            <!-- 交管释放 -->
            <el-tooltip effect="dark"
                        content="交管释放"
                        placement="top">
              <transition name="slide-fade">
                <el-button @click="freeControlAgvDialogOpen"
                           circle
                           icon="el-icon-unlock"></el-button>

              </transition>
            </el-tooltip>
            <!-- 交管释放 -->

          </template>
        </div>

        <!-- 左下角菜单功能按钮区 -->

        <!-- 左上角tip -->

        <!-- <el-link id="mapTip"
                 :underline="false">
          <i class="el-icon-info"></i>
        </el-link> -->
        <!-- 左上角tip -->

      </el-card>
    </el-col>

    <!-- 任务派发对话框 -->
    <el-dialog title="任务派发"
               :visible.sync="taskModelDialogVisible"
               width="630px">
      <!-- 搜索栏 -->
      <el-row :gutter="24">
        <el-col :span="15">
          <div class="taskModelToolBar">
            <div>任务模板名:</div>
            <div>
              <el-input class="searchInput"
                        clearable
                        placeholder="请输入任务模板名"
                        prefix-icon="el-icon-search"
                        @input="searchInputChange"
                        v-model="modelNameSearch"> </el-input>
            </div>
          </div>
        </el-col>
      </el-row>
      <!-- 搜索栏 -->
      <!-- 任务列表 -->
      <el-table :data="taskModelData.taskModelList"
                border
                highlight-current-row
                height="500px">
        <el-table-column label="任务模板名"
                         width="200px"
                         prop="taskModelName"></el-table-column>
        <el-table-column label="备注"
                         prop="remark"></el-table-column>
        <!-- 操作区 -->
        <el-table-column label="操作"
                         width="100px"
                         fixed="right">
          <template slot-scope="scope">
            <el-button type="primary"
                       size="mini"
                       @click="showBindBoxNumDialog(scope.row)">派发</el-button>
          </template>
        </el-table-column>
      </el-table>
      <!-- 任务列表 -->
    </el-dialog>
    <!-- 任务派发对话框 -->

    <!-- 任务派发&箱号绑定的对话框 -->
    <el-dialog title="箱号绑定"
               :visible.sync="bindBoxNumDialogVisible"
               width="630px">
      <!-- 流水线操作 -->
      <el-form ref="waterLineFormRef"
               :model="waterLineForm"
               :rules="waterLineFormRules"
               label-width="100px">
        <el-form-item label="有无流水线"
                      prop="actionOrNot">
          <el-switch v-model="waterLineForm.waterLineOrNot"
                     active-color="#13ce66"
                     inactive-color="#ff4949"
                     @change="handleWaterLineOrNot(waterLineForm.waterLineOrNot)">
          </el-switch>
        </el-form-item>
        <template v-if="waterLineForm.waterLineOrNot">
          <el-form-item label="上料/下料"
                        prop="inOrOut">
            <el-select v-model="waterLineForm.inOrOut"
                       placeholder="请选择"
                       clearable>
              <el-option label="上料"
                         value="G"></el-option>
              <el-option label="下料"
                         value="P"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="流水线点位"
                        prop="point">
            <el-input v-model="waterLineForm.point"></el-input>
          </el-form-item>

          <el-form-item label="友情提示">
            1_(_GR21E_000000_999999)
          </el-form-item>
          <el-form-item label="流水线动作"
                        prop="action">
            <el-input type="textarea"
                      v-model="waterLineForm.action"></el-input>
          </el-form-item>
        </template>

      </el-form>
      <!-- 流水线操作 -->

      <!-- 箱号绑定 -->
      <el-table :data="nodeList"
                border
                stripe
                height="350px">
        <el-table-column label="编号"
                         prop="id"></el-table-column>
        <el-table-column label="点位"
                         prop="From"></el-table-column>
        <el-table-column label="动作"
                         prop="action">
          <template slot-scope="scope">
            <template v-if="scope.row.action == 'G'">上料</template>
            <template v-else-if="scope.row.action == 'P'">下料</template>
            <template v-else>无</template>
          </template>
        </el-table-column>
        <el-table-column label="方向"
                         prop="direction">
          <template slot-scope="scope">
            <template v-if="scope.row.direction == 'R'">右</template>
            <template v-else-if="scope.row.direction == 'L'">左</template>
          </template>
        </el-table-column>
        <el-table-column label="货架层数"
                         prop="shelf_num"></el-table-column>

        <el-table-column label="箱号"
                         prop="boxNum"
                         width="100px">
          <template slot-scope="scope">
            <template v-if="scope.row.actionOrNot">
              <el-input size="mini"
                        v-model="scope.row.boxNum"></el-input>
            </template>
            <template v-else>
              <el-input size="mini"
                        :disabled="true"
                        v-model="scope.row.boxNum"></el-input>
            </template>

          </template>

        </el-table-column>

      </el-table>
      <!-- 箱号绑定 -->

      <!-- 底部区 -->
      <span slot="footer"
            class="dialog-footer">
        <el-button @click="bindBoxNumDialogVisible = false">取 消</el-button>
        <el-button type="primary"
                   @click="dispatchMission">派 发</el-button>
      </span>
    </el-dialog>
    <!-- 任务派发箱号绑定的对话框 -->

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
    <!-- 释放AGV对话框 -->

  </el-row>

</template>

<script>
import * as d3 from '../assets/js/d3.min'
import '../assets/js/jquery.svg.pan.zoom'

export default {
  data () {
    return {
      viewBoxInitWidth: 0,
      viewBoxInitHeight: 0,
      minX: null,
      minY: null,
      maxX: null,
      maxY: null,
      scale: null,
      mapObj: null,
      svgPanZoom: null,
      searchPointRes: {
        pointName: '',
        pointList: [],
        selectNum: 0,
        lastPoint: null
      },
      searchAgvRes: {
        agvName: '',
        agvList: [],
        selectNum: 0,
        lastAgv: null
      },
      svgNS: 'http://www.w3.org/2000/svg',
      oParent: null,
      oSvg: null,
      agvInfoClick: null,
      mapData: [],
      agvListDate: [],
      // map height
      mapHeight: window.innerHeight * 0.8,
      // map width
      mapWidth: window.innerWidth,
      loading: true,
      searchOptions: [{
        value: 'point',
        label: '点位'
      }, {
        value: 'agv',
        label: '车号'
      }],
      searchSelect: 'point',
      searchContent: '',
      agvClicked: '',
      // agv基础信息面板显示
      agvInfoCardVissble: false,
      // agv任务进度基础信息面板显示
      agvLeftInfoCardVisible: false,
      agvClickedInfo: {},
      agvInfoCardData: [{
        agvValue: '',
        agvKey: ''
      }],
      taskScheduleCardData: [],
      agvForkLayer: [0, 0, 0, 0, 0, 0],
      agvBoxNum: [0, 0, 0, 0, 0, 0],
      agvGreenPath: {},
      // 计时器
      timer: [],
      // 上次浏览时间
      lastBrowseDate: 0,
      // 清除timer延时器
      lastBrowseTimeouter: [],
      hiddenTimer: [],
      browseInterval: 1000 * 60 * 5,
      // 速度仪表盘颜色
      colors: [
        { color: '#f56c6c', percentage: 20 },
        { color: '#e6a23c', percentage: 40 },
        { color: '#5cb87a', percentage: 60 },
        { color: '#1989fa', percentage: 80 },
        { color: '#6f7ad3', percentage: 100 }
      ],
      // 左下角菜单按钮显示隐藏
      menuBtnVisible: false,
      // 任务模板框显示隐藏
      taskModelDialogVisible: false,
      // 任务模板信息
      taskModelData: {},
      // 任务模板搜索参数
      taskModelQueryInfo: {
        query: {},
      },
      // 任务模板名搜索框
      modelNameSearch: '',
      nodeList: [],
      // 控制bindBoxNum对话框的显示与隐藏
      bindBoxNumDialogVisible: false,
      // 流水线表单
      waterLineForm: {
        waterLineOrNot: false,
        inOrOut: '',
        point: '',
        action: ''
      },
      // 流水线表单的验证规则对象
      waterLineFormRules: {
      },
      waterLineFormRulesSource: {
        inOrOut: [{ required: true, message: '请选择上料/下料', trigger: 'blur' }],
        point: [{ required: true, message: '请输入点位', trigger: 'blur' }],
        action: [{ required: true, message: '请输入动作', trigger: 'blur' }],
      },
      // 凑数
      addTaskModelForm: {},

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
      receiveTrafficData: {},



    }
  },
  created () { },
  mounted () {
    this.mapInit()
    this.checkDocVis()
  },
  beforeDestroy () {
    this.cleanTimer()
    this.cleanHiddenTimer()
  },
  methods: {
    // 检测 document visible
    checkDocVis () {
      document.onvisibilitychange = () => {
        // let browseInterval = 1000 * 60 * 30
        // let browseInterval = 1000 * 60 * 5
        let browseInterval = this.browseInterval

        if (document.visibilityState == 'visible') {
          if (this.lastBrowseTimeouter.length > 0) {
            for (let i = 0; i < this.lastBrowseTimeouter.length; i++) {
              clearInterval(this.lastBrowseTimeouter.pop())
            }
            this.cleanHiddenTimer()
          }

          if (window.sessionStorage.mapDataSwitch == 'off') {
            window.sessionStorage.mapDataSwitch = 'on'
            window.location.reload()
          }
        } else {
          if (window.sessionStorage.mapDataSwitch == 'off') {
            this.cleanTimer()
          }
          this.lastBrowseTimeouter.push(setTimeout(() => {
            this.cleanTimer()
            window.sessionStorage.mapDataSwitch = 'off'
          }, browseInterval))
          this.lastBrowseTimeouter.push(setTimeout(() => {
            window.location.reload()
          }, browseInterval * 2))
        }

      }
    },
    // 地图初始化
    mapInit () {
      this.oParent = document.getElementById('mapDiv')
      this.oSvg = document.getElementById('svgMap')
      this.getMapInfo()
      setTimeout(() => {
        this.loading = false
      }, 500)
      this.reConnectMapInfo()
      setTimeout(() => {
        if (window.sessionStorage.mapDataSwitch == 'off') {
          this.cleanTimer()
          this.hiddenTimer.push(setInterval(() => {
            if (document.visibilityState == 'hidden') {
              window.location.reload()
            }
          }, this.browseInterval * 2.1))
        }

      }, 5000);
    },
    // 断线重连
    reConnectMapInfo () {
      this.timer.push(setInterval(() => {
        if (this.mapData.length == 0) {
          this.getMapInfo()
        }
      }, 10000))
    },
    // agv实时移动
    agvMoveRT () {
      this.getAgvState()
      this.timer.push(setInterval(() => {
        this.getAgvState()
      }, 1000))
    },
    // 获取地图信息
    async getMapInfo () {
      const { data: res } = await this.$http.get('getMapInfo')
      if (res.meta.status == 200) {
        this.mapData = res.data.mapInfoList
        await this.handleYAxis()
        await this.createMap(this.mapData, this.oSvg)
        this.svgPanZoom = await $('#svgMap').svgPanZoom()
        this.agvMoveRT()
        // setTimeout(() => {
        //   this.createMap(this.mapData, this.oSvg)
        //   setTimeout(() => {
        //     this.svgPanZoom = $('#svgMap').svgPanZoom()
        //     setTimeout(() => {
        //       this.agvMoveRT()
        //     }, 100);
        //   }, 100);
        // }, 100);


      }

    },
    // 获取agvList信息
    async getAgvState () {
      const { data: res } = await this.$http.get('getAgvState')

      if (res.meta.status == 200) {
        this.agvListDate = res.data.agvList
        this.agvMove(this.mapData, this.agvListDate, this.oSvg)
      }

    },
    // 清除timer
    cleanTimer () {
      for (let i = 0; i < this.timer.length; i++) {
        clearInterval(this.timer.pop())
      }
    },
    // 清除hiddenTimer
    cleanHiddenTimer () {
      for (let i = 0; i < this.hiddenTimer.length; i++) {
        clearInterval(this.hiddenTimer.pop())
      }
    },
    // svg ↑
    svgPanZoomScaleUp () {
      let vBWidth = Number(document.getElementById('svgMap').getAttribute('viewBox').split(' ')[2])

      if (vBWidth >= this.viewBoxInitWidth / 4) {
        this.svgPanZoom.zoomIn()
      }
    },
    // svg ↓
    svgPanZoomScaleDown () {
      let vBWidth = Number(document.getElementById('svgMap').getAttribute('viewBox').split(' ')[2])

      if (vBWidth < this.viewBoxInitWidth) {
        this.svgPanZoom.zoomOut()
      }

    },
    // svg ♨
    svgPanZoomReset () {
      this.svgPanZoom.reset()
    },

    createSvgTag (tag, objAttr) {
      var oTag = document.createElementNS(this.svgNS, tag)
      for (var attr in objAttr) {
        oTag.setAttribute(attr, objAttr[attr])
      }
      return oTag
    },
    handleYAxis () {
      let newMapData = this.mapData.map(point => {
        point.map_y = -point.map_y
        return point
      })
      this.mapData = newMapData

    },
    // 获取任务状态列表
    async getTaskModel () {
      const { data: res } = await this.$http.get('taskModelPlus', { params: this.taskModelQueryInfo })
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          showClose: true,
          message: res.meta.msg,
          type: 'error'
        })
      }
      this.taskModelData = res.data
      this.taskModelDialogVisible = true
    },
    // 检测搜索栏
    searchInputChange () {
      if (this.modelNameSearch !== '') {
        this.taskModelQueryInfo.query.taskModelName = this.modelNameSearch
      } else {
        this.taskModelQueryInfo.query = {}
      }
      this.getTaskModel()
    },
    // nodeList解码
    nodeListDecode (taskData) {
      let actionList = taskData.missionData
      if (!actionList) return
      this.addTaskModelForm.taskModelName = taskData.taskModelName
      this.addTaskModelForm.remark = taskData.remark

      if (taskData.inPoint || taskData.outPoint) {
        this.waterLineForm.waterLineOrNot = true
        if (taskData.inPoint) {
          this.waterLineForm.inOrOut = "G"
          this.waterLineForm.point = taskData.inPoint
          this.waterLineForm.action = taskData.inAction
        } else {
          this.waterLineForm.inOrOut = "P"
          this.waterLineForm.point = taskData.outPoint
          this.waterLineForm.action = taskData.outAction
        }
      }

      actionList.forEach((act, index) => {
        let nodeRow = {}
        if (act == '') {
          nodeRow.boxNum = ''
          nodeRow.From = ''
          nodeRow.direction = ''
          nodeRow.action = ''
          nodeRow.shelf_num = ''
          nodeRow.actionOrNot = false
          this.nodeList.push(nodeRow)
          return
        }

        nodeRow.boxNum = act.itemNum
        nodeRow.From = act.pointId
        nodeRow.direction = act.lr
        nodeRow.action = act.gp
        nodeRow.shelf_num = act.floorNum
        if (act.gp) {
          nodeRow.actionOrNot = true
        } else {
          nodeRow.actionOrNot = false
        }
        this.nodeList.push(nodeRow)

      })

      this.nodeList.forEach((node, index) => {
        node.id = index
      })
    },
    // 报文格式编码
    submitMsgEncode () {
      let subInfo = {}
      subInfo.dispatchId = (new Date()).getTime() + Math.ceil(Math.random() * 1000000)
      let missionData = []
      this.nodeList.forEach(node => {
        let temp = {}
        temp.itemNum = node.boxNum
        temp.pointId = node.From
        temp.lr = node.direction
        temp.gp = node.action
        temp.floorNum = node.shelf_num
        missionData.push(temp)
      })
      subInfo.missionData = missionData
      if (this.waterLineForm.waterLineOrNot) {
        if (this.waterLineForm.inOrOut == "G") {
          subInfo.inPoint = this.waterLineForm.point
          subInfo.inAction = this.waterLineForm.action
        } else {
          subInfo.outPoint = this.waterLineForm.point
          subInfo.outAction = this.waterLineForm.action
        }
      }
      subInfo.taskModelName = this.addTaskModelForm.taskModelName
      subInfo.remark = this.addTaskModelForm.remark
      return subInfo
    },
    // 箱号绑定框打开
    showBindBoxNumDialog (rowData) {
      if (rowData.missionData.length === 0) {
        // return this.$message.error('任务列表不能为空')
        return this.$message({
          showClose: true,
          message: '任务列表不能为空',
          type: 'error'
        })

      }
      this.nodeList = []
      this.submitForm = {}
      this.nodeListDecode(rowData)
      this.bindBoxNumDialogVisible = true
    },
    // 任务派发
    async dispatchMission (taskModel) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将提交任务, 是否继续?', '提示', {
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
          showClose: true,
          message: '已取消操作！',
          type: 'info'
        })
      }

      if (this.nodeList.length === 0) {
        // return this.$message.error('任务列表不能为空')
        return this.$message({
          showClose: true,
          message: '任务列表不能为空',
          type: 'error'
        })
      }

      if (this.waterLineForm.waterLineOrNot) {
        let res = false
        this.$refs.waterLineFormRef.validate(valid => {
          res = valid
        })
        if (!res) return
      }


      let subInfo = this.submitMsgEncode()

      const { data: res } = await this.$http.post('/dispatchMissionPlus', subInfo)
      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          type: 'error',
          message: res.meta.msg,
          showClose: true
        })
      }
      this.bindBoxNumDialogVisible = false
      // this.$message.success(res.meta.msg)
      this.$message({
        showClose: true,
        message: res.meta.msg,
        type: 'success'
      })
      this.taskModelDialogVisible = false

    },
    // 是否流水线
    handleWaterLineOrNot (waterLineOrNot) {
      if (waterLineOrNot) {
        this.waterLineFormRules = this.waterLineFormRulesSource
      } else {
        this.waterLineFormRules = {}
        // this.waterLineForm = {
        //   waterLineOrNot: false,
        //   inOrOut: '',
        //   point: '',
        //   action: ''
        // }
      }
    },
    // 打开充电检测
    async openCheckAllEQ () {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将打开充电检测, 是否继续?', '提示', {
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
          showClose: true,
          message: '已取消操作！',
          type: 'info'
        })
      }

      const { data: res } = await this.$http.get('/checkALLEQ')
      if (res.meta.status != 200) {
        // return this.$message.error(res.meta.msg)
        return this.$message({
          showClose: true,
          message: res.meta.msg,
          type: 'error'
        })
      }
      // this.$message.success(res.meta.msg)
      this.$message({
        showClose: true,
        message: res.meta.msg,
        type: 'success'
      })

    },

    // 释放交管区
    async freeControlArea (rowData) {
      // 弹框提示用户是否删除信息
      const confirmResult = await this.$confirm('此操作将释放该交管区, 是否继续?', '提示', {
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

      const { data: res } = await this.$http.get('freeControlArea', { params: { controlArea: rowData.controlArea } })
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
    // 获取任务状态列表
    async getTrafficInfoList () {
      const { data: res } = await this.$http.get('getTrafficInfo', {})
      if (res.meta.status !== 200) {
        // return this.$message.error(res.meta.msg)
        return console.log(res.meta.msg)
      }
      this.receiveTrafficData = res.data
    },
    // 打开 释放AGV dialog
    async freeControlAgvDialogOpen () {
      await this.getTrafficInfoList()
      this.agvOptions = []
      this.receiveTrafficData.trafficControlList.forEach(tfArea => {
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
    },

    structmapData (mapData) {
      const ret = {}
      this.mapData.forEach((point) => {

        const pointName = point.currentPoint
        ret[pointName] = point
      })
      return ret
    },

    structAgvListDate (agvListDate) {
      const ret = {}
      agvListDate.forEach((agv) => {
        const agvName = agv.agvId
        ret[agvName] = agv
      })
      return ret
    },

    getScale (mapData) {
      const winX = window.outerWidth
      const winY = window.outerHeight
      let maxX = null
      let maxY = null
      let minX = null
      let minY = null

      mapData.forEach((point) => {
        if (point.map_x > maxX || maxX == null) {
          maxX = point.map_x
        }
        if (point.map_y > maxY || maxY == null) {
          maxY = point.map_y
        }
        if (point.map_x < minX || minX == null) {
          minX = point.map_x
        }
        if (point.map_y < minY || minY == null) {
          minY = point.map_y
        }
      })

      if (minX == maxX && minX != null) {
        maxX += 10
      }

      if (minY == maxY && minY != null) {
        maxY += 10
      }

      const scale1 = winX / Math.abs(maxX - minX)
      const scale2 = winY / Math.abs(maxY - minY)
      const scaleRes = scale1 > scale2 ? scale2 : scale1

      return { scale: scaleRes, minX: minX, minY: minY, maxX: maxX, maxY: maxY }
    },

    switchAngle (radian) {
      return (radian * 180) / Math.PI
    },

    switchRadian (angle) {
      return (angle * Math.PI) / 180
    },

    objectFocus (point, oSvg, pointSize, pointFontSize, scale) {
      const pointStrokeColor = '#98999c'
      // let pointInfoFontColor = '#804000'
      const pointInfoFontColor = '#804000'
      const pointFontBgColor = '#d5d5d5'
      const pointFontBgStrokeColor = '#383838'

      // let pointFontSize = pointFontSize
      const pointSelect = document.getElementById(point.currentPoint)
      if (pointSelect != null) {
        pointSelect.setAttribute('stroke', pointStrokeColor)
        pointSelect.setAttribute('stroke-width', pointFontSize / 10)
        pointSelect.setAttribute('stroke-opti', 0.8)
      }

      const fontTagIsExist = document.getElementById(point.currentPoint + 'Info')
      if (fontTagIsExist == null) {
        // let pointNumIndex = point.currentPoint.indexOf('-')
        // let realPointNum = Number(point.currentPoint.substring(pointNumIndex +1)) + 1000000000
        const pointFontInitX = point.map_x * scale
        const pointFontInitY = point.map_y * scale - pointSize - pointFontSize
        const pointFontTag = this.createSvgTag('text', {
          id: point.currentPoint + 'Font',
          class: 'pointFontTag',
          x: pointFontInitX,
          y: pointFontInitY,
          'font-size': pointFontSize,
          fill: pointInfoFontColor,
          'text-anchor': 'middle'
          // 'style': 'cursor: pointer;',
        })

        pointFontTag.innerHTML = point.currentPoint

        const pointFontBgHeight = pointFontSize * 1.8
        const pointFontBgWidth =
          String(point.currentPoint).length * pointFontSize * 0.8
        const pointFontBgInitX = point.map_x * scale - pointFontBgWidth / 2
        const pointFontBgInitY =
          point.map_y * scale -
          pointFontBgHeight / 2 -
          pointSize -
          pointFontSize * 1.3
        const pointFontBgTag = this.createSvgTag('rect', {
          id: point.currentPoint + 'FontBg',
          class: 'pointFontBgTag',
          x: pointFontBgInitX,
          y: pointFontBgInitY,
          width: pointFontBgWidth,
          height: pointFontBgHeight,
          rx: (pointFontSize * 2) / 5,
          ry: (pointFontSize * 2) / 5,
          fill: pointFontBgColor,
          stroke: pointFontBgStrokeColor,
          opacity: 0.8,
          'stroke-width': pointFontSize / 10
        })

        const pointInfoTag = this.createSvgTag('g', {
          id: point.currentPoint + 'Info',
          style: 'cursor: pointer;'
        })

        pointInfoTag.appendChild(pointFontBgTag)
        pointInfoTag.appendChild(pointFontTag)
        //
        //

        oSvg.appendChild(pointInfoTag)
      }
    },

    objectBlur (point, oSvg) {
      const pointSelect = document.getElementById(point.currentPoint)
      // console.log(point);
      if (pointSelect != null) {
        pointSelect.removeAttribute('stroke')
        pointSelect.removeAttribute('stroke-width')
        pointSelect.removeAttribute('stroke-opti')
      }
      // console.log(pointSelect);
      const fontTag = document.getElementById(point.currentPoint + 'Info')
      if (fontTag != null) {
        oSvg.removeChild(fontTag)
      }
    },
    // 关闭信息框
    agvInfoCardClose () {
      // const agvInfoCardTag = document.getElementById('agvInfoCard')
      // agvInfoCardTag.style.visibility = 'hidden'
      this.agvInfoCardVissble = false

      // const agvLeftInfoCardTag = document.getElementById('agvLeftInfoCard')
      // agvLeftInfoCardTag.style.visibility = 'hidden'
    },
    // 关闭任务进度信息框
    agvLeftInfoCardClose () {
      // const agvInfoCardTag = document.getElementById('agvInfoCard')
      // agvInfoCardTag.style.visibility = 'hidden'

      // const agvLeftInfoCardTag = document.getElementById('agvLeftInfoCard')
      // agvLeftInfoCardTag.style.visibility = 'hidden'
      this.agvLeftInfoCardVisible = false
    },

    agvInfoCardUpdate (agv) {
      this.agvClicked = agv.agvId
      this.agvClickedInfo = agv
      let agvInfoRes = []
      agvInfoRes.push({
        agvValue: '车体区域',
        agvKey: agv.agvArea
      })
      agvInfoRes.push({
        agvValue: '任务状态',
        agvKey: agv.taskStatus
      })
      agvInfoRes.push({
        agvValue: '车体停止原因',
        agvKey: agv.agvStopReasonS
      })
      agvInfoRes.push({
        agvValue: '当前电量',
        agvKey: agv.batteryLevel
      })
      agvInfoRes.push({
        agvValue: '当前卡号',
        agvKey: agv.now
      })
      agvInfoRes.push({
        agvValue: '速度',
        agvKey: agv.speed
      })
      agvInfoRes.push({
        agvValue: '角度',
        agvKey: agv.headingAngle
      })

      this.agvInfoCardData = agvInfoRes


      if (agv.loading.length == 0 || agv.boxNum.length == 0) {
        this.agvForkLayer = [0, 0, 0, 0, 0, 0]
        this.agvBoxNum = [0, 0, 0, 0, 0, 0]
      } else {
        let tempLoading = JSON.parse(JSON.stringify(agv.loading))
        let tempBoxNum = JSON.parse(JSON.stringify(agv.boxNum))
        if (tempLoading.length > 6) { tempLoading = tempLoading.slice(0, 6) }
        if (tempBoxNum.length > 6) { tempBoxNum = tempBoxNum.slice(0, 6) }
        this.agvForkLayer = tempLoading.reverse()
        this.agvBoxNum = tempBoxNum.reverse()
      }

      // taskSchedule
      let taskActDate = {}
      taskActDate.taskId = agv.taskId
      taskActDate.taskActionList = agv.taskActionList
      taskActDate.taskActionIndex = agv.taskActionIndex
      let taskArrDate = [taskActDate]



      this.taskScheduleCardData = taskArrDate

    },

    // 任务进度翻译
    // "1_(_GR21E_000000_ffffff)"
    // "1_(_GR21E_000000_ffffff),
    // 2_(_PL53E_000000_ffffff,_PL54R_000000_ffffff)"
    translateAction (item) {
      let action = item.action
      let finishTime = item.finishTime
      if (action.trim() == '') {
        return "无动作"
      } else {
        let actionListStr = action.substring(action.indexOf('(') + 1, action.lastIndexOf(')'))
        let actionList = actionListStr.split(',')
        if (actionList.length == 1) {
          return this.translateSingleAction(actionList[0]) + '\n\n' + finishTime
        } else {
          let res = ''
          for (let i = 0; i < actionList.length; i++) {
            res += (i + 1) + '. ' + this.translateSingleAction(actionList[i]) + '\n'
          }
          res += '\n' + finishTime
          return res
        }

      }
    },

    // 翻译单个动作
    // "1_(_GR21E_000000_ffffff)"
    translateSingleAction (action) {
      let baseAct = ''
      let rackClass = ''
      let boxNum = action.substring(14, 21)
      let rackLayer = action[3]
      if (action[1] == 'G') {
        baseAct = 'G'
      } else if (action[1] == 'P') {
        baseAct = 'P'
      }

      if (action[5] == 'R') {
        rackClass = 'R'
      } else if (action[5] == 'E') {
        rackClass = 'E'
      }
      let res = ''

      if (baseAct == '' || rackClass == '') {
        return '无法识别动作'
      } else {
        if (baseAct == 'G') {
          if (rackClass == 'R') {
            res = '从货架第' + rackLayer + "层上料"
          } else if (rackClass == 'E') {
            res = '从接驳线第' + rackLayer + "层上料"
          }
        } else if (baseAct == 'P') {
          if (rackClass == 'R') {
            res = "下料到货架第" + rackLayer + "层"
          } else if (rackClass == 'E') {
            res = "下料到接驳线第" + rackLayer + "层"
          }
        }
      }
      if (boxNum != "999999") {
        res += "，\n箱号是" + boxNum
      }
      return res
    },


    // 速度dashboard 百分比处理
    handleSpeedDashboard (speed) {
      speed = Math.abs(speed)
      if (!speed) {
        return 0
      }
      if (speed >= 2) {
        return 100
      } else if (speed <= 0) {
        return 0
      } else {
        return speed / 2 * 100
      }
    },

    // 速度dashboard format
    speedDashboardFormat (percentage) {
      return Math.abs(this.agvClickedInfo.speed.toFixed(3)) + 'm/s'
    },

    // 车体状态dashboard format
    moveStatusDashboardFormat (percentage) {
      return this.agvClickedInfo.moveStatus
    },

    // 卡号状态dashboard format
    cardNowStatusDashboardFormat (percentage) {
      if (this.agvClickedInfo.now != 0) {
        return this.agvClickedInfo.now
      } else {
        return '无法识别'
      }

    },

    // 车辆区域dashboard format
    agvAreaDashboardFormat (percentage) {
      return this.agvClickedInfo.agvArea
    },

    agvClick (agv) {
      this.agvInfoCardUpdate(agv)

      // console.log(agv)
      // const agvInfoCard = document.getElementById('agvInfoCard')
      // agvInfoCard.style.visibility = 'visible'
      this.agvInfoCardVissble = true



      // const agvLeftInfoCard = document.getElementById('agvLeftInfoCard')
      // agvLeftInfoCard.style.visibility = 'visible'
      this.agvLeftInfoCardVisible = true
    },

    agvFocus (agv, oSvg) {
      const agvSelect = document.getElementById(agv.agvId)
      const agvInfoSelect = document.getElementById(agv.agvId + 'Info')
      if (agvSelect != null && agvInfoSelect != null) {
        oSvg.removeChild(agvSelect)
        oSvg.removeChild(agvInfoSelect)
      }
      oSvg.appendChild(agvSelect)
      oSvg.appendChild(agvInfoSelect)
    },

    agvBlur (agv, oSvg) { },

    setScaleAndViewBox (mapData, oSvg) {
      const getScaleRes = this.getScale(mapData)
      this.scale = getScaleRes.scale
      this.minX = getScaleRes.minX
      this.minY = getScaleRes.minY
      this.maxX = getScaleRes.maxX
      this.maxY = getScaleRes.maxY

      const oSvgWidth = Math.abs(this.maxX - this.minX) * this.scale * 1.1
      const oSvgHeight = Math.abs(this.maxY - this.minY) * this.scale * 1.1
      const oSvgX = (this.minX) * this.scale - (oSvgWidth * 0.05)
      const oSvgY = (this.minY) * this.scale - (oSvgHeight * 0.05)
      const viewBoxAttr = oSvgX + ' ' + oSvgY + ' ' + oSvgWidth + ' ' + oSvgHeight
      this.viewBoxInitWidth = oSvgWidth
      this.viewBoxInitHeight = oSvgHeight
      oSvg.setAttribute('viewBox', viewBoxAttr)
    },

    createMap (mapData, oSvg) {
      // const backgroundMapHref = './map_resource/img/map.jpg'

      const pointSize = 3
      let pointColor = '#fffffe'
      const pointOpacity = 0.7
      let pathColor = '#0080008a'
      const pathWidth = 2
      const pathOpacity = 0.9
      const pointFontSize = 5
      let backgroundMapHref = null

      try {
        backgroundMapHref = require('../assets/img/map.jpg')
      } catch (error) {
        console.log(error)
      }

      if (this.mapObj == null) {
        this.mapObj = this.structmapData(mapData)
      }
      if (this.scale == null) {
        this.setScaleAndViewBox(mapData, oSvg)
      }
      const scale = this.scale
      const mapObj = this.mapObj

      // 底图绘制
      if (mapObj['Point-0001'] != null && mapObj['Point-0002'] != null && backgroundMapHref != null) {
        const p1 = mapObj['Point-0001']
        const p2 = mapObj['Point-0002']
        const backgroundMapX = p1.map_x * scale
        const backgroundMapY = p1.map_y * scale
        const backgroundMapWidth = Math.abs(p2.map_x - p1.map_x) * scale
        const backgroundMapHeight = Math.abs(p2.map_y - p1.map_y) * scale
        const backgroundMapTag = this.createSvgTag('image', {
          id: 'backgroundMap',
          // 'class':'agvTag',
          x: backgroundMapX,
          y: backgroundMapY,
          width: backgroundMapWidth,
          height: backgroundMapHeight,
          // 'style': 'cursor: pointer;',
          href: backgroundMapHref
          // 'href':{'baseVal':"./img/agv.png"},
        })
        oSvg.appendChild(backgroundMapTag)
      } else {
        // oSvg.style.background = '#303133'
        pointColor = '#171746'
      }

      // path绘制
      this.mapData.forEach((point) => {
        const startPoint = point.map_x * scale + ' ' + point.map_y * scale
        if (
          Object.prototype.toString.call(point.targetPoint).indexOf('String') !== -1
        ) {
          point.targetPoint = JSON.parse(point.targetPoint)
        }

        if (point.BezierControlPoints != null) {
          if (
            Object.prototype.toString
              .call(point.BezierControlPoints)
              .indexOf('String') !== -1
          ) {
            point.BezierControlPoints = JSON.parse(point.BezierControlPoints)
          }
        } else {
          point.BezierControlPoints = []
        }

        point.targetPoint.forEach((tp) => {
          if (!mapObj[tp]) {
            return false
          }
          const endPoint = mapObj[tp].map_x * scale + ' ' + mapObj[tp].map_y * scale
          let tagDAttr = ''
          if (point.BezierControlPoints[point.targetPoint.indexOf(tp)] != null) {
            tagDAttr = 'M' + startPoint + ' C'
            point.BezierControlPoints[point.targetPoint.indexOf(tp)].forEach(
              (aPoint) => {
                tagDAttr =
                  tagDAttr + ' ' + aPoint.x * scale + ' ' + aPoint.y * scale
              }
            )
            tagDAttr = tagDAttr + ' ' + endPoint
          } else {
            tagDAttr = 'M' + startPoint + 'L' + endPoint
          }

          const pathTag = this.createSvgTag('path', {
            id: point.currentPoint + '---' + tp,
            class: 'pathTag',
            d: tagDAttr,
            stroke: pathColor,
            'stroke-width': pathWidth,
            fill: 'none',
            opacity: pathOpacity,
            // style: 'cursor: pointer;visibility:hidden;',
            style: 'visibility:hidden;'
          })
          oSvg.appendChild(pathTag)
        })
      })

      // point绘制
      this.mapData.forEach((point) => {
        if (
          point.currentPoint === 'Point-0001' ||
          point.currentPoint === 'Point-0002'
        ) {
          return false
        }
        const pointTag = this.createSvgTag('rect', {
          id: point.currentPoint,
          class: 'pointTag',
          x: point.map_x * scale - (1 / 2) * pointSize,
          y: point.map_y * scale - (1 / 2) * pointSize,
          fill: pointColor,
          width: pointSize,
          height: pointSize,
          opacity: pointOpacity,
          // 'stroke':"black",
          // 'stroke-width':"1"
          style: 'cursor: pointer;'
        })
        pointTag.onmouseenter = () => {
          this.objectFocus(point, oSvg, pointSize, pointFontSize, scale)
        }

        pointTag.onmouseleave = () => {
          this.objectBlur(point, oSvg)
        }

        oSvg.appendChild(pointTag)
      })
    },

    agvMove (mapData, agvListDate, oSvg) {
      const agvImgWidth = 28
      const agvImgHeight = 14
      const agvFontSize = 5
      // const agvImg = './map_resource/img/keriAGV.png'
      const agvImg = require('../assets/img/keriAGV.png')
      const agvFontColor = '#804000'
      const agvFontBgColor = '#d5d5d5'
      const agvFontBgOpacity = 0.8
      const agvFontStrokeColor = '#383838'

      if (this.mapObj == null) {
        this.mapObj = this.structmapData(mapData)
      }
      if (this.scale == null) {
        this.setScaleAndViewBox(mapData, oSvg)
      }
      const scale = this.scale
      const mapObj = this.mapObj

      const agvImgCEdge = Math.sqrt(
        Math.pow(agvImgHeight, 2) + Math.pow(agvImgWidth, 2)
      )

      agvListDate.forEach((agv) => {
        if (agv.onLine === 'on' && agv.now !== '' && agv.now !== '0' && mapObj[agv.now] != null) {

          const pointNowName = agv.now
          const agvNowPoint = mapObj[pointNowName]
          const pointToName = agv.to
          const agvToPoint = mapObj[pointToName]
          const pointYetName = agv.yet
          const agvYetPoint = mapObj[pointYetName]


          if (agvNowPoint != null) {
            // 隐藏的线
            if (this.agvGreenPath[agv.agvId] == null) {
              this.agvGreenPath[agv.agvId] = []
            } else {
              this.agvGreenPath[agv.agvId].forEach(agPath => {
                const toHiddenPath = document.getElementById(agPath)
                if (toHiddenPath != null) {
                  toHiddenPath.setAttribute(
                    'style',
                    // 'cursor: pointer;visibility:hidden;'
                    'visibility:hidden;'
                  )
                }
              })
              this.agvGreenPath[agv.agvId] = []
            }
            // 路线绘制
            if (agv.taskList != null && agv.taskList.length !== 0) {
              const taskIndex = agv.taskIndex
              const taskList = agv.taskList


              // 要绿的线
              for (let i = taskIndex; i < agv.taskList.length - 1; i++) {
                const toLightPathId = taskList[i] + '---' + taskList[i + 1]
                this.agvGreenPath[agv.agvId].push(toLightPathId)
                const toLightPath = document.getElementById(toLightPathId)
                if (toLightPath != null) {
                  toLightPath.setAttribute(
                    'style',
                    // 'cursor: pointer;visibility:visible;'
                    'visibility:visible;'
                  )
                }
              }
            }

            // agvNowPoint.headingAngleForMap = JSON.parse(agvNowPoint.headingAngleForMap)
            let agvAngle = 0
            const agvSysAngle = agv.headingAngle
            // 角度为空则自动判断
            if (agvSysAngle != null) {
              agvAngle = this.switchRadian(Number(agvSysAngle))
            } else {
              if (agvToPoint != null && agvToPoint !== 0) {
                // let angleIndex = agvNowPoint.targetPoint.indexOf(agvToPoint.currentPoint)
                // if (angleIndex != -1) {
                //   agvAngle = Number(agvNowPoint.headingAngleForMap[angleIndex])
                // }
                agvAngle = -Math.atan2(
                  agvToPoint.map_y * scale - agvNowPoint.map_y * scale,
                  agvToPoint.map_x * scale - agvNowPoint.map_x * scale
                )
              } else if (agvYetPoint != null && agvYetPoint !== 0) {
                agvAngle = -Math.atan2(
                  agvNowPoint.map_y * scale - agvYetPoint.map_y * scale,
                  agvNowPoint.map_x * scale - agvYetPoint.map_x * scale
                )
              } else {
                const agvFakeToPoint = mapObj[agvNowPoint.targetPoint[0]]
                if (agvFakeToPoint != null) {
                  agvAngle = -Math.atan2(
                    agvFakeToPoint.map_y * scale - agvNowPoint.map_y * scale,
                    agvFakeToPoint.map_x * scale - agvNowPoint.map_x * scale
                  )
                }
              }
            }

            const agvX = agvNowPoint.map_x * scale
            const agvY = agvNowPoint.map_y * scale

            // let agvX = agvNowPoint.map_x*scale - Math.cos(agvAngle - Math.atan2(agvImgHeight , agvImgWidth)) * (agvImgCEdge / 2)
            // let agvY = agvNowPoint.map_y*scale + Math.sin(agvAngle - Math.atan2(agvImgHeight , agvImgWidth)) * (agvImgCEdge / 2)
            const fontX = agvNowPoint.map_x * scale
            // let fontY = agvNowPoint.map_y*scale
            // let fontY = agvNowPoint.map_y*scale + (agvImgCEdge / 2)
            // while (agvAngle < 0) {
            //   agvAngle += 2 * Math.PI;
            // }
            const fontY =
              agvNowPoint.map_y * scale -
              Math.abs(Math.sin(agvAngle - Math.atan2(agvImgHeight, agvImgWidth))) *
              (agvImgCEdge / 2)

            const agvOnSvg = document.getElementById(agv.agvId)
            if (agvOnSvg == null) {
              const agvImgTag = this.createSvgTag('image', {
                id: agv.agvId + 'Img',
                class: 'agvImgTag',
                x: -agvImgWidth / 2,
                y: -agvImgHeight / 2,
                width: agvImgWidth,
                height: agvImgHeight,
                style: 'cursor: pointer;',
                href: agvImg
                // 'href':{'baseVal':"./img/agv.png"},
              })

              const agvBgTag = this.createSvgTag('circle', {
                id: agv.agvId + 'Bg',
                class: 'agvBgTag',
                // cx: -agvImgWidth / 2,
                // cy: -agvImgHeight / 2,
                r: agvImgWidth / 2,
                fill: 'none'
                // stroke:"red",
                // 'stroke-width':"5",
                // 'stroke-opacity':"0.1",
              })

              const agvTag = this.createSvgTag('g', {
                id: agv.agvId,
                style: 'cursor: pointer;'
              })

              agvTag.appendChild(agvBgTag)
              agvTag.appendChild(agvImgTag)

              const agvFontInitX = 0
              const agvFontInitY = -agvFontSize * 1.5
              const agvFontTag = this.createSvgTag('text', {
                id: agv.agvId + 'Font',
                class: 'agvFontTag',
                x: agvFontInitX,
                y: agvFontInitY,
                'font-size': agvFontSize,
                fill: agvFontColor,
                'text-anchor': 'middle'
                // 'style': 'cursor: pointer;',
              })

              agvFontTag.innerHTML = agv.agvId

              const agvFontBgHeight = agvFontSize * 1.8
              // let agvFontBgWidth = agvFontSize * 4.5
              const agvFontBgWidth = String(agv.agvId).length * agvFontSize * 0.8
              const agvFontBgInitX = -agvFontBgWidth / 2
              const agvFontBgInitY = -agvFontBgHeight / 2 - agvFontSize * 1.8
              const agvFontBgTag = this.createSvgTag('rect', {
                id: agv.agvId + 'FontBg',
                class: 'agvFontBgTag',
                x: agvFontBgInitX,
                y: agvFontBgInitY,
                width: agvFontBgWidth,
                height: agvFontBgHeight,
                rx: (agvFontSize * 2) / 5,
                ry: (agvFontSize * 2) / 5,
                fill: agvFontBgColor,
                opacity: agvFontBgOpacity,
                stroke: agvFontStrokeColor,
                'stroke-width': agvFontSize / 10
              })

              const agvInfoTag = this.createSvgTag('g', {
                id: agv.agvId + 'Info',
                style: 'cursor: pointer;'
              })

              agvInfoTag.appendChild(agvFontBgTag)
              agvInfoTag.appendChild(agvFontTag)

              // agvTag.onmouseenter = () => {
              //   agvFocus(agv, oSvg)
              // }
              // agvInfoTag.onmouseleave = () => {
              //   agvBlur(agv, oSvg)
              // }
              agvTag.onclick = () => {
                this.agvClick(agv)
              }
              agvInfoTag.onclick = () => {
                this.agvClick(agv)
              }

              oSvg.appendChild(agvTag)
              oSvg.appendChild(agvInfoTag)

              d3.select('#' + agv.agvId)
                // .transition()
                // .duration(1000)
                .attr(
                  'transform',
                  `translate(${agvX},${agvY})  rotate(${-this.switchAngle(agvAngle)})`
                )

              d3.select('#' + agv.agvId + 'Info')
                // .transition()
                // .duration(1000)
                .attr('transform', `translate(${fontX},${fontY})  `)

              if (agv.agvStopReasonS == null || agv.agvStopReasonS == '' ||
                agv.agvStopReasonS == 'STOP_ACT' ||
                agv.agvStopReasonS == 'STOP_CARD') {
                d3.select('#' + agv.agvId + 'Bg').attr(
                  'style',
                  'animation: aniGreen 3s linear infinite;'
                )
              } else if (agv.agvStopReasonS != null || agv.agvStopReasonS != '') {
                d3.select('#' + agv.agvId + 'Bg').attr(
                  'style',
                  'animation: aniRed 3s linear infinite;'
                )
              }

            } else {
              // agv移动
              d3.select('#' + agv.agvId)
                .transition()
                .duration(1000)
                .attr(
                  'transform',
                  `translate(${agvX},${agvY})  rotate(${-this.switchAngle(agvAngle)})`
                )

              // Info移动
              d3.select('#' + agv.agvId + 'Info')
                .transition()
                .duration(1000)
                .attr('transform', `translate(${fontX},${fontY})  `)

              if (agv.agvStopReasonS == null || agv.agvStopReasonS == '' ||
                agv.agvStopReasonS == 'STOP_ACT' ||
                agv.agvStopReasonS == 'STOP_CARD') {
                d3.select('#' + agv.agvId + 'Bg').attr(
                  'style',
                  'animation: aniGreen 3s linear infinite;'
                )
              } else if (agv.agvStopReasonS != null || agv.agvStopReasonS != '') {
                d3.select('#' + agv.agvId + 'Bg').attr(
                  'style',
                  'animation: aniRed 3s linear infinite;'
                )
              }


            }
          }
        } else {
          const notExistAgv = document.getElementById(agv.agvId)
          const notExistAgvFont = document.getElementById(agv.agvId + 'Info')

          if (notExistAgv != null) {
            oSvg.removeChild(notExistAgv)
            oSvg.removeChild(notExistAgvFont)
          }

          // 隐藏的线
          if (this.agvGreenPath[agv.agvId] == null) {
            this.agvGreenPath[agv.agvId] = []
          } else {
            this.agvGreenPath[agv.agvId].forEach(agPath => {
              const toHiddenPath = document.getElementById(agPath)
              if (toHiddenPath != null) {
                toHiddenPath.setAttribute(
                  'style',
                  // 'cursor: pointer;visibility:hidden;'
                  'visibility:hidden;'
                )
              }
            })
            this.agvGreenPath[agv.agvId] = []
          }

        }

        // const agvInfoCard = document.getElementById('agvInfoCard')
        if (
          // agvInfoCard.style.visibility === 'visible' &&
          (this.agvInfoCardVissble || this.agvLeftInfoCardVisible) == true &&
          this.agvClicked === agv.agvId
        ) {
          this.agvInfoCardUpdate(agv)
        }
      })
    },

    // 定位到选定物
    locateSearchObject () {
      if (this.searchSelect === 'point') {
        this.locatePoint(this.searchContent)
      } else if (this.searchSelect === 'agv') {
        this.locateAgv(this.searchContent)
      }
    },

    // 定位点位
    locatePoint (pointName) {
      const pointSize = 3
      const pointFontSize = 5
      const searchPointRes = this.searchPointRes
      // let pointName = document.getElementById('pointName').value

      if (searchPointRes.pointName !== pointName) {
        searchPointRes.pointList = []
        searchPointRes.selectNum = 0
        searchPointRes.pointName = pointName
        this.mapData.forEach((point) => {
          if (
            point.currentPoint === 'Point-0001' ||
            point.currentPoint === 'Point-0002'
          ) {
            return false
          }
          if (point.currentPoint.indexOf(pointName) !== -1) {
            searchPointRes.pointList.push(point)
          }
        })
      }

      const selectNum = searchPointRes.selectNum
      const pointListLen = searchPointRes.pointList.length
      const pointList = searchPointRes.pointList
      const lastPoint = searchPointRes.lastPoint
      if (pointListLen > 0) {
        if (lastPoint != null) {
          // let tempPoint = document.getElementById(searchPointRes.lastPoint.currentPoint)
          // tempPoint.removeAttribute('stroke')
          // tempPoint.removeAttribute('stroke-width')
          // tempPoint.removeAttribute('stroke-opti')
          this.objectBlur(searchPointRes.lastPoint, this.oSvg)
        }

        searchPointRes.selectNum = (selectNum + 1) % pointListLen
        const selectPoint = pointList[selectNum]
        // document.getElementById(selectPoint.currentPoint).setAttribute('stroke' , 'red')
        // document.getElementById(selectPoint.currentPoint).setAttribute('stroke-width' , 2)
        // document.getElementById(selectPoint.currentPoint).setAttribute('stroke-opti' , 2)
        this.objectFocus(selectPoint, this.oSvg, pointSize, pointFontSize, this.scale)
        searchPointRes.lastPoint = selectPoint
        // console.log(selectPoint)
        this.svgPanZoom.setCenter(selectPoint.map_x * this.scale, selectPoint.map_y * this.scale)
      }
    },

    // 定位agv
    locateAgv (agvName) {
      // let agvName = document.getElementById('agvName').value
      const searchAgvRes = this.searchAgvRes

      if (searchAgvRes.agvName !== agvName) {
        searchAgvRes.agvList = []
        searchAgvRes.selectNum = 0
        searchAgvRes.agvName = agvName
        this.agvListDate.forEach((agv) => {
          if (
            agv.agvId.indexOf(agvName) !== -1 &&
            agv.onLine === 'on' &&
            agv.now !== '' &&
            this.mapObj[agv.now] != null
          ) {
            searchAgvRes.agvList.push(agv)
          }
        })
      }

      const selectNum = searchAgvRes.selectNum
      const agvListLen = searchAgvRes.agvList.length
      const agvList = searchAgvRes.agvList
      // const lastAgv = searchAgvRes.lastAgv
      if (agvListLen > 0) {
        searchAgvRes.selectNum = (selectNum + 1) % agvListLen
        const selectAgv = agvList[selectNum]
        searchAgvRes.lastAgv = selectAgv
        const selectAgvTag = document.getElementById(selectAgv.agvId)
        const transformAttr = selectAgvTag.getAttribute('transform')
        // console.log(transformAttr)
        if (transformAttr != null) {
          const agvX = transformAttr.substring(
            transformAttr.indexOf('(') + 1,
            transformAttr.indexOf(',')
          )
          const agvY = transformAttr.substring(
            transformAttr.indexOf(',') + 1,
            transformAttr.indexOf(')')
          )
          // console.log(agvX)
          // console.log(agvY)
          this.svgPanZoom.setCenter(agvX, agvY)
        }
      }
    }
    //
  }
}
</script>

<style lang="less" scoped>
#mapCard {
  position: relative;
}

#svgMap {
  background: #c3c3c31c;
}

#searchMapArea {
  position: absolute;
  right: 5%;
  top: 3%;
  z-index: 5;
  opacity: 0.9;
  width: 300px;
  .el-select {
    width: 75px !important;
  }
}

#agvInfoCard {
  width: 300px;
  height: 450px;
  // visibility: hidden;
  position: absolute;
  right: 5%;
  top: 13%;
  z-index: 5;
  opacity: 0.9;

  .el-table {
    padding-top: 0;
    margin-top: 0;
    border-top: 0;
  }

  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background-color: #f5f5f5;
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #c8c8c8;
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }
}

#agvLeftInfoCard {
  width: 300px;
  // visibility: hidden;
  position: absolute;
  left: 5%;
  top: 3%;
  z-index: 5;
  opacity: 0.9;
  .el-table {
    padding-top: 0;
    margin-top: 0;
    border-top: 0;
  }

  ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  ::-webkit-scrollbar-track {
    background-color: #f5f5f5;
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }
  ::-webkit-scrollbar-thumb {
    background-color: #c8c8c8;
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }
}

#btn-area {
  padding: 0px;
  position: absolute;
  right: 5%;
  bottom: 5%;
  background-color: rgba(0, 0, 0, 0);
  z-index: 5;
  div {
    padding: 2px;
  }
}

// 上线 + 电量
.mainPlate {
  .mainPlateCol {
    // padding: 0px;
    // padding-bottom: 0%;
    height: 100%;
    // font-size: 20px;
    // font-weight: 700;
    display: flex;
    flex-direction: column;
    // span {
    //   color: #fff;
    // }
    .el-card {
      .mainCardTitle {
        display: flex;
        justify-content: center;
        padding-bottom: 20px;
        // padding: 6px 20px !important;
      }
      #onlineTitle {
        padding-bottom: 10px;
      }
      .el-result {
        padding: 0;
        .el-result__subtitle {
          margin-top: 0;
        }
      }
      height: 50%;
      .rectContent {
        display: flex;
        justify-content: center;
      }
    }
  }
}

// 装箱情况
.forkLayer {
  // position: absolute;
  // left: 50%;
  // transform: translateX(-100%);
  .el-tag {
    width: 100%;
    height: 2.6rem !important;
    display: flex;
    justify-content: center;
    flex-direction: column;
    .forkLayerFont {
      color: #fff;
      font-size: 14px;
      text-align: center;
      font-weight: 500;
      line-height: 1.3;
    }
    .agvBoxNumFont {
      color: #fff;
      font-size: 10px;
      text-align: center;
      // font-weight: 500;
      line-height: 1.5;
    }
  }
}

// 左下角菜单功能按钮区
.menuBtnArea {
  padding: 0px;
  position: absolute;
  left: 5%;
  bottom: 5%;
  background-color: rgba(0, 0, 0, 0);
  z-index: 5;
  div {
    padding: 2px;
  }
}

//左下角菜单功能按钮区动画
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
  transform: translateX(-20px);
  opacity: 0;
}

// 任务模板工具栏
.taskModelToolBar {
  display: flex;
  justify-content: center;
  align-items: center;
  div {
    padding: 5px;
  }
}

// #mapTip {
//   position: absolute;
//   left: 3%;
//   top: 6%;
//   z-index: 5;
//   opacity: 0.9;
// }
</style>
