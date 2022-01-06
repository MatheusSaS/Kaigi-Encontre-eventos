<template>
  <div class="EventList">
    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full pl-2 pr-2 rounded-md">
        <main class="flex-1 pt-2">
          <div class="p-4 text-white rounded-md shadow-md">
            <div class="flex items-center justify-center">
              <span class="text-3xl font-semibold tracking-wider uppercase "
                >Criar novo evento</span
              >
            </div>
            

            <div
              class=" flex  flex-col  md:flex-row justify-center  flex-wrap gap-3 mt-10  "
            >
              <div class="">
                <div
                  class="bg-white dark:bg-dark-second max-w-xs shadow-lg  mx-auto border-b-4 border-yellow-600 rounded-lg overflow-hidden  hover:shadow-2xl transition duration-500 transform hover:scale-105 cursor-pointer"
                >
                  <div class="bg-yellow-500  flex h-20  items-center">
                    <h1 class="text-white ml-4 border-2 py-2 px-4 rounded-full">
                      <i class="fas fa-map-marked-alt"></i>
                    </h1>
                    <p class="ml-4 text-white uppercase">Evento presencial</p>
                  </div>
                  <p
                    class="py-6 px-6 text-dark-main dark:text-white text-lg tracking-wide text-center"
                  >
                    Vendas online e ferramentas para gestão de acesso/portaria
                    em espaço físico
                  </p>
                  <div class="flex justify-center px-5 mb-2 text-sm ">
                    <router-link
                      to="/create-event/1"
                      type="button"
                      class="border border-yellow-500 text-yellow-600 rounded-md px-4 py-2 m-2 transition duration-500 ease select-none hover:text-white hover:bg-yellow-500 focus:outline-none focus:shadow-outline"
                    >
                      Criar Agora
                    </router-link>
                  </div>
                </div>
              </div>

              <div class="">
                <div
                  class="bg-white dark:bg-dark-second max-w-xs mx-auto rounded-lg border-b-4 border-blue-500 overflow-hidden shadow-lg hover:shadow-2xl transition duration-500 transform hover:scale-105 cursor-pointer"
                >
                  <div class="h-20 bg-blue-500 flex items-center ">
                    <h1 class="text-white ml-4 border-2 py-2 px-4 rounded-full">
                      <i class="fas fa-globe"></i>
                    </h1>
                    <p class=" text-white text-base ml-4 uppercase">
                      Evento online
                    </p>
                  </div>
                  <p
                    class="py-6 px-6 text-dark-main dark:text-white text-lg tracking-wide text-center"
                  >
                    Video conferências, lives, desafios virtuais e transmissões
                    ao vivo via outros plataformas.
                  </p>
                  <div class="flex justify-center px-5 mb-2 text-sm ">
                    <router-link
                      to="/create-event/2"
                      type="button"
                      class="border border-blue-500 text-blue-500 rounded-md px-4 py-2 m-2 transition duration-500 ease select-none hover:text-white hover:bg-blue-500 focus:outline-none focus:shadow-outline"
                    >
                      Criar Agora
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="p-4 text-white h-96">
            <div class="flex justify-center h-screen">
              <div class="w-full  ">
                <div
                  class="text-white bg-white dark:bg-dark-main rounded-md shadow-lg h-auto w-full "
                >
                  <div class="w-full overflow-hidden rounded-lg shadow-lg">
                    <div class="w-full overflow-x-auto">
                      <table class="w-full">
                        <thead>
                          <tr
                            class="text-md font-semibold tracking-wide text-left text-gray-700 dark:text-white bg-gray-100 dark:bg-black uppercase border-b border-gray-300 dark:border-gray-600"
                          >
                            <th class="px-4 py-3">Img</th>
                            <th class="px-4 py-3 text-center">
                              Nome do evento
                            </th>
                            <th class="px-4 py-3 text-center">Local</th>
                            <th class="px-4 py-3 text-center">
                              Horário do evento
                            </th>
                            <th class="px-4 py-3 text-center">Ações</th>
                          </tr>
                        </thead>
                        <tbody
                          class=" bg-white dark:bg-dark-second text-gray-800 dark:text-white"
                        >
                          <tr v-for="item in events.events" :key="item.id">
                            <td class="px-4 py-3 ">
                              <div class="flex items-center text-sm">
                                <div
                                  class="relative w-8 h-8 mr-3 rounded-full md:block"
                                >
                                  <img
                                    class="object-cover w-full h-full rounded-full"
                                    :src="item.image"
                                    alt=""
                                    loading="lazy"
                                  />
                                </div>
                              </div>
                            </td>
                            <td class="px-4 py-3 text-sm text-center">
                              {{ item.name }}
                            </td>
                            <td class="px-4 py-3 text-sm text-center">
                              {{ item.local }}
                            </td>
                            <td class="px-4 py-3 text-sm text-center">
                              {{ item.final_date }}
                            </td>
                            <td class="py-4 px-3 ">
                              <div class="flex item-center justify-center">
                                <button
                                  v-on:click="alterEvent(item.public_id)"
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
                                </button>
                                <button
                                  v-on:click="DeleteTicket(item.public_id)"
                                  class="w-4 mr-2 transform hover:text-red-500 hover:scale-110"
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
                                </button>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import Event from "@/services/Events.js";
import { createToast } from "mosha-vue-toastify";
import router from "@/router/index";

export default {
  name: "EventList",
  data() {
    return {
      events: [],
    };
  },
  setup() {
    const toast = (type, msg) => {
      createToast(msg, { type: type, transition: "zoom" });
    };
    return { toast };
  },
  mounted() {
    Event.myEvent(localStorage.getItem("public_id")).then((response) => {
      this.events = response.data;
    });
  },
  methods: {
    DeleteTicket(public_id) {
      Event.deleteEvent(public_id)
        .then((response) => {
          this.toast("success", response.data["message"]);
          router.go();
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    },
    alterEvent: function(public_id) {
      this.$router.push({
        path: "/create-event/"+public_id,
      });
    },
  },
};
</script>
