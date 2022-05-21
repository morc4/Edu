<template>
  <div class="home">
    <div class='hero is-info is-medium'>
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to ProfePro</h1>
        <h2 class='subtitle'>A thesis project to gamify learning</h2>
      </div>
    </div>

<section class='section'>
  <div class='container'>
    <div class='columns is-multiline'>

      <div class='column is-4'>
        <div class='box has-text-centered'>
          <span class='icon is-size-2 has-text-info'><i class='far fa-clock'></i></span>

          <h2 class='is-size-4 mt-4 mb-4'>Learn in a storyfied way</h2>

          <p>Choose your path and see what happens</p>
        </div>
      </div>

      <div class='column is-4'>
        <div class='box has-text-centered'>
          <span class='icon is-size-2 has-text-info'><i class='far fa-comments'></i></span>

          <h2 class='is-size-4 mt-4 mb-4'>Develop skills effectively</h2>

          <p>Good pedagogical practices mean you actually internalize the information</p>
        </div>
      </div>

      <div class='column is-4'>
        <div class='box has-text-centered'>
          <span class='icon is-size-2 has-text-info'><i class='fas fa-home'></i></span>

          <h2 class='is-size-4 mt-4 mb-4'>Make things happen</h2>

          <p>Advance at your own pace</p>
        </div>
      </div>

<div class='column is-12 has-text-centered'>
  <a href='/sign-up' class='button is-info is-size-3 mt-6 mb-6'>Get started!</a>
</div>

<hr>

<div
class='column is-3'
v-for='course in courses'
v-bind:key='course.id'
>
<CourseItem :course='course'/>
</div>

    </div>
  </div>
</section>


  </div>

</template>

<script>
import axios from 'axios'
import CourseItem from '@/components//CourseItem.vue'

export default {
  name: 'HomeView',
  data() {
    return {
      courses: []
    }
  },
  components: {
    CourseItem
},
  mounted() {
    console.log('mounted')
    document.title = 'Welcome' + ' | EduProject'
    axios
        .get('courses/get_frontpage_courses/')
        .then(response=> {
          console.log(response.data)

          this.courses = response.data
        })
  }
}
</script>
