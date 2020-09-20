<!-- TODO: Rename these files to something more meaningful -->

<template>
  <div id="major-form">
    <form>
      <div class="select">
        <label>What is your major?</label>
        <select v-model="major" onchange="validateDropdown(this)">
          <option disabled value="">Major</option>
          <option v-for="major in majors" :key="major.id" :value="major">{{ major.value }}</option>
        </select>
      </div>
      <div class="select">
        <label>What is your expected graduation year?</label>
        <select v-model="year">
          <option disabled value="">Year</option>
          <option v-for="year in years" :key="year.id" :value="year">{{ year.value }}</option>
        </select>
      </div>
      <b-button variant="info" class="submit">Submit</b-button>
    </form>

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
      },
       validateDropDown(dd){
        var input = document.getElementById('seedoc')
        if(dd.value == '') input.disabled = true; else input.disabled = false;
      }
    }
  }
</script>

<style scoped>
  form {
    padding-bottom: 2rem;
    margin-bottom: 2rem;
    border-bottom: 2px solid black;
  }
  label {
    display: block;
  }
  .select {
    display: block;
    margin-bottom: 1rem;
  }
  .submit {
    display: block;
    margin: auto;
  }
</style>