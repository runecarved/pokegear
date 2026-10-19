<!--
Source - https://stackoverflow.com/a/56572392
Posted by user6848902
Retrieved 2026-10-16, License - CC BY-SA 4.0
-->

$(function () {
    var bar = '';
    bar += '<nav class="navbar navbar-default" role="navigation">';
    bar += '<div class="container-fluid">';
    bar += '<div>';
    bar += '<ul class="nav navbar-nav">';
    bar += '<li id="map"><a href="map.html">Home</a></li>';
    bar += '<li id="calendar"><a href="calendar.html">Index</a></li>';
    bar += '<li id="phone"><a href="phone.html">Phonebook</a></li>';
    bar += '<li id="evolution-planner"><a href="evolution.html">Evolution Planner</a></li>';
    bar += '<li id="stat-exp"><a href="statexp.html">Stat EXP Tracker</a></li>';
    bar += '<li id="about"><a href="index.html">About</a></li>';
    bar += '</ul>';
    bar += '</div>';
    bar += '</div>';
    bar += '</nav>';

    $("#main-bar").html(bar);

    var id = getValueByName("id");
    $("#" + id).addClass("active");
});

function getValueByName(name) {
    var url = document.getElementById('nav-bar').getAttribute('src');
    var param = new Array();
    if (url.indexOf("?") != -1) {
        var source = url.split("?")[1];
        items = source.split("&");
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            var parameters = item.split("=");
            if (parameters[0] == "id") {
                return parameters[1];
            }
        }
    }
}
