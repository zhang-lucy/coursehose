<template>
  <div id="road">
    <table>
      <thead>
        <tr>
          <th>Semester</th>
          <th>Course</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="course in courses" :key="course.id">
            <td>{{ course.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'road',
    propsData: {
        courses: 'Array',
    }
  }
</script>

<style scoped></style>