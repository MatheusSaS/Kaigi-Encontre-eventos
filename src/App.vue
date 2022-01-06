<template>
  <router-view/>
</template>

<script>
import Token from "@/services/Token";

export default {
  mounted() {  
    if(localStorage.getItem('token')){
      Token.setToken()
    }            
  },  
}
</script>

