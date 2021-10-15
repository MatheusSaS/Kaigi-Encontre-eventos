<template>
  <label for="{{ label }}" class="text-sm text-gray-700 dark:text-white">
      {{ label }}
  </label>
  <div class="flex">
    <div
      class="text-center pointer-events-none flex items-center justify-center"
    ></div>
    <div class="flex-shrink w-full inline-block relative">
      <select
        name="{{name}}"
        class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
      >
        <option v-for="value in values" v-bind:key="value.id">
            {{ value.name }}
        </option>
      </select>
      <div
        class="pointer-events-none absolute top-0 mt-1  right-0 flex items-center px-2 text-gray-600 dark:text-white"
      >
        <svg
          class="fill-current h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <path
            d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
          />
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomInput",
  props: {
    label: {
      type: String,
      required: true,
    },
  },
  computed: {
    name() {
      return this.label.toLowerCase();
    },
  },
};
</script>
