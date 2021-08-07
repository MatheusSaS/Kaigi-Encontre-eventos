<template>
  <div class="ModalTicketPaid">
    <div
      class="modal-pago fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
      style="background: rgba(0,0,0,.7); display: none;"
    >
      <div
        class="shadow-lg modal-container mt-80 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
      >
        <div class="modal-content py-4 text-left px-6">
          <!--Title-->
          <div class="flex justify-between pb-3">
            <h3 class="text-2xl text-center">
              Criar ingresso <strong>pago</strong>
            </h3>
            <div
              v-on:click="modalClose()"
              class="modal-close cursor-pointer z-50"
            >
              <i class="fas fa-times text-gray-800 dark:text-white"></i>
            </div>
          </div>
          <form class="">
            <div class="md:flex md:justify-between -mx-3 mt-5">
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Nome</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="name"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
                </div>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Quantidade</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="amount"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
                </div>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Preço</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="price"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
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

            <div class="md:flex md:justify-between -mx-3 ml-1">
              <label class="inline-flex items-center mt-3">
                <input
                  type="checkbox"
                  value="false"
                  class="form-checkbox h-5 w-5 text-gray-600"
                  checked
                /><span class="ml-2 text-gray-700 dark:text-white"
                  >Criar meia-entrada para este ingresso:</span
                >
              </label>
            </div>

            <div class="md:justify-between -mx-3 mt-5 hidden">
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Nome</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="name"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
                </div>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Quantidade</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="amount"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
                </div>
              </div>
              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Preço</label
                >
                <div class="flex">
                  <input
                    type="text"
                    name="price"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
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
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                      :value="inputValue"
                      v-on="inputEvents"
                      name="datainiciovendas"
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
                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
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
                  Quantidade por compra 
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
                    name="amount"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
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
                    name="amount"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  />
                </div>
              </div>

              <div class="w-full px-3 mb-5">
                <label for="" class="text-sm text-gray-700 dark:text-white"
                  >Descrição do Ingresso</label
                >
                <div class="flex">
                  <textarea
                    rows="2"
                    maxlength="110"
                    x-model="maximum"
                    x-ref="maximum"
                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                  ></textarea>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { DatePicker } from "v-calendar";

export default {
  name: "CreateEvent",
  components: {
    DatePicker,
  },
  data() {
    return {
      dateStartTicket: new Date(),
      dateEndTicket: new Date(),
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
  },
};
</script>
