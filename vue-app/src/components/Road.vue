<template>
  <div id="road">
      <div v-for="(courses, semester) in semesters" :key="semester">
        <h3 class="semesterName">{{ semester }}</h3>
        <p>Total hours: {{ totalHours(courses) }}</p>
        <draggable class="list-group row" :list="courses" group="g1"> 

          <!-- TODO I don't think the semester values change in App when you move them around tbh oops -->
          <course-block v-for="course in getTitles(courses)" 
          class="course list-group-item" 
          :key="course.name" 
          :courseName="course.name"
          :courseTitle="course.title"
          />

        </draggable>
        
      </div>
    </div>
</template>

<script>
import draggable from "@/../node_modules/vuedraggable";
import CourseBlock from "@/components/CourseBlock.vue";
import { classes } from "@/../data/allCourses.js";

export default {
  name: 'road',
  display: "Road",
  order: 1,
  components: {
    CourseBlock,
    draggable
  },
  props: ['semesters'],
  methods: {
    handleDelete(course, semester) {
      this.$emit('remove:course', course, semester);
    },
    getTitles(courses) {
      let allCourses = [];
      var courseItem;
      for (let i=0; i<courses.length; i++) {
        if (courses[i].name in classes) { // TODO: Handle lowercase
          courseItem = {name: courses[i].name, title: classes[courses[i].name]['title']};
          allCourses.push(courseItem);
        } else if (courses[i].name == "CI-H") {
          courseItem = {name: courses[i].name, title: "Generic CI-H"};
          allCourses.push(courseItem);
        } else if (courses[i].name == "HASS") {
          courseItem = {name: courses[i].name, title: "Generic HASS"};
          allCourses.push(courseItem);
        }
      }
      return allCourses;
    },
    totalHours(courses) {
      let hours = 0;
      for (let i=0; i<courses.length; i++) {
        if (courses[i].name in classes) {
          hours += classes[courses[i].name]["out_of_class_hours"] + classes[courses[i].name]["in_class_hours"];
        } 
      }
      return hours.toFixed(2);
    }
    // sample fields
    // "1.00": {"rating": 5.57, "gir_attribute": "REST", "has_final": false, "description": "Presents engineering problems in a computational setting with emphasis on data science and problem abstraction. Introduces modern development tools, patterns, and libraries for distributed-asynchronous computing, including distributed hash tables, Merkle trees, PKI encryption and zero knowledge proofs. Covers data cleaning and filtering, linear regression, and basic machine learning algorithms, such as clustering, classifiers, decision trees. Sharpens problem-solving skills in an active learning lab setting. In-class exercises and weekly assignments lead to a group project. Students taking graduate version complete additional assignments and project work.", "offered_fall": false, "offered_spring": true, "meets_with_subjects": ["1.001"], "instructors": ["J. Williams"], "out_of_class_hours": 7.95, "total_units": 12, "related_subjects": ["1.125", "1.124", "1.082", "1.95", "6.851", "1.000", "1.631", "1.063", "1.013", "1.142"], "pdf_option": false, "in_class_hours": 5.38, "is_half_class": false, "level": "U", "prerequisites": "GIR:CAL1", "subject_id": "1.00", "title": "Engineering Computation and Data Science", "lab_units": 2, "design_units": 0, "public": true, "offered_summer": false, "lecture_units": 3, "preparation_units": 7, "enrollment_number": 32.75, "url": "http://student.mit.edu/catalog/m1a.html#1.00", "is_variable_units": false, "offered_IAP": false}
  },
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

  .larger {
    font-size: 20px;
  }
  .smaller {
    font-size: 15px;
  }
  .row {
    display: block;
    margin: auto;
    border-bottom: 2px solid black;
    width: 100%;
    border-radius: 15px;
  }
  .semesterName {
    margin-top: 20px;
    font-size: 24px;
  }
  #road {
    margin-top:0;
  }
</style>