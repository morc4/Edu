<template>

  <div class='column'>
    <figure class='image is-128x128'><img v-bind:src='icon.get_image'></figure>
  </div>


</template>
<script>

export default {
  props: ['icon']
}


</script>
