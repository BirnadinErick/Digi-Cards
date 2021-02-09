/* ===================================
    sticky nav
 ====================================== */

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('nav').addClass('shrink');
    } else {
        $('nav').removeClass('shrink');
    }
});

$(document).ready(function () {
    let scrollAnimationTime;
    let scrollAnimation;

    /*==============================================================
            smooth scroll
    ==============================================================*/
    let hash = window.location.hash.substr(1);
    if (hash !== "") {
        scrollAnimationTime = 1200;
        scrollAnimation = 'easeInOutExpo';

        let target = '#' + hash;
        $('html, body').stop()
            .animate({
                'scrollTop': $(target)
                    .offset()
                    .top
            }, scrollAnimationTime, scrollAnimation, function () {
                window.location.hash = target;
            });
    }

    scrollAnimationTime = 1200;
    scrollAnimation = 'easeInOutExpo';

    // noinspection SpellCheckingInspection
    $('a.scrollto').bind('click.smoothscroll', function (event) {
        event.preventDefault();
        let target = this.hash;
        $('html, body').stop()
            .animate({
                'scrollTop': $(target)
                    .offset()
                    .top
            }, scrollAnimationTime, scrollAnimation, function () {
                window.location.hash = target;
            });
    });

    /*==============================================================
        set parallax
     ==============================================================*/
    let IsParallaxGenerated = false;
    function SetParallax() {
        if ($(window).width() > 1030 && !IsParallaxGenerated) {
            $('.parallax1').parallax("50%", 0.1);
            $('.parallax2').parallax("50%", 0.2);
            $('.parallax3').parallax("50%", 0.3);
            $('.parallax4').parallax("50%", 0.4);
            $('.parallax5').parallax("50%", 0.5);
            $('.parallax6').parallax("50%", 0.6);
            $('.parallax7').parallax("50%", 0.7);
            $('.parallax8').parallax("50%", 0.8);
            $('.parallax9').parallax("50%", 0.05);
            $('.parallax10').parallax("50%", 0.02);
            $('.parallax11').parallax("50%", 0.01);
            $('.parallax12').parallax("50%", 0.099);
            IsParallaxGenerated = true;
        }
    }
    SetParallax();

    $('.parallax-fix').each(function () {
        if ($(this).children('.parallax-background-img').length) {
            const imgSrc = jQuery(this).children('.parallax-background-img').attr('src');
            jQuery(this).css('background', 'url("' + imgSrc + '")');
            jQuery(this).children('.parallax-background-img').remove();
            $(this).css('background-position', '50% 0%');
        }
    });
});

/*==============================================================
    full screen
 ==============================================================*/

function SetResizeContent() {
    // noinspection SpellCheckingInspection
    const minheight = $(window).height();
    $(".full-screen").css('min-height', minheight);
}
SetResizeContent();

$(window).resize(function () {
    SetResizeContent();
});