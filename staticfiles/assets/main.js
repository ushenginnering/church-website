$('.owl-carousel').owlCarousel({
    autoplay: true,
    autoplayTimeout: 4000,
    autoplayHoverPause: true,
    loop: true,
    margin: 50,
    responsiveClass: true,
    nav: false,
    loop: true,
    stagePadding: 100,
    responsive: {
        0: {
            items: 1
        },
        568: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 3
        }
    }
})


jQuery(document).ready(function($) {
    "use strict";
    $('#customers-testimonials').owlCarousel({
        loop: true,
        center: true,
        items: 3,
        margin: 0,
        autoplay: true,
        dots:false,
        autoplayTimeout: 3000,
        smartSpeed: 450,
        responsive: {
          0: {
            items: 1
          },
          768: {
            items: 1
          },
          1170: {
            items: 3
          }
        }
    });
});