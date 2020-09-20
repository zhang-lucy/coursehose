<template>
  <div id="road">
      <div v-for="(courses, semester) in semesters" :key="semester">
        <h3 class="semesterName">{{ semester }}</h3>
        <p>Total hours: {{ totalHours(courses) }}</p>
        <draggable class="list-group row" :list="courses" group="g1"> 

          <!-- TODO I don't think the semester values change in App when you move them around tbh oops -->
          <div v-for="course in getTitles(courses)" class="course list-group-item" :key="course.name">
            <div>
                <button type="button" class="close-button" aria-label="Close" @click="handleDelete(course,semester)">
                  <span aria-hidden="true">&times;</span>
                </button>
                <span class="larger">{{ course.name }}</span><br>
                <span class="smaller">{{ course.title }}</span>
            </div>
          </div>
        </draggable>
        
      </div>
        <!-- <rawDisplayer class="col-3" :value="courses" title="List 1" />  ????  -->
        <!-- <rawDisplayer class="col-3" :value="list2" title="List 2" /> -->
    </div>
</template>

<script>
import draggable from "@/../node_modules/vuedraggable";
import { classes } from "../scripts/allCourses.js";

export default {
  name: 'road',
  display: "Road",
  order: 1,
  components: {
    draggable
  },
  props: ['semesters'],
  methods: {
    handleDelete(course, semester) {
      this.$emit('remove:course', course, semester);
    },
    getTitles(courses) {
      let allCourses = [];
      var courseItem;
      for (let i=0; i<courses.length; i++) {
        if (courses[i].name in classes) { // TODO: Handle lowercase
          courseItem = {name: courses[i].name, title: classes[courses[i].name]['n']};
          allCourses.push(courseItem);
        } 
      }
      return allCourses;
    },
    totalHours(courses) {
      let hours = 0;
      for (let i=0; i<courses.length; i++) {
        if (courses[i].name in classes) {
          hours += classes[courses[i].name]['h']
        } 
      }
      return hours.toFixed(1);
    }
  },
}

</script>

<style scoped>
  .close-button {
    float: right;
    border: none;
    color: white;
    font-size: 20px;
  }
  .close-button:hover {
    background: transparent;
    color: #454545;
  }
  .course {
    width: 200px;
    height: 125px;
    font-size: 15px;
    background: var(--course-color-1);
    color: white;
    border: none;
    margin: 10px;
    padding: 10px;
    display: inline-block;
    vertical-align: middle;
    overflow:scroll;
    border-radius: 15px;
  }
  .larger {
    font-size: 20px;
  }
  .smaller {
    font-size: 15px;
  }
  .row {
    display: block;
    margin: auto;
    border-bottom: 2px solid black;
    width: 100%;
    border-radius: 15px;
  }
  .semesterName {
    margin-top: 20px;
    font-size: 24px;
  }
  #road{
    margin-top:0;
  }
</style>