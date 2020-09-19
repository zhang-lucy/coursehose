<template>
  <div id="app" class="small-container">
    <h1>CourseHose</h1>
    <major-form />
    <add-course @add:course="addCourse"/>
    <road :semesters="semesters"/>

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
      semesters: { // TODO remove hardcode later
        f20: [],
        s21: [],
      },
      // courses: [
      //     {
      //     id: 1,
      //     name: '6.009',
      //     sem: 'Fall 2020',
      //     },
      //     {
      //     id: 2,
      //     name: '18.404',
      //     sem: 'Fall 2020',
      //     },
      //     {
      //     id: 3,
      //     name: '22.09',
      //     sem: 'Fall 2020',
      //     },
      // ],
      major: 0
    }
  },
  methods: {
    // addCourse(courseName) {
    //   const lastId = this.courses.length > 0
    //     ? this.courses[this.courses.length - 1].id
    //     : 0;
    //   const id = lastId + 1;
    //   const newCourse = { ...courseName, id };
    //   this.courses = [...this.courses, newCourse];
    // }
    addCourse(course) {
      this.semesters[course.sem].push(course.name);
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
