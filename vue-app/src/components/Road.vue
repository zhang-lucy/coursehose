<template>
  <div id="road">
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
        <!-- <rawDisplayer class="col-3" :value="courses" title="List 1" />  ????  -->
        <!-- <rawDisplayer class="col-3" :value="list2" title="List 2" /> -->
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
}

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