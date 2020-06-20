
  document.addEventListener('DOMContentLoaded', function() {
    var elemsparallax = document.querySelectorAll('.parallax');
    var instancesparallax = M.Parallax.init(elemsparallax);
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {indicators:true});
    var elemssidenav = document.querySelectorAll('.sidenav');
    var instancessidenav = M.Sidenav.init(elemssidenav);
  });