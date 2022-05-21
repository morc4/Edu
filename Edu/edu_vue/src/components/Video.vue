<template>

  <div class='video-container'>
    <iframe
      :src="'https://www.youtube.com/embed/' + youtube_link"
      width='100%'
      height='400'
      frameborder='0'
      allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture;'
      allowfullscreen
    >
  </iframe>
  </div>

</template>

<script>
export default {
  props: ['youtube_link'],
}


</script>
