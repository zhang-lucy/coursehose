<template>
  <div id="road">
      <form id="addCourseForm" v-on:submit.prevent="addCourse">
            <input type="text" id="courseNumber">
            <button type="submit">Add Course</button>
        </form>
        <!-- <div v-for="course in courseList" v-bind:key="course.number" class="course">
            <div>
                <button @click="deleteCourse(course)">x</button>
                <span class = "larger">{{ course.number }} </span>
                <span class = "smaller">{{ course.name }}</span>        
            </div>

        </div> -->
  </div>
</template>

<script>
// TODO: figure out why it's buggy
// import '../scripts/course'
export default {
name: 'road',
el: '#courses',
data() {
    return []
},
methods: {
}
}

</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>