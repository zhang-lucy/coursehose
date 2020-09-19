<template>
  <div id="road">
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

<style scoped></style>