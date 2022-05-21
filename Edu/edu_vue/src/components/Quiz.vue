<template>
  <div>

    <h3>{{ quiz.question }} </h3>
    <div class='control'>
      <label class='radio'>
        <input type='radio' :value='quiz.option1' v-model='selectedAnswer'> {{ quiz.option1 }}
      </label>
    </div>
    <div class='control'>
      <label class='radio'>
        <input type='radio' :value='quiz.option2' v-model='selectedAnswer'> {{ quiz.option2 }}
      </label>
    </div>
    <div class='control'>
      <label class='radio'>
        <input type='radio' :value='quiz.option3' v-model='selectedAnswer'> {{ quiz.option3 }}
      </label>
    </div>

    <div class='control mt-4'>
      <button class='button is-info' @click='submitQuiz'>Submit</button>
    </div>

    <template v-if='quizResult == "correct"'>
      <div class="notification is-success mt-4">Correct!</div>
    </template>
    <template v-if='quizResult == "incorrect"'>
      <div class="notification is-danger mt-4">Wrong answer</div>
    </template>


  </div>
</template>

<script>
export default {
    props: ['quiz'],
    data() {
      return {
        selectedAnswer: '',
        quizResult: null,
      }
    },
    methods: {

      submitQuiz(){
        this.quizResult = null
        if (this.selectedAnswer) {
          if (this.selectedAnswer === this.quiz.answer)
   {
              this.quizResult = 'correct'
   }         else {
              this.quizResult = 'incorrect'
   }
        } else {
          alert('Select an answer first')
        }
      },
    },




}



</script>
