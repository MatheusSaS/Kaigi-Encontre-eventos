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
                  <p class="py-6 px-6 text-dark-main dark:text-white text-lg tracking-wide text-center">
                    Vendas online e ferramentas para gestão de acesso/portaria em espaço físico
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
                  <p class="py-6 px-6 text-dark-main dark:text-white text-lg tracking-wide text-center">
                      Video conferências, lives, desafios virtuais e transmissões ao vivo via outros plataformas.
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
          <div
            class="p-4 text-white bg-white dark:bg-dark-third rounded-md shadow-md mt-3 h-96"
          >
            <div class="flex items-stretch justify-ri"></div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EventList",
};
</script>
