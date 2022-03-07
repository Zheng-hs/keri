import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
import Map from '../components/Map'
import TaskList from '../components/TaskList'
import AgvList from '../components/AgvList'
import TrafficControlList from '../components/TrafficControlList'
import TaskModel from '../components/taskModel/TaskModel'
import TaskModelAdd from '../components/taskModel/TaskModelAdd'
import TaskModelEdit from '../components/taskModel/TaskModelEdit'
import TaskModelPlus from '../components/taskModelPlus/TaskModelPlus'
import TaskModelAddPlus from '../components/taskModelPlus/TaskModelAddPlus'
import TaskModelEditPlus from '../components/taskModelPlus/TaskModelEditPlus'
import User from '../components/User'
import SystemTaskAdd from '../components/SystemTaskAdd'
import originmodel from '../components/originmodel'
// admin
import AdminHome from '../components/admin/AdminHome'

// test
import TestOrder from '../components/test/TestOrder'
import Testss from '../components/test/Testss'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  // TestOrder
  { path: '/testorder', component: TestOrder },
  { path: '/testss', component: Testss },
  {
    path: '/home',
    component: Home,
    redirect: '/map',
    children: [
      { path: '/map', component: Map },
      { path: '/tasklist', component: TaskList },
      { path: '/agvlist', component: AgvList },
      { path: '/trafficcontrollist', component: TrafficControlList },
      { path: '/taskmodel', component: TaskModel },
      { path: '/taskmodeladd', component: TaskModelAdd },
      { name: 'taskModelEdit', path: '/taskmodeledit', component: TaskModelEdit },
      { path: '/taskmodelplus', component: TaskModelPlus },
      { path: '/taskmodeladdplus', component: TaskModelAddPlus },
      { name: 'taskModelEditPlus', path: '/taskmodeleditplus', component: TaskModelEditPlus },
      { path: '/user', component: User },
      {
        path: '/systemtaskadd',
        component: SystemTaskAdd
      },
      {
        path: '/originmodel',
        component: originmodel
      }
    ]
  },
  // admin
  {
    path: '/admin',
    component: AdminHome,
    redirect: '/admin/map',
    children: [
      { path: '/admin/map', component: Map },
      { path: '/admin/tasklist', component: TaskList },
      { path: '/admin/agvlist', component: AgvList },
      { path: '/admin/trafficcontrollist', component: TrafficControlList },
      { path: '/admin/taskmodel', component: TaskModel },
      { path: '/admin/taskmodeladd', component: TaskModelAdd },
      { name: 'adminTaskModelEdit', path: '/admin/taskmodeledit', component: TaskModelEdit },
      { path: '/admin/user', component: User },
      {
        path: '/admin/systemtaskadd',
        component: SystemTaskAdd
      },
      {
        path: '/admin/originmodel',
        component: originmodel
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  if (to.path === '/mobileLogin') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  const powerStr = window.sessionStorage.getItem('power')
  if (to.path.indexOf('admin') != -1 && powerStr != '0') {
    return next(to.path.replace('/admin', ''))
  }
  next()
})

export default router
