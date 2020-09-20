<template>
    <b-navbar class="left-sidebar" fixed="left">
        <h1><img src="../coursehose.jpg" style="height: 50px"></h1>

        <!-- <h2 id="big-title">CourseHose</h2> -->
        <constraint-burger/>
    </b-navbar>
</template>

<script>
import ConstraintBurger from "@/components/ConstraintBurger.vue"
export default {
    name: "left-sidebar",
    components: {ConstraintBurger}
}
</script>


<style scoped>
    html, body { height: 100%; width: 100%; margin: 0; }
    constraint-burger {
        vertical-align: top;
        
    }
    #big-title {
    float:left;
    font-size: 24px;
    }
    .left-sidebar {
        flex: 20%;
        background: green;
        /* width: 100px;
        height: 100vh; */
    }
</style>