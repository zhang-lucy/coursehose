<template>
  <div id="road">
      <div v-for="(courses, semester) in semesters" :key="semester">
        <h3 class="semesterName">{{ semester }}</h3>
        <draggable class="list-group row" :list="courses" group="g1"> <!-- TODO I don't think the semester values change in App when you move them around tbh oops -->
          <div v-for="course in courses" class="course list-group-item" :key="course.name">
            <div>
                <button type="button" class="close" aria-label="Close" @click="handleDelete(course,semester)">
                  <span aria-hidden="true">&times;</span>
                </button>
                <!-- <span class = "larger">{{ course.name }} </span> -->
                <!-- TODO attempt to add course names fix later need to access course.js -->
                <!-- <span class = "smaller">{{ classes[course.name]['n'] }}</span>-->
                <span class="smaller">{{ course.name }}</span>
                <!-- if (course.toString() in classes) {
                    courseItem = {number: course, name: classes[course.toString()]['n']};
                } else {
                    courseItem = {number: course, name: "No Class Found"};
                } -->
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
    width: 20%;
    background: teal;
    color: white;
    border-radius: 5px;
    margin: 10px;
    padding: 10px;
    display: inline-block;
  }
  .larger {
    font-size: 25px;
  }
  .smaller {
    font-size: 20px;
  }
  .row {
    display: block;
    margin: auto;
    border-bottom: 2px solid black;
  }
  .semesterName {
    margin-top: 20px;
    font-size: 24px;
  }
</style>