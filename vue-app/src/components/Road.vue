<template>
  <div id="road">
    <div v-for="(courses, semester) in semesters" :key="semester.name">
      <h3>{{ semester }}</h3>

      <div v-for="course in courses" class="course" :key="course.name">
        <div>
            <button class="close-button" @click="handleDelete(semester, course)">x</button>
            <span class = "smaller">{{ course.name }}</span>        
        </div>
      </div>
    </div>


  </div>
</template>

<script>
  export default {
    name: 'road',
    props: ['semesters'],
    methods: {
      handleDelete(semester, course) {
        this.$emit('remove:course', {sem: semester, name: course});
      }
    }
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
    border-radius: 10px;
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
</style>