<template>
  <div id="road">
    <!-- <div v-for="(courses, semester) in semesters" :key="semester.name">
      <h3>{{ semester }}</h3>

      <div v-for="course in courses" class="course" :key="course.name">
        <div>
            <button @click="handleDelete(semester, course)">x</button> -->
            <!-- <span class = "larger">{{ course.number }} </span> -->
            <!-- <span class = "smaller">{{ course }}</span>        
        </div>
      </div>
    </div> -->

    <div class="row">
      <div v-for="(courses, semester) in semesters" :key="semester.name">
        <h3>{{ semester }}</h3>
        <draggable class="list-group" :list="courses" group="g1">
          <div v-for="course in courses" class="course list-group-item" :key="course.name">
            <div>
                <button @click="handleDelete(semester, course)">x</button>
                <!-- <span class = "larger">{{ course.number }} </span> -->
                <span class = "smaller">{{ course }}</span>        
            </div>
          </div>
        </draggable>
        
      </div>
<!-- 
        <div class="col-3">
        <h3>Draggable 1</h3>
        <draggable class="list-group" :list="list1" group="people" @change="log">
            <div
            class="list-group-item"
            v-for="(element, index) in list1"
            :key="element.name"
            >
            {{ element.name }} {{ index }}
            </div>
        </draggable>
        </div>

        <div class="col-3">
        <h3>Draggable 2</h3>
        <draggable class="list-group" :list="list2" group="people" @change="log">
            <div
            class="list-group-item"
            v-for="(element, index) in list2"
            :key="element.name"
            >
            {{ element.name }} {{ index }}
            </div>
        </draggable>
        </div> -->

        <!-- <rawDisplayer class="col-3" :value="list1" title="List 1" />

        <rawDisplayer class="col-3" :value="list2" title="List 2" /> -->
    </div>

  </div>
</template>

<script>
import draggable from "@/../node_modules/vuedraggable";

export default {
  name: 'road',
  display: "Road",
  order: 1,
  components: {
    draggable
  },
  props: ['semesters'],
  methods: {
    handleDelete(semester, course) {
      this.$emit('remove:course', {sem: semester, name: course});
    }
  },

  // data() {

  // }
}
// export default {
//   name: "two-lists",
//   display: "Two Lists",
//   order: 1,
//   components: {
//     draggable
//   },
//   data() {
//     return {
//       list1: [
//         { name: "John", id: 1 },
//         { name: "Joao", id: 2 },
//         { name: "Jean", id: 3 },
//         { name: "Gerard", id: 4 }
//       ],
//       list2: [
//         { name: "Juan", id: 5 },
//         { name: "Edgard", id: 6 },
//         { name: "Johnson", id: 7 }
//       ]
//     };
//   },
</script>

<style scoped>
  .course {
    width: 20%;
    background: teal;
    color: white;
    border-radius: 10px;
    margin: 10px;
    padding: 10px;
    display: inline-block;
  }
  .larger {
      font-size: 25px;
  }
  .smaller {
      font-size: 20px;
  }
</style>