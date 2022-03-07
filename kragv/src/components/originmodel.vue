<template>
  <div :class="{mobileClass:isMobile}">
    <el-card>
      <iframe style="height:80vh;"
              src="
       http://10.189.117.74:8088/home/index.html"
              width="100%"
              height="100%"></iframe>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 是否是移动端
      isMobile: false
    }
  },
  created () {
    // 处理移动端大小
    this.handleMobile()
  },
  methods: {
    // 分辨率改变时，处理控件的宽度
    handleWidth (width) {
      const screenWidth = window.innerWidth
      if (screenWidth < 1024) {
        return screenWidth * 0.8 + 'px'
      } else {
        return width + '%'
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
  }
}
</script>

<style  lang="less" scoped>
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
