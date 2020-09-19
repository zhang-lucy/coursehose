<!-- TODO: Rename these files to something more meaningful -->

<template>
  <div id="major-form">
    <form>
      <div class="select">
        <label>What is your course?</label>
        <select v-model="major">
          <option disabled value="">Course</option>
          <option v-for="major in majors" :key="major.id" :value="major">{{ major.value }}</option>
        </select>
        <button>Submit</button><br>
      </div>
      <div class="select">
        <label>What is your expected graduation year?</label>
        <select v-model="year">
          <option disabled value="">Year</option>
          <option v-for="year in years" :key="year.id" :value="year">{{ year.value }}</option>
        </select>
        <button>Submit</button>
      </div>
    </form>
    <span>Selected: {{ year }}</span>

  </div>
</template>

<script>
  export default {
    name: 'major-form',
    props: ['years','majors'],
    data() {
      return {
        major: '',
        year: ''
      }
    },
    methods: {
      selectYear(year) {
        this.year = year.value;
      }
    }
  }
</script>

<style scoped>
  form {
    margin-bottom: 2rem;
  }
  label {
    display: block;
  }
  .select {
    display: block;
    margin-bottom: 1rem;
  }
</style>