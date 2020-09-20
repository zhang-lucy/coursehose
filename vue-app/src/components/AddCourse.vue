<template>
  <div id="add-course">
    <form @submit.prevent="handleSubmit">

      <label>Add a course:</label>
      <input
        ref="first"
        type="text"
        placeholder="Course"
        v-model="course.name"
      >
      <select v-model="course.sem">
        <option disabled value="">Term</option>
        <option>Fall 2020</option>
        <option>Spring 2021</option>
      </select>
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'add-course',
    props: ['semesters'],
    data() {
      return {
        course: {
          name: '',
          sem: '',
        },
      }
    },
    methods: {
      handleSubmit() {
        console.log("Added " + this.course.name + " in " + this.course.sem + "!");
        this.$emit('add:course', this.course)
      },
    }
  }

</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>