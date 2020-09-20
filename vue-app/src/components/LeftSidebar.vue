<template>
    <div class="left-sidebar" fixed="left">
        <div id="logo-container">
            <img src="../coursehose.jpg" id="logo">
        </div>

        <!-- <h2 id="big-title">CourseHose</h2> -->
        <constraint-burger/>
    </div>
    
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
    .left-sidebar {
        position: fixed;
        flex: 20%;
        background: green;
        width: 400px;
        height: 100vh;
        padding: 20px;
    }

    #logo {
        float: center;
        width: 90%;        
    }
    #logo-container {
        width:100%
    }
</style>