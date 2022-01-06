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
        <h1>{{testa}}</h1>
          <form @submit.prevent="CreateTicket">
            <div class="md:flex md:justify-between -mx-3 mt-5">
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white">
                  Nome Ingresso
                </label>
                <div class="flex">
                  <input
                    name="NameEvent"
                    v-model="ticket.ticket_name"
                    type="text"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                  />
                </div>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Quantidade</label
                >
                <div class="flex">
                  <input
                    name="Amount"
                    v-model="ticket.amount"
                    type="number"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                  />
                </div>
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
                    <input
                      type="text"
                      name="Price"
                      v-model="ticket.price"
                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                      placeholder="0.00"
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
              </div>
              <div class="w-15 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Total</label
                >
                <div class="flex mt-5">
                  <p class="text-green-500">
                    {{ ticket.amount * ticket.price }}
                  </p>
                </div>
              </div>
            </div>

            <div class="md:flex md:justify-between -mx-3 ml-1">
              <label class="inline-flex items-center mt-3">
                <input
                  type="checkbox"
                  value="True"
                  v-model="ticket.half"
                  class="form-checkbox h-5 w-5 text-gray-600"
                  unchecked
                /><span class="ml-2 text-gray-700 dark:text-white"
                  >Criar meia-entrada para este ingresso:</span
                >
              </label>
            </div>

            <div v-if="ticket.half === true">
              <div class="md:flex md:justify-between -mx-3 mt-5">
                <div class="w-full px-3 mb-5">
                  <label for="" class="text-sm text-gray-700 dark:text-white">
                    Nome meio impresso
                  </label>
                  <div class="flex">
                    <input
                      name="NameEventHelf"
                      type="text"
                      v-model="ticket.half_description"
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    />
                  </div>
                </div>
                <div class="w-full px-3 mb-5">
                  <label for="" class="text-sm text-gray-700 dark:text-white "
                    >Quantidade</label
                  >
                  <div class="flex">
                    <input
                      @keypress="validateNumber"
                      v-model="ticket.half_amount"
                      name="AmountHelf"
                      type="text"
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                    />
                  </div>
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
                      <input
                        type="text"
                        v-model="ticket.half_price"
                        name="PriceHelf"
                        class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                        placeholder="0.00"
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
                  v-model="ticket.initial_date_time"
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
                  v-model="ticket.final_date_time"
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
                  <input
                    type="text"
                    v-model="ticket.amount_min"
                    name="Amountminimum"
                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                  />
                </div>
              </div>

              <div class="w-48 px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Maxima</label
                >
                <div class="flex">
                  <input
                    type="text"
                    v-model="ticket.amount_max"
                    name="Amountmax"
                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                  />
                </div>
              </div>

              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Descrição do Ingresso</label
                >
                <div class="flex">
                  <textarea
                    v-model="ticket.description"
                    name="Description"
                    rows="2"
                    maxlength="110"
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
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Ticket from "@/services/Events.js";
import { createToast } from "mosha-vue-toastify";

import { DatePicker } from "v-calendar";

export default {
  name: "ModalTicketPaid",
  components: {
    DatePicker,
  },
  data() {
    return {
      halfprice: "",
      descriptionHelfprice: "",
      ticket: {
        id_type_ticket: "",
        user_id: "",
        ticket_name: "",
        amount: "",
        price: "",
        initial_date_time: "",
        final_date_time: "",
        amount_min: "",
        amount_max: "",
        description: "",
        total: "",

        half: false,
        half_description: "",
        half_amount: 0,
        half_price: 0,
        half_total: 0,
      },      
    };
  },
  setup() {
    const toast = (type, msg) => {
      createToast(msg, { type: type, transition: "zoom" });
    };

    return {
      toast,
    };
  },  
  methods: {
    CreateTicket() {
      if (localStorage.getItem("public_id")) {
        this.ticket.id_type_ticket = 1
        this.ticket.user_id = localStorage.getItem("public_id");
        this.ticket.total = (this.ticket.amount * this.ticket.price)
        Ticket.createTicket(this.ticket)
          .then((response) => {
            this.toast("success", response.data["message"]);
            this.modalClose()
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      }
    },
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
