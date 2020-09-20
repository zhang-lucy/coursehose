<template>
  <div>
    <b-sidebar id="sidebar-right" title="Customize" left shadow>
      <div class="px-3 py-2">
        <v-expansion-panels accordion>
          <v-expansion-panel>
            <v-expansion-panel-header>Add Major/Minor</v-expansion-panel-header>
            <v-expansion-panel-content>
              Dropdowns to add more majors/minors
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>Units</v-expansion-panel-header>
            <v-expansion-panel-content>
              Maximum units per semester
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>Hours</v-expansion-panel-header>
            <v-expansion-panel-content>
              Maximum hours per semester
            </v-expansion-panel-content>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-header>Hours</v-expansion-panel-header>
            <v-expansion-panel-content>
              Optimization
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