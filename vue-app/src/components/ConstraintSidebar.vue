<template>
  <div>
    <b-sidebar id="sidebar-right" title="Add Constraints" right shadow>
      <div class="px-3 py-2">
        <p>
          This is some temporary placeholder text, constraints will be added.
        </p>
        <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>

        <v-expansion-panels>
          <v-expansion-panel
            v-for="(item,i) in 5"
            :key="i"
          >
            <v-expansion-panel-header>Item</v-expansion-panel-header>
            <v-expansion-panel-content>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
  export default {
    name: 'constraint-sidebar'
  }
</script>

<style scoped>
</style>