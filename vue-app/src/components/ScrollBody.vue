<template>
    <div class="scroll-body" fixed="left">
        hiwi
        <major-form/>
        <add-course/>
        <road/>
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
        'semesters'
    ],
    components: {
        MajorForm,
        AddCourse,
        Road
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
        flex: 80%;
        background: pink;
        /* width: 50%;
        height: 100vh; */
    }
</style>