<template>
  <Carousel :settings="settings" :breakpoints="breakpoints">
    <Slide v-for="slide in 7" :key="slide">
      <div class="w-16 h-16 sm:w-28 sm:h-28 rounded-full overflow-hidden">
        <div class="relative h-full group cursor-pointer">
          <img
            src="../assets/images/user.jpg"
            alt="Story images"
            class="group-hover:transform group-hover:scale-110 transition-all duration-700 h-full w-full"
          />
          <div
            class="w-full h-full bg-black absolute top-0 left-0 bg-opacity-10"
          ></div>
          <span class="absolute bottom-0 left-2 pb-2 font-semibold text-white">
            Your story
          </span>
        </div>
      </div>
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Navigation, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
export default defineComponent({
  name: "ExamplePagination",
  components: {
    Carousel,
    Slide,
    Navigation,
  },
  data: () => ({
    // carousel settings
    settings: {
      itemsToShow: 1,
      snapAlign: "center",
    },
    // breakpoints are mobile first
    // any settings not specified will fallback to the carousel settings
    breakpoints: {
      // 700px and up
      100: {
        itemsToShow: 3.5,
        snapAlign: "center",
      },
      // 1024 and up
      1024: {
        itemsToShow: 5,
        snapAlign: "start",
      },
    },
  }),
});
</script>
