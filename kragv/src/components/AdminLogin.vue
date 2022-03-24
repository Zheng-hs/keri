<template>
  <div>

  </div>
</template>

<script>
export default {
  data () {
    return {


    }
  },
  created () {
    this.turnToMobileLogin()
  },
  mounted () {
    this.adminLogin()
  },
  methods: {
    async adminLogin () {
      window.sessionStorage.setItem('token', "admin")
      window.sessionStorage.setItem('power', "1")
      window.sessionStorage.setItem('currentUser', "admin")
      window.sessionStorage.setItem('activePath', '/map')

      this.$router.push('/home')
    },

  }
}
</script>

<style lang="less" scoped>
</style>
