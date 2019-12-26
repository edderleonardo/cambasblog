$(function() {
    const logout = $('#logout');

    logout.click(function () {
        sessionStorage.removeItem("token");
        window.location.href = '/'
    });
});