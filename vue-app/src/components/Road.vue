<template>
  <div id="road">
    <h3 v-for="(courses, semester) in semesters" :key="semester.name">
      {{ semester }}

      <div v-for="course in courses" class="course" :key="course.name">
        <div>
            <button @click="deleteCourse(course)">x</button>
            <!-- <span class = "larger">{{ course.number }} </span> -->
            <span class = "smaller">{{ course }}</span>        
        </div>
      </div>
    </h3>

    <table>
      <thead>
        <tr>
          <th>Semester</th>
          <th>Courses</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(courses, semester) in semesters" :key="semester.name">
            <td>{{ semester }}</td>
            <td>{{ courses }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
  export default {
    name: 'road',
    props: ['semesters']
  }
</script>

<style scoped>
  .course {
    width: 20%;
    background: teal;
    color: white;
    border-radius: 10px;
    margin: 10px;
    padding: 10px;
  }
  .larger {
      font-size: 25px;
  }
  .smaller {
      font-size: 20px;
  }
</style>