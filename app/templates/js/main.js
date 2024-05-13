console.log("main.js is started");

var localhost_ip = 'localhost'; // localhost
//var localhost_ip ='192.168.43.32'; // km phone wifi ip address

// 22.017735, 96.460437
var user_own_position = [22.012989, 96.454909]; //famous 22.012989  96.454909
//var user_location_id = 3; // famous hotel node id
var user_location_id = 23; // famous hotel node id


var mymap = L.map('mapid').setView([22.0333331, 96.4666670], 15);
// move to POL
//mymap.panTo(new L.LatLng(22.017735, 96.460437));
// FCTS 22.535243,75.750383
// https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
// 'http://' + localhost_ip + '/google_map/leaflet/tiles/0/{z}/{x}/{y}.png'
// mymap.setView([22.535243, 75.750383], 15);
mymap.setView([22.012989,  96.454909], 18);
/*
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: 'Sandar Map',
    maxZoom: 18,
    minZoom: 13
}).addTo(mymap);
*/

L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(mymap);



// mymap.locate({ setView: true, maxZoom: 16 });

/*
function onLocationFound(e) {
    var radius = e.accuracy / 2;

    L.marker(e.latlng).addTo(mymap)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

    L.circle(e.latlng, radius).addTo(mymap);
}
*/

//mymap.on('locationfound', onLocationFound);

function onLocationError(e) {
    //alert(e.message);
    console.log("onLocationError is " + e.message);
}

// mymap.on('locationerror', onLocationError);


var greenIcon = L.icon({
    iconUrl: 'images/leaf-green.png',
    shadowUrl: 'images/leaf-shadow.png',

    iconSize: [38, 95], // size of the icon
    shadowSize: [50, 64], // size of the shadow
    iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62], // the same for the shadow
    popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
});

var map_marker_icon = L.icon({
    iconUrl: 'images/map_marker.png',

    iconSize: [38, 95], // size of the icon
    shadowSize: [50, 64], // size of the shadow
    iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62], // the same for the shadow
    popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
});

var markerIconRed = L.icon({
    iconUrl: 'images/marker.png',
    iconSize: [38, 95], // size of the icon
    shadowSize: [50, 64], // size of the shadow
    iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62], // the same for the shadow
    popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
});

//L.marker([22.0333331, 96.4666670], {icon: greenIcon}).addTo(mymap).bindPopup("I am a green leaf.");

//var marker = L.marker([22.1333390, 96.4666670],{icon:markerIconRed}).addTo(mymap);


var markerList = [];
var shortest_path_line = new L.Polyline([], {
    color: 'blue',
    weight: 5,
    opacity: 0.5,
    smoothFactor: 1
});

function add_marker(lat, long, name) {
    // add marker
    let marker = L.marker([lat, long], { icon: map_marker_icon }).addTo(mymap).bindPopup(name);
    markerList[markerList.length] = marker;
    // let marker = new L.marker([lat, long], { icon: map_marker_icon }).bindPopup(name);
    // markerList.push(marker);
    // mymap.addLayer(markerList.length - 1);
    mymap.setView([lat, long], 15);
}

function removeAllMarker() {
    console.log("removeAllMarker");
    for (let i = 0; i < markerList.length; i++) {
        console.log("marker " + i);
        mymap.removeLayer(markerList[i]);
    }
}

function removeLine() {
    mymap.removeLayer(shortest_path_line);
}


var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mymap);
}

mymap.on('click', onMapClick);




var pointA = new L.LatLng(22.0333331, 96.4666670);
var pointB = new L.LatLng(22.030719, 96.467678);
var pointC = new L.LatLng(22.031992, 96.476602);
var pointD = new L.LatLng(22.03772, 96.470038);

var pointList = [pointA, pointB, pointC, pointD];

var firstpolyline = new L.Polyline(pointList, {
    color: 'blue',
    weight: 5,
    opacity: 0.5,
    smoothFactor: 1
});

//firstpolyline.addTo(mymap);

$("#mapid").on('click', function() {
    //alert("map id is clicked");
});


