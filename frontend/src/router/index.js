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
import HomeworkCreate from '../views/AfterLogin/HomeworkCreate'
import HomeworkView from '../views/AfterLogin/HomeworkView'
import HomeworkChange from '../views/AfterLogin/HomeworkChange'
import HomeworkStatus from '../views/AfterLogin/HomeworkStatus'
import HomeworkStudent from '../views/AfterLogin/HomeworkStudent'
import Notice from '../views/AfterLogin/Notice'
import NoticeCreate from '../views/AfterLogin/NoticeCreate'
import NoticeView from '../views/AfterLogin/NoticeView'
import Attendance from '../views/AfterLogin/Attendance'
import Attitude from '../views/AfterLogin/Attitude'
import AttitudeInfo from '../views/AfterLogin/AttitudeInfo'
import AttitudeCreate from '../views/AfterLogin/AttitudeCreate'
import AttitudeView from '../views/AfterLogin/AttitudeView'
import AttitudeChange from '../views/AfterLogin/AttitudeChange'
import StudentInfo from '../views/AfterLogin/StudentInfo'
import TimetableChange from '../views/AfterLogin/TimetableChange'
import Notification from '../views/AfterLogin/Notification'
import HomeworkSubmit from '../views/AfterLogin/HomeworkSubmit'
import MyPage from '../views/AfterLogin/MyPage'

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
    props: true,
  },
  {
    path: '/password_change',
    name: 'PasswordChange',
    component: PasswordChange,
    props: true,
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
    path: '/student_info/:id',
    name: 'StudentInfo',
    component: StudentInfo,
  },
  {
    path: '/timetable',
    name: 'Timetable',
    component: Timetable,
  },
  {
    path: '/timetable_change',
    name: 'TimetableChange',
    component: TimetableChange
  },
  {
    path: '/homework',
    name: 'Homework',
    component: Homework,
  },
  {
    path: '/homework_create',
    name: 'HomeworkCreate',
    component: HomeworkCreate,
  },
  {
    path: '/homework_view',
    name: 'HomeworkView',
    component: HomeworkView,
    props: true,
  },
  {
    path: '/homework_change',
    name: 'HomeworkChange',
    component: HomeworkChange,
  },
  {
    path: '/homework_status',
    name: 'HomeworkStatus',
    component: HomeworkStatus,
  },
  {
    path: '/homework_student',
    name: 'HomeworkStudent',
    component: HomeworkStudent,
  },
  {
    path: '/notice',
    name: 'Notice',
    component: Notice,
  },
  {
    path: '/notice_create',
    name: 'NoticeCreate',
    component: NoticeCreate,
  },
  {
    path: '/notice_view',
    name: 'NoticeView',
    component: NoticeView,
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
  {
    path: '/attitude_info/:id',
    name: 'AttitudeInfo',
    component: AttitudeInfo,
  },
  {
    path: '/attitude_create/:id',
    name: 'AttitudeCreate',
    component: AttitudeCreate,
  },
  {
    path: '/attitude_view',
    name: 'AttitudeView',
    component: AttitudeView,
  },
  {
    path: '/attitude_change',
    name: 'AttitudeChange',
    component: AttitudeChange,
  },
  {
    path: '/notification',
    name: 'Notification',
    component: Notification,
  },
  {
    path: '/homework-submit/:id',
    name: 'HomeworkSubmit',
    component: HomeworkSubmit,
  },
  {
    path: '/mypage/:id',
    name: 'MyPage',
    component: MyPage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
