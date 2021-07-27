<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'BeforeLogin',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.background-color {
  background: #fff8d6;
  height:100vh;
}
.logo {
  width: 200px;
  position: absolute;
  left: 20px;
  top: 20px;
}
</style>
