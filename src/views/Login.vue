<template>
  <div class="Login">
    <NavBar />
    <div class="Header">
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
      <section class="absolute w-full mt-24">
        <div class="mx-auto px-4 h-full">
          <div class="flex content-center items-center justify-center h-full">
            <div class="w-full lg:w-5/12 px-4 pt-32 bg-white dark:bg-dark-main">
              <div
                class="relative flex flex-col min-w-0 break-words w-full mb-6"
              >
                <div class="rounded-t mb-0 px-6 py-6">
                
                  <hr class="mt-6 border-b-2 dark:border-white" />
                </div>
                <div class="flex-auto px-4 lg:px-5 py-6 pt-0">
                  <div
                    class="
                      text-gray-800
                      dark:text-gray-50
                      text-sm
                      font-normal
                      mb-3
                    "
                  >
                    <small>Ou faça login com credenciais</small>
                  </div>
                  <form @submit.prevent="Login">
                    <div class="relative w-full mb-3">
                      <div class="custom-input">
                        <label
                          for="email"
                          class="text-sm text-gray-700 dark:text-white"
                          >Email</label
                        >
                        <div class="flex">
                          <div
                            class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"
                          ></div>
                          <input
                            type="email"
                            placeholder="email@example.com"
                            name="femail"
                            id="femail"
                            v-model="email"
                            class="CustomInput"
                          />
                        </div>                                                                
                      </div>
                    </div>

                    <div class="relative w-full mb-3">
                      <div class="custom-input">
                        <label
                          for="password"
                          class="text-sm text-gray-700 dark:text-white"
                          >Senha</label
                        >
                        <div class="flex">
                          <div
                            class="w-10 z-10 pl-1 text-center pointer-events-none flex items-center justify-center"
                          ></div>
                          <input
                            type="password"
                            name="fpasswordl"
                            id="fpassword"
                            v-model="password"
                            class="CustomInput"
                          />
                        </div>                               
                      </div>
                    </div>

                    <div>
                      <label class="inline-flex items-center cursor-pointer">
                        <input
                          id="customCheckLogin"
                          type="checkbox"
                          class="form-checkbox text-gray-800 ml-1 w-5 h-5"
                          style="transition: all 0.15s ease 0s"
                        /><span
                          class="
                            ml-2
                            text-sm
                            font-semibold
                            text-gray-800
                            dark:text-gray-50
                          "
                          >Remember me</span
                        >
                      </label>
                    </div>
                    <div class="text-right">
                      <label
                        class="
                          inline-flex
                          items-center
                          cursor-pointer
                          text-right
                        "
                      >
                        <a class="ml-2 text-sm font-semibold text-blue-600"
                          >Esqueceu a senha?</a
                        >
                      </label>
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
                        Login
                      </button>
                    </div>
                  </form>
                </div>
                <div
                  class="
                    flex
                    w-1/2
                    text-center
                    ml-6
                    mb-1
                    text-gray-800
                    dark:text-gray-50
                  "
                >
                  <p>
                    Não possui uma conta?
                    <a href="" class="text-blue-600">Criar</a>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
<script>
import NavBar from "@/components/NavBar.vue";
import User from "@/services/User";
import Token from "@/services/Token";
import router from "@/router/index";

import { createToast } from "mosha-vue-toastify";

export default {
  components: {
    NavBar,
  },
  data() {
    return {      
        email: "",
        password: "",      
    }
  },
  setup() {
    const toast = (type,msg) => {
      createToast(msg,{type: type,transition: 'zoom',});
    };
    return { toast };
  },
  methods: {
    Login() {
      User.login(this.email,this.password)
        .then((response) => {
          localStorage.setItem('token',  response.data.token);
          localStorage.setItem('public_id',  response.data.public_id);
          localStorage.setItem("admin", response.data.admin);
    
          
          Token.setToken()
          
          router.push({ name: 'Home',})
          this.toast('success','Logado corretamente!');
        })
        .catch((e) => {
          this.toast('danger',e.response.data["message"]);
        });
    },
  },
};
</script>
<style lang="scss" scoped>
.Header__shape {
  animation-duration: 4s;
  animation-timing-function: cubic-bezier(0.18, 1.17, 0.03, 1.46);
  animation-fill-mode: backwards;
  transform-origin: center;
  transform-box: fill-box;
}


.Header {
  position: relative;
  min-height: 100vh;
}

.Header__svg {
  position: absolute;
  width: 100%;
  top: 50%;
  transform: translateY(-50%);
  z-index: -1;
  will-change: transform;
}
.Header__title {
  font-family: Avenir, Futura, "Open Sans", "Gill Sans", "Helvetica Neue", Ariel,
    sans-serif;
  font-weight: bold;
  font-size: 6vw;
  margin: 0;
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
