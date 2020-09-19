<template>
  <div id="app" class="small-container">
    <h1>CourseHose</h1>
    <major-form />
    <road />
  </div>
</template>

<script>
import MajorForm from '@/components/MajorForm.vue'
import Road from '@/components/Road.vue'

export default {
  name: 'App',
  components: {
    MajorForm,
    Road
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
