import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import About from "../views/AboutView.vue";
import Recommend from "../views/RecommendView.vue";
import SignUp from "../views/SignUp.vue";
import LogIn from "../views/Login.vue";
import Courses from "../views/Courses.vue";
import Course from "../views/Course.vue";
import MyAccount from "../views/dashboard/MyAccount.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/recommend",
    name: "Recommend",
    component: Recommend,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/dashboard/my-account",
    name: "MyAccount",
    component: MyAccount,
  },
  {
    path: "/courses",
    name: "Courses",
    component: Courses,
  },
  // For unauthenticated user
  {
    path: "/courses/:slug",
    name: "Course",
    component: Course,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
