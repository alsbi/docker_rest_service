$(document).ready(function () {

    get_all();
    get_info();
    explore();
    setInterval(explore, 3000);


});

function explore() {
    $('.thumbnail').each(function (e, val) {
        $.ajax({
            url: '/v0.1/containers/' + val.id,
            type: 'GET',
            success: function (res) {
                if (res.State.Running == true) {
                    $(val).children().find(".btn-primary").text('stop');
                }
                else {
                    $(val).children().find(".btn-primary").text('start');
                }
                ;
            }

        });

    });
}


function get_container_info(e, id) {
    console.log("Get container info " + id);
    $("#info").empty();
    $.ajax({
        url: '/v0.1/containers/' + id,
        type: 'GET',
        success: function (res) {
            $("#info").append(
                "<p> Name : " + res.Name + "</p>" +
                "<p> Base image : " + res.Config.Image + "</p>" +
                "<p> Created: " + res.Created + "</p>" +
                "<p> Running : " + res.State.Running + "</p>"
            );
        }
    });
}

function get_container_log(e, id) {
    console.log("Get container info " + id);
    $("#info").empty();
    $.ajax({
        url: '/v0.1/containers/' + id + '/get_log',
        type: 'POST',
        success: function (res) {
            $("#info").append(
                "<p> Name : " + res.message + "</p>"
            );
        }
    });
}


function get_container_action(e, id) {
    console.log("Container " + id + ' action ' + e.text);
    $("#info").empty();
    $.ajax({
        url: '/v0.1/containers/' + id + '/' + e.text,
        type: 'POST',
        error: function () {
            console.log("Error in action container " + id + " action " + e.text);
            alert('Error execute action');
        },
        success: function (res) {
            $("#info").append(
                "<p> Status : " + res + "</p>"
            );
        }
    });
}


function get_all() {
    console.log("Get all containers");
    $("#containers").empty();
    $.getJSON('/v0.1/containers/json', function (data) {

        $.each(data, function (key, val) {
            var running = 'start';
            if (val.State.Running == true) {
                running = 'stop'
            }

            $('<div class="thumbnail" id="' + val.Id + '">' +
                '<div class="caption"><h3>' + val.Name + '</h3>' +
                '<p>' + val.State.Running + '</p>' +
                '<p>' +

                '<a href="#" class="btn btn-primary" onclick="get_container_action(this, \'' + val.Id + '\')" role="button">' + running + '</a>' +
                '<a href="#" class="btn btn-default" onclick="get_container_info(this,\'' + val.Id + '\')" role="button">Info</a>' +
                '<a href="#" class="btn btn-default" onclick="get_container_log(this,\'' + val.Id + '\')" role="button">Log</a>' +
                '</p>' +
                '</div>' +
                '</div>').appendTo('#containers');

        });

    });
}


function get_info() {
    console.log("Get system info");
    $("#info").empty();
    $.ajax({
        url: '/v0.1/info',
        type: 'GET',
        error: function () {
            console.log("Error in get info")
        },
        success: function (res) {
            $("#info").append(
                "<p> System : " + res.OperatingSystem + "</p>" +
                "<p> Server name: " + res.Name + "</p>" +
                "<p> System time: " + res.SystemTime + "</p>" +
                "<p> Images : " + res.Images + "</p>"
            );
        }
    });
}
