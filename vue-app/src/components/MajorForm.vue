<!-- TODO: Rename these files to something more meaningful -->

<template>
  <div id="course-form">
    <form>
      <label>What is your course?</label>
      <input type="text" />
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'course-form',
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>