<template >
  <div class="NavBar">
    <nav
      class="bg-white dark:bg-dark-second h-max md:h-14 w-full shadow flex flex-col md:flex-row md:justify-between fixed top-0 z-50 border-b dark:border-dark-third"
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
            <span class="mx-2 font-semibold dark:text-dark-txt">Tuat</span>
            <i class="fas fa-angle-down text-gray-700 dark:text-dark-txt"></i>
          </div>
          <!-- BUSCA -->
          <div
            class="relative bg-gray-100 dark:bg-dark-third px-2 py-2  h-10  sm:h-11 lg:h-10 w-10 sm:w-96 lg:w-96 xl:w-96 xl:pl-3 xl:pr-8 rounded-full flex items-center justify-center cursor-pointer m-1"
          >
            <i
              class="fas fa-search text-gray-500 text-xl xl:mr-2 dark:text-dark-txt"
            ></i>
            <input
              type="text"
              placeholder="Buscar"
              class="outline-none bg-transparent hidden sm:inline-block w-96"
            />
          </div>
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
        <li class="w-1/5 md:w-max text-center">
          <router-link
            to="/home"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded text-gray-600 hover:bg-gray-100 dark:hover:bg-dark-third dark:text-dark-txt relative "
            :class="$route.params.route==='home' ? 'border-b-4 text-blue-500 border-blue-500': ''"
          >
            <i class="fas fa-home "></i>
          </router-link>
        </li>
        <li class="w-1/5 md:w-max text-center">
          <router-link
            to="/my-events"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded text-gray-600 hover:bg-gray-100 dark:hover:bg-dark-third dark:text-dark-txt relative"
            :class="$route.params.route==='my-events' ? 'border-b-4 text-blue-500 border-blue-500' : ''" 
          >
            <i class="fas fa-list-ul"></i>
          </router-link>
        </li>
        <li class="w-1/5 md:w-max text-center">
          <router-link
            to="/dashboard"
            class="w-full mt-1 text-2xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded text-gray-600 hover:bg-gray-100 dark:hover:bg-dark-third dark:text-dark-txt relative"
            :class="$route.params.route==='dashboard' ? 'border-b-4 text-blue-500 border-blue-500' : ''" 
          >
            <i class="fas fa-columns"></i>
          </router-link>
        </li>
        <li
          class="absolute bottom-0 right-1 md:w-max text-center inline-block md:hidden"
        >
          <a
            href="#"
            class="w-full text-3xl py-2 px-3 xl:px-12 cursor-pointer text-center inline-block rounded text-gray-600 hover:bg-gray-100 dark:hover:bg-dark-third dark:text-dark-txt relative"
          >
            <i class="fas fa-bars"></i>
          </a>
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
            <span class="mx-2 font-semibold dark:text-dark-txt">Tuat</span>
            <i class="fas fa-angle-down text-gray-700 dark:text-dark-txt"></i>
          </button>
        </li>
        <li class="h-10 hidden md:flex">
          <button
            v-on:click="show = !show"
            type="button"
            class="inline-flex items-center justify-center p-1 rounded-full hover:bg-gray-200 dark:hover:bg-dark-third mx-1"
            id="menu-button"
            aria-expanded="true"
            aria-haspopup="true"
          >
            <img
              src="../assets/images/user.jpg"
              alt="Profile picture"
              class="rounded-full h-9 w-9"
            />
            <span class="mx-2 font-semibold dark:text-dark-txt">Tuat</span>
          </button>
          <transition :name="'fade'">
            <div
              class="bg-white dark:bg-dark-second dropdown-menu text-white mt-14 ml-3 rounded absolute z-10 shadow-lg w-40 max-w-xs border border-solid dark:border-dark-third"
              v-if="show"
            >
              <ul class="list-none overflow-hidden rounded">
                <router-link
                  to="/about"
                  class="flex py-2 px-4 transition duration-300 text-gray-700 dark:text-dark-txt"
                  >Sobre</router-link>
                  <a
                  href=""
                  class="flex py-2 px-4 transition duration-300 text-gray-700 dark:text-dark-txt"
                  :class="''"
                  >a</a>
                  <a
                  href=""
                  class="flex py-2 px-4 transition duration-300 text-gray-700 dark:text-dark-txt"
                  :class="''"
                  >a</a>
                  <a
                  href=""
                  class="flex py-2 px-4 transition duration-300 text-gray-700 dark:text-dark-txt"
                  :class="''"
                  >a</a>
                  <a
                  href=""
                  class="flex py-2 px-4 transition duration-300 text-gray-700 dark:text-dark-txt"
                  :class="''"
                  >a</a>
              </ul>
            </div>
          </transition>
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
          <div
            class="grid place-items-center bg-gray-200 dark:bg-dark-third dark:text-dark-txt rounded-full mx-1 p-3 cursor-pointer hover:bg-gray-300 relative"
          >
            <i class="fas fa-angle-down text-gray-600 dark:text-dark-txt"></i> 
          </div>
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
export default {
  name: "NavBar",
  props: {},
  data: function() {
    return {
      show: false,
      cars: ["BMW", "Mercedes", "Audi", "Volvo"],
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
  },
};
</script>
