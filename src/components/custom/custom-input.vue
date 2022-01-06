<template>
  <div class="custom-input">
    <label :v-for="name" class="text-sm text-gray-700 dark:text-white">{{
      label
    }}</label>
    <div class="flex">
      <div
        class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"
      ></div>
      <input
        :type="togglePassword ? '' : 'text'"
        :name="name"
        :id="name"
        v-model="model"
        class="CustomInput"
      />
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
    value: {
      type: String,
      required: true,
    },
  },
  computed: {
    model: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit('input', value);
      },
    },
  },
};
</script>
