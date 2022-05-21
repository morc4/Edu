<template>
<section class='section'>
<div>
  <div class='columns is-centered'>
    <div class='column'>
      <div class='block'>
        <div class='content has-text-centered'>
          <h1> Quest Finale</h1>
        </div>
      </div>
    </div>
  </div>
</div>

  <div class='block'>
    <div class='columns'>

    <div>


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
    variable: '',
  }
    },

  async mounted() {
    console.log('mounted')
    const slug = this.$route.params.slug

  await axios
      .get(`quests/${slug}/get_quest_map`)
      .then(response=> {
        console.log(response.data)
        this.variable = response.data


      })


  document.title = this.$route.params.slug + ' map | EduProject'

},
  methods: {},

}


</script>
