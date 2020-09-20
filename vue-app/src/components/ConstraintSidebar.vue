<template>
  <div id="constraint-sidebar">
    <b-sidebar id="sidebar-right" title="Customize" left shadow>
      <div class="panels">
        <v-expansion-panels accordion>
          <v-expansion-panel>
            <v-expansion-panel-header>Add Major/Minor</v-expansion-panel-header>
            <v-expansion-panel-content>
              Change major:
              <form @submit.prevent="handleMajorSubmit" id="majorForm">
                <div class="select">
                  <select v-model="major">
                    <option disabled value="">Major</option>
                    <option v-for="major in majors" :key="major.id" :value="major">{{ major.value }}</option>
                  </select>
                </div>
              </form>
                <!-- 
                <div class="select">
                  <select v-model="major">
                    <option disabled value="">Second Major</option>
                    <option v-for="major in majors" :key="major.id" :value="major">{{ major.value }}</option>
                  </select>
                </div>
                <b-button variant="info" type="submit" form="majorForm">Save</b-button>
              </form> -->
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
            <v-expansion-panel-header>Optimization</v-expansion-panel-header>
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
    name: 'constraint-sidebar',
    props: ['majors', 'selected_majors'],
    data() {
      return {
        'major': 0
      }
    }
  }
</script>

<style scoped>
  /* TODO: debug this formatting */
  #sidebar-right {
    background: pink;
  }
  b-sidebar {
    /* background: var(--background-color); */
    background: pink;
  }
  #constraint-sidebar {
    background: pink;
  }
</style>