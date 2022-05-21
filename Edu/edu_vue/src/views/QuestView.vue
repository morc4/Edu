<template>
  <div class='Quest'>
    <div class='hero is-info'>
      <div class="hero-body has-text-centered">
        <h1 class="title"> {{ questData.name }} </h1>
      </div>
    </div>
    <section class='section'>
      <div class='container'>
        <div class='columns content'>

          <div class='column is-one-third'>
            <figure class='image is-200x200' alt='quest image'>
              <img :src='questData.get_image'>
            </figure>
          </div>
          <div class='column is-two-thirds'>
            <div class='block'>
              <article class="message is-dark">
                <div class="message-header">
                  <p>Quest Itroduction</p>
                </div>
                <div class="message-body">
                  {{ questData.description }}
                </div>
              </article>
          </div>
            <div class='block'>
              <div class='columns'>
                <div class='column has-text-centered'>
                  <router-link class='button is-link' :to='{name: "Map"}'>Start Quest</router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    </div>

</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      questData: {}
  }},
  async mounted() {

    console.log('mounted')

    const slug = this.$route.params.slug

    await axios
        .get(`quests/${slug}/get_quest`)
        .then(response=> {
          console.log(response.data)

          this.questData = response.data
        })


    document.title = this.questData.name + ' | EduProject'

  },

}
</script>
