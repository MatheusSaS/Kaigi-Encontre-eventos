<template>
  <label :v-for="name" class="text-sm text-gray-700 dark:text-white"
    >{{ label }}</label
  >
  <div class="flex">
    <div
      class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"
    ></div>
    <Field
      type="text"
      :name="name"
      :id="name"
      v-model="value"
      class="w-full -ml-10 pl-1 pr-3 py-2 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
    />
  </div>  
</template>

<script>
import {Field } from "vee-validate";
import * as Yup from "yup";

export default {
  name: "CustomInput",
  components: {
    Field,
  },
  setup() {
    const schema = Yup.object().shape({
      fassunto : Yup.string()
        .min(this.characters, `Minimo ${this.characters} caracteres!`)
        .required("Campo Obrigatório"),
    });

    const onSubmit = (values) => {
      // display form values on success
      alert("SUCCESS!! :-)\n\n" + JSON.stringify(values, null, 4));
    };

    return {
      schema,
      onSubmit,
    };
  },
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
