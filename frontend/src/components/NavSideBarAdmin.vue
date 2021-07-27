<template>
  <div style="font-family: 'Jua', sans-serif;" class="sidenav con w3-sidebar w3-bar-block fixed-top" aria-label="Sidebar with custom footer" no-header shadow>      
    <img class="navbar-logo" src="@/assets/슬학생_로고.png" alt="슬학생_로고">
    <div style="margin-top:10%;">
      <router-link class="w3-bar-item w3-button tablink text-decoration-none" to="/home">선생님 관리</router-link><br>
      <router-link class="w3-bar-item w3-button text-decoration-none" to="/class">학생 관리</router-link><br>
    </div>
    <!-- <footer id="navFooter">슬기로운 학교생활</footer> -->
  </div>
  
</template>

<script>
export default {
  name: 'NavsidebarAdmin',
  methods: {
    myDropFunc: function () {
      var x = document.getElementById("demoDrop")
      if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-green"
      } else { 
        x.className = x.className.replace(" w3-show", "")
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace(" w3-green", "")
      }
    }
  }
}

</script>

<style>
/* The sidebar menu */
.sidenav {
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 20%; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  background-color: #fff8d6;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 2%;
  padding-left: 1%;
  margin-right: 1%;
}

/* The navigation menu links */
.sidenav a {
  padding-left: 5%;
  font-size: 200%;
  color: #818181;
  display: block;
  text-align: left;
}

/* When you mouse over the navigation links, change their color */
.sidenav a:hover {
  text-decoration: none;
  color: black;
  /* background-color: white; */
}

/* Style page content */
.main {
  margin-left: 100%; /* Same as the width of the sidebar */
  padding: 0px 10px;
}

/* On smaller screens, where height is less than 450px, change the style of the sidebar (less padding and a smaller font size) */
@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}

/* #navFooter {
  padding-top: 100px;
} */

/* 고정테스트 */
.tablink {
  cursor:pointer;
}

/* 더 고민 */
.icon {
  width: 60px;
  right: 10px;
  position: absolute;
  left:140px;
  bottom: 290px;
}
.navbar-logo {
  width: 90%;
  margin-right: 5%;
}
</style>
