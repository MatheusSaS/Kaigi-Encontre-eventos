<template>
  <div class="custom-radio">
    <label
      class="flex justify-start items-center text-truncate rounded-lg bg-white pl-4 pr-6 py-3 shadow-sm mr-4"
    >
      <div class="text-teal-600 mr-3">
        <input
          type="radio"
          v-model="model"     
          :value="model" 
          class="form-radio focus:outline-none focus:shadow-outline"
        />
      </div>
      <div class="select-none text-gray-700">{{label}}</div>
    </label>
  </div>
</template>

<script>
export default {
  name: "CustomRadio",
  props: {
    label: {
      type: String,
      required: true,
    },
  },
};
</script>
