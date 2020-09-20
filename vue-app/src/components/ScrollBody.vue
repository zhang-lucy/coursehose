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
        <footer style="margin-top: 50px">Made by Ashley Lin, Lucy Zhang, Melinda Sun, and Mindren Lu for HackMIT 2020. Many thanks to 
            <a href="https://github.com/edfan/firehose">Firehose</a>, 
            <a href="https://github.com/sipb/courseroad2">Courseroad</a>, and 
            <a href="https://github.com/venkatesh-sivaraman/FireRoad">Fireroad</a> for inspiration, data, and implementations.</footer>
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