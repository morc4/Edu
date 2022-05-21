<template>
<section class='Finish'>
<div>
  <div class='columns is-centered'>
    <div class='column'>
      <div class='block'>
        <div class='content has-text-centered'>
          <h1> End Of The Quest</h1>
        </div>
      </div>
    </div>
  </div>
</div>

<div class='container'>
  <div class='columns content'>

    <div class='column is-one-third'>
      <figure class='image is-200x200' alt='quest image'>
        <img :src='final.get_picture'>
      </figure>
    </div>
    <div class='column is-two-thirds'>
      <div class='block'>
        <article class="message is-dark">
          <div class="message-header">
            <p>{{ final.name }}</p>
          </div>

          <div>
            <div class="message-body">
              {{ final.text }}
            </div>

          </div>
        </article>
      </div>
    </div>
  </div>
</div>


</section>


</template>
<script>
import axios from 'axios'

export default {

  data() {
    return {
    score: {},
    final: {},
  }
    },

  async mounted() {
    console.log('mounted')
    const slug = this.$route.params.slug

  await axios
      .get(`quests/${slug}/calculate_score`)
      .then(response=> {
        console.log(response.data)
        this.score = response.data
      })

  await axios
      .get(`quests/${slug}/get_final`)
      .then(response=> {
        console.log(response.data)
        this.final = response.data
      })


  document.title = this.$route.params.slug + ' map | EduProject'

},
  methods: {},

}


</script>
