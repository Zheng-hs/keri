module.exports = {
  lintOnSave: false, // false为关闭true为开启
  publicPath: './', // 编译后的资源路径

  chainWebpack: config => {
    // 生产模式
    config.when(process.env.NODE_ENV === 'production', config => {
      config
        .entry('app')
        .clear()
        .add('./src/main-prod.js')
    })

    // 开发模式
    config.when(process.env.NODE_ENV === 'development', config => {
      config
        .entry('app')
        .clear()
        .add('./src/main-dev.js')
    })
  },

  devServer: {
    proxy: {
      '/': {
        target: 'http://127.0.0.1:10088/', // 你要跨域的网址  比如  'http://news.baidu.com',
        // target: 'http://192.168.43.244:8080/', // 你要跨域的网址  比如  'http://news.baidu.com',
        // secure: true, // 如果是https接口，需要配置这个参数
        changeOrigin: true, // 这个参数是用来回避跨站问题的，配置完之后发请求时会自动修改http header里面的host，但是不会修改别的
        pathRewrite: {
          '^/api': '/' // 路径的替换规则
          // 这里的配置是正则表达式，以/api开头的将会被用用‘/api’替换掉，假如后台文档的接口是 /api/list/xxx
          // 前端api接口写：axios.get('/api/list/xxx') ， 被处理之后实际访问的是：http://news.baidu.com/api/list/xxx
        }
      }
    }
  }
}
