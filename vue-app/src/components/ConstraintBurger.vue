<template>
    <div id="burger"
         :class="{ 'active' : isBurgerActive }"
         @click.prevent="toggle">
        <slot>
            <b-button v-b-toggle.sidebar-right type="button" id="bootstrap-overrides" class="burger-button" title="Menu">
                <span class="burger-bar burger-bar--1"></span>
                <span class="burger-bar burger-bar--2"></span>
                <span class="burger-bar burger-bar--3"></span>
            </b-button>
        </slot>
    </div>
</template>

<script>
    export default {
        data: () => ({
            isBurgerActive: false
        }),
        methods: {
            toggle() {
                this.isBurgerActive = !this.isBurgerActive
            }
        }
    }
</script>

<style>
   .hidden {
        visibility: hidden;
    }

    button {
        cursor: pointer;
    }

    /* remove blue outline */
    button:focus {
        outline: 0;
    }

    .burger-button {
        position: relative;
        height: 35px;
        width: 45px;
        display: block;
        z-index: 999;
        border: 0;
        border-radius: 0;
        background-color: transparent;
        pointer-events: all;
        float: left;
    }
   .burger-bar {
        background-color: #130f40;
        position: absolute;
        top: 50%;
        right: 6px;
        left: 6px;
        height: 2px;
        width: auto;
        margin-top: -1px;
    }

    .burger-bar--1 {
        -webkit-transform: translateY(-6px);
        transform: translateY(-8px);
    }

    .burger-bar--2 {
        transform-origin: 100% 50%;
    }

    .burger-bar--3 {
        transform: translateY(8px);
    }

    .burger-button:hover .burger-bar  {
        background-color:grey;
    }

    #burger.active .burger-bar {
        background-color:black;
    }

    #bootstrap-overrides {
        background-color: transparent;
        border-color: transparent;
        outline: 0;
    }

    #bootstrap-overrides:focus {
        border-color: transparent;
        box-shadow: none;
    }



</style>