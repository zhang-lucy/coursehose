<template>
  <div id="add-course">
    <form @submit.prevent="handleSubmit" id="courseForm">

      <span>Add a course: </span>
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
        <option>Fall 2021</option>
        <option>Spring 2022</option>
        <option>Fall 2022</option>
        <option>Spring 2023</option>
        <option>Fall 2023</option>
        <option>Spring 2024</option>
      </select>
    <!-- <v-menu open-on-hover bottom offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Term
        </v-btn>
      </template>

      <v-list>
        <v-list-item
          v-for="semester in semesters.keys"
          :key="semester"
        >
          <v-list-item-title>{{ semester }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu> -->

      <b-button variant="info" form="courseForm" type="submit">Submit</b-button>
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
        }
      }
    },
    methods: {
      handleSubmit() {
        console.log("Added " + this.course.name + " in " + this.course.sem + "!");
        this.$emit('add:course', this.course)
        this.course.name = '';
        this.course.sem = '';
      },
    }
  }

</script>

<style scoped>
  button {
    margin-left: 15px; 
  }
  label {
    margin-right: 5px;
  }
  select {
    background: pink;
  }
</style>