<template>
    <div class="scroll-body" fixed="left">
        <h1 id="logo-container">
            Coursehose
        </h1>
        <major-form
            v-if="login_page"
            :years="years"
            :majors="majors" 
            @next:page="nextPage"
        />
        <constraint-burger
            v-if="!login_page"
        />
        <add-course
            v-if="!login_page"
            :semesters="semesters" 
            @add:course="addCourse"
        />
        <road 
            v-if="!login_page"
            :semesters="semesters"
            @remove:course="removeCourse" 
        />
        <footer style="margin-top: 50px"
                v-if="!login_page"
        >Made with &hearts; by Ashley Lin, Lucy Zhang, Melinda Sun, and Mindren Lu for HackMIT 2020. Email coursehose@mit.edu 
            for bugs or suggestions. Many thanks to 
            <a href="https://github.com/edfan/firehose">Firehose</a>, 
            <a href="https://github.com/sipb/courseroad2">Courseroad</a>, and 
            <a href="https://github.com/venkatesh-sivaraman/FireRoad">Fireroad</a> for inspiration, data, and implementations.</footer>
    </div>
</template>

<script>
import ConstraintBurger from '@/components/ConstraintBurger.vue'
import MajorForm from '@/components/MajorForm.vue'
import AddCourse from '@/components/AddCourse.vue'
import Road from '@/components/Road.vue'

export default {
    name: "scroll-body",
    props: [
        'years',
        'majors',
        'semesters',
        'login_page'
    ],
    components: {
        ConstraintBurger,
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
        },
        addMajor(major, year) {
            this.$emit('add:major', major, year)
        },
        nextPage() {
            this.$emit('next:page');
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
    constraint-burger {
        position: fixed;    
    }
    major-form {
        margin-top: 40%;
    }
    .scroll-body {
        padding: 20px;
        flex: 80%;
        background: var(--background-color);
        overflow: auto;
    }
    #logo-container{

    }
</style>