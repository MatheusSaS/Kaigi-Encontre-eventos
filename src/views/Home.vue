<template>  
  <div class="home">
    <NavBar />
    <div v-if="$route.name === 'Home'">
      <div class="flex justify-center h-screen">
        <Category />
        <Navegation />        
      </div>
    </div>
    <div v-else-if="$route.name === 'my-events'">
      <EventList />
    </div>
    <div v-else-if="$route.name === 'dashboard'">
      <Dashboard />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import Category from "@/components/Category.vue";
import Navegation from "@/components/Navegation.vue";
import EventList from "@/views/EventList.vue";
import Dashboard from "@/views/Dashboard.vue";

export default {
  name: "Home",
  components: {
    NavBar,
    Category,
    Navegation,
    EventList,
    Dashboard,
  },
  methods: {
    setup() {
      return {
        isSidebarOpen: false,
        toggleSidebar() {
          this.isSidebarOpen = !this.isSidebarOpen;
        },
        isSettingsPanelOpen: false,
        toggleSettingsPanel() {
          this.isSettingsPanelOpen = !this.isSettingsPanelOpen;
        },
      };
    },
  },
  mounted() {},
};
</script>
