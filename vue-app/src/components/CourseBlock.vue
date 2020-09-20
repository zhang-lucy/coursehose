<template>
    <div id="course-block"  :style="isClicked ? { 'background-color': '#ff4b5c' } : null" @click="toggleIsClicked">
        <button type="button" class="close-button" aria-label="Close" @click="handleDelete(course,semester)">
            <span aria-hidden="true">&times;</span>
        </button>
        <span class="larger">{{ courseName }}</span><br>
        <span class="smaller">{{ courseTitle }}</span>
    </div>
</template>

<script>
export default {
    name: "course-block",
    props: ["courseName","courseTitle"],
    data() {
        return {
            isClicked: false
        }
    },

    methods: {
          toggleIsClicked: function () {
    this.isClicked = !this.isClicked
  },
        handleDelete(course, semester){
            this.$emit('remove:course', course, semester);
        }
    }
}
</script>

<style scoped>
  .close-button {
    float: right;
    border: none;
    color: white;
    font-size: 20px;
  }
  .close-button:hover {
    background: transparent;
    color: #454545;
  }
  #course-block {
    width: 200px;
    height: 115px;
    font-size: 15px;
    background: var(--course-color-1);
    color: white;
    border: none;
    margin: 10px;
    padding: 8px;
    display: inline-block;
    vertical-align: middle;
    overflow-y: scroll;
    border-radius: 15px;
  }

</style>

