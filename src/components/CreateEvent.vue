<template>
  <div class="createevent">
      <NavBar />
    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <!-- Main Content -->
        <main class="flex-1 pt-2">
          <!-- Placeholder Cards -->
          <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
            <div class="flex items-center justify-start">
              <span class="text-3xl font-semibold tracking-wider uppercase">
                Criar Evento
                <span class="font-bold" v-if="$route.params.type === '1'">
                  Pago
                </span>
                <span class="font-bold" v-if="$route.params.type === '2'">
                  Online
                </span>
              </span>
            </div>
          </div>
          <div class="flex justify-center h-screen">
            <div class="w-full 2xl:w-3/6 pt-5 lg:pt-5 ">
              <form action="">
                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >1. Informações básicas
                  </span>
                  <div class="flex -mx-3 mt-5">
                    <div class="w-full px-3 mb-5">
                      <CustomInput
                        :label="'Nome do evento'"
                        :name="'fassunto'"
                      />

                      <div class="mt-5">
                        <UploadImages
                          :max="3"
                          :class="bg - gray - 700"
                          @change="handleImages"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="flex -mx-3 ">
                    <div class="w-full px-3 mb-5">
                      <CustomSelect :label="'Assunto'" :name="'fassunto'" />
                    </div>
                    <div class="w-full px-3 mb-5">
                      <CustomSelect :label="'Categoria'" :name="'fcategoria'" />
                    </div>
                  </div>
                </div>

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >2. Onde o seu evento vai acontecer
                  </span>
                  <div class="font-bold" v-if="$route.params.type === '1'">
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mb-5">
                        <CustomSelect :label="'Local'" :name="'flocal'" />
                      </div>
                    </div>
                    <div class="flex -mx-3">
                      <div class="w-full px-3 mb-5">
                        <CustomInput :label="'Endereço'" :name="'fendereco'" />
                      </div>
                      <div class="w-full px-3 mb-5">
                        <CustomInput
                          :label="'Nome do Local'"
                          :name="'fnomelocal'"
                        />
                      </div>
                    </div>
                    <div class="flex -mx-3 m">
                      <div class="w-full px-3 mb-5">
                        <CustomInput :label="'CEP'" :name="'fcep'" />
                      </div>
                      <div class="w-full px-3 mb-5">
                        <CustomInput :label="'Av./Rua'" :name="'fav-rua'" />
                      </div>
                    </div>
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mb-5">
                        <CustomInput :label="'Número'" :name="'fnumero'" />
                      </div>
                      <div class="w-full px-3 ">
                        <CustomInput
                          :label="'Complemento'"
                          :name="'fcomplemento'"
                        />
                      </div>
                    </div>
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3">
                        <CustomInput :label="'Bairro'" :name="'fbairro'" />
                      </div>
                      <div class="w-full px-3 ">
                        <CustomInput :label="'Cidade'" :name="'fcidade'" />
                      </div>
                      <div class="w-full px-3">
                        <CustomInput :label="'Estado'" :name="'festado'" />
                      </div>
                    </div>
                  </div>
                  <div class="font-bold" v-else-if="$route.params.type === '2'">
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mt-2">
                        <CustomSelect
                          :label="'Plataforma'"
                          :name="'fplataforma'"
                        />
                      </div>
                    </div>
                  </div>
                </div>

                <div class="cardEvent">
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

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >4. Ingressos
                  </span>
                  <div class="flex items-center justify-center mt-3">
                    <div
                      v-on:click="openModalPaid()"
                      type="button"
                      class="focus:outline-none cursor-pointer text-white py-2.5 px-8 rounded-lg bg-yellow-500 hover:bg-yellow-400"
                    >
                      Pago
                    </div>
                    <ModalTicketPaid></ModalTicketPaid>

                    <div
                      v-on:click="openModalFree()"
                      type="button"
                      class="focus:outline-none cursor-pointer text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                    >
                      Gratuito
                    </div>
                    <ModalTicketFree></ModalTicketFree>

                    <div
                      v-on:click="openModalDonation()"
                      type="button"
                      class="focus:outline-none cursor-pointer text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                    >
                      Doação
                    </div>
                  </div>
                  <ModalTicketDonation></ModalTicketDonation>

                  <div
                    class="w-full mb-8 mt-6 overflow-hidden rounded-lg shadow-lg"
                  >
                    <div class="w-full overflow-x-auto">
                      <table class="w-full">
                        <thead>
                          <tr
                            class="text-md font-semibold tracking-wide text-left text-gray-700 dark:text-white bg-gray-100 dark:bg-dark-main uppercase border-b border-gray-300 dark:border-gray-600"
                          >
                            <th class="px-4 py-3">Name</th>
                            <th class="px-4 py-3">Age</th>
                            <th class="px-4 py-3">Date</th>
                            <th class="px-4 py-3 text-center">Ações</th>
                          </tr>
                        </thead>
                        <tbody class=" bg-white dark:bg-dark-second">
                          <tr class="text-gray-700 dark:text-white">
                            <td class="px-4 py-3 ">
                              <div class="flex items-center text-sm">
                                <div
                                  class="relative w-8 h-8 mr-3 rounded-full md:block"
                                >
                                  <img
                                    class="object-cover w-full h-full rounded-full"
                                    src="https://images.pexels.com/photos/5212324/pexels-photo-5212324.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260"
                                    alt=""
                                    loading="lazy"
                                  />
                                  <div
                                    class="absolute inset-0 rounded-full shadow-inner"
                                    aria-hidden="true"
                                  ></div>
                                </div>
                                <div>
                                  <p
                                    class="font-semibold text-gray-700 dark:text-white"
                                  >
                                    Sufyan
                                  </p>
                                  <p
                                    class="text-xs text-gray-600 dark:text-gray-300"
                                  >
                                    Developer
                                  </p>
                                </div>
                              </div>
                            </td>
                            <td class="px-4 py-3 text-ms font-semibold">
                              22
                            </td>
                            <td class="px-4 py-3 text-sm ">6/4/2000</td>
                            <td class="py-4 px-3 ">
                              <div class="flex item-center justify-center">
                                <div
                                  class="w-4 mr-2 transform hover:text-blue-500 hover:scale-110"
                                >
                                  <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                  >
                                    <path
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                      stroke-width="2"
                                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                                    />
                                    <path
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                      stroke-width="2"
                                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                                    />
                                  </svg>
                                </div>
                                <div
                                  class="w-4 mr-2 transform hover:text-blue-500 hover:scale-110"
                                >
                                  <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                  >
                                    <path
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                      stroke-width="2"
                                      d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                                    />
                                  </svg>
                                </div>
                                <div
                                  class="w-4 mr-2 transform hover:text-blue-500 hover:scale-110"
                                >
                                  <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    stroke="currentColor"
                                  >
                                    <path
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                      stroke-width="2"
                                      d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                                    />
                                  </svg>
                                </div>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >5. Descrição do evento
                  </span>
                  <div class="p-1 -mx-3 mt-5 ">
                    <editor api-key="no-api-key" :class="'w-full h-72'" />
                  </div>
                </div>
                <div class="cardEvent mb-2">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >6. Responsabilidades
                  </span>
                  <div class="p-1 -mx-3 mt-5 "></div>
                </div>
              </form>
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
import ModalTicketPaid from "@/components/modal/ModalTicketPaid.vue";
import ModalTicketFree from "@/components/modal/ModelTicketFree.vue";
import ModalTicketDonation from "@/components/modal/ModalTicketDonation.vue";
import CustomInput from "@/components/custom/custom-input.vue";
import CustomSelect from "@/components/custom/custom-select.vue";

import Editor from "@tinymce/tinymce-vue";

export default {
  name: "CreateEvent",
  components: {
    NavBar,
    UploadImages,
    LitepieDatepicker,
    editor: Editor,
    ModalTicketPaid,
    ModalTicketFree,
    ModalTicketDonation,
    CustomInput,
    CustomSelect,
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
    openModalFree() {
      const modal = document.querySelector(".modal-gratis");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },
    openModalDonation() {
      const modal = document.querySelector(".modal-doacao");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },
  },
};
</script>
