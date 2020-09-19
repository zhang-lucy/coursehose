<template>
  <div id="add-course">
    <form @submit.prevent="handleSubmit">

      <label>Add a course:</label>
      <input
        ref="first"
        type="text"
        :class="{ 'has-error': submitting && invalidName }"
        v-model="course.name"
      >
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
          semester: 'Fall 2019' // TODO: Un-hardcode
        },
      }
    },
    methods: {
      handleSubmit() {
        console.log("Added " + this.course.name + "!");
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