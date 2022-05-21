<template>
<div class='block'>
  <div class='content'>
    <div class='columns'>
      <div class='column'>

          <div v-for='choice in choices'>
            <div class='block'>
              <div class='content'>
                <div class='column'>
                  <button
                  class='button is-primary is-rounded'
                  @click='setActiveChoice(choice.text)'
                  >
                    {{ choice.letter }}. {{ choice.text }}</button>
                </div>
              </div>
            </div>
          </div>

          <div class='column has-text-centered'>
            <button class='button is-link' @click='submitActiveChoice'>Confirm</button>
          </div>

      </div>
    </div>
  </div>
</div>


</template>
<script>
import axios from 'axios'

export default {
props: ['choiceSubmited',],
  data() {
    return {
    activeChoice: {'text': ''},
    choices: []
  }
    },
    async mounted() {
      console.log('mounted')
      const slug = this.$route.params.slug
      const scene_slug =this.$route.params.scene_slug

    await axios
        .get(`quests/${slug}/${scene_slug}/get_choices`)
        .then(response=> {
          console.log(response.data)
          this.choices = response.data

        })

  },

  methods: {
    setActiveChoice(answer){
      this.activeChoice.text = answer
      console.log(this.activeChoice)
    },
    submitActiveChoice() {
      axios
        .post(`quests/${this.$route.params.slug}/${this.$route.params.scene_slug}/add_answer`, this.activeChoice)
        .then(response=> {

            window.location.reload();

        })
        .catch(error => {
          console.log(error)})
    }
    }

  }



</script>
