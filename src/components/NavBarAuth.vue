<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
<template>
  <div class="NavBarAuth">
    <nav class="bg-white dark:bg-dark-main">
      <div
        class="flex items-center justify-center p-2 mx-auto text-gray-600 capitalize dark:text-gray-50"
      >
        <a href="/" class="inline-block ">
          <img
            src="../assets/images/logo-c.png"
            alt=""
            class="w-40 mt-3 pb-3 h-auto"
          />
        </a>
      </div>
    </nav>
  </div>
</template>

<script>

export default {
  name: "NavBarAuth",
  data: function() {
    return {};
  },
  methods: {
  },
  setup() {},
  mounted() {},
};
</script>
