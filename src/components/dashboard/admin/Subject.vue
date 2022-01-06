<template>
  <div class="Subject">
    <NavBar />

    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <main class="flex-1 pt-2">
          <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
            <div class="flex items-center justify-center md:justify-start">
              <span
                class="text-3xl font-semibold tracking-wider uppercase mb-2"
              >
                Assuntos
              </span>
            </div>
            <div class="flex justify-center ">
              <button
                type="button"
                v-on:click="openModalSubject"
                class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-600 hover:bg-yellow-500  "
              >
                Criar Assunto
              </button>
            </div>
            <div
              class="modal-assunto fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
              style="background: rgba(0,0,0,.7); display: none;"
            >
              <div
                class="shadow-lg modal-container mt-60 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
              >
                <div class="modal-content mt-10 sm:mt-0 py-4 text-left px-6">
                  <!--Title-->
                  <div class="flex justify-between pb-3">
                    <h3 class="text-2xl text-center">
                      Criar <strong>Categoria</strong>
                    </h3>
                    <div
                      v-on:click="modalClose"
                      class="modal-close cursor-pointer z-50 mt-2"
                    >
                      <i class="fas fa-times text-gray-800 dark:text-white"></i>
                    </div>
                  </div>
                  <form @submit.prevent="Subject(Subject_id)">
                    <div class="md:flex md:justify-between -mx-3 mt-5">
                      <div class="w-full px-3 mb-5">
                        <label
                          for=""
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Descrição
                        </label>
                        <div class="flex">
                          <input
                            name="NameEvent"
                            v-model="subject.description"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="text-center mt-6">
                      <button
                        class="
                          focus:outline-none
                          text-white
                          py-2.5
                          px-5
                          rounded-lg
                          bg-blue-600
                          hover:bg-blue-700
                          w-full
                        "
                        type="submit"
                        style="transition: all 0.15s ease 0s"
                      >
                        Salvar
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div v-if="subjects">
            <div class="flex justify-center h-screen">
              <div class="w-full 2xl:w-3/6 pt-5 lg:pt-5 ">
                <div
                  class="text-white bg-white dark:bg-dark-main rounded-md shadow-lg mt-5 h-auto w-full "
                >
                  <div
                    class="w-full mb-8 mt-6 overflow-hidden rounded-lg shadow-lg"
                  >
                    <div class="w-full overflow-x-auto">
                      <table class="w-full">
                        <thead>
                          <tr
                            class="text-md font-semibold tracking-wide text-left text-gray-700 dark:text-white bg-gray-100 dark:bg-black uppercase border-b border-gray-300 dark:border-gray-600"
                          >
                            <th class="px-4 py-3 text-center">Descrição</th>
                            <th class="px-4 py-3 text-center">Ações</th>
                          </tr>
                        </thead>
                        <tbody
                          class=" bg-white dark:bg-dark-second text-gray-800 dark:text-white"
                        >
                          <tr v-for="item in subjects.subject" :key="item.id">
                            <td class="px-4 py-3 text-sm text-center">
                              {{ item.description }}
                            </td>
                            <td class="py-4 px-3 ">
                              <div class="flex item-center justify-center">
                                <button
                                  v-on:click="
                                    openModalAlterSubject(
                                      item.public_id,
                                      item.description
                                    )
                                  "
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
                                  v-on:click="DeleteSubject(item.public_id)"
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
import NavBar from "@/components/NavBar.vue";
import Admin from "@/services/Admin.js";
import { createToast } from "mosha-vue-toastify";
import router from "@/router/index";

export default {
  name: "Subject",
  components: {
    NavBar,
  },
  data() {
    return {
      subject: {
        description: "",
      },
      subject_id: null,
      subjects: null,
    };
  },
  setup() {
    const toast = (type, msg) => {
      createToast(msg, { type: type, transition: "zoom" });
    };
    return { toast };
  },
  mounted() {
    if (localStorage.getItem("public_id")) {
      Admin.subjects()
        .then((response) => {
          this.subjects = [];
          this.subjects = response.data;
        })
        .catch((e) => {
          this.subjects = null;
          this.toast("danger", e.response.data["message"]);
        });
    }
  },
  methods: {
    Subject(public_id) {
      if (public_id) {
        Admin.alterSubjects(public_id, this.subject)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.go();
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        Admin.createSubject(this.subject)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.go();
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      }
    },
    DeleteSubject(public_id) {
      Admin.deleteSubjects(public_id)
        .then((response) => {
          this.toast("success", response.data["message"]);
          router.go();
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    },
    openModalSubject() {
      const modal = document.querySelector(".modal-assunto");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
      this.Subject_id = null;
    },
    
    openModalAlterSubject(subject_id, description) {
      const modal = document.querySelector(".modal-assunto");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
      this.Subject_id = subject_id;
      this.subject.description = description;
    },
    modalClose() {
      this.Subject_id = null;
      this.subject.description = "";
      const modal = document.querySelector(".modal-assunto");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
  },
};
</script>
