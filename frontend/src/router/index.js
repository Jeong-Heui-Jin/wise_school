import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/BeforeLogin/Login.vue'
import PasswordReset from '../views/BeforeLogin/PasswordReset'
import PasswordChange from '../views/BeforeLogin/PasswordChange'
import ServiceRequest from '../views/BeforeLogin/ServiceRequest'
import Home from '../views/AfterLogin/Home'
import Class from '../views/AfterLogin/Class'
import Timetable from '../views/AfterLogin/Timetable'
import Homework from '../views/AfterLogin/Homework'
import Notice from '../views/AfterLogin/Notice'
import Attendance from '../views/AfterLogin/Attendance'
import Attitude from '../views/AfterLogin/Attitude'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/password_reset',
    name: 'PasswordReset',
    component: PasswordReset,
  },
  {
    path: '/password_change',
    name: 'PasswordChange',
    component: PasswordChange,
  },
  {
    path: '/service_request',
    name: 'ServiceRequest',
    component: ServiceRequest,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/class',
    name: 'Class',
    component: Class,
  },
  {
    path: '/timetable',
    name: 'Timetable',
    component: Timetable,
  },
  {
    path: '/homework',
    name: 'Homework',
    component: Homework,
  },
  {
    path: '/notice',
    name: 'Notice',
    component: Notice,
  },
  {
    path: '/attendance',
    name: 'Attendance',
    component: Attendance,
  },
  {
    path: '/attitude',
    name: 'Attitude',
    component: Attitude,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
