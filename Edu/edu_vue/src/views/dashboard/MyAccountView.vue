<template>
  <div class="about">

    <div class='hero is-info'>
      <div class="hero-body has-text-centered">
        <h1 class="title">My account</h1>
      </div>
    </div>

    <section class='section'>
      <div class='columns is-multiline'>
        <div class='coulumn is-12'>
          <h2 class='subtitle is-size-3'>Your Active Courses</h2>
          <div class='columns is-multiline'>
            <div
              class='column is-4'
              v-for='course in courses'
              v-bind:key='course.id'
            >
              <CourseItem :course="course" />
            </div>
          </div>
        </div>
    </div>

      <hr>


      <button @click="logout()" class='button is-danger'>Log out</button>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import CourseItem from'@/components/CourseItem.vue'
export default {
  data() {
    return {
      courses: []
    }
  },
  components: {
    CourseItem
  },
  mounted() {
      axios
        .get('activities/get_active_courses/')
        .then(response => {
          console.log(response.data)

          this.courses = response.data
        })
  },
  methods: {
    async logout() {
      console.log('logout')

      await axios
      .post('token/logout')
      .then(response =>{
        console.log('logged out')
      })

      axios.defaults.headers.common['Authorization'] = ""

      localStorage.removeItem('token')

      this.$store.commit('removeToken')

      this.$router.push('/')
    }
  }
}
</script>
