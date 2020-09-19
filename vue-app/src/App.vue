<template>
  <div id="app" class="small-container">
    <h1>CourseHose</h1>
    <major-form :majors="majors"
    :years="years"/>
    <add-course @add:course="addCourse"/>
    <road :courses="courses"/>

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
        // TODO: Unhardcode  
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
        majors: [{id: 0, value: "1"},{id: 1, value: "6"},{id: 2, value: "18"}],
        years: [{id: 0, value: 2021},{id: 1, value: 2022},{id: 2, value: 2023},{id: 3, value: 2024}]
    }
  },
  methods: {
    addCourse(courseName) {
      const lastId = this.courses.length > 0
        ? this.courses[this.courses.length - 1].id
        : 0;
      const id = lastId + 1;
      const newCourse = { ...courseName, id };
      this.courses = [...this.courses, newCourse];
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
