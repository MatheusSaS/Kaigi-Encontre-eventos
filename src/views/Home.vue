<template>
  <NavBar />
  <div class="home">
    <div v-if="$route.params.route === 'home'">
      <div class="flex justify-center h-screen">
        <Category />
        <Navegation />
      </div>
    </div>
    <div v-else-if="$route.params.route === 'my-events'">
      <div class="flex justify-center h-screen mt-32 md:mt-14">
        <div class="flex flex-col flex-1 max-h-full pl-2 pr-2 rounded-md">
          <!-- Main Content -->
          <main class="flex-1 pt-2">
            <!-- Placeholder Cards -->
            <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
              <div class="flex items-center justify-center">
                <span class="text-3xl font-semibold tracking-wider uppercase "
                  >Meus Eventos</span
                >
              </div>
              <div class="flex items-center justify-center mt-3">
                <router-link
                  to="/create-event"
                  type="button"
                  class="focus:outline-none text-white py-2.5 px-5 border-b-4 border-yellow-600 rounded-lg bg-yellow-500 hover:bg-yellow-400"
                  >Criar Evento</router-link
                >
              </div>
            </div>
            <div
              class="p-4 text-white bg-white dark:bg-dark-third rounded-md shadow-md mt-3 h-96"
            >
              <div class="flex items-stretch justify-ri"></div>
            </div>
          </main>
        </div>
      </div>
    </div>
    <div v-else-if="$route.params.route === 'dashboard'">
      <div class="relative flex h-screen ">
        <div
          class="flex flex-col flex-1 max-h-full pl-2 pr-2 rounded-md mt-14"
        >
          <!-- Main Content -->
          <main class="flex-1 pt-2">
            <!-- Placeholder Cards -->
            <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
              <div class="flex items-center justify-center">
                <span class="text-3xl font-semibold tracking-wider uppercase"
                  >Dashboard</span
                >
              </div>
            </div>
            <div
              class="flex items-center justify-center p-4 mt-4 bg-white rounded-md shadow-md"
            >
              <span class="text-xl tracking-wider text-gray-500 uppercase"
                >placeholder</span
              >
            </div>
            <div class="grid grid-cols-1 gap-6 mt-4 md:grid-cols-2">
              <template x-for="i in 4">
                <div
                  class="flex items-center justify-center w-full h-32 bg-white rounded-md shadow-md"
                >
                  <span class="text-xl tracking-wider text-gray-500 uppercase"
                    >placeholder</span
                  >
                </div>
              </template>

              <div
                class="flex items-center justify-center w-full h-32 bg-white rounded-md shadow-md"
              >
                <span class="text-xl tracking-wider text-gray-500 uppercase"
                  >placeholder</span
                >
              </div>

              <div
                class="flex items-center justify-center w-full h-32 bg-white rounded-md shadow-md"
              >
                <span class="text-xl tracking-wider text-gray-500 uppercase"
                  >placeholder</span
                >
              </div>

              <div
                class="flex items-center justify-center w-full h-32 bg-white rounded-md shadow-md"
              >
                <span class="text-xl tracking-wider text-gray-500 uppercase"
                  >placeholder</span
                >
              </div>

              <div
                class="flex items-center justify-center w-full h-32 bg-white rounded-md shadow-md"
              >
                <span class="text-xl tracking-wider text-gray-500 uppercase"
                  >placeholder</span
                >
              </div>
            </div>
            <div class="grid grid-cols-1 gap-6 my-4 mt-4">
              <template x-for="i in 4">
                <div
                  class="flex items-center justify-center w-full h-56 bg-white rounded-md shadow-md"
                >
                  <span class="text-xl tracking-wider text-gray-500 uppercase"
                    >placeholder</span
                  >
                </div>
              </template>
            </div>
          </main>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import Category from "@/components/Category.vue";
import Navegation from "@/components/Navegation.vue";

export default {
  name: "Home",
  components: {
    NavBar,
    Category,
    Navegation,
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
};
</script>
