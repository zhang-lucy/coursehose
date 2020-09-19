<template>
  <div id="app" class="small-container">
    <h1>CourseHose</h1>
    <major-form />
    <add-course />
    <road :courses="courses"   
    />

  </div>
</template>

<script>
import MajorForm from '@/components/MajorForm.vue'
import AddCourse from '@/components/AddCourse.vue'
import Road from '@/components/Road.vue'

export default {
  name: 'App',
  components: {
    MajorForm,
    AddCourse,
    Road
  },
  data() {
    return {
        courses: [
            {
            id: 1,
            name: '6.009',
            },
            {
            id: 2,
            name: '18.404',
            },
            {
            id: 3,
            name: '22.09',
            },
        ],
    }
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
