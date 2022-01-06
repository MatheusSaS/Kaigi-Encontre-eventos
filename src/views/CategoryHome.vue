<template>
  <div class="CategoryHome">
    <NavBar />
    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <main class="flex-1 pt-2">
          <div class="p-4 text-white rounded-md shadow-md bg-blue-500">
            <div class="flex items-center justify-center">
              <span class="text-3xl font-semibold tracking-wider uppercase "
                >{{$route.params.type}}</span
              >
            </div>
          </div>
          <div class="p-4 text-white h-96">
            <div class="flex justify-center h-screen">
              <div class="w-full  container mt-10">
                <div class="dark:text-gray-50 rounded-lg mb-5">
                  <div
                    class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
                  >
                     <div
                      v-for="item in categories" :key="item.id"
                      class="col-span-4 sm:col-span-4 md:col-span-2 lg:col-span-1 xl:col-span-1 flex flex-col items-center"
                    >
                      <div class="bg-white rounded-lg mt-5">
                        <img
                          :src="item.image"
                          class="h-40 rounded-md"
                          alt=""
                        />
                      </div>
                      <div class="bg-white shadow-lg rounded-lg -mt-4 w-64">
                        <div class="py-5 px-5">
                          <span class="font-bold text-gray-800 text-lg"
                            >{{item.name}}</span
                          >
                        </div>
                      </div>
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import Events from "@/services/Events.js";

export default {
  name: "CategoryHome",
  components: {
    NavBar,
  },
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    Events.Category(this.$route.params.type).then((response) => {
      this.categories = response.data.category;
      console.log('====================================');
      console.log(this.categories);
      console.log('====================================');
    });
  },
};
</script>
