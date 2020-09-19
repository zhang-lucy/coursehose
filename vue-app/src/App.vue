<template>
  <div id="app" class="small-container">
    <h1>CourseHose</h1>
    <major-form :majors="majors"
    :years="years"/>
    <add-course @add:course="addCourse"/>
    <road 
    :semesters="semesters" 
    :majors="majors" 
    @remove:course="removeCourse"
    />
    <constraint-sidebar/>
  </div>
</template>

<script>
import MajorForm from '@/components/MajorForm.vue'
import AddCourse from '@/components/AddCourse.vue'
import Road from '@/components/Road.vue'
import ConstraintSidebar from '@/components/ConstraintSidebar.vue'

export default {
  name: 'App',
  components: {
    MajorForm,
    AddCourse,
    Road,
    ConstraintSidebar
  },
  data() {
    return {
      semesters: { // TODO remove hardcode later, also probably rewrite with Sets idk
        f20: [],
        s21: [],
      },
      majors: [{id: 0, value: "1"},{id:1, value: "2"},{id: 2, value: "6-1"},{id: 3, value: "6-3"},{id: 4, value: "18"}],
      years: [{id: 0, value: 2021},{id: 1, value: 2022},{id: 2, value: 2023},{id: 3, value: 2024}]
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
    },

    removeCourse: function(course) {
      const index = this.semesters[course.sem].indexOf(course);
      this.semesters[course.sem].splice(index, 1);
    },
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
