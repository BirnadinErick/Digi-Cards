!function (n) {
    "use strict";

    function t() {
        n.main = n(".main"), n.mainContent = n(".main_content"), n.contentMargin = (n(window).height() - n.mainContent.height()) / 2, n.main.css({height: n(window).height() + "px"}), n.mainContent.css({"margin-top": n.contentMargin + "px"})
    }

    n(window).resize(function (n) {
        t()
    }), n(window).scroll(function (n) {
    }), n(window).load(function (n) {
    }), n(document).ready(function (i) {
        t(), n("#scene").parallax({
            scalarX: 10,
            scalarY: 10,
            frictionX: .1,
            frictionY: .1
        }), n(document).on("contextmenu", function (n) {
            return !1
        })
    })
}(jQuery);