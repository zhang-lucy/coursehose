<!-- TODO: Rename these files to something more meaningful -->

<template>
  <div id="major-form">
    <form @submit.prevent="handleMajorSubmit" id="majorForm">
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
      <b-button variant="info" type="submit" form="majorForm">Submit</b-button>
    </form>
  </div>
</template>

<script>
  // import $ from 'jquery';
  // import { getRoad } from "../scripts/roadAPICall.js";
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
      validateDropdown() {
        // TODO
        // var input = document.getElementById('seedoc')
        // if(dd.value == '') input.disabled = true; else input.disabled = false;
      },
      // updateRoad(data) {
      //   this.$emit('update:road', data);
      // },
      handleMajorSubmit() {
        console.log("Major: "+this.major.value+", Year: "+this.year.value);
        this.$emit('add:major', this.major, this.year);
        this.$emit('next:page');

        // var dummyEndpoint = "/getRoad" // TODO update with actual endpoint, also maybe need to incorporate year
        // var major = JSON.parse(JSON.stringify(this.major)); // weird bug with observables
        // var year = JSON.parse(JSON.stringify(this.year));
        // var road = getRoad(dummyEndpoint, major, year);
        var data = {"Fall 2020": [{name: "6.0001"}], "Spring 2021": [{name: "6.0002"}]};
        this.$emit('update:road', data);
        // $.post("http://localhost:5000/apiCall", {'major': major})
        //   .done(function(data) {
        //     console.log(data);
        //     updateRoad(data);
        //   });
        
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