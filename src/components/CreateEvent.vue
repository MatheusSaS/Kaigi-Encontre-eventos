<template>
  <div class="createevent">
    <NavBarAuth />
    <div class="flex justify-center h-screen ">
      <div class="flex flex-col flex-1 max-h-full  rounded-md">
        <!-- Main Content -->
        <main class="flex-1 ">
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
            <div class="w-full 2xl:w-9/12 pt-5 lg:pt-5 ">
              <form @submit.prevent="SaveEvent">
                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >1. Informações básicas
                  </span>
                  <div class="flex -mx-3 mt-5">
                    <div class="w-full px-3 mb-5">
                      <label
                        for="name"
                        class="text-sm text-gray-700 dark:text-white"
                      >
                        Nome do evento
                      </label>
                      <div class="flex">
                        <input
                          name="fname"
                          v-model="event.name"
                          type="text"
                          class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                        />
                      </div>
                      <div class="mt-5">
                        <div v-if="!image">
                          <h2>Selecione uma imagem</h2>
                          <input
                            class="focus:outline-none cursor-pointer text-white py-2.5 px-8 rounded-lg bg-yellow-500 hover:bg-yellow-400"
                            type="file"
                            @change="onFileChange"
                          />
                        </div>
                        <div v-else>
                          <img class="w-48 h-48 rounded-md" :src="image" />
                          <button
                            type="button"
                            class="focus:outline-none cursor-pointer text-white py-2.5 px-8 rounded-lg bg-yellow-500 hover:bg-yellow-400 mt-2"
                            @click="removeImage"
                          >
                            Remove image
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="flex -mx-3 ">
                    <div class="w-full px-3 mb-5">
                      <label
                        for="Assunto"
                        class="text-sm text-gray-700 dark:text-white"
                      >
                        Assunto
                      </label>
                      <div class="flex">
                        <div
                          class="text-center pointer-events-none flex items-center justify-center"
                        ></div>
                        <div class="flex-shrink w-full inline-block relative">
                          <select
                            name="Assunto"
                            v-model="event.subject"
                            class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
                          >
                            <option
                              v-for="value in assuntos.subject"
                              v-bind:key="value.id"
                              :value="value.public_id"
                            >
                              {{ value.description }}
                            </option>
                          </select>

                          <div
                            class="pointer-events-none absolute top-0 mt-1  right-0 flex items-center px-2 text-gray-600 dark:text-white"
                          >
                            <svg
                              class="fill-current h-4 w-4"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 20 20"
                            >
                              <path
                                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                              />
                            </svg>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="w-full px-3 mb-5">
                      <label
                        for="Categoria"
                        class="text-sm text-gray-700 dark:text-white"
                      >
                        Categoria
                      </label>
                      <div class="flex">
                        <div
                          class="text-center pointer-events-none flex items-center justify-center"
                        ></div>
                        <div class="flex-shrink w-full inline-block relative">
                          <select
                            v-model="event.category"
                            name="Categoria"
                            class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
                          >
                            <option
                              v-for="value in categorias.category"
                              v-bind:key="value.id"
                              :value="value.public_id"
                            >
                              {{ value.description }}
                            </option>
                          </select>
                          <div
                            class="pointer-events-none absolute top-0 mt-1  right-0 flex items-center px-2 text-gray-600 dark:text-white"
                          >
                            <svg
                              class="fill-current h-4 w-4"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 20 20"
                            >
                              <path
                                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                              />
                            </svg>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >2. Onde o seu evento vai acontecer
                  </span>
                  {{ event.id_type_event }}
                  <div
                    class="font-bold"
                    v-if="
                      $route.params.type != '1' && $route.params.type != '2'
                    "
                  >
                    <div class="font-bold" v-if="event.id_type_event === 1">
                      <div class="flex -mx-3 ">
                        <div class="w-full px-3 mb-5">
                          <label
                            for="Local"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Local
                          </label>
                          <div class="flex">
                            <input
                              name="Local"
                              v-model="event.local"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="flex -mx-3">
                        <div class="w-full px-3 mb-5">
                          <label
                            for="location_name"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Nome do Local
                          </label>
                          <div class="flex">
                            <input
                              name="location_name"
                              v-model="event.location_name"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                        <div class="w-full px-3 mb-5">
                          <label
                            for="location_name"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            CEP
                          </label>
                          <div class="flex">
                            <input
                              name="CEP"
                              v-model="event.cep"
                              @keyup="onKeyup"
                              @keydown="onKeydown($event)"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="flex -mx-3 m">
                        <div class="w-full px-3 mb-5">
                          <label
                            for="address"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Endereço
                          </label>
                          <div class="flex">
                            <input
                              name="address"
                              v-model="event.address"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                        <div class="w-full px-3 mb-5">
                          <label
                            for="road"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Av./Rua
                          </label>
                          <div class="flex">
                            <input
                              name="road"
                              v-model="event.road"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="flex -mx-3 ">
                        <div class="w-full px-3 mb-5">
                          <label
                            for="number"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Número
                          </label>
                          <div class="flex">
                            <input
                              name="number"
                              v-model="event.number"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                        <div class="w-full px-3 ">
                          <label
                            for="complement"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Complemento
                          </label>
                          <div class="flex">
                            <input
                              name="complement"
                              v-model="event.complement"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                      </div>
                      <div class="flex -mx-3 ">
                        <div class="w-full px-3">
                          <label
                            for="district"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Bairro
                          </label>
                          <div class="flex">
                            <input
                              name="district"
                              v-model="event.district"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                        <div class="w-full px-3 ">
                          <label
                            for="city"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Cidade
                          </label>
                          <div class="flex">
                            <input
                              name="city"
                              v-model="event.city"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                        <div class="w-full px-3">
                          <label
                            for="state"
                            class="text-sm text-gray-700 dark:text-white"
                          >
                            Estado
                          </label>
                          <div class="flex">
                            <input
                              name="state"
                              v-model="event.state"
                              type="text"
                              class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div
                      class="font-bold"
                      v-else-if="event.id_type_event === 2"
                    >
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
                  <div class="font-bold" v-if="$route.params.type === '1'">
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mb-5">
                        <label
                          for="Local"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Local
                        </label>
                        <div class="flex">
                          <input
                            name="Local"
                            v-model="event.local"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="flex -mx-3">
                      <div class="w-full px-3 mb-5">
                        <label
                          for="location_name"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Nome do Local
                        </label>
                        <div class="flex">
                          <input
                            name="location_name"
                            v-model="event.location_name"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                      <div class="w-full px-3 mb-5">
                        <label
                          for="location_name"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          CEP
                        </label>
                        <div class="flex">
                          <input
                            name="CEP"
                            v-model="event.cep"
                            @keyup="onKeyup"
                            @keydown="onKeydown($event)"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="flex -mx-3 m">
                      <div class="w-full px-3 mb-5">
                        <label
                          for="address"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Endereço
                        </label>
                        <div class="flex">
                          <input
                            name="address"
                            v-model="event.address"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                      <div class="w-full px-3 mb-5">
                        <label
                          for="road"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Av./Rua
                        </label>
                        <div class="flex">
                          <input
                            name="road"
                            v-model="event.road"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mb-5">
                        <label
                          for="number"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Número
                        </label>
                        <div class="flex">
                          <input
                            name="number"
                            v-model="event.number"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                      <div class="w-full px-3 ">
                        <label
                          for="complement"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Complemento
                        </label>
                        <div class="flex">
                          <input
                            name="complement"
                            v-model="event.complement"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3">
                        <label
                          for="district"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Bairro
                        </label>
                        <div class="flex">
                          <input
                            name="district"
                            v-model="event.district"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                      <div class="w-full px-3 ">
                        <label
                          for="city"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Cidade
                        </label>
                        <div class="flex">
                          <input
                            name="city"
                            v-model="event.city"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                      <div class="w-full px-3">
                        <label
                          for="state"
                          class="text-sm text-gray-700 dark:text-white"
                        >
                          Estado
                        </label>
                        <div class="flex">
                          <input
                            name="state"
                            v-model="event.state"
                            type="text"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="font-bold" v-else-if="$route.params.type === '2'">
                    <div class="flex -mx-3 ">
                      <div class="w-full px-3 mt-2">
                        <div class="flex-shrink w-full inline-block relative">
                          <select
                            name="Categoria"
                            class="block appearance-none text-gray-600 dark:text-white w-full bg-white dark:bg-dark-third border border-dark-txt dark:border-dark-second shadow-inner px-4 py-2 pr-8 rounded-lg"
                          >
                            <option>
                              Google Meet (Videoconferência)        
                            </option>
                            <option>
                              Microsoft Teams (Videoconferência)               
                            </option>
                            <option>
                              Zoom (Videoconferência)              
                            </option>
                            <option>
                              Youtube (Live)               
                            </option>
                            <option>
                              Facebook (Live)              
                            </option>
                            <option>
                              Instagram (Live)               
                            </option>
                          </select>
                          <div
                            class="pointer-events-none absolute top-0 mt-1  right-0 flex items-center px-2 text-gray-600 dark:text-white"
                          >
                            <svg
                              class="fill-current h-4 w-4"
                              xmlns="http://www.w3.org/2000/svg"
                              viewBox="0 0 20 20"
                            >
                              <path
                                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                              />
                            </svg>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >3. Quando vai acontecer
                  </span>
                  <div class="md:flex md:justify-between -mx-3 mt-5">
                    <div class="w-full px-3 mb-5">
                      <label
                        for=""
                        class="text-sm text-gray-700 dark:text-white"
                        >Data / Horário de Início das Vendas</label
                      >
                      <DatePicker
                        v-model="event.initial_date"
                        mode="dateTime"
                        is24hr
                        is-dark
                      >
                        <template v-slot="{ inputValue, inputEvents }">
                          <input
                            name="dateStartTicket"
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            :value="inputValue"
                            v-on="inputEvents"
                          />
                        </template>
                      </DatePicker>
                    </div>
                    <div class="w-full px-3 mb-5">
                      <label
                        for=""
                        class="text-sm text-gray-700 dark:text-white"
                        >Data / Horário de Término das Vendas</label
                      >
                      <DatePicker
                        v-model="event.final_date"
                        mode="dateTime"
                        is24hr
                        is-dark
                      >
                        <template v-slot="{ inputValue, inputEvents }">
                          <input
                            class="w-full pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600 dark:border-dark-second dark:focus:border-blue-600"
                            :value="inputValue"
                            v-on="inputEvents"
                            name="datainiciovendas"
                          />
                        </template>
                      </DatePicker>
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
                    <!-- Init ModalTicketPaid -->
                    <div class="ModalTicketPaid">
                      <div
                        class="modal-pago fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
                        style="background: rgba(0,0,0,.7); display: none;"
                      >
                        <div
                          class="shadow-lg modal-container mt-96 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
                        >
                          <div
                            class="modal-content mt-10 sm:mt-0 py-4 text-left px-6"
                            :class="{ 'mt-96': halfprice }"
                          >
                            <!--Title-->
                            <div class="flex justify-between pb-3">
                              <h3 class="text-2xl text-center">
                                Criar ingresso <strong>pago</strong>
                              </h3>
                              <div
                                v-on:click="modalPriceClose()"
                                class="modal-close cursor-pointer z-50 mt-2"
                              >
                                <i
                                  class="fas fa-times text-gray-800 dark:text-white"
                                ></i>
                              </div>
                            </div>
                            <form @submit.prevent="SaveTicket(ticket_id)">
                              <div
                                class="md:flex md:justify-between -mx-3 mt-5"
                              >
                                <input
                                  type="text"
                                  name="id_type_ticket"
                                  v-model="ticket.id_type_ticket"
                                  hidden
                                />
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                  >
                                    Nome Ingresso
                                  </label>
                                  <div class="flex">
                                    <input
                                      name="NameEvent"
                                      v-model="ticket.ticket_name"
                                      type="text"
                                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Quantidade</label
                                  >
                                  <div class="flex">
                                    <input
                                      name="Amount"
                                      v-model="ticket.amount"
                                      type="number"
                                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>
                                <div class="w-full sm:w-2/5 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Preço
                                  </label>
                                  <div class="flex">
                                    <div
                                      class="mt-1 relative rounded-md shadow-sm"
                                    >
                                      <div
                                        class="absolute inset-y-0 left-0 pl-1 flex items-center pointer-events-none"
                                      >
                                        <span class="text-gray-500 sm:text-sm">
                                          R$
                                        </span>
                                      </div>
                                      <input
                                        type="text"
                                        name="Price"
                                        v-model="ticket.price"
                                        class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                        placeholder="0.00"
                                      />
                                      <div
                                        class="absolute inset-y-0 right-0 flex items-center"
                                      >
                                        <label for="currency" class="sr-only"
                                          >Currency</label
                                        >
                                        <select
                                          id="currency"
                                          name="currency"
                                          class="focus:ring-indigo-500 focus:border-indigo-500 h-full py-0 pl-2 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md"
                                        >
                                          <option>BRL</option>
                                          <option>USD</option>
                                        </select>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                                <div class="w-15 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Total</label
                                  >
                                  <div class="flex mt-5">
                                    <p class="text-green-500">
                                      {{ ticket.amount * ticket.price }}
                                    </p>
                                  </div>
                                </div>
                              </div>

                              <div
                                class="md:flex md:justify-between -mx-3 ml-1"
                              >
                                <label class="inline-flex items-center mt-3">
                                  <input
                                    type="checkbox"
                                    value="True"
                                    v-model="ticket.half"
                                    class="form-checkbox h-5 w-5 text-gray-600"
                                    unchecked
                                  /><span
                                    class="ml-2 text-gray-700 dark:text-white"
                                    >Criar meia-entrada para este
                                    ingresso:</span
                                  >
                                </label>
                              </div>

                              <div v-if="ticket.half === true">
                                <div
                                  class="md:flex md:justify-between -mx-3 mt-5"
                                >
                                  <div class="w-full px-3 mb-5">
                                    <label
                                      for=""
                                      class="text-sm text-gray-700 dark:text-white"
                                    >
                                      Nome meio impresso
                                    </label>
                                    <div class="flex">
                                      <input
                                        name="NameEventHelf"
                                        type="text"
                                        v-model="ticket.half_description"
                                        class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                      />
                                    </div>
                                  </div>
                                  <div class="w-full px-3 mb-5">
                                    <label
                                      for=""
                                      class="text-sm text-gray-700 dark:text-white "
                                      >Quantidade</label
                                    >
                                    <div class="flex">
                                      <input
                                        @keypress="validateNumber"
                                        v-model="ticket.half_amount"
                                        name="AmountHelf"
                                        type="text"
                                        class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                      />
                                    </div>
                                  </div>
                                  <div class="w-full sm:w-2/5 px-3 mb-5">
                                    <label
                                      for=""
                                      class="text-sm text-gray-700 dark:text-white"
                                      >Preço
                                    </label>
                                    <div class="flex">
                                      <div
                                        class="mt-1 relative rounded-md shadow-sm"
                                      >
                                        <div
                                          class="absolute inset-y-0 left-0 pl-1 flex items-center pointer-events-none"
                                        >
                                          <span
                                            class="text-gray-500 sm:text-sm"
                                          >
                                            R$
                                          </span>
                                        </div>
                                        <input
                                          type="text"
                                          v-model="ticket.half_price"
                                          name="PriceHelf"
                                          class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                          placeholder="0.00"
                                        />
                                        <div
                                          class="absolute inset-y-0 right-0 flex items-center"
                                        >
                                          <label for="currency" class="sr-only"
                                            >Currency</label
                                          >
                                          <select
                                            id="currency"
                                            name="currency"
                                            class="focus:ring-indigo-500 focus:border-indigo-500 h-full py-0 pl-2 border-transparent bg-transparent text-gray-500 sm:text-sm rounded-md"
                                          >
                                            <option>BRL</option>
                                            <option>USD</option>
                                          </select>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="w-15 px-3 mb-5">
                                    <label
                                      for=""
                                      class="text-sm text-gray-700 dark:text-white"
                                      >Total</label
                                    >
                                    <div class="flex mt-5">
                                      <p class="text-green-500">R$:10</p>
                                    </div>
                                  </div>
                                </div>
                              </div>

                              <div
                                class="md:flex md:justify-between -mx-3 mt-5"
                              >
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Data / Horário de Início das Vendas</label
                                  >
                                  <DatePicker
                                    v-model="ticket.initial_date_time"
                                    mode="dateTime"
                                    is24hr
                                    is-dark
                                  >
                                    <template
                                      v-slot="{ inputValue, inputEvents }"
                                    >
                                      <input
                                        name="dateStartTicket"
                                        class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                        :value="inputValue"
                                        v-on="inputEvents"
                                      />
                                    </template>
                                  </DatePicker>
                                </div>

                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Data / Horário de Término das Vendas</label
                                  >
                                  <DatePicker
                                    v-model="ticket.final_date_time"
                                    mode="dateTime"
                                    is24hr
                                    is-dark
                                  >
                                    <template
                                      v-slot="{ inputValue, inputEvents }"
                                    >
                                      <input
                                        class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                        :value="inputValue"
                                        v-on="inputEvents"
                                        name="datainiciovendas"
                                      />
                                    </template>
                                  </DatePicker>
                                </div>
                              </div>
                              <div class="md:flex mt-1">
                                <div class="flex justify-between pb-3">
                                  <h6 class="text-2xl text-center">
                                    Quantidade por compra:
                                  </h6>
                                </div>
                              </div>

                              <div class="md:flex -mx-3 mt-5">
                                <div class="w-48 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Mínima</label
                                  >
                                  <div class="flex">
                                    <input
                                      type="text"
                                      v-model="ticket.amount_min"
                                      name="Amountminimum"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>

                                <div class="w-48 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Maxima</label
                                  >
                                  <div class="flex">
                                    <input
                                      type="text"
                                      v-model="ticket.amount_max"
                                      name="Amountmax"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>

                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Descrição do Ingresso</label
                                  >
                                  <div class="flex">
                                    <textarea
                                      v-model="ticket.description"
                                      name="Description"
                                      rows="2"
                                      maxlength="110"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    ></textarea>
                                  </div>
                                </div>
                              </div>

                              <div class="flex mt-3">
                                <button
                                  type="submit"
                                  class="focus:outline-none cursor-pointer text-white p-2.5 rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3 text-center"
                                >
                                  <p v-if="ticket_id">Salvar</p>
                                  <p v-else>Criar evento</p>
                                </button>

                                <div
                                  type="button"
                                  v-on:click="modalPriceClose()"
                                  class="focus:outline-none cursor-pointer text-white py-2.5 rounded-lg text-red-700 ml-8 text-center "
                                >
                                  Cancelar
                                </div>
                              </div>
                            </form>
                          </div>
                        </div>
                      </div>
                    </div>
                    <!-- Final ModalTicketPaid -->
                    <div
                      v-on:click="openModalFree()"
                      type="button"
                      class="focus:outline-none cursor-pointer text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                    >
                      Gratuito
                    </div>
                    <!-- Init ModelFree -->
                    <div class="ModalTicketFree">
                      <div
                        class="modal-gratis fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
                        style="background: rgba(0,0,0,.7); display: none;"
                      >
                        <div
                          class="shadow-lg modal-container mt-60 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
                        >
                          <div
                            class="modal-content mt-10 sm:mt-0 py-4 text-left px-6"
                          >
                            <!--Title-->
                            <div class="flex justify-between pb-3">
                              <h3 class="text-2xl text-center">
                                Criar ingresso <strong>grátis</strong>
                              </h3>
                              <div
                                v-on:click="modalFreeClose()"
                                class="modal-close cursor-pointer z-50 mt-2"
                              >
                                <i
                                  class="fas fa-times text-gray-800 dark:text-white"
                                ></i>
                              </div>
                            </div>
                            <form @submit.prevent="SaveTicket(ticket_id)">
                              <div
                                class="md:flex md:justify-between -mx-3 mt-5"
                              >
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                  >
                                    Nome Ingresso
                                  </label>
                                  <div class="flex">
                                    <input
                                      name="name"
                                      v-model="ticket.ticket_name"
                                      type="text"
                                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Quantidade</label
                                  >
                                  <div class="flex">
                                    <input
                                      v-model="ticket.amount"
                                      name="Amount"
                                      type="text"
                                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>
                                <div class="w-full sm:w-2/5 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Preço
                                  </label>
                                  <div class="flex">
                                    <div class="flex">
                                      <input
                                        name="Price"
                                        value="Grátis"
                                        type="text"
                                        class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-dark-second dark:text-gray-300 dark:bg-dark-second border focus:border-blue-600  dark:focus:border-blue-600 cursor-not-allowed"
                                        disabled
                                      />
                                    </div>
                                  </div>
                                </div>
                              </div>

                              <div
                                class="md:flex md:justify-between -mx-3 mt-5"
                              >
                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Data / Horário de Início das Vendas</label
                                  >
                                  <DatePicker
                                    v-model="ticket.initial_date_time"
                                    mode="dateTime"
                                    is24hr
                                    is-dark
                                  >
                                    <template
                                      v-slot="{ inputValue, inputEvents }"
                                    >
                                      <input
                                        name="dateStartTicket"
                                        class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                        :value="inputValue"
                                        v-on="inputEvents"
                                      />
                                    </template>
                                  </DatePicker>
                                </div>

                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Data / Horário de Término das Vendas</label
                                  >
                                  <DatePicker
                                    v-model="ticket.final_date_time"
                                    mode="dateTime"
                                    is24hr
                                    is-dark
                                  >
                                    <template
                                      v-slot="{ inputValue, inputEvents }"
                                    >
                                      <input
                                        class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                        :value="inputValue"
                                        v-on="inputEvents"
                                        name="datainiciovendas"
                                      />
                                    </template>
                                  </DatePicker>
                                </div>
                              </div>
                              <div class="md:flex mt-1">
                                <div class="flex justify-between pb-3">
                                  <h6 class="text-2xl text-center">
                                    Quantidade por compra:
                                  </h6>
                                </div>
                              </div>

                              <div class="md:flex -mx-3 mt-5">
                                <div class="w-48 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Mínima</label
                                  >
                                  <div class="flex">
                                    <input
                                      type="text"
                                      v-model="ticket.amount_min"
                                      name="Amountminimum"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>

                                <div class="w-48 px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Maxima</label
                                  >
                                  <div class="flex">
                                    <input
                                      v-model="ticket.amount_max"
                                      type="text"
                                      name="Amountmax"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    />
                                  </div>
                                </div>

                                <div class="w-full px-3 mb-5">
                                  <label
                                    for=""
                                    class="text-sm text-gray-700 dark:text-white"
                                    >Descrição do Ingresso</label
                                  >
                                  <div class="flex">
                                    <textarea
                                      v-model="ticket.description"
                                      name="Description"
                                      rows="2"
                                      maxlength="110"
                                      class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                    ></textarea>
                                  </div>
                                </div>
                              </div>

                              <div class="flex mt-3">
                                <button
                                  type="submit"
                                  class="focus:outline-none cursor-pointer text-white p-2.5 rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3 text-center"
                                >
                                  <p v-if="ticket_id">Salvar</p>
                                  <p v-else>Criar evento</p>
                                </button>

                                <div
                                  type="button"
                                  v-on:click="modalFreeClose()"
                                  class="focus:outline-none cursor-pointer text-white py-2.5 rounded-lg text-red-700 ml-8 text-center "
                                >
                                  Cancelar
                                </div>
                              </div>
                            </form>
                          </div>
                        </div>
                      </div>
                    </div>
                    <!-- End ModelFree -->
                    <div
                      v-on:click="openModalDonation()"
                      type="button"
                      class="focus:outline-none cursor-pointer text-white py-2.5 px-5  rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3"
                    >
                      Doação
                    </div>
                  </div>
                  <div class="ModalTicketDonation">
                    <div
                      class="modal-doacao fixed w-full h-100 inset-0 z-50 overflow-auto flex justify-center items-center animated fadeIn faster dark:bg-dark-third border border-dark-third "
                      style="background: rgba(0,0,0,.7); display: none;"
                    >
                      <div
                        class="shadow-lg modal-container mt-60 sm:mt-0 bg-white dark:bg-dark-second w-11/12 md:max-w-6xl mx-auto rounded z-50 overflow-y-auto"
                      >
                        <div
                          class="modal-content mt-10 sm:mt-0 py-4 text-left px-6"
                        >
                          <!--Title-->
                          <div class="flex justify-between pb-3">
                            <h3 class="text-2xl text-center">
                              Criar ingresso <strong>doação</strong>
                            </h3>
                            <div
                              v-on:click="modalDonationClose()"
                              class="modal-close cursor-pointer z-50 mt-2"
                            >
                              <i
                                class="fas fa-times text-gray-800 dark:text-white"
                              ></i>
                            </div>
                          </div>
                          <form @submit.prevent="SaveTicket(ticket_id)">
                            <div class="md:flex md:justify-between -mx-3 mt-5">
                              <div class="w-full px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                >
                                  Nome Ingresso
                                </label>
                                <div class="flex">
                                  <input
                                    name="name"
                                    v-model="ticket.ticket_name"
                                    type="text"
                                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                  />
                                </div>
                              </div>
                              <div class="w-full px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Quantidade</label
                                >
                                <div class="flex">
                                  <input
                                    @keypress="validateNumber"
                                    v-model="ticket.amount"
                                    name="Amount"
                                    type="text"
                                    class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                  />
                                </div>
                              </div>
                              <div class="w-full sm:w-2/5 px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >doação
                                </label>
                                <div class="flex">
                                  <div class="flex">
                                    <input
                                      name="Price"
                                      type="text"
                                      class="w-full  pl-1 pr-3 py-2 mt-1 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"                                     
                                    />
                                  </div>
                                </div>
                              </div>
                            </div>

                            <div class="md:flex md:justify-between -mx-3 mt-5">
                              <div class="w-full px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Data / Horário de Início das Vendas</label
                                >
                                <DatePicker
                                  v-model="ticket.initial_date_time"
                                  mode="dateTime"
                                  is24hr
                                  is-dark
                                >
                                  <template
                                    v-slot="{ inputValue, inputEvents }"
                                  >
                                    <input
                                      name="dateStartTicket"
                                      class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                      :value="inputValue"
                                      v-on="inputEvents"
                                    />
                                  </template>
                                </DatePicker>
                              </div>

                              <div class="w-full px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Data / Horário de Término das Vendas</label
                                >
                                <DatePicker
                                  v-model="ticket.final_date_time"
                                  mode="dateTime"
                                  is24hr
                                  is-dark
                                >
                                  <template
                                    v-slot="{ inputValue, inputEvents }"
                                  >
                                    <input
                                      class="w-full pl-1 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                      :value="inputValue"
                                      v-on="inputEvents"
                                      name="datainiciovendas"
                                    />
                                  </template>
                                </DatePicker>
                              </div>
                            </div>
                            <div class="md:flex mt-1">
                              <div class="flex justify-between pb-3">
                                <h6 class="text-2xl text-center">
                                  Quantidade por compra:
                                </h6>
                              </div>
                            </div>

                            <div class="md:flex -mx-3 mt-5">
                              <div class="w-48 px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Mínima</label
                                >
                                <div class="flex">
                                  <input
                                    type="text"
                                    v-model="ticket.amount_min"
                                    name="Amountminimum"
                                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                  />
                                </div>
                              </div>

                              <div class="w-48 px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Maxima</label
                                >
                                <div class="flex">
                                  <input
                                    type="text"
                                    v-model="ticket.amount_max"
                                    name="Amountmax"
                                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                  />
                                </div>
                              </div>

                              <div class="w-full px-3 mb-5">
                                <label
                                  for=""
                                  class="text-sm text-gray-700 dark:text-white"
                                  >Descrição do Ingresso</label
                                >
                                <div class="flex">
                                  <textarea
                                    name="Description"
                                    v-model="ticket.description"
                                    rows="2"
                                    maxlength="110"
                                    x-model="maximum"
                                    x-ref="maximum"
                                    class="w-full pl-7 pr-12 py-2 rounded-lg  outline-none text-black dark:text-white dark:bg-dark-third border focus:border-blue-600  dark:focus:border-blue-600"
                                  ></textarea>
                                </div>
                              </div>
                            </div>

                            <div class="flex mt-3">
                              <button
                                type="submit"
                                class="focus:outline-none cursor-pointer text-white p-2.5 rounded-lg bg-yellow-500 hover:bg-yellow-400 ml-3 text-center"
                              >
                                <p v-if="ticket_id">Salvar</p>
                                <p v-else>Criar evento</p>
                              </button>

                              <div
                                type="button"
                                v-on:click="modalDonationClose()"
                                class="focus:outline-none cursor-pointer text-white py-2.5 rounded-lg text-red-700 ml-8 text-center "
                              >
                                Cancelar
                              </div>
                            </div>
                          </form>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div
                    v-if="tickets_data"
                    class="w-full mb-8 mt-6 overflow-hidden rounded-lg shadow-lg"
                  >
                    <div class="w-full overflow-x-auto">
                      <table class="w-full">
                        <thead>
                          <tr
                            class="font-semibold tracking-wide text-left text-gray-700 dark:text-white bg-gray-100 dark:bg-dark-main border-b border-gray-300 dark:border-gray-600"
                          >
                            <th class="px-4 py-3"></th>
                            <th class="px-4 py-3 text-center">Nome</th>
                            <th class="px-4 py-3 text-center">Quantidade</th>
                            <th class="px-4 py-3 text-center">Preço</th>
                            <th class="px-4 py-3 text-center">Total</th>
                            <th class="px-4 py-3 text-center">Ações</th>
                          </tr>
                        </thead>
                        <tbody class="bg-white dark:bg-dark-second">
                          <tr
                            class="text-gray-800 dark:text-white"
                            v-for="item in tickets_data.tickets"
                            :key="item.id"
                            checked
                          >
                            <td class="px-4 py-3">
                              <label class="inline-flex items-center mt-3">
                                <input
                                  v-model="event.ticket_id"
                                  :value="item.public_id"
                                  type="checkbox"
                                  class="form-checkbox h-5 w-5 "
                                />
                              </label>
                            </td>
                            <td
                              class="px-4 py-3 text-ms font-semibold text-center"
                            >
                              {{ item.ticket_name }}
                            </td>
                            <td
                              class="px-4 py-3 text-ms font-semibold text-center"
                            >
                              {{ item.amount }}
                            </td>
                            <td
                              class="px-4 py-3 text-ms font-semibold text-center"
                            >
                              <div v-if="item.id_type_ticket === 1">
                                R$ {{ item.price }}
                              </div>
                              <div v-else-if="item.id_type_ticket === 2">
                                Grátis
                              </div>
                              <div v-else>
                                Doação
                              </div>
                            </td>
                            <td
                              class="px-4 py-3 text-ms font-semibold text-center"
                            >
                              R$ {{ item.total }}
                            </td>
                            <td class="py-4 px-3 ">
                              <div class="flex item-center justify-center">
                                <div v-if="item.id_type_ticket === 1">
                                  <button
                                    v-on:click="openModalPaid(item.public_id)"
                                    type="button"
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
                                </div>
                                <div v-else-if="item.id_type_ticket === 2">
                                  <button
                                    v-on:click="openModalFree(item.public_id)"
                                    type="button"
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
                                </div>
                                <div v-else>
                                  <button
                                    v-on:click="
                                      openModalDonation(item.public_id)
                                    "
                                    type="button"
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
                                </div>

                                <button
                                  v-on:click="DeleteTicket(item.public_id)"
                                  type="button"
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

                <div class="cardEvent">
                  <span
                    class="text-1xl font-semibold tracking-wider uppercase text-gray-700 dark:text-white"
                    >5. Descrição do evento
                  </span>
                  <div class="p-1 -mx-3 mt-5 ">
                    <editor
                      api-key="no-api-key"
                      v-model="event.description"
                      :class="'w-full h-72'"
                    />
                  </div>
                </div>
                <div class="flex mt-3 mb-3" data-v-6bcb2f40="">
                  <button
                    class="focus:outline-none text-white py-2.5 px-5  rounded-lg bg-yellow-600 hover:bg-blue-700"
                    type="submit"
                  >
                    Salvar
                  </button>
                  <a
                    href="/"
                    class="focus:outline-none text-red-600 py-2.5 px-5 font-semibold"
                    type="text"
                  >
                    Cancelar
                  </a>
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
import NavBarAuth from "@/components/NavBarAuth.vue";
import CustomSelect from "@/components/custom/custom-select.vue";

