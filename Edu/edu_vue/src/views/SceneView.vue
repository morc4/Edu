<template>
  <div class='Scene'>
    <div class='hero is-info'>
      <div class="hero-body has-text-centered">
        <h1 class="title"> {{ questAssets.get_location }} </h1>
      </div>
    </div>

  <section class='section'>
    <div class='container'>
      <div class='columns content'>

        <div class='column is-one-third'>
          <figure class='image is-200x200' alt='quest image'>
            <img :src='questAssets.get_character_pic'>
          </figure>
        </div>
        <div class='column is-two-thirds'>
          <div class='block'>
            <article class="message is-dark">
              <div class="message-header">
                <p>{{ questAssets.get_character }}</p>
              </div>

              <div v-if='answers.length===0'>
                <div class="message-body">
                  {{ questAssets.intro_dialogue }}
                </div>
                <Choices/>
              </div>

              <div v-else>
                <div class='message-body'>
                  {{ this.characterAnswer }}
              </div>
            </div>


            </article>
        </div>
          <div class='block'>
            <div class='columns'>
              <div class='column has-text-centered'>
                <router-link class='button' :to='{name: "Map"}'>back to map</router-link>
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
import Choices from '@/components/Choices'
export default {

  components: {
    Choices,
  },
  data() {
    return {
    questAssets: {},
    answers: [],
    choiceSubmited: false,
    characterAnswer: '',
    charIndex: -1,
    choices: null,
    dialogue: ''
  }
    },

    async mounted() {
      console.log('mounted')
      const slug = this.$route.params.slug
      const scene_slug =this.$route.params.scene_slug

    await axios
        .get(`quests/${slug}/${scene_slug}/get_scene`)
        .then(response=> {
          console.log(response.data)
          this.questAssets = response.data

        })

    await axios
        .get(`quests/${slug}/${scene_slug}/get_answers`)
        .then(response=> {
          console.log(response.data)
          this.answers = response.data
          if (this.answers.length !== 0){
          this.characterAnswer = response.data[0].get_answer}
        })

    await axios
        .get(`quests/${slug}/${scene_slug}/get_choices`)
        .then(response=> {
          console.log(response.data)
          this.choices = response.data.questions
	})

    document.title = this.$route.params.scene_slug + ' | EduProject'
},

    methods: {
      setAnswer(answers, choices){

        this.charIndex = choices.find(function(choice, index) {
          if(choice.id == this.characterAnswer)
          return true;
          });
          },
        },
        getAnswer(placeholder){
          axios
              .get(`quests/${slug}/${scene_slug}/get_answers`)
              .then(response=> {
                console.log(response.data)
                this.answers = response.data
                if (this.answers.length === 0){
                this.characterAnswer = response.data[0].get_answer}
              })
        },


        }





</script>
