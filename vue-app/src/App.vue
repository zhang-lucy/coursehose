<template>
  <div id="app" class="small-container">
    <left-sidebar/>
    <scroll-body
          :years="years"
          :semesters="semesters" 
          :majors="majors" 
          @remove:course="removeCourse"
    />
    <constraint-sidebar/>
  </div>
</template>

<script>

import ConstraintSidebar from '@/components/ConstraintSidebar.vue'
import LeftSidebar from '@/components/LeftSidebar.vue'
import ScrollBody from '@/components/ScrollBody.vue'

export default {
  name: 'App',
  components: {
    ConstraintSidebar,
    LeftSidebar,
    ScrollBody
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
    addCourse(course) {
      for(let i = 0; i < this.semesters[course.sem].length; i++) {
        let c = this.semesters[course.sem][i];
        if (course.name == c.name) {
          return;
        }
      }
      this.semesters[course.sem].push({name: course.name});
      console.log(this.semesters[course.sem]);
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
  margin-top: 20px;
  margin-left: 20px;
  display:flex;
  height:100vh;
}
</style>