import { DatePicker } from "v-calendar";
import { createToast } from "mosha-vue-toastify";

import Admin from "@/services/Admin";
import Ticket from "@/services/Events.js";
import Event from "@/services/Events.js";
import router from "@/router/index";

import Editor from "@tinymce/tinymce-vue";

export default {
  name: "CreateEvent",
  components: {
    NavBarAuth,
    editor: Editor,
    CustomSelect,
    DatePicker,
  },
  setup() {
    const toast = (type, msg) => {
      createToast(msg, { type: type, transition: "zoom" });
    };
    return { toast };
  },
  data() {
    return {
      dateStartTicket: new Date(),
      dateEndTicket: new Date(),
      checkedTicket: [],
      assuntos: [],
      categorias: [],
      public_id: "",
      event: {
        name: "",
        image: "",
        id_type_event: "",
        user_id: "",
        subject: "",
        category: "",
        initial_date: new Date(),
        final_date: new Date(),
        ticket_id: [],
        description: "",
        platform: "",

        local: "",
        address: "",
        location_name: "",
        cep: "",
        road: "",
        number: "",
        complement: "",
        district: "",
        city: "",
        state: "",
      },
      tickets_modal: {
        id_type_ticket: "",
        user_id: "",
        ticket_name: "",
        amount: "",
        price: "",
        initial_date_time: "",
        final_date_time: "",
        amount_min: "",
        amount_max: "",
        description: "",
        total: "",

        half: false,
        half_description: "",
        half_amount: 0,
        half_price: 0,
        half_total: 0,
      },
      tickets_data: null,
      ticket: {
        id_type_ticket: "",
        user_id: "",
        ticket_name: "",
        amount: "",
        price: "",
        initial_date_time: "",
        final_date_time: "",
        amount_min: "",
        amount_max: "",
        description: "",
        total: "",

        half: false,
        half_description: "",
        half_amount: 0,
        half_price: 0,
        half_total: 0,
      },
    };
  },
  mounted() {
    if (this.$route.params.type != "1" && this.$route.params.type != "2") {
      Event.GetEvent(this.$route.params.type)
        .then((response) => {
          this.event = response.data.event;
          this.public_id = this.$route.params.type;
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    }
    if (localStorage.getItem("token")) {
      Admin.subjects().then((response) => {
        this.assuntos = response.data;
      });

      Admin.category().then((response) => {
        this.categorias = response.data;
      });
    }
    window.setInterval(() => {
      if (localStorage.getItem("token")) {
        Ticket.ticket().then((response) => {
          this.tickets_data = [];
          this.tickets_data = response.data;
        });
      }
    }, 5000);
  },
  methods: {
    onKeydown: function(e) {
      if (
        // permite somente numeros
        (e.keyCode >= 48 && e.keyCode <= 57) ||
        (e.keyCode >= 96 && e.keyCode <= 105) ||
        // permite teclas lado direito, esquerdo, delete, backspace, tab e enter
        /^(8|9|13|46|37|39|17)$/.test(e.keyCode) ||
        // permite ctrl+ c,v,x,a,z
        (/^(67|86|88|65|90)$/.test(e.keyCode) && e.ctrlKey)
      )
        return;
      e.preventDefault();
      e.stopPropagation();
    },
    onKeyup: function() {
      this.event.address = "";
      this.event.road = "";
      this.event.district = "";
      this.event.city = "";
      this.event.state = "";
      console.log(this.event.cep);
      if (!/^[0-9]{8}$/.test(this.event.cep)) return;
      Event.GetViacep(this.event.cep)
        .then((obj) => {
          console.log(obj.data.result.logradouro);
          this.event.address =
            obj.data.result.logradouro + ", " + obj.data.result.bairro;
          this.event.road = obj.data.result.logradouro;
          this.event.district = obj.data.result.bairro;
          this.event.city = obj.data.result.localidade;
          this.event.state = obj.data.result.uf;
          this.$els.event.numero.focus();
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    },

    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var reader = new FileReader();
      var vm = this;

      reader.onload = (e) => {
        vm.image = e.target.result;
        this.event.image = vm.image;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function() {
      this.image = "";
    },
    DeleteTicket(public_id) {
      Ticket.deleteTicket(public_id)
        .then((response) => {
          this.toast("success", response.data["message"]);
        })
        .catch((e) => {
          this.toast("danger", e.response.data["message"]);
        });
    },
    handleImages(files) {
      console.log(files);
    },
    SaveTicket(public_id) {
      if (localStorage.getItem("public_id")) {
        if (public_id) {
          Ticket.alterTicket(public_id, this.ticket)
            .then((response) => {
              this.toast("success", response.data["message"]);
              this.modalPriceClose();
              this.modalFreeClose();
            })
            .catch((e) => {
              this.toast("danger", e.response.data["message"]);
            });
        } else {
          if (this.ticket.id_type_ticket == 1) {
            this.ticket.total = this.ticket.amount * this.ticket.price;
          } else if (
            this.ticket.id_type_ticket == 2 ||
            this.ticket.id_type_ticket == 3
          ) {
            this.ticket.price = 0;
            this.ticket.total = 0;
          }

          this.ticket.user_id = localStorage.getItem("public_id");
          Ticket.createTicket(this.ticket)
            .then((response) => {
              this.toast("success", response.data["message"]);

              this.modalPriceClose();
              this.modalFreeClose();
              this.modalDonationClose();
            })
            .catch((e) => {
              this.toast("danger", e.response.data["message"]);
            });
        }
      }
    },
    SaveEvent() {
      if (this.public_id) {
        Event.alterEvent(this.public_id, this.event)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.push({ name: 'Home',})
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        this.event.id_type_event = 1;
        this.event.user_id = localStorage.getItem("public_id");
        Event.createEvent(this.event)
          .then((response) => {
            this.toast("success", response.data["message"]);
            router.push({ name: 'Home',})
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      }
    },
    openModalPaid(public_id) {
      if (public_id) {
        Ticket.GetTicket(public_id)
          .then((response) => {
            this.ticket = [];
            this.ticket = response.data.ticket;
            this.ticket_id = public_id;

            const modal = document.querySelector(".modal-pago");
            modal.classList.remove("fadeOut");
            modal.classList.add("fadeIn");
            modal.style.display = "flex";
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        this.ticket_id = null;
        this.ticket = [];
        this.ticket = this.tickets_modal;
        console.log(this.ticket);
        this.ticket.id_type_ticket = 1;

        const modal = document.querySelector(".modal-pago");
        modal.classList.remove("fadeOut");
        modal.classList.add("fadeIn");
        modal.style.display = "flex";
      }
    },
    openModalFree(public_id) {
      this.ticket = this.tickets_modal;
      this.ticket.id_type_ticket = 2;

      if (public_id) {
        this.ticket_id = public_id;
        Ticket.GetTicket(public_id)
          .then((response) => {
            this.ticket = [];
            this.ticket = response.data.ticket;
            this.ticket_id = public_id;

            const modal = document.querySelector(".modal-gratis");
            modal.classList.remove("fadeOut");
            modal.classList.add("fadeIn");
            modal.style.display = "flex";
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        this.ticket_id = null;
        const modal = document.querySelector(".modal-gratis");
        modal.classList.remove("fadeOut");
        modal.classList.add("fadeIn");
        modal.style.display = "flex";
      }
    },

    openModalDonation(public_id) {
      this.ticket = this.tickets_modal;
      this.ticket.id_type_ticket = 3;

      if (public_id) {
        this.ticket_id = public_id;
        Ticket.GetTicket(public_id)
          .then((response) => {
            this.ticket = [];
            this.ticket = response.data.ticket;
            this.ticket_id = public_id;

            const modal = document.querySelector(".modal-doacao");
            modal.classList.remove("fadeOut");
            modal.classList.add("fadeIn");
            modal.style.display = "flex";
          })
          .catch((e) => {
            this.toast("danger", e.response.data["message"]);
          });
      } else {
        this.ticket_id = null;
        const modal = document.querySelector(".modal-doacao");
        modal.classList.remove("fadeOut");
        modal.classList.add("fadeIn");
        modal.style.display = "flex";
      }
      const modal = document.querySelector(".modal-doacao");
      modal.classList.remove("fadeOut");
      modal.classList.add("fadeIn");
      modal.style.display = "flex";
    },

    modalPriceClose() {
      this.ticket_id = null;
      this.ticket = this.tickets_modal;
      const modal = document.querySelector(".modal-pago");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
    modalFreeClose() {
      this.ticket_id = null;
      this.ticket = this.tickets_modal;

      const modal = document.querySelector(".modal-gratis");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
    modalDonationClose() {
      this.ticket_id = null;
      this.ticket = this.tickets_modal;

      const modal = document.querySelector(".modal-doacao");
      modal.classList.remove("fadeIn");
      modal.classList.add("fadeOut");
      setTimeout(() => {
        modal.style.display = "none";
      }, 100);
    },
  },
};
</script>
