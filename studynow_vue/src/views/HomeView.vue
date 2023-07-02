<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNow</h1>
        <h2 class="subtitle">A place for learning what you want</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-clock"></i
              ></span>

              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>

              <p>This is a random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-clock"></i
              ></span>

              <h2 class="is-size-4 mt-4 mb-4">Explore more from others</h2>

              <p>This is a random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"
                ><i class="far fa-clock"></i
              ></span>

              <h2 class="is-size-4 mt-4 mb-4">Study from home</h2>

              <p>This is a random placeholder text</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <router-link
              to="/recommend"
              class="button is-info is-size-3 mt-6 mb-6"
              >Click to get recommendation</router-link
            >
          </div>

          <hr />
          <div
            class="column is-3"
            v-for="course in courses"
            v-bind:key="course.id"
          >
            <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CourseItem from "@/components/CourseItem.vue";
export default {
  data() {
    return {
      courses: [],
    };
  },
  components: {
    CourseItem,
  },
  mounted() {
    console.log("mounted");

    axios.get("/api/v1/courses/get_frontpage_courses/").then((response) => {
      console.log(response.data);

      this.courses = response.data;
    });
  },
  name: "HomeView",
};
</script>
