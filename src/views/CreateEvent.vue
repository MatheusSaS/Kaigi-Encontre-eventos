<template>
  <NavBar />
  <div class="createevent">
    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <!-- Main Content -->
        <main class="flex-1 pt-2">
          <!-- Placeholder Cards -->
          <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
            <div class="flex items-center justify-start">
              <span class="text-3xl font-semibold tracking-wider uppercase"
                >Criar Evento</span
              >
            </div>
          </div>
          <div class="flex justify-center h-screen">
            <div class="w-full 2xl:w-3/6 pt-5 lg:pt-5 ">
              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-1 h-auto w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >1. Informações básicas
                </span>
                <div class="flex -mx-3 mt-5">
                  <div class="w-full px-3 mb-5">
                    <label for="" class="text-sm text-gray-700 dark:text-white"
                      >Nome do evento</label
                    >
                    <div class="flex mb-2">
                      <div
                        class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"
                      ></div>
                      <input
                        type="text"
                        name="name"
                        class="w-full -ml-10 pl-1 pr-3 py-2 mt-1 rounded-lg border outline-none focus:border-blue-600 text-black dark:text-white dark:bg-dark-third border-dark-txt dark:border-dark-second dark:focus:border-blue-600"
                      />
                    </div>

                    <div class="mt-5">
                      <UploadImages
                        :max="3"
                        :class="bg - gray - 700"
                        @change="handleImages"
                      />
                    </div>
                  </div>
                </div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-auto w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >2. Onde o seu evento vai acontecer
                </span>
                <div class="flex -mx-3 mt-5">
                  <div class="w-full px-3 mb-5">
                    <label for="" class="text-sm text-gray-700 dark:text-white"
                      >First name</label
                    >
                    <div class="flex">
                      <div
                        class="text-center pointer-events-none flex items-center justify-center"
                      ></div>
                      <div class="flex-shrink w-full inline-block relative">
                        <select
                          class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
                        >
                          <option>Novo endereço</option>
                          <option>Local a definir</option>
                          <option>Evento Online</option>
                        </select>
                        <div
                          class="pointer-events-none absolute top-0 mt-3  right-0 flex items-center px-2 text-gray-600 dark:text-white"
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
                  </div>
                  <div class="w-full px-3 mb-5">
                    <label for="" class="text-sm text-gray-700 dark:text-white"
                      >First name</label
                    >
                    <div class="flex">
                      <div
                        class="text-center pointer-events-none flex items-center justify-center"
                      ></div>
                      <div class="flex-shrink w-full inline-block relative">
                        <select
                          class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
                        >
                          <option>Novo endereço</option>
                          <option>Local a definir</option>
                          <option>Evento Online</option>
                        </select>
                        <div
                          class="pointer-events-none absolute top-0 mt-3  right-0 flex items-center px-2 text-gray-600 dark:text-white"
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
                  </div>
                </div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-auto w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >3. Quando vai acontecer
                </span>
                <div class="flex -mx-3 mt-5">
                  <div
                    type="button"
                    id="open-datepicker"
                    class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                  >
                    Gratuito
                  </div>
                  <div class="w-full px-3 mb-5">
                    <litepie-datepicker
                      trigger="open-datepicker"
                      :lang="pt - br"
                      v-model="dateValue"
                    ></litepie-datepicker>
                  </div>
                </div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-auto w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >4. Ingressos
                </span>
                <div class="flex items-center justify-center mt-3">
                  <div
                    v-on:click="openModalPaid()"
                    type="button"
                    class="focus:outline-none text-white py-2.5 px-8 rounded-lg bg-yellow-500 hover:bg-yellow-400"
                  >
                    Pago
                  </div>

                  <ModalTicketPaid></ModalTicketPaid>

                  <div
                    type="button"
                    class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                  >
                    Gratuito
                  </div>
                  <div
                    type="button"
                    class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                  >
                    Doação
                  </div>
                </div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-96 w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >5. Quando vai acontecer
                </span>
                <div class="p-1 -mx-3 mt-5 ">
                  <editor api-key="no-api-key" :class="'w-full h-72'" />
                </div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-auto w-full"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >6. Categoria
                </span>
                <div class="p-1 -mx-3 mt-5 "></div>
              </div>

              <div
                class="p-4 text-white bg-white dark:bg-dark-second rounded-md shadow-lg mt-5 h-auto w-full mb-10"
              >
                <span
                  class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                  >7. Responsabilidades
                </span>
                <div class="p-1 -mx-3 mt-5 "></div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>
<script>
import NavBar from "@/components/NavBar.vue";
import UploadImages from "vue-upload-drop-images";
import LitepieDatepicker from "litepie-datepicker";
import ModalTicketPaid from "@/components/modal/ModalTicketPaid.vue"

import Editor from "@tinymce/tinymce-vue";

export default {
  name: "CreateEvent",
  components: {
    NavBar,
    UploadImages,
    LitepieDatepicker,
    editor: Editor,
    ModalTicketPaid,
  },
  setup() {
    const dateValue = [];
    return {
      dateValue,
    };
  },
  data() {
    return {
      dateStartTicket: new Date(),
      dateEndTicket: new Date(),
    };
  },
  methods: {
    handleImages(files) {
      console.log(files);
    },
    openModalPaid() {
      const modal = document.querySelector(".modal-pago");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },
  },
};
</script>
