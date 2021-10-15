<template>
  <div class="w-full lg:w-2/3 xl:w-2/4 pt-32 lg:pt-16 px-2">
    <div class="Header mt-12">
      <svg
        class="Header__svg"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 1337.97 684.43"
      >
        <path
          class="Header__shape bigSquare"
          fill="#16d5d1"
          d="M546.519 349.271l86.383-56.098 56.097 86.383-86.383 56.098z"
        />
        <path
          class="Header__shape triangle"
          fill="none"
          stroke="#ff4676"
          stroke-width="8"
          d="M372.15 462.17L321 434.58l-4.88 56.16z"
        />
        <circle
          class="Header__shape bigCircle"
          fill="#ff4676"
          cx="1076.52"
          cy="262.17"
          r="59"
        />
        <path
          class="Header__shape littleSquare"
          fill="#ffe430"
          d="M285.523 262.61l12.372-53.59 53.59 12.372-12.372 53.59z"
        />
        <circle
          class="Header__shape hoop"
          fill="none"
          stroke="#ffe430"
          stroke-width="13"
          cx="905.52"
          cy="447.17"
          r="45"
        />
        <circle
          class="Header__shape littleCircle"
          fill="#0f1c70"
          cx="1036.52"
          cy="203.17"
          r="27"
        />
      </svg>

      <div class="relative w-full mb-16">
        <div class="absolute inset-y-0 left-0 text-gray-800 dark:text-gray-50">
          <h1 class="text-2xl font-bold">
            Crie e viva experiências únicas quando e onde quiser
          </h1>
          <p class="text-base text-gray-500 dark:text-gray-300">
            Aprenda, divirta-se ou empreenda com eventos presenciais, online e
            conteúdos gravados.
          </p>
          <div class="flex mt-3">
            <router-link
              to="/create-event"
              type="button"
              class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-blue-600 hover:bg-blue-700 "
              >Produzir um evento
            </router-link>
            <router-link
              to="/create-event"
              type="text"
              class="focus:outline-none text-blue-600 py-2.5 px-5 font-semibold "
              >Conferir eventos
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-between items-center px-4 h-4 group mt-24 mb-5">
      <span class="font-semibold text-gray-800 text-lg dark:text-gray-100">
        Recomendados para você
      </span>
    </div>

    <!-- CIRCLE -->
    <div
      class="text-gray-800 dark:text-gray-50 mt-4 h-32 w-32"
    >
      <div class="rounded-full h-32 w-32 flex items-center justify-center bg-gray-900">
        Circle
      </div>
      <div class="relative">
        <p class="text-center mt-1">Circle</p>
      </div>      
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16">
      <span class="font-semibold text-gray-800 text-lg dark:text-gray-100"
        >Vistos recentemente por você</span
      >
    </div>

    <!-- Card -->
    <div
      class="dark:text-gray-50 rounded-lg "
    >
      <div class="px-1 grid grid-cols-2 xl:grid-cols-2 2xl:grid-cols-4 gap-4">
        <!-- CARD -->
        <div class="py-4 px-1 w-56 md:w-52 lg:w-56 xl:w-60 2xl:w-72">
          <a href="/donee/donee-3">
            <div
              class="relative rounded-lg text-gray-800 hover:shadow-xl dark:hover:bg-dark-second "
            >
              <div
                class="right-0 mt-4 rounded-l-full absolute text-center font-bold text-xs text-white px-2 py-1 bg-yellow-500"
              >
                0 Visualização
              </div>
              <img
                src="https://source.unsplash.com/MNtag_eXMKw/1600x900"
                class="h-32 rounded-lg w-full object-cover"
              />
              <div class="p-2">
                <div class="font-title text-red-600 text-left">
                  18 OUT <span class="text-gray-400">></span> 20 OUT
                </div>

                <div
                  class="text-sm font-semibold my-2 text-gray-800 dark:text-gray-50 text-left"
                >
                  Kumpulan Narasi Tidak Lazim
                </div>
                <div
                  class="text-sm font-light my-2 text-gray-800 dark:text-gray-50 text-left"
                >
                  Fernandopolis - São Paulo - SP
                </div>
              </div>
            </div>
          </a>
        </div>
        
      </div>
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-800 text-lg dark:text-gray-100"
        >Em destaque</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-gray-50 mt-4 rounded-lg"
    >
      <div class="text-justify px-4 py-2">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates,
        autem earum cum ullam odio, molestias maxime aperiam in id aspernatur
        vel ratione odit molestiae minus ipsa obcaecati quia! Doloribus, illum.
      </div>
    </div>

    <div class="flex justify-between items-center px-4 h-4 group mt-16 mb-5">
      <span class="font-semibold text-gray-500 text-lg dark:text-dark-txt"
        >Cidades</span
      >
    </div>
    <div
      class="shadow bg-white dark:bg-dark-second dark:text-dark-txt mt-4 rounded-lg"
    ></div>
  </div>
</template>
<script>
// @ is an alias to /src

export default {
  name: "Navegation",
  components: {},
};
</script>
<style lang="scss" scoped>

.Header__shape {
  animation-duration: 4s;
  animation-timing-function: cubic-bezier(0.18, 1.17, 0.03, 1.46);
  animation-fill-mode: backwards;
  transform-origin: center;
  // this here is the good stuff
  transform-box: fill-box;
}
.Header {
  position: relative;
  min-height: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.Header__svg {
  position: absolute;
  width: 100%;
  top: 50%;
  transform: translateY(-50%);
  z-index: -1;
  will-change: transform;
}

.bigSquare {
  animation-name: bigSquare;
}
@keyframes bigSquare {
  from {
    transform: translateY(10%) rotate(-80deg) scale(0);
  }
  to {
    transform: translateY(0) rotate(0deg) scale(1);
  }
}
.littleSquare {
  animation-name: littleSquare;
}
@keyframes littleSquare {
  from {
    transform: translate(226%, 183%) rotate(140deg) scale(0);
  }
  to {
    transform: translate(0%, 0%) rotate(0deg) scale(1);
  }
}
.triangle {
  animation-name: triangle;
}
@keyframes triangle {
  from {
    transform: rotate(-140deg) scale(0);
  }
  to {
    transform: rotate(0deg) scale(1);
  }
}
.hoop {
  animation-name: hoop;
}
@keyframes hoop {
  from {
    transform: translate(-160%, -33%) scale(0);
  }
  to {
    transform: translate(0%, 0%) scale(1);
  }
}
.bigCircle {
  animation-name: bigCircle;
}
@keyframes bigCircle {
  from {
    transform: scale(0) translate(60%, 3%);
  }
  to {
    transform: scale(1) translate(0%, 0%);
  }
}
.littleCircle {
  animation-name: littleCircle;
}
@keyframes littleCircle {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

// some lovely sass fun to stagger the animation

@for $i from 1 to 12 {
  .Header__shape:nth-child(#{$i}) {
    animation-delay: $i * 0.16s;
  }
}
</style>
