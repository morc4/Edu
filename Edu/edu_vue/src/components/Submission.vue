<template>
  <div>
  <form v-on:submit.prevent='submitSubmission'>
    <div class='field'>
      <label class='label'>Name</label>
      <div class='control'>
        <input type='text' class='input' v-model='submission.name'>
      </div>
    </div>

    <div class='field'>
      <label class='label'>Your Answer</label>
      <div class='control'>
        <textarea class='textarea' v-model='submission.text_submission'></textarea>
      </div>
    </div>

    <input type="file" @change="onFileChanged">
    <button @click="onUpload">Upload</button>



      <br>
      <br>
    <div
    class='notification is-danger'
    v-for='error in errors'
    v-bind:key='error'
    >

    {{ error }}

  </div>

    <div class='field'>
      <div class='control'>
        <button class='button is-link'>Submit</button>
      </div>
    </div>
  </form>
</div>
<div class='columns'>

    <div class='column is-one-third'>
    </div>

    <div class='column is-one-third'>
      <router-link class="button is-primary" :to='{name: "Quest"}'>Go to Quest</router-link>
    </div>
</div>

</template>

<script>
import axios from 'axios'

export default {
  props: [
    'course', 'activeLesson'
  ],
  data() {
    return {
      submission: {
        name: '',
        text_submission: '',
        file_submission: null

      },
      file: null,
      errors: [],
    }
  },
  methods: {

    onFileChanged (event) {
    this.file = event.target.files[0]

    console.log(this.file)
  },

    onUpload() {
      let formData = new FormData()
      formData.append('homework', this.file, this.file.name)
      axios.post(`courses/${this.$route.params.slug}/${this.activeLesson.slug}/add_homework`, formData)
    },

    submitSubmission(){


    },

  }
}

</script>
