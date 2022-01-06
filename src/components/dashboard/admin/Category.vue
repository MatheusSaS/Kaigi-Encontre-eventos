<template>
  <div class="Category">
    <NavBar />

    <div class="flex justify-center h-screen mt-32 md:mt-14">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <main class="flex-1 pt-2">
          <div class="p-4 text-white bg-blue-500 rounded-md shadow-md">
            <div class="flex items-center justify-center md:justify-start">
              <span
                class="text-3xl font-semibold tracking-wider uppercase mb-2"
              >
                Categorias
              </span>
            </div>
            <div class="flex justify-center ">
              <button
                type="button"
                v-on:click="openModalCategory"
                class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-600 hover:bg-yellow-500  "
              >
                Criar Categoria
              </button>
            </div>
            <div
              class="modal-categoria fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
              style="background: rgba(0,0,0,.7); display: none;"
            >
              <div
                class="shadow-lg modal-container mt-60 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
              >
                <div class="modal-content mt-10 sm:mt-0 py-4 text-left px-6">
                  <!--Title-->
                  <div class="flex justify-between pb-3">
                    <h3 class="text-2xl text-center text-gray-800 dark:text-gray-50">
                      Criar <strong>Categoria</strong>
                    </h3>
                    <div
                      v-on:click="modalClose"
                      class="modal-close cursor-pointer z-50 mt-2"
                    >
                      <i class="fas fa-times text-gray-800 dark:text-white"></i>
                    </div>
                  </div>
                  <form @submit.prevent="Category(category_id)">
                    <div class="col-span-6 ml-2 sm:col-span-4 md:mr-3">
                      <label
                        class="block text-gray-700 text-sm font-bold mb-2 text-center"
                        for="photo"
                      >
                        Foto Categoria <span class="text-red-600"> </span>
                      </label>

                      <div class="text-center">
                        <!-- Current Profile Photo -->
                        <div class="mt-2 mb-16">
                          <vue-avatar
                            :width="200"
                            :height="200"
                            :rotation="rotation"
                            :scale="scale"
                            ref="vueavatar"
                            @vue-avatar-editor:image-ready="onImageReady"
                            class="w-40 h-40 m-auto rounded-full shadow"
                          >
                          </vue-avatar>
                        </div>
                      </div>
                    </div>
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
                            v-model="category.description"
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
          <div v-if="categories">
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
                            <th class="px-4 py-3">Img</th>
                            <th class="px-4 py-3 text-center">Descrição</th>
                            <th class="px-4 py-3 text-center">Ações</th>
                          </tr>
                        </thead>
                        <tbody
                          class=" bg-white dark:bg-dark-second text-gray-800 dark:text-white"
                        >
                          <tr v-for="item in categories.category" :key="item.id">
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
                              {{ item.description }}
                            </td>
                            <td class="py-4 px-3 ">
                              <div class="flex item-center justify-center">
                                <button
                                  v-on:click="
                                    openModalAlterCategory(
                                      item.public_id,
                                      item.description,
                                      item.image
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
                                  v-on:click="DeleteCategory(item.public_id)"
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
import { VueAvatar } from "vue-avatar-editor-improved";

export default {
  name: "Category",
  components: {
    NavBar,
    VueAvatar,
  },
  data() {
    return {
      category: {
        description: "",
        image:"",
      },
      category_id: null,
      categories: null,
      rotation: 0,
      scale: 1,
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
      Admin.category()
        .then((response) => {
          this.categories = [];
          this.categories = response.data;
        })
        .catch((e) => {
          this.categories = null;
          this.toast("danger", e.response.data["message"]);
        });
    }
  },
  methods: {
    saveClicked() {
      this.category.image = this.$refs.vueavatar.getImageScaled();
      this.category.image = this.category.image.toDataURL();     
    },
    onImageReady() {
      this.scale = 1;
      this.rotation = 0;
    },
    Category(public_id) {
      if (public_id) {
        this.saveClicked()
        Admin.alterCategory(public_id, this.category)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.go();
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        this.saveClicked()
        Admin.createCategory(this.category)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.go();
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      }
    },
    DeleteCategory(public_id) {
      Admin.deleteCategory(public_id)
        .then((response) => {
          this.toast("success", response.data["message"]);
          router.go();
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    },
    openModalCategory() {
      const modal = document.querySelector(".modal-categoria");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
      this.category_id = null;
    },

    openModalAlterCategory(category_id, description,img) {
      const modal = document.querySelector(".modal-categoria");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
      this.category_id = category_id;
      this.category.description = description;
      this.category.image = img;
    },
    modalClose() {
      this.category_id = null;
      this.categories.description = "";
      this.categories.image = "";
      const modal = document.querySelector(".modal-categoria");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
  },
};
</script>
