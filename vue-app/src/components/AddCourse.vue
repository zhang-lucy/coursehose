<template>
  <div id="add-course">
    <!-- <form @submit.prevent="handleSubmit">

      <label>Add a course: </label>
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
      </select>



      <v-btn>Submit</v-btn>
    </form> -->

    <v-menu open-on-hover bottom offset-y>
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
    </v-menu>

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
        // this.$emit('add:course', this.course)
      },
    }
  }

</script>

<style scoped>
  label {
    margin-right: 5px;
  }
  form {
    margin-bottom: 2rem;
  }
  input {
    background: white;
    width: 100px;
  }
  select {
    background: pink;
  }
</style>