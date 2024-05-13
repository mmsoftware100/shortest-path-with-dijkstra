console.log("koye.js is started");
// famous 22.012989  96.454909
// famous second point 22.0125647,96.4533621
var user_own_position = [22.012989,  96.454909]; 

var mymap = L.map('mapid').setView(user_own_position, 18);
//mymap.setView(user_own_position, 15);
L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(mymap);

// 1st person
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

L.marker(user_own_position, { icon: markerIconRed }).addTo(mymap).bindPopup("Aung Aung - 24");

