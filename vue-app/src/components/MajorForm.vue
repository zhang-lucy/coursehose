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
      handleMajorSubmit() {
        console.log("Major: "+this.major.value+", Year: "+this.year.value);
        this.$emit('add:major', this.major, this.year);
        this.$emit('next:page');

        var major = JSON.parse(JSON.stringify(this.major)); // weird bug with observables
        var year = JSON.parse(JSON.stringify(this.year));
        console.log(year);

        // major: "sample road"
        var maps = {"4: Architecture": {"Fall 2020": [{name: "2.00"}], "Spring 2021": [{name: "6.0002"}]},
                    "6-3: Computer Science": {"Fall 2020": [{name: "6.0001"}, {name: "18.02"}, {name: "8.02"}, {name: "CI-H"}],
                      "Spring 2021": [{name: "6.042"}, {name: "6.009"}, {name: "7.012"}, {name: "HASS"}],
                      "Fall 2021": [{name: "6.006"}, {name: "6.004"}, {name: "3.091"}, {name: "CI-H"}],
                      "Spring 2022": [{name: "6.046"}, {name: "6.01"}, {name: "HASS"}, {name: "6.033"}],
                      "Fall 2022": [{name: "6.031"}, {name: "6.UAT"}, {name: "18.03"}, {name: "HASS"}],
                      "Fall 2023": [{name: "6.840"}, {name: "6.036"}, {name: "HASS"}, {name: "HASS"}],
                      "Spring 2023": [{name: "6.215"}, {name: "HASS"}, {name: "6.172"}],
                      "Spring 2024": [{name: "HASS"}, {name: "7.03"}, {name: "6.047"}]}};
        console.log("here"+maps[major.value]);
        this.$emit('update:road', maps[major.value]);

        // TODO this is all broken and I spent too long on this and am crying a lot
        // let self = this;
        // $.post("http://localhost:5000/apiCall", {'major': major.value, 'year': year.value}, function(data) {
        //   console.log(data);
        //   // var newData = JSON.parse(JSON.stringify(data));
        //   // console.log(newData);
        //   // self.$emit('update:road', newData);
          
        //   var data2 = {"Fall 2020": [{name: "6.0001"}], "Spring 2021": [{name: "6.0002"}]};
        //   self.$emit('update:road', data2);
        // });

        // var data = {"Fall 2020": [{name: "6.0001"}], "Spring 2021": [{name: "6.0002"}]};
        // console.log(data);
        // this.$emit('update:road', data);
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