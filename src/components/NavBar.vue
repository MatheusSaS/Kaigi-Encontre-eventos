<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
<template>
  <div class="NavBar">
    <nav
      class="bg-white dark:bg-dark-main h-max md:h-14 w-full  flex flex-col md:flex-row md:justify-between fixed top-0 z-50  dark:border-dark-third"
    >
      <!-- LEFT NAV -->
      <div class="flex items-center justify-between w-full md:w-max px-4 ">
        <a href="#" class="mr-2 hidden md:inline-block">
          <img
            src="../assets/images/logo3.png"
            alt="Kaigi logo"
            class="w-24 sm:w-28 lg:w-14  h-auto"
          />
        </a>
        <a href="#" class="mr-2 inline-block md:hidden">
          <img
            src="../assets/images/logo-c.png"
            alt=""
            class="w-40 mt-3 pb-3 h-auto"
          />
        </a>

        <div class="flex items-center justify-between ">
          <div
            v-on:click="openModal()"
            class="inline-flex items-center justify-center p-1 rounded-full hover:bg-gray-200 dark:hover:bg-dark-third mx-1 md:hidden"
          >
            <i class="fas fa-map-marker-alt text-blue-500"></i>
            <span class="mx-2 font-semibold dark:text-dark-txt">Fernandopolis</span>
            <i class="fas fa-angle-down text-gray-700 dark:text-dark-txt"></i>
          </div>
          <!-- BUSCA -->
          <button
            type="button"
            class="group leading-6 font-medium  items-center space-x-3 sm:space-x-4 text-gray-600 dark:text-gray-50 transition-colors duration-200 w-full py-2 ml-4 hidden md:flex"
          >
            <svg
              width="24"
              height="24"
              fill="none"
              class="text-gray-600 dark:text-gray-50 group-hover:text-gray-400 dark:group-hover:text-gray-300 transition-colors duration-200"
            >
              <path
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              ></path>
            </svg>
            <span>
              Pesquisa rápida
              <span class="hidden sm:inline">
                para qualquer coisa
              </span>
            </span>
            <span
              style="opacity: 1;"
              class="hidden sm:block text-gray-400 text-sm leading-5 py-0.5 px-1.5 border border-gray-300 rounded-md"
              ><span class="sr-only">Press </span
              ><kbd class="font-sans"
                ><abbr title="Control" class="no-underline">Ctrl </abbr></kbd
              ><span class="sr-only"> and </span><kbd class="font-sans">K</kbd
              ><span class="sr-only"> to search</span></span
            >
          </button>

          <!-- MD ITENS LEFT -->
          <div
            class="text-2xl grid place-items-center md:hidden bg-gray-200 dark:bg-dark-third rounded-full w-10 h-10 cursor-pointer hover:bg-gray-300 dark:text-dark-txt m-1"
          >
            <img
              src="../assets/images/user.jpg"
              alt="Profile picture"
              class="rounded-full h-9 w-9"
            />
          </div>
          <div
            v-on:click="darkmode()"
            class="text-2xl grid place-items-center md:hidden bg-gray-200 dark:bg-dark-third rounded-full w-10 h-10 cursor-pointer hover:bg-gray-300 dark:text-dark-txt m-1"
            id="dark-mode-toggle-mb"
          >
            <i class="fas fa-moon text-gray-700  dark:text-yellow-500 "></i>
          </div>
        </div>
      </div>
      <!-- END LEFT NAV -->

      <!-- MAIN NAV -->
      <ul class="flex w-full lg:w-max items-center justify-center mr-24">
        <li class="w-1/5 md:w-max text-center text-gray-800 dark:text-gray-50">
          <router-link
            to="/"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded hover:bg-gray-100 dark:hover:bg-dark-third  relative "
            :class="
              $route.name === 'Home'
                ? 'border-b-4 text-blue-500 border-blue-500'
                : ''
            "
          >
            <i class="fas fa-home "></i>
          </router-link>
        </li>
        <div v-if="user"></div>
        <li
          class="w-1/5 md:w-max text-center text-gray-800 dark:text-gray-50"
          v-if="user"
        >
          <router-link
            to="/my-events"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded hover:bg-gray-100 dark:hover:bg-dark-third  relative"
            :class="
              $route.name === 'my-events'
                ? 'border-b-4 text-blue-500 border-blue-500'
                : ''
            "
          >
            <i class="fas fa-list-ul"></i>
          </router-link>
        </li>
        <li
          class="w-1/5 md:w-max text-center text-gray-800 dark:text-gray-50"
          v-if="user"
        >
          <router-link
            to="/dashboard/home"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded  hover:bg-gray-100 dark:hover:bg-dark-third  relative"
            :class="
              $route.name === 'dashboard'
                ? 'border-b-4 text-blue-500 border-blue-500'
                : ''
            "
          >
            <i class="fas fa-columns"></i>
          </router-link>
        </li>
        <li
          class="absolute bottom-0 right-1 md:w-max text-center inline-block md:hidden"
        >
          <button
            v-on:click="openMobileMenu()"
            id="buttonmodal"
            class="w-full text-3xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded text-gray-600 hover:bg-gray-100 dark:hover:bg-dark-third dark:text-dark-txt relative"
          >
            <i class="fas fa-bars"></i>
          </button>

          <!-- Mobile Menu -->
          <div
            class="mobile-menu-modal fixed w-full h-100 inset-0 z-50 overflow-hidden flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third blur-3xl"
            style=" background: rgba( 255, 255, 255, 0.6 );
                    box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
                    backdrop-filter: blur( 20px );
                    -webkit-backdrop-filter: blur( 20px );
                    border: 1px solid rgba( 255, 255, 255, 0.18 ); display: none;"
          >
            <div
              class="shadow-lg modal-container bg-white dark:bg-dark-second w-11/12 md:max-w-2xl mx-auto rounded z-50 overflow-y-auto"
            >
              <div class="modal-content py-4 text-left px-6">
                <!--Title-->
                <div class="flex justify-between items-center pb-3">
                  <div
                    v-on:click="coloseMobileMenu()"
                    class="modal-close cursor-pointer z-50"
                  >
                    <i class="fas fa-times text-gray-800 dark:text-white"></i>
                  </div>
                </div>

                <div
                  class="relative bg-gray-100 dark:bg-dark-third px-2 py-2 h-10 w-auto pr-8 rounded-full flex items-center justify-center cursor-pointer m-1"
                >
                  <i
                    class="fas fa-search text-gray-500 text-xl mr-2 dark:text-dark-txt"
                  ></i>
                  <input
                    type="text"
                    placeholder="Buscar"
                    class="outline-none bg-transparent inline-block w-96"
                  />
                </div>
                <!--Body-->
                <div v-if="user">
                  <ul class="list-none overflow-hidden rounded ">
                    <button
                      v-on:click="show = !show"
                      type="button"
                      class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                      id="menu-button"
                      aria-expanded="true"
                      aria-haspopup="true"
                    >
                      <img
                        src="../assets/images/user.jpg"
                        alt="Profile picture"
                        class="rounded-full h-14 w-14"
                      />
                      <div class="flex items-center">
                        <h1
                          class="ml-2 font-semibold dark:text-dark-txt break-words "
                        >
                          {{ user["user"]["name"] }}
                        </h1>
                      </div>
                    </button>
                  </ul>
                  <ul class="list-none overflow-hidden rounded ">
                    <button
                      type="button"
                      v-on:click="logout"
                      class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:hover:text-red-500 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    >
                      <i class="fas fa-sign-in-alt mt-1 mr-2 fa-lg "></i>
                      <span>Logout</span>
                    </button>
                  </ul>
                </div>
                <div v-else>
                  <ul class="list-none overflow-hidden rounded ">
                    <router-link
                      to="/login"
                      class="flex py-2 px-5 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    >
                      <i class="fas fa-user-lock mt-1 mr-2 fa-lg"></i>
                      <span>Login</span>
                    </router-link>
                  </ul>
                  <ul class="list-none overflow-hidden rounded ">
                    <router-link
                      to="/register"
                      class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    >
                      <i class="fas fa-user-plus mt-1 mr-2 fa-lg"></i>
                      <span>Sign Up</span>
                    </router-link>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <!-- END MAIN NAV -->

      <!-- RIGHT NAV -->
      <ul class="hidden md:flex mx-4 items-center justify-center">
        <li class="h-10 flex">
          <button
            v-on:click="openModal()"
            class="inline-flex items-center justify-center p-1 rounded-full hover:bg-gray-200 dark:hover:bg-dark-third mx-1"
          >
            <i class="fas fa-map-marker-alt text-blue-500"></i>
            <span class="mx-2 font-semibold dark:text-dark-txt">Fernandopolis</span>
            <i class="fas fa-angle-down text-gray-700 dark:text-dark-txt"></i>
          </button>
        </li>
        <li>
          <div
            v-on:click="darkmode()"
            class="hidden md:grid place-items-center bg-gray-200 dark:bg-dark-third dark:text-dark-txt rounded-full mx-1 p-3 cursor-pointer hover:bg-gray-300 relative"
            id="dark-mode-toggle"
          >
            <i class="fas fa-moon text-gray-700  dark:text-yellow-500 "></i>
          </div>
        </li>
        <li>
          <button
            type="button"
            v-on:click="show = !show"
            class="grid place-items-center bg-gray-200 dark:bg-dark-third dark:text-dark-txt rounded-full mx-1 p-3 cursor-pointer hover:bg-gray-300 relative"
          >
            <i class="fas fa-angle-down text-gray-600 dark:text-dark-txt"></i>
          </button>
          <transition name="fade" mode="out-in">
            <div
              class="bg-white dark:bg-dark-second dropdown-menu text-white mt-2 -ml-64 w-72 rounded absolute  shadow-lg max-w-xs border border-solid dark:border-dark-third"
              v-if="show"
            >
              <div v-if="user">
                <ul class="list-none overflow-hidden rounded ">
                  <button
                    v-on:click="show = !show"
                    type="button"
                    class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    id="menu-button"
                    aria-expanded="true"
                    aria-haspopup="true"
                  >
                    <img
                      src="../assets/images/user.jpg"
                      alt="Profile picture"
                      class="rounded-full h-14 w-14"
                    />
                    <div class="flex items-center">
                      <h1
                        class="ml-2 font-semibold dark:text-dark-txt break-words "
                      >
                        {{ user["user"]["name"] }}
                      </h1>
                    </div>
                  </button>
                </ul>
                <ul class="list-none overflow-hidden rounded ">
                  <div v-if="admin">
                    <router-link
                      to="/dashboard/admin/category"
                      class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:hover:text-red-500 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    >
                      <i class="fas fa-closed-captioning mt-1 mr-2 fa-lg "></i>
                      <span>Categoria</span>
                    </router-link>
                    <router-link
                      to="/dashboard/admin/subject"
                      class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:hover:text-red-500 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                    >
                      <i class="fas fa-align-center mt-1 mr-2 fa-lg "></i>
                      <span>Assuntos</span>
                    </router-link>
                  </div>
                  <button
                    type="button"
                    v-on:click="logout"
                    class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:hover:text-red-500 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                  >
                    <i class="fas fa-sign-in-alt mt-1 mr-2 fa-lg "></i>
                    <span>Logout</span>
                  </button>
                </ul>
              </div>
              <div v-else>
                <ul class="list-none overflow-hidden rounded ">
                  <router-link
                    to="/login"
                    class="flex py-2 px-5 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                  >
                    <i class="fas fa-user-lock mt-1 mr-2 fa-lg"></i>
                    <span>Login</span>
                  </router-link>
                </ul>
                <ul class="list-none overflow-hidden rounded ">
                  <router-link
                    to="/register"
                    class="flex py-2 px-4 w-full transition duration-300 text-gray-700 dark:text-dark-txt hover:bg-gray-100 dark:hover:bg-dark-third"
                  >
                    <i class="fas fa-user-plus mt-1 mr-2 fa-lg"></i>
                    <span>Sign Up</span>
                  </router-link>
                </ul>
              </div>
            </div>
          </transition>
        </li>
      </ul>

      <div
        class="main-modal fixed w-full h-100 inset-0 z-50 overflow-hidden flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
        style="background: rgba(0,0,0,.7); display: none;"
      >
        <div
          class="shadow-lg modal-container bg-white dark:bg-dark-second w-11/12 md:max-w-2xl mx-auto rounded z-50 overflow-y-auto"
        >
          <div class="modal-content py-4 text-left px-6">
            <!--Title-->
            <div class="flex justify-between items-center pb-3">
              <p class="text-2xl font-bold text-gray-700 dark:text-white">
                Localização
              </p>
              <div
                v-on:click="modalClose()"
                class="modal-close cursor-pointer z-50"
              >
                <i class="fas fa-times text-gray-800 dark:text-white"></i>
              </div>
            </div>

            <div
              class="relative bg-gray-100 dark:bg-dark-third px-2 py-2 h-10 sm:h-11 lg:h-10 w-full xl:pl-3 xl:pr-8 rounded-full flex items-center justify-center cursor-pointer m-1"
            >
              <input
                type="text"
                placeholder="Onde?"
                class="outline-none bg-transparent inline-block w-full text-gray-900 dark:text-white"
              />
            </div>
            <!--Body-->
            <div class="my-5 text-gray-900 dark:text-white">
              <div
                class="flex-1 lg:flex-initial w-full rounded-t-lg bg-whitedark:bg-dark-second mt-4 sm:-mt-4 z-30 flex flex-col "
              >
                <div
                  class="w-full mt-5 text-lg font-bold border-0 border-t border-grey-light border-solid dark:text-white"
                >
                  <i class="fas fa-search-location text-blue-500 mt-5"></i>
                  <span class="text-gray-700 dark:text-white ml-2"
                    >Localização atual</span
                  >
                  <div
                    class="text-sm text-gray-600 dark:text-gray-300 font-light ml-6"
                  >
                    Encontre eventos perto de você
                  </div>
                  <table class="w-full mt-5">
                    <tbody class="justify-between overflow-y-scroll">
                      <tr
                        class="relative transform scale-100 border-b border-t border-grey-light border-solid cursor-default text-left text-lg flex flex-col p-3"
                      >
                        <td class="whitespace-no-wrap">
                          <i class="fas fa-map-marker-alt text-blue-500"></i>
                          <span class="dark:text-white ml-2 font-medium"
                            >Fernandopolis</span
                          >
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
      <!-- END RIGHT NAV -->
    </nav>
  </div>
