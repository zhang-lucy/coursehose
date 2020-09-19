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
        <option>f20</option>
        <option>s21</option>
      </select>
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
  // TODO: figure out why it's buggy
  // import '../scripts/course'
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