import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import MyAccountView from '../views/dashboard/MyAccountView.vue'
import CoursesView from '../views/CoursesView.vue'
import CourseView from '../views/CourseView.vue'
import QuestView from '../views/QuestView.vue'
import MapView from '../views/MapView.vue'
import SceneView from '../views/SceneView.vue'
import FinishView from '../views/FinishView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/log-in',
    name: 'login',
    component: LogInView
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccountView
  },
  {
    path: '/courses',
    name: 'Courses',
    component: CoursesView
  },
  {
    path: '/course/:slug',
    name: 'Course',
    component: CourseView
  },
  {
    path: '/quest/:slug',
    name: 'Quest',
    component: QuestView
  },
  {
    path: '/quest/:slug/map',
    name: 'Map',
    component: MapView
  },
  {
    path: '/quest/:slug/:scene_slug',
    name: 'Scene',
    component: SceneView
  },
  {
    path: '/quest/:slug/final',
    name: 'Final',
    component: FinishView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
