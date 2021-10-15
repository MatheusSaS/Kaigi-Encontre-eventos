<template>
  <div class="Dashboard">
    <div v-if="$route.params.type === 'home'">
      <h1 class="text-red-600 mt-16" >{{selected}}</h1>
    </div>
    <div v-else-if="$route.name === 'my-events'">

    </div>
    <VueBottomNavigation :options="options"  :value="selected" v-model="selected"/>    
  </div>
</template>
<script>
import VueBottomNavigation from "bottom-navigation-vue";
export default {
  name: "Dashboard",
  components: {
    VueBottomNavigation,
  },
  data: () => ({
    selected: 1,    
    options: [
      {
        id: 1,
        icon: "fas fa-home",
        title: "Home",
        href:"/Homea",
      },
      {
         id: 2, 
         icon: "fas fa-wallet",
         title: "Wallet", 
         href:"/Home",
         },
      {
        id: 3,
        icon: "fas fa-plus",
        title: "Setting",
        childs: [
          { id: 301, icon: "fas fa-bookmark", title: "Bookmarks" },
          { id: 302, icon: "fas fa-tasks", title: "Tasks" },
          { id: 303, icon: "fas fa-tachometer-alt", title: "Dashboard" },
          { id: 304, icon: "fas fa-ticket-alt", title: "Tickets" },
          { id: 305, icon: "fas fa-file-signature", title: "Contract" },
        ],
      },
      { id: 4, icon: "fas fa-bell", title: "Notification", badge: 15,href:"/Home", },
      { id: 5, icon: "fas fa-user", title: "Account",href:"/Home", },
    ],
  }),
};
</script>
