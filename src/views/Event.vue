<template>
  <div class="Event">
    <NavBar />
    <main class="relative mx-auto px-4 ">
      <div class="relative -mx-4 top-0   h-96 overflow-hidden">
        <img
          class="absolute inset-0 object-cover object-top w-full h-full filter blur"
          :src="events.image"
          alt=""
        />
      </div>
      <div class="-mt-40 md:w-4/6 lg:w-1/3 w-full  mx-auto">
        <div class="relative pt-[56.25%] overflow-hidden rounded-2xl">
          <img
            class="w-full h-full absolute inset-0 object-cover"
            :src="events.image"
            alt=""
          />
        </div>
      </div>

      <article class="max-w-5xl mx-auto py-8">
        <h1 class="text-2xl font-bold text-gray-800 dark:text-gray-50">
         {{events.name}}
        </h1>
        <h2 class="mt-2 text-sm text-red-500">{{events.initial_date}}</h2>

        <h2 v-if="events.platform" class="mt-2 text-sm text-gray-500 ">Local {{events.platform}}</h2>
        <h2 v-else class="mt-2 text-sm text-gray-500 ">Local: {{events.location_name}} - {{events.city}} {{events.state}}</h2>

        <p class="mt-6 text-gray-800 dark:text-gray-50" v-html="events.description">

        </p>
      </article>
    </main>
  </div>
</template>
<script>
// @ is an alias to /src
import Event from "@/services/Events.js";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "Event",
  components: {
    NavBar,
  },
  data() {
    return {
      events: [],
    };
  },
  mounted() {
    Event.GetEvent(this.$route.params.id).then((response) => {
      this.events = response.data.event;
    });
  },
};
</script>
<style>
.pt-\[17\%\] {
  padding-top: 17%;
}
.mt-\[-10\%\] {
  margin-top: -10%;
}
.pt-\[56\.25\%\] {
  padding-top: 56.25%;
}
</style>
