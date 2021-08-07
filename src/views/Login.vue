<template>
  <section class="absolute w-full top-0">


    <div class="container mx-auto px-4 h-full">
      <div class="flex content-center items-center justify-center h-full">
        <div class="w-full lg:w-4/12 px-4 pt-32">
          <div
            class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-gray-300 border-0"
          >
            <div class="rounded-t mb-0 px-6 py-6">
              <div class="text-center mb-3">
                <h6 class="text-gray-600 text-sm font-bold">Entrar Com</h6>
              </div>
              <div class="btn-wrapper text-center">
                <button
                  class="bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs"
                  type="button"
                  style="transition: all 0.15s ease 0s;"
                >
                  <img
                    alt="..."
                    class="w-5 mr-1"
                    src="../assets/images/github.png"
                  />Github
                </button>
                <button
                  class="bg-white active:bg-gray-100 text-gray-800 font-normal px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 uppercase shadow hover:shadow-md inline-flex items-center font-bold text-xs"
                  type="button"
                  style="transition: all 0.15s ease 0s;"
                >
                  <img
                    alt="..."
                    class="w-5 mr-1"
                    src="../assets/images/google.png"
                  />Google
                </button>
              </div>
              <hr class="mt-6 border-b-1 border-gray-400" />
            </div>
            <div class="flex-auto px-4 lg:px-5 py-6 pt-0">
              <div class="text-gray-500 text-center mb-3 font-bold">
                <small>Ou faça login com credenciais</small>
              </div>
              <form>
                <div class="relative w-full mb-3">
                  <label
                    class="block uppercase text-gray-700 text-xs font-bold mb-2"
                    for="grid-password"
                    >Email</label
                  >
                  <input
                    type="email"
                    class="px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded-md text-sm shadow focus:outline-none focus:shadow-outline w-full"
                    placeholder="Email"
                    style="transition: all 0.15s ease 0s;"
                  />
                </div>
                <div class="relative w-full mb-3">
                  <label
                    class="block uppercase text-gray-700 text-xs font-bold mb-2"
                    for="grid-password"
                    >Senha</label
                  >
                  <input
                    type="password"
                    class="px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded-md text-sm shadow focus:outline-none focus:shadow-outline w-full"
                    style="transition: all 0.15s ease 0s;"
                  />
                </div>
                <div>
                  <label class="inline-flex items-center cursor-pointer">
                    <input
                      id="customCheckLogin"
                      type="checkbox"
                      class="form-checkbox text-gray-800 ml-1 w-5 h-5"
                      style="transition: all 0.15s ease 0s;"
                    /><span class="ml-2 text-sm font-semibold text-gray-700"
                      >Remember me</span
                    >
                  </label>
                </div>
                <div class="text-right">
                  <label
                    class="inline-flex items-center cursor-pointer text-right"
                  >
                    <a class="ml-2 text-sm font-semibold text-gray-900"
                      >Esqueceu a senha?</a
                    >
                  </label>
                </div>
                <div class="text-center mt-6">
                  <button
                    class="bg-gray-900 text-white active:bg-gray-700 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full"
                    type="button"
                    style="transition: all 0.15s ease 0s;"
                  >
                    Login
                  </button>
                </div>
              </form>
            </div>
            <div class="flex w-1/2 text-center ml-6 mb-1">
                  <p>Não possui uma conta? <a href="" class="text-blue-600">Criar</a></p>
              </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
