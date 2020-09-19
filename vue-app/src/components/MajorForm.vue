<!-- TODO: Rename these files to something more meaningful -->

<template>
  <div id="major-form">
    <form>
      <label>What is your major?</label>
      <input 
        type="text"
        v-model="major"
      />
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'major-form',
    data() {
      return {
        major: ''
      }
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
</style>