$("#draw_graph_button").on('click', function() {
    console.log("draw graph button is clicked");
    // we need to get all places and link to draw graph
    show_loading_modal('Getting categories from server');
    var requested_data = { operation: "get_graph" };
    $.ajax({
            method: "GET",
            //url: "http://" + localhost_ip + "/google_map/server.php",
            url: "./server.php",
            data: requested_data
        })
        .done(function(msg) {

            setTimeout(hide_loading_modal, 1000);
            // validate returned data => success or display error message
            console.log("categories get response is : " + msg);
            var returned_data = JSON.parse(msg);
            if (returned_data.status == "success") {
                var places = returned_data.places;
                var links = returned_data.links;
                for (var i = 0; i < places.length; i++) {
                    // add circle to graph
                    L.circle([places[i].lat, places[i].long], { radius: 10 }).addTo(mymap).bindPopup(places[i].name);
                }

                for (var j = 0; j < links.length; j++) {
                    var source_node_id = links[j]['node1'] + "";
                    var destination_node_id = links[j]['node2'] + "";

                    var source_node_index = places.map(function(e) { return e.id; }).indexOf(source_node_id);
                    var destination_node_index = places.map(function(e) { return e.id; }).indexOf(destination_node_id);

                    console.log(" links is  is " + JSON.stringify(links));

                    var latlngs = [
                        [places[source_node_index].lat, places[source_node_index].long],
                        [places[destination_node_index].lat, places[destination_node_index].long]
                    ];
                    var polyline = L.polyline(latlngs, { color: 'white' }).addTo(mymap);
                }
            } else {
                var error_msg = returned_data.err_msg;
                console.log("No graph data :  " + error_msg);
            }
        });

});


$("#categories_button").on('click', function() {
    //alert("categories_button is clicked");
    show_loading_modal('Getting categories from server');
    var requested_data = { operation: "get_categories" };
    $.ajax({
            method: "GET",
            //url: "http://" + localhost_ip + "/google_map/server.php",
            url: "./server.php",
            data: requested_data
        })
        .done(function(msg) {

            setTimeout(hide_loading_modal, 1000);
            // validate returned data => success or display error message
            console.log("categories get response is : " + msg);
            var returned_data = JSON.parse(msg);
            if (returned_data.status == "success") {
                // requested data is ok 
                // we need to re-render our data view with latest server returned data
                // initialize localStorage and 
                // set new Data
                // render backbone view for retrieveing
                // and reload the whole app
                var categories = returned_data.categories;
                //save_localStorage("data",new_data);
                //render_new_data(0);
                //show_notification(newSoldier.mc+" is inserted into database server",'success');

                // we need to show those categories in cat table
                var str = "";
                for (var i = 0; i < categories.length; i++) {
                    console.log("<li class='cat_list_item' href='#" + categories[i].id + "'><button>" + categories[i].name + "</button></li>");
                    str = str + "<li class='cat_list_item' href='#" + categories[i].id + "'><button>" + categories[i].name + "</button></li>";
                }

                $("#cat_list").html(str);
                add_listner_on_list();

                console.log("str is " + str);

            } else {
                // requested data is not ok 
                // we have to show the error message
                // and stay on the last page condition
                // highlight the error section
                var error_msg = returned_data.error_msg;
                //error_msg = error_msg.sqlMessage;

                //$("#new_soldier").modal("hide");
                //show_notification("insert data error response is "+error_msg,'error');
                console.log("We faced with error in inserting new data and error is " + error_msg);
            }
        });
});

