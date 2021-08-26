<template>
  <div class="ModalTicketFree">
    <div
      class="modal-gratis fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
      style="background: rgba(0,0,0,.7); display: none;"
    >
      <div
        class="shadow-lg modal-container mt-60 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
      >
        <div
          class="modal-content mt-10 sm:mt-0 py-4 text-left px-6"
        >
          <!--Title-->
          <div class="flex justify-between pb-3">
            <h3 class="text-2xl text-center">
              Criar ingresso <strong>grátis</strong>
            </h3>
            <div
              v-on:click="modalClose()"
              class="modal-close cursor-pointer z-50 mt-2"
            >
              <i class="fas fa-times text-gray-800 dark:text-white"></i>
            </div>
          </div>
          <Form
            @submit="onSubmit"
            :validation-schema="schema"
            v-slot="{ errors }"
          >
            <div class="md:flex md:justify-between -mx-3 mt-5">
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white">
                  Nome Ingresso
                </label>
                <div class="flex">
                  <Field
                    name="NameEvent"
                    v-model="descriptionHelfprice"
                    type="text"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    :class="{ 'border border-red-600': errors.NameEvent }"
                  />
                </div>
                <label for="" class="text-sm text-red-600">
                  {{ errors.NameEvent }}
                </label>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Quantidade</label
                >
                <div class="flex">
                  <Field
                    @keypress="validateNumber"
                    name="Amount"
                    type="text"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    :class="{ 'border border-red-600': errors.Amount }"
                  />
                </div>
                <label for="" class="text-sm text-red-600">
                  {{ errors.Amount }}
                </label>
              </div>
              <div class="w-full sm:w-2/5 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Preço
                </label>
                <div class="flex">
                  <div class="flex">
                  <input
                    name="Price"
                    value="Grátis"
                    type="text"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-dark-second dark:text-gray-300 dark:bg-dark-second border focus:border-blue-600  dark:focus:border-blue-600 cursor-not-allowed"
                    disabled
                  />
                </div>
                </div>
              </div>
            </div>

            <div class="md:flex md:justify-between -mx-3 mt-5">
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Data / Horário de Início das Vendas</label
                >
                <DatePicker
                  v-model="dateStartTicket"
                  mode="dateTime"
                  is24hr
                  is-dark
                >
                  <template v-slot="{ inputValue, inputEvents }">
                    <input
                      name="dateStartTicket"
                      class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                      :value="inputValue"
                      v-on="inputEvents"
                    />
                  </template>
                </DatePicker>
              </div>

              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Data / Horário de Término das Vendas</label
                >
                <DatePicker
                  v-model="dateEndTicket"
                  mode="dateTime"
                  is24hr
                  is-dark
                >
                  <template v-slot="{ inputValue, inputEvents }">
                    <input
                      class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                      :value="inputValue"
                      v-on="inputEvents"
                      name="datainiciovendas"
                    />
                  </template>
                </DatePicker>
              </div>
            </div>
            <div class="md:flex mt-1">
              <div class="flex justify-between pb-3">
                <h6 class="text-2xl text-center">
                  Quantidade por compra:
                </h6>
              </div>
            </div>

            <div class="md:flex -mx-3 mt-5">
              <div class="w-48 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Mínima</label
                >
                <div class="flex">
                  <Field
                    type="text"
                    name="Amountminimum"
                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    :class="{ 'border border-red-600': errors.Amountminimum }"
                  />
                </div>
                <label for="" class="text-sm text-red-600">
                  {{ errors.Amountminimum }}
                </label>
              </div>

              <div class="w-48 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Maxima</label
                >
                <div class="flex">
                  <Field
                    type="text"
                    name="Amountmax"
                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    :class="{ 'border border-red-600': errors.Amountmax }"
                  />
                </div>
                <label for="" class="text-sm text-red-600">
                  {{ errors.Amountmax }}
                </label>
              </div>

              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Descrição do Ingresso</label
                >
                <div class="flex">
                  <textarea
                    name="Description"
                    rows="2"
                    maxlength="110"
                    x-model="maximum"
                    x-ref="maximum"
                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                  ></textarea>
                </div>
              </div>
            </div>

            <div class="flex mt-3">
              <button
                type="submit"
                class="focus:outline-none cursor-pointer text-white p-2.5 rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3 text-center"
              >
                Criar evento
              </button>

              <div
                type="button"
                v-on:click="modalClose()"
                class="focus:outline-none cursor-pointer text-white py-2.5 rounded-lg text-red-700 ml-8 text-center "
              >
                Cancelar
              </div>
            </div>
          </Form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { DatePicker } from "v-calendar";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";

export default {
  name: "ModalTicketFree",
  components: {
    DatePicker,
    Form,
    Field,
  },
  setup() {
    const schema = Yup.object().shape({
      NameEvent: Yup.string()
        .min(3, "Minimo 3 caracteres!")
        .required("Campo Obrigatório"),
      Amount: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "A quantidade tem que ser maior que 0"),
      Amountminimum: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
      Amountmax: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
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
  data() {
    return {
      dateStartTicket: new Date(),
      dateEndTicket: new Date(),
      descriptionHelfprice: "",
    };
  },
  methods: {
    modalClose() {
      const modal = document.querySelector(".modal-gratis");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
    validateForm(scope) {
      this.$validator.validateAll(scope).then((result) => {
        if (result) {
          // eslint-disable-next-line
          alert("Form Submitted!");
        }
      });
    },
    validateNumber: (event) => {
      let keyCode = event.keyCode;
      if (keyCode < 48 || keyCode > 57) {
        event.preventDefault();
      }
    },
  },
};
</script>