</template>

<script>
import User from "@/services/User";
import router from "@/router/index";

import { createToast } from "mosha-vue-toastify";
import VueGeolocation from "vue-browser-geolocation";

export default {
  name: "NavBar",
  data: function() {
    return {
      show: false,
      admin: false,
      user: null,
      options: {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0,
      },
    };
  },
  methods: {
    darkmode() {
      document.querySelector("#dark-mode-toggle").onclick = () => {
        document.documentElement.classList.toggle("dark");
      };

      document.querySelector("#dark-mode-toggle-mb").onclick = () => {
        document.documentElement.classList.toggle("dark");
      };
    },
    openModal() {
      const modal = document.querySelector(".main-modal");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },
    modalClose() {
      const modal = document.querySelector(".main-modal");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
    openMobileMenu() {
      const modal = document.querySelector(".mobile-menu-modal");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },
    coloseMobileMenu() {
      const modal = document.querySelector(".mobile-menu-modal");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("public_id");
      localStorage.removeItem("admin");

      router.push({ name: "Login" });
    },
  },
  setup() {
    const toast = (type, msg) => {
      createToast(msg, { type: type, transition: "zoom" });
    };
    return { toast };
  },
  mounted() {
    
    VueGeolocation.getLocation(this.options).then((coordinates) => {
      console.log(coordinates);
    });
    if (localStorage.getItem("public_id")) {
      User.user(localStorage.getItem("public_id"))
        .then((response) => {
          this.user = response.data;
          console.log(this.user.user.admin);
          if(this.user.user.admin){
            this.admin = true;
          }
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    }
    
  },
};
</script>
