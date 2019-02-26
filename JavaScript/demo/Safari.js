if (isSafari()) {
    $(window).bind("pageshow",
    function(event) {
        if (event.originalEvent.persisted && $('body').hasClass("no-cache")) {
            document.body.style.display = "none";
            window.location.reload()
        }
    })
}
function isSafari() {
    if (navigator.userAgent.indexOf("Safari") > -1) {
        return true
    }
    return false
}