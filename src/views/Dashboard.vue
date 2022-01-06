<template>
  <div class="Dashboard">
    <AlterUser />
  </div>
</template>
<script>
import AlterUser from "@/components/dashboard/user/AlterUser.vue";

export default {
  name: "Dashboard",
  components: {
    AlterUser,
  },
  data: () => ({
    selected: 1,
    gender: "masculino",
  }),
};
</script>
