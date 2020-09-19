<template>
  <div id="add-course">
    <form @submit.prevent="handleSubmit">

      <label>Add a course:</label>
      <input
        ref="first"
        type="text"
        placeholder="Course"
        :class="{ 'has-error': submitting && invalidName }"
        v-model="course.name"
      >
      <select v-model="course.sem">
        <option>f20</option>
        <option>s21</option>
      </select>
      <!-- <input type="text" placeholder="Semester" :class="{ 'has-error': submitting && invalidName }" v-model="course.sem"> -->
      <!-- TODO -->
      <!-- <p
        v-if="error && submitting"
        class="error-message"
      >❗Please fill out all required fields</p> 
      <p
        v-if="success"
        class="success-message"
      >✅ Course successfully added</p>-->
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
  // TODO: figure out why it's buggy
  // import '../scripts/course'
  export default {
    name: 'add-course',
    data() {
      return {
        course: {
          name: '',
          semester: '',
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