function add_listner_on_list() {
    $("li.cat_list_item").on('click', function() {
        //alert("cat list item is clicked on "+$(this).text());
        var cat_id = $(this).attr("href");
        //alert("cat id is "+cat_id);
        //alert("real id is "+cat_id.slice(1, cat_id.length));
        var real_cat_id = cat_id.slice(1, cat_id.length);
        // call ajax to server 

        var requested_data = { operation: "get_places", cat_id: real_cat_id };
        $.ajax({
                method: "GET",
                url: "./server.php",
                data: requested_data
            })
            .done(function(msg) {

                setTimeout(hide_loading_modal, 1000);
                // validate returned data => success or display error message
                console.log("get_places get response is : " + msg);
                var returned_data = JSON.parse(msg);
                if (returned_data.status == "success") {
                    // requested data is ok 
                    // we need to re-render our data view with latest server returned data
                    // initialize localStorage and 
                    // set new Data
                    // render backbone view for retrieveing
                    // and reload the whole app
                    var places = returned_data.places;
                    //save_localStorage("data",new_data);
                    //render_new_data(0);
                    //show_notification(newSoldier.mc+" is inserted into database server",'success');

                    // we need to show those categories in cat table
                    var str = "";
                    for (var i = 0; i < places.length; i++) {
                        console.log("<li class='place_list_item' data-id='" + places[i].id + "' data-lat='" + places[i].lat + "' data-long='" + places[i].long + "'><button>" + places[i].name + "</button></li>");
                        str = str + "<li class='place_list_item' data-id='" + places[i].id + "'  data-lat='" + places[i].lat + "' data-long='" + places[i].long + "'><button>" + places[i].name + "</button></li>";
                    }

                    $("#place_list").html(str);
                    add_listner_on_place_list();

                    console.log("str is " + str);

                } else {
                    // requested data is not ok 
                    // we have to show the error message
                    // and stay on the last page condition
                    // highlight the error section
                    var error_msg = returned_data.error_msg;
                    //error_msg = error_msg.sqlMessage;

                    //$("#new_soldier").modal("hide");
                    //show_notification("insert data error response is "+error_msg,'error');
                    console.log("We faced with error in inserting new data and error is " + error_msg);
                }
            });



    });
}


show_loading_modal('Map is initializing..');
setTimeout(hide_loading_modal, 1000);

function add_listner_on_place_list() {
    console.log("hello we");
    $("li.place_list_item").on('click', function() {
        //alert("cat list item is clicked on "+$(this).text());

        var data_lat = $(this).attr("data-lat");
        var data_long = $(this).attr("data-long");
        var data_name = $(this).text();
        //alert("lat is "+data_lat+"|"+data_long+"|"+data_name);
        // call ajax to server 
        //add_marker(data_lat,data_long,data_name);
        //add_marker("22.0333331", "96.4666670","it is function marker");

        // call to ajax using data-id
        var data_id = $(this).attr("data-id");
        //alert("place id is "+data_id);

        var requested_data = { operation: "shortest_path", source_id: user_location_id, destination_id: data_id };
        $.ajax({
                method: "GET",
                url: "./server.php",
                data: requested_data
            })
            .done(function(msg) {

                setTimeout(hide_loading_modal, 1000);
                // validate returned data => success or display error message
                console.log("shortest_path get response is : " + msg);
                var returned_data = JSON.parse(msg);
                if (returned_data.status == "success") {
                    // requested data is ok 
                    // we need to re-render our data view with latest server returned data
                    // initialize localStorage and 
                    // set new Data
                    // render backbone view for retrieveing
                    // and reload the whole app
                    var path = returned_data.solution.solution_path;
                    var status = returned_data.solution.status;
                    var distance = returned_data.solution.distance;
                    var error_msg = returned_data.solution.err_msg;
                    var places = returned_data.places;

                    /*
                    // add all marker  
                    for(var j=0; j<places.length; j++){
                        add_marker(places[j].lat,places[j].long,places[j].name);
                    }
                    */

                    console.log("the status is " + status);

                    if (status == "no_route") {
                        // there is no path 
                        console.log("there is no path");
                        return;
                        // end request operation
                    } else {
                        // loop through path 
                        // draw poly line on map
                        //var first_place_id = parseInt(path[0], 10);

                        var first_place_id = "" + path[0];
                        // we also need to get the index of those first place id in places

                        var first_place_index = places.map(function(e) { return e.id; }).indexOf(first_place_id);
                        //console.log("first place index is "+first_place_index);


                        var pointA = new L.LatLng(places[first_place_index].lat, places[first_place_index].long);
                        var pointList = [pointA];

                        console.log("place index is " + first_place_index + " and id is " + first_place_id);
                        add_marker(places[first_place_index].lat, places[first_place_index].long, places[first_place_index].name);

                        var solution_text = "Total Distance is " + distance + " from " + places[first_place_index].name;

                        var list_text = "<li>" + places[first_place_index].name + "</li>";
                        for (var i = 1; i < path.length; i++) {
                            //var place_id = parseInt(path[i], 10);
                            //var place_id = ""+path[i];
                            //var place_index =  places.map(function(e) { return e.id; }).indexOf(place_id);

                            //var pointX = new L.LatLng(places[place_id].lat,places[place_id].long);
                            //pointList[pointList.length] = pointX;

                            //add_marker(places[place_id].lat,places[place_id].long,places[place_id].name+place_id+" and "+place_index);

                            var place_id = path[i] + "";
                            var place_index = places.map(function(e) { return e.id; }).indexOf(place_id);
                            console.log("for i is " + i + " place index is " + place_index + " and id is " + place_id + " path [ i ] is " + path[i]);
                            solution_text = solution_text + " => " + places[place_index].name;

                            add_marker(places[place_index].lat, places[place_index].long, places[place_index].name);
                            var pointX = new L.LatLng(places[place_index].lat, places[place_index].long);
                            pointList[pointList.length] = pointX;


                            list_text = list_text + "<li>" + places[place_index].name + "</li>";

                        }

                        $("#shortest_path_list").html(list_text);
                        $("#total_distance_span").text(distance);

                        console.log("point list is " + JSON.stringify(pointList));
                        console.log("Solution text is" + solution_text);



                        shortest_path_line = new L.Polyline(pointList, {
                            color: 'blue',
                            weight: 5,
                            opacity: 0.5,
                            smoothFactor: 1
                        });


                        shortest_path_line.addTo(mymap);

                    } // end for path => if else

                    //save_localStorage("data",new_data);
                    //render_new_data(0);
                    //show_notification(newSoldier.mc+" is inserted into database server",'success');

                    // we need to show those categories in cat table

                    /*
                    var str  = "";
                    for(var i=0; i<places.length; i++){
                        console.log("<li class='place_list_item' data-id='"+places[i].id+"' data-lat='"+places[i].lat+"' data-long='"+places[i].long+"'><button>"+places[i].name+"</button></li>");
                        str = str + "<li class='place_list_item' data-id='"+places[i].id+"'  data-lat='"+places[i].lat+"' data-long='"+places[i].long+"'><button>"+places[i].name+"</button></li>";
                    }

                    $("#place_list").html(str);
                    add_listner_on_place_list();

                    console.log("str is "+str);
                    */

                } else {
                    // requested data is not ok 
                    // we have to show the error message
                    // and stay on the last page condition
                    // highlight the error section
                    var error_msg = returned_data.error_msg;
                    //error_msg = error_msg.sqlMessage;

                    //$("#new_soldier").modal("hide");
                    //show_notification("insert data error response is "+error_msg,'error');
                    console.log("We faced with error in inserting new data and error is " + error_msg);
                } // server response is not success . just it's fail , notify user with error message
            });


    });

};

