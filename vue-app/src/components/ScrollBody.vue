<template>
    <div class="scroll-body" fixed="left">
        <major-form
            :years="years"
            :majors="majors" 
        />
        <add-course
            :semesters="semesters" 
            @add:course="addCourse"
        />
        <road 
            :semesters="semesters"
            @remove:course="removeCourse" 
        />
    </div>
</template>

<script>
import MajorForm from '@/components/MajorForm.vue'
import AddCourse from '@/components/AddCourse.vue'
import Road from '@/components/Road.vue'

export default {
    name: "scroll-body",
    props: [
        'years',
        'majors',
        'semesters',
    ],
    components: {
        MajorForm,
        AddCourse,
        Road
    },
    methods: {
        addCourse(course) {
            this.$emit('add:course', course)
        },
        removeCourse(course, semester) {
            this.$emit('remove:course', course, semester)
        }
    }
}
</script>


<style scoped>
    html, body { height: 100%; width: 100%; margin: 0; }
    #big-title {
    float:left;
    font-size: 24px;
    }
    .scroll-body {
        padding: 20px;
        flex: 80%;
        background: lightskyblue;
        overflow: auto;
        /* width: 50%;
        height: 100vh; */
    }
</style>