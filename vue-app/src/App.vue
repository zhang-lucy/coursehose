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
    <constraint-sidebar/>
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
        "Fall 2020": [],
        "Spring 2021": [],
        "Fall 2021": [],
        "Spring 2022": [],
        "Fall 2022": [],
        "Spring 2023": [],
        "Fall 2023": [],
        "Spring 2024": [],
      },
      login_page: true,
      selected_majors: [],
      selected_year: 0,
      majors: [{id: 0, value: "1-ENG: Civil and Environmental Engineering"},{id: 1, value: "2: Mechanical Engineering"},{id: 2, value: "2-A: Mechanical Engineering"},{id: 3, value: "2-OE: Mechanical and Ocean Engineering"},{id: 4, value: "3: Materials Science and Engineering"},{id: 5, value: "3-A: Materials Science and Engineering"},{id: 6, value: "3-C: Archaeology and Materials"},{id: 7, value: "4: Architecture"},{id: 8, value: "4-B: Art and Design"},{id: 9, value: "5: Chemistry"},{id: 10, value: "5-7: Chemistry and Biology"},{id: 11, value: "6-1: Electrical Engineering"},{id: 12, value: "6-14: Computer Science and Economics"},{id: 13, value: "6-2: Electrical Engineering and Computer Science"},{id: 14, value: "6-3: Computer Science"},{id: 15, value: "6-7: Computer Science and Molecular Biology"},{id: 16, value: "7: Biology"},{id: 17, value: "7-A: Biology"},{id: 18, value: "8: Physics"},{id: 19, value: "8-Flex: Physics"},{id: 20, value: "9: Brain and Cognitive Sciences"},{id: 21, value: "10: Chemical Engineering"},{id: 22, value: "10-B: Chemical-Biological Engineering"},{id: 23, value: "10-C: Chemical Engineering"},{id: 24, value: "10-ENG: Chemical Engineering"},{id: 25, value: "11: Planning"},{id: 26, value: "11-6: Urban Planning with CS"},{id: 27, value: "12: Earth and Planetary Sciences"},{id: 28, value: "14-1: Economics"},{id: 29, value: "14-2: Mathematical Economics"},{id: 30, value: "15-1: Management"},{id: 31, value: "15-2: Business Analytics"},{id: 32, value: "15-3: Finance"},{id: 33, value: "16: Aerospace Engineering"},{id: 34, value: "16-ENG: Aeronautics and Astronautics"},{id: 35, value: "17: Political Science"},{id: 36, value: "18: Applied Mathematics"},{id: 37, value: "18: General Mathematics"},{id: 38, value: "18: Pure Mathematics"},{id: 39, value: "18-C: Mathematics with Computer Science"},{id: 40, value: "20: Biological Engineering"},{id: 41, value: "21: American Studies"},{id: 42, value: "21: Ancient and Medieval Studies"},{id: 43, value: "21: Asian and Asian Diaspora Studies"},{id: 44, value: "21: Latin American and Latino Studies"},{id: 45, value: "21: Russian and Eurasian Studies"},{id: 46, value: "21: Women's and Gender Studies"},{id: 47, value: "21A: Anthropology"},{id: 48, value: "21E: Humanities and Engineering"},{id: 49, value: "21G: Global Studies and Languages"},{id: 50, value: "21G: Global Studies and Languages"},{id: 51, value: "21G: Global Studies and Languages"},{id: 52, value: "21H: History"},{id: 53, value: "21L: Literature"},{id: 54, value: "21M-1: Music"},{id: 55, value: "21M-2: Theater Arts"},{id: 56, value: "21S: Humanities and Science"},{id: 57, value: "21W: Creative Writing"},{id: 58, value: "21W: Digital Media"},{id: 59, value: "21W: Science Writing"},{id: 60, value: "22: Nuclear Science and Engineering"},{id: 61, value: "24-1: Philosophy"},{id: 62, value: "24-2: Linguistics and Philosophy"},{id: 63, value: "24-2: Linguistics and Philosophy"},{id: 64, value: "CMS: Comparative Media Studies"},{id: 65, value: "STS: Science, Technology, and Society"}],
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
  --course-color-1: #a37eba;
  --course-color-2: #e5df88;

}
  select {
    background: pink;
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
