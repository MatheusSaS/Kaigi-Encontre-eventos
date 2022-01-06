import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Event from '../views/Event.vue'
import CreateEvent from '../components/CreateEvent.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Subject from '../components/dashboard/admin/Subject.vue'
import Category from '../components/dashboard/admin/Category.vue'
import CategoryHome from '../views/CategoryHome.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },  
  {
    path: '/event/:id',
    name: 'Event',
    component: Event,
  }, 
  {
    path: '/my-events',
    name: 'my-events',
    component: Home,
  }, 
  {
    path: '/dashboard/admin/category',
    name: 'category',
    component: Category,
  },
  {
    path: '/dashboard/:type',
    name: 'dashboard',
    component: Home,
  }, 
  {
    path: '/create-event/:type',
    name: 'CreateEvent',
    component: CreateEvent,
  },
  {
    path: '/dashboard/admin/subject',
    name: 'subject',
    component: Subject,
  },  
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/category/:type',
    name: 'category',
    component: CategoryHome,
  }, 
  
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
