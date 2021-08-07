<template>
  <div class="w-full lg:w-2/3 xl:w-2/5 pt-32 lg:pt-16 px-2">
    <!-- STORY -->
    <div class="flex justify-between items-center h-4 group mt-3">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Ultimos eventos</span
      >
    </div>

    <div class="relative space-x-2 pt-4 m-4">
      <Carousel />
    </div>
    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Recomendados para você</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-dark-txt mt-4 rounded-lg"
    >
      <div class="text-justify px-4 py-2">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates,
        autem earum cum ullam odio, molestias maxime aperiam in id aspernatur
        vel ratione odit molestiae minus ipsa obcaecati quia! Doloribus, illum.
      </div>
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Vistos recentemente por você</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-dark-txt mt-4 rounded-lg"
    >
      <div class="px-1 grid grid-cols-2 xl:grid-cols-2 2xl:grid-cols-4 gap-4">
        <div class="py-4 px-1 w-56 md:w-52 lg:w-56 xl:w-60 2xl:w-72">
          <a href="/donee/donee-3">
            <div
              class="bg-white dark:bg-dark-third relative p-2 rounded-lg text-gray-800 hover:shadow-lg"
            >
              <div
                class="right-0 mt-4 rounded-l-full absolute text-center font-bold text-xs text-white px-2 py-1 bg-yellow-500"
              >
                0 Visualização
              </div>
              <img
                src="https://source.unsplash.com/MNtag_eXMKw/1600x900"
                class="h-32 rounded-lg w-full object-cover"
              />
              <div class="flex justify-center">
                <img
                  src="https://source.unsplash.com/MNtag_eXMKw/1600x900"
                  class="rounded-full -mt-6 border-4 object-center object-cover border-white dark:border-dark-third mr-2 h-16 w-16"
                />
              </div>
              <div class="py-2 px-2">
                <div class=" font-bold font-title text-center text-gray-800 dark:text-white">KNTL</div>

                <div class="text-sm font-light text-center my-2 text-gray-800 dark:text-white">
                  Kumpulan Narasi Tidak Lazim
                </div>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Em destaque</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-dark-txt mt-4 rounded-lg"
    >
      <div class="text-justify px-4 py-2">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates,
        autem earum cum ullam odio, molestias maxime aperiam in id aspernatur
        vel ratione odit molestiae minus ipsa obcaecati quia! Doloribus, illum.
      </div>
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Cidades</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-dark-txt mt-4 rounded-lg"
    ></div>
  </div>
</template>
<script>
// @ is an alias to /src
import Carousel from "@/components/Carousel.vue";

export default {
  name: "Navegation",
  components: {
    Carousel,
  },
};
</script>
