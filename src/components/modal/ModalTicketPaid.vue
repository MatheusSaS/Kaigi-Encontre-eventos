<template>
  <div class="ModalTicketPaid">
    <div
      class="modal-pago fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
      style="background: rgba(0,0,0,.7); display: none;"
    >
      <div
        class="shadow-lg modal-container mt-96 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
      >
        <div
          class="modal-content mt-10 sm:mt-0 py-4 text-left px-6"
          :class="{ 'mt-96': halfprice }"
        >
          <!--Title-->
          <div class="flex justify-between pb-3">
            <h3 class="text-2xl text-center">
              Criar ingresso <strong>pago</strong>
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
                  <div class="mt-1 relative rounded-md shadow-sm">
                    <div
                      class="absolute inset-y-0 left-0 pl-1 flex items-center pointer-events-none"
                    >
                      <span class="text-gray-500 sm:text-sm">
                        R$
                      </span>
                    </div>
                    <Field
                      type="text"
                      name="Price"
                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                      placeholder="0.00"
                      :class="{ 'border border-red-600': errors.Price }"
                    />
                    <div class="absolute inset-y-0 right-0 flex items-center">
                      <label for="currency" class="sr-only">Currency</label>
                      <select
                        id="currency"
                        name="currency"
                        class="focus:ring-indigo-500 focus:border-indigo-500 h-full py-0 pl-2 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md"
                      >
                        <option>BRL</option>
                        <option>USD</option>
                      </select>
                    </div>
                  </div>
                </div>
                <label for="" class="text-sm text-red-600">
                  {{ errors.Price }}
                </label>
              </div>
              <div class="w-15 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Total</label
                >
                <div class="flex mt-5">
                  <p class="text-green-500">R$:10</p>
                </div>
              </div>
            </div>

            <div class="md:flex md:justify-between -mx-3 ml-1">
              <label class="inline-flex items-center mt-3">
                <input
                  type="checkbox"
                  value="True"
                  v-model="halfprice"
                  class="form-checkbox h-5 w-5 text-gray-600"
                  unchecked
                /><span class="ml-2 text-gray-700 dark:text-white"
                  >Criar meia-entrada para este ingresso:</span
                >
              </label>
            </div>

            <div v-if="halfprice === true">
              <div class="md:flex md:justify-between -mx-3 mt-5">
                <div class="w-full px-3 mb-5">
                  <label for="" class="text-sm text-gray-700 dark:text-white">
                    Nome meio impresso
                  </label>
                  <div class="flex">
                    <Field
                      name="NameEventHelf"
                      type="text"
                      v-model="descriptionHelfprice"
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-dark-second dark:text-gray-300 dark:bg-dark-second border focus:border-blue-600  dark:focus:border-blue-600 cursor-not-allowed"
                      disabled
                    />
                  </div>
                </div>
                <div class="w-full px-3 mb-5">
                  <label
                    for=""
                    class="text-sm text-gray-700 dark:text-white "
                    :class="{
                      'text-red-600 dark:text-red-600': errors.AmountHelf,
                    }"
                    >Quantidade</label
                  >
                  <div class="flex">
                    <Field
                      @keypress="validateNumber"
                      name="AmountHelf"
                      type="text"
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                      :class="{ 'border border-red-600': errors.AmountHelf }"
                    />
                  </div>
                  <label for="" class="text-sm text-red-600">
                    {{ errors.AmountHelf }}
                  </label>
                </div>
                <div class="w-full sm:w-2/5 px-3 mb-5">
                  <label for="" class="text-sm text-gray-700 dark:text-white"
                    >Preço
                  </label>
                  <div class="flex">
                    <div class="mt-1 relative rounded-md shadow-sm">
                      <div
                        class="absolute inset-y-0 left-0 pl-1 flex items-center pointer-events-none"
                      >
                        <span class="text-gray-500 sm:text-sm">
                          R$
                        </span>
                      </div>
                      <Field
                        type="text"
                        name="PriceHelf"
                        class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                        placeholder="0.00"
                        :class="{ 'border border-red-600': errors.PriceHelf }"
                      />
                      <div class="absolute inset-y-0 right-0 flex items-center">
                        <label for="currency" class="sr-only">Currency</label>
                        <select
                          id="currency"
                          name="currency"
                          class="focus:ring-indigo-500 focus:border-indigo-500 h-full py-0 pl-2 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md"
                        >
                          <option>BRL</option>
                          <option>USD</option>
                        </select>
                      </div>
                    </div>
                  </div>
                  <label for="" class="text-sm text-red-600">
                    {{ errors.PriceHelf }}
                  </label>
                </div>
                <div class="w-15 px-3 mb-5">
                  <label for="" class="text-sm text-gray-700 dark:text-white"
                    >Total</label
                  >
                  <div class="flex mt-5">
                    <p class="text-green-500">R$:10</p>
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
  name: "CreateEvent",
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
      Price: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
      Amountminimum: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
      Amountmax: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
      AmountHelf: Yup.string()
        .required("Campo  Obrigatório")
        .min(1, "O valor menimo é 1"),
      PriceHelf: Yup.string()
        .min(1, "O valor menimo é 1")
        .required("Campo  Obrigatório"),
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
      halfprice: "",
      descriptionHelfprice: "",
    };
  },
  methods: {
    modalClose() {
      const modal = document.querySelector(".modal-pago");
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
