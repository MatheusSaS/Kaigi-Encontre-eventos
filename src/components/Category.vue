<template>
  <div class="Category">
    <div
      class="w-1/5 pt-16 h-full hidden xl:flex flex-col fixed top-0 left-0 mt-5"
    >
      <div class="flex justify-between items-center px-4 h-4 group">
        <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
          >Categorias:</span
        >
        <span
          class="text-blue-500 cursor-pointer hover:bg-gray-200 dark:hover:bg-dark-third p-2 rounded-md hidden group-hover:inline-block"
          >Edit</span
        >
      </div>
      <ul class="p-4">
        <li>
          <a
            href="/category"
            class="flex items-center space-x-2 p-2 hover:bg-gray-200 rounded-lg transition-all dark:text-dark-txt dark:hover:bg-dark-third"
          >
            <img
              src="../assets/images/event.png"
              alt="Profile picture"
              class="w-10 h-10 rounded-lg"
            />
            <span class="font-semibold">Todos os Eventos</span>
          </a>
        </li>
        <li v-for="item in categories.category" :key="item.id">
          <button   
            v-on:click="Category(item.description)"
            class="flex items-center space-x-2 p-2 hover:bg-gray-200 rounded-lg transition-all dark:text-dark-txt dark:hover:bg-dark-third"
          >
            <img
              :src="item.image"
              alt="Profile picture"
              class="w-10 h-10 rounded-lg"
            />
            <span class="font-semibold">{{item.description}}</span>
          </button>
        </li>
      </ul>
      <div class="mt-auto p-6 text-sm text-gray-500 dark:text-dark-txt mb-2">
        <a href="#">Todos os direitos reservados </a>

        <span>Matheud Gabriel © 2021</span>
      </div>
    </div>
  </div>
</template>
<script>
import Category from "@/services/Admin.js";

export default {
  name: "Category",
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    Category.category().then((response) => {
      this.categories = response.data;
    });
  },
  methods:{
    Category: function(category) {
      this.$router.push({
        path: "/category/"+category,
      });
    },
  }
};
</script>
