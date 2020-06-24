
  document.addEventListener('DOMContentLoaded', function() {
    var elemsparallax = document.querySelectorAll('.parallax');
    var instancesparallax = M.Parallax.init(elemsparallax);
    var elemscarousel = document.querySelectorAll('.carousel');
    var instancescarousel = M.Carousel.init(elemscarousel, {indicators:true});
    var elemssidenav = document.querySelectorAll('.sidenav');
    var instancessidenav = M.Sidenav.init(elemssidenav);
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems);
  });