<template>
<section class='section'>
<div>
  <div class='columns is-centered'>
    <div class='column'>
      <div class='block'>
        <div class='content has-text-centered'>
          <h1>{{ mapName }}</h1>
        </div>
      </div>
    </div>
  </div>
</div>

  <div class='block'>
    <div class='columns is-centered has-text-centered'>

      <div
      class= 'column'
      v-for='icon in icons'
      :key='icon.name'
      >

        <div class='content'>
          <h2>{{ icon.name }}</h2>
        </div>

        <div class='block'>
          <div class='content'>
            <p class='is-align-content-center'>
              <figure class='image-center is-128x128'><img v-bind:src='icon.get_icon'></figure>
            </p>
        </div>
      </div>
        <div class='block'>
          <router-link class='button is-success' :to='{name: "Scene", params: {slug: this.$route.params.slug, scene_slug: scene_slug[icon.name]}}' >Go to {{ icon.name }}</router-link>
        </div>

    </div>

    </div>
  </div>

  <div class='block'>
    <div class='content'>
      <div class='columns is-centered has-text-centered'>
        <div class='column'>
          <router-link v-if='been.answered===1' class='button is-link' :to='{name: "Final", params: {slug: this.$route.params.slug}}'>Face your destiny</router-link>
          <div v-else class='button' title="Disabled button" disabled>Face your destiny</div>
        </div>
      </div>
    </div>
  </div>

</section>


</template>
<script>
import axios from 'axios'
import Icons from '@/components/Icons.vue'

export default {
  components: {
    Icons,
  },

  data() {
    return {
    icons: [],
    map: '',
    mapName: '',
    scene_slug: {},
    been: {},
  }
    },

  async mounted() {
    console.log('mounted')
    const slug = this.$route.params.slug

  await axios
      .get(`quests/${slug}/get_quest_map`)
      .then(response=> {
        console.log(response.data)
        this.map = response.data.map.get_map
        this.icons = response.data.locations
        this.mapName = response.data.map.map_name
        this.scene_slug = response.data.link

      })

  await axios
      .get(`quests/${slug}/been_answered`)
      .then(response=> {
        console.log(response.data)
            this.been = response.data

          })


  document.title = this.$route.params.slug + ' map | EduProject'

},
  methods: {},

}


</script>
