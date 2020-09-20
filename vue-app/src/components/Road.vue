<template>
  <div id="road">
      <div v-for="(courses, semester) in semesters" :key="semester">
        <h3 class="semesterName">{{ semester }}</h3>
        <draggable class="list-group row" :list="courses" group="g1"> 

          <!-- TODO I don't think the semester values change in App when you move them around tbh oops -->
          <div v-for="course in getTitles(courses)" class="course list-group-item" :key="course.name">
            <div>
                <button type="button" class="close" aria-label="Close" @click="handleDelete(course,semester)">
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
        if (courses[i].name in classes) {
          courseItem = {name: courses[i].name, title: classes[courses[i].name]['n']};
        } else {
          courseItem = {name: courses[i].name, title: "No Class Found"};
        } 
        allCourses.push(courseItem);
      }
      return allCourses;
    }
  },
}

</script>

<style scoped>
  .close-button {
    float: left;
    border: none;
    background: transparent;
  }
  .close-button:hover {
    color: #454545;
  }
  .course {
    width: 15%;
    background: teal;
    color: white;
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
    display: inline-block;
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
  }
  .semesterName {
    margin-top: 20px;
    font-size: 24px;
  }
</style>