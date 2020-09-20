<template>
  <div id="app" class="small-container">
    <scroll-body
          :years="years"
          :semesters="semesters" 
          :majors="majors" 
          :login_page="login_page"
          @add:course="addCourse"
          @remove:course="removeCourse"
          @add:major="addMajor"
          @next:page="nextPage"
          @update:road="updateRoad"
    />
    <constraint-sidebar
      :majors="majors" 
      @add:major="addMajor"

    />
  </div>
</template>

<script>

import ConstraintSidebar from '@/components/ConstraintSidebar.vue'
import ScrollBody from '@/components/ScrollBody.vue'

export default {
  name: 'App',
  components: {
    ConstraintSidebar,
    ScrollBody
  },
  data() {
    return {
      semesters: { // TODO remove hardcode later, also probably rewrite with Sets idk jk use with sets not supported
        // "Fall 2020": [],
        // "Spring 2021": [],
        // "Fall 2021": [],
        // "Spring 2022": [],
        // "Fall 2022": [],
        // "Spring 2023": [],
        // "Fall 2023": [],
        // "Spring 2024": [],
      },
      login_page: true,
      selected_majors: [],
      selected_year: 0,
      majors: [{id: 0, value: "1-ENG: Civil and Environmental Engineering"},{id: 1, value: "2: Mechanical Engineering"},{id: 2, value: "2-A: Mechanical Engineering"},{id: 3, value: "2-OE: Mechanical and Ocean Engineering"},{id: 4, value: "3: Materials Science and Engineering"},{id: 5, value: "3-A: Materials Science and Engineering"},{id: 6, value: "3-C: Archaeology and Materials"},{id: 7, value: "4: Architecture"},{id: 8, value: "4-B: Art and Design"},{id: 9, value: "5: Chemistry"},{id: 10, value: "5-7: Chemistry and Biology"},{id: 11, value: "5-Flex: Chemistry"},{id: 12, value: "6-1: Electrical Engineering"},{id: 13, value: "6-1/8-Flex: Electrical Engineering for Double Majors in Physics"},{id: 14, value: "6-14: Computer Science and Economics"},{id: 15, value: "6-2: Electrical Engineering and Computer Science"},{id: 16, value: "6-3: Computer Science"},{id: 17, value: "6-7: Computer Science and Molecular Biology"},{id: 18, value: "6-9: Computation and Cognition"},{id: 19, value: "7: Biology"},{id: 20, value: "7-A: Biology"},{id: 21, value: "8: Physics"},{id: 22, value: "8-Flex: Physics"},{id: 23, value: "9: Brain and Cognitive Sciences"},{id: 24, value: "10: Chemical Engineering"},{id: 25, value: "10-B: Chemical-Biological Engineering"},{id: 26, value: "10-C: Chemical Engineering"},{id: 27, value: "10-ENG: Chemical Engineering"},{id: 28, value: "11: Planning"},{id: 29, value: "11-6: Urban Planning with CS"},{id: 30, value: "12: Earth and Planetary Sciences"},{id: 31, value: "14-1: Economics"},{id: 32, value: "14-2: Mathematical Economics"},{id: 33, value: "15-1: Management"},{id: 34, value: "15-2: Business Analytics"},{id: 35, value: "15-3: Finance"},{id: 36, value: "16: Aerospace Engineering"},{id: 37, value: "16-ENG: Aeronautics and Astronautics"},{id: 38, value: "17: Political Science"},{id: 39, value: "18: Applied Mathematics"},{id: 40, value: "18: General Mathematics"},{id: 41, value: "18: Pure Mathematics"},{id: 42, value: "18-C: Mathematics with Computer Science"},{id: 43, value: "20: Biological Engineering"},{id: 44, value: "21: American Studies"},{id: 45, value: "21: Ancient and Medieval Studies"},{id: 46, value: "21: Asian and Asian Diaspora Studies"},{id: 47, value: "21: Latin American and Latino Studies"},{id: 48, value: "21: Russian and Eurasian Studies"},{id: 49, value: "21: Women's and Gender Studies"},{id: 50, value: "21A: Anthropology"},{id: 51, value: "21E: Humanities and Engineering"},{id: 52, value: "21G: Global Studies and Languages"},{id: 53, value: "21G: Global Studies and Languages"},{id: 54, value: "21G: Global Studies and Languages"},{id: 55, value: "21H: History"},{id: 56, value: "21L: Literature"},{id: 57, value: "21M-1: Music"},{id: 58, value: "21M-2: Theater Arts"},{id: 59, value: "21S: Humanities and Science"},{id: 60, value: "21W: Creative Writing"},{id: 61, value: "21W: Digital Media"},{id: 62, value: "21W: Science Writing"},{id: 63, value: "22: Nuclear Science and Engineering"},{id: 64, value: "22-ENG: Nuclear Science and Engineering - Flexible"},{id: 65, value: "24-1: Philosophy"},{id: 66, value: "24-2: Linguistics and Philosophy"},{id: 67, value: "24-2: Linguistics and Philosophy"},{id: 68, value: "CMS: Comparative Media Studies"},{id: 69, value: "STS: Science, Technology, and Society"}],
      years: [{id: 0, value: 2021},{id: 1, value: 2022},{id: 2, value: 2023},{id: 3, value: 2024}]
    }
  },
  methods: {
    addCourse: function(course) {
      for(let i = 0; i < this.semesters[course.sem].length; i++) {
        let c = this.semesters[course.sem][i];
        if (course.name == c.name) {
          return;
        }
      }
      this.semesters[course.sem].push({name: course.name});
    },

    removeCourse: function(course, semester) {
      for(let i = 0; i < this.semesters[semester].length; i++) {
        let c = this.semesters[semester][i];
        if (course.name == c.name) {
          this.semesters[semester].splice(i, 1);
          return;
        }
      }
    },
    addMajor: function(major, year) {
      this.year = year;
      for(let i = 0; i < this.majors.length; i++) {
        let m = this.majors[i];
        if (m.value == major.value) {
          return;
        }
      }
      this.majors.push(major);
    },
    nextPage: function() {
      console.log("next page!");
      this.login_page = false; // TODO: accomodate more pages
    },

    updateRoad: function(road) {
      for (var semester in road) {
        this.semesters[semester] = road[semester];
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Condensed');

#app {
  font-family: "Roboto", Candara, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display:flex;
  height:100vh;
  --background-color: #ecf4f3;
  --text-color-main: #006a71;
  --select-color: #e0ece4;
  --course-color-1: #a37eba;
  --course-color-2: #e5df88;

}
  select {
    background: var(--select-color);
    padding: 5px;
    border-radius: 3px;
  }
  form {
    padding-bottom: 2rem;
    border-bottom: 2px solid black;
  }
  input {
    background: white;
    width: 100px;
        padding: 5px;

  }
  ::-webkit-scrollbar {
    width: 0px;
  }

</style>
