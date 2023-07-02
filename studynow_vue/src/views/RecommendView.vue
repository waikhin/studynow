<template>
  <div class="recommend">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Coursera Recommender</h1>
      </div>
    </div>
    <div class="section no-pad-bot" id="index-banner">
      <div class="container">
        <br /><br />
        <h1 class="title is-1 has-text-centered has-text-orange">
          Courses recommender
        </h1>
        <div class="columns is-centered">
          <div class="column is-8">
            <h5 class="title is-5 has-text-centered">
              Coursera Courses recommender
            </h5>
            <br />
          </div>
        </div>

        <div class="columns is-centered">
          <div class="column is-6">
            <form @submit.prevent="getRecommendation">
              <div class="field">
                <label class="label has-text-weight-bold">Search Courses</label>
                <div class="control">
                  <input
                    class="input"
                    v-model="courseName"
                    type="text"
                    placeholder="Type course name to get recommendations"
                    required
                  />
                </div>
              </div>
              <div class="field has-text-centered">
                <button type="submit" class="button is-orange is-large">
                  Get Recommendations
                </button>
              </div>
            </form>
            <div class="server-message">{{ serverMessage }}</div>

            <div v-html="recommendationHtml"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      courseName: "",
      recommendationHtml: "",
      serverMessage: "",
    };
  },
  methods: {
    getRecommendation() {
      axios
        .post("http://localhost:8000/coursereco/api/recommend/", {
          // adjust the URL based on your Django server
          course: this.courseName,
        })
        .then((response) => {
          this.recommendationHtml = response.data.pred;
          this.serverMessage = response.data.message;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