function show_loading_modal(msg) {
    //sleep(1000);
    $('body').loadingModal({
        position: 'auto',
        text: msg,
        color: '#fff',
        opacity: '0.7',
        backgroundColor: 'rgb(0,0,0)',
        animation: 'wave'
    });
}

function hide_loading_modal() {
    $('body').loadingModal('hide');
    // destroy the plugin
    $('body').loadingModal('destroy');
}


// getting list of places
var requested_data_places = { operation: "places" };
$.ajax({
        method: "GET",
        url: "./server.php",
        data: requested_data_places
    })
    .done(function(msg) {
        // validate returned data => success or display error message
        console.log("places get response is : " + msg);
        var returned_data = JSON.parse(msg);
        if (returned_data.status == "success") {
            var places = returned_data.places;
            var str = "";
            for (var i = 0; i < places.length; i++) {
                str = str + "<option value=" + places[i].id + " class='place_list_item'>" + places[i].name + "</option>";
            }

            $("#source").html(str);
            $("#destination").html(str);

        } else {
            var error_msg = returned_data.error_msg;
            console.log("We faced with error in inserting new data and error is " + error_msg);
        }
    });

function findShortestPath(source_id, destination_id) {
    removeAllMarker();
    removeLine();
    // clear previous path
    var requested_data = { operation: "shortest_path", source_id: source_id, destination_id: destination_id };
    $.ajax({
            method: "GET",
            url: "./server.php",
            data: requested_data
        })
        .done(function(msg) {

            setTimeout(hide_loading_modal, 1000);
            // validate returned data => success or display error message
            console.log("shortest_path get response is : " + msg);
            var returned_data = JSON.parse(msg);
            if (returned_data.status == "success") {
                // requested data is ok 
                // we need to re-render our data view with latest server returned data
                // initialize localStorage and 
                // set new Data
                // render backbone view for retrieveing
                // and reload the whole app
                var path = returned_data.solution.solution_path;
                var status = returned_data.solution.status;
                var distance = returned_data.solution.distance;
                var error_msg = returned_data.solution.err_msg;
                var places = returned_data.places;

                /*
                // add all marker  
                for(var j=0; j<places.length; j++){
                    add_marker(places[j].lat,places[j].long,places[j].name);
                }
                */

                console.log("the status is " + status);

                if (status == "no_route") {
                    // there is no path 
                    console.log("there is no path");
                    return;
                    // end request operation
                } else {
                    // loop through path 
                    // draw poly line on map
                    //var first_place_id = parseInt(path[0], 10);

                    var first_place_id = "" + path[0];
                    // we also need to get the index of those first place id in places

                    var first_place_index = places.map(function(e) { return e.id; }).indexOf(first_place_id);
                    //console.log("first place index is "+first_place_index);


                    var pointA = new L.LatLng(places[first_place_index].lat, places[first_place_index].long);
                    var pointList = [pointA];

                    console.log("place index is " + first_place_index + " and id is " + first_place_id);
                    add_marker(places[first_place_index].lat, places[first_place_index].long, places[first_place_index].name);

                    var solution_text = "Total Distance is " + distance + " from " + places[first_place_index].name;

                    var list_text = "<li>" + places[first_place_index].name + "</li>";
                    for (var i = 1; i < path.length; i++) {
                        //var place_id = parseInt(path[i], 10);
                        //var place_id = ""+path[i];
                        //var place_index =  places.map(function(e) { return e.id; }).indexOf(place_id);

                        //var pointX = new L.LatLng(places[place_id].lat,places[place_id].long);
                        //pointList[pointList.length] = pointX;

                        //add_marker(places[place_id].lat,places[place_id].long,places[place_id].name+place_id+" and "+place_index);

                        var place_id = path[i] + "";
                        var place_index = places.map(function(e) { return e.id; }).indexOf(place_id);
                        console.log("for i is " + i + " place index is " + place_index + " and id is " + place_id + " path [ i ] is " + path[i]);
                        solution_text = solution_text + " => " + places[place_index].name;

                        add_marker(places[place_index].lat, places[place_index].long, places[place_index].name);
                        var pointX = new L.LatLng(places[place_index].lat, places[place_index].long);
                        pointList[pointList.length] = pointX;


                        list_text = list_text + "<li>" + places[place_index].name + "</li>";

                    }

                    $("#shortest_path_list").html(list_text);
                    $("#total_distance_span").text(distance);

                    console.log("point list is " + JSON.stringify(pointList));
                    console.log("Solution text is" + solution_text);



                    shortest_path_line = new L.Polyline(pointList, {
                        color: 'blue',
                        weight: 5,
                        opacity: 0.5,
                        smoothFactor: 1
                    });


                    shortest_path_line.addTo(mymap);

                } // end for path => if else

                //save_localStorage("data",new_data);
                //render_new_data(0);
                //show_notification(newSoldier.mc+" is inserted into database server",'success');

                // we need to show those categories in cat table

                /*
                var str  = "";
                for(var i=0; i<places.length; i++){
                    console.log("<li class='place_list_item' data-id='"+places[i].id+"' data-lat='"+places[i].lat+"' data-long='"+places[i].long+"'><button>"+places[i].name+"</button></li>");
                    str = str + "<li class='place_list_item' data-id='"+places[i].id+"'  data-lat='"+places[i].lat+"' data-long='"+places[i].long+"'><button>"+places[i].name+"</button></li>";
                }

                $("#place_list").html(str);
                add_listner_on_place_list();

                console.log("str is "+str);
                */

            } else {
                // requested data is not ok 
                // we have to show the error message
                // and stay on the last page condition
                // highlight the error section
                var err_msg = returned_data.err_msg;
                //error_msg = error_msg.sqlMessage;

                //$("#new_soldier").modal("hide");
                //show_notification("insert data error response is "+error_msg,'error');
                console.log("no shortest path " + err_msg);
            } // server response is not success . just it's fail , notify user with error message
        });

}
$("#find_shortest_path").on('click', function() {
    let source_id = $("#source").val();
    let destination_id = $("#destination").val();
    findShortestPath(source_id, destination_id);
});