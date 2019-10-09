<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <ClimbApp title="Welcome to Your ClimbApp"/>
  </div>
</template>

<script>
import ClimbApp from './components/ClimbApp.vue'

export default {
  name: 'app',
  components: {
    ClimbApp
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
