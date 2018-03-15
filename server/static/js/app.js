Vue.component('todo-item', {
    template: '<li>This is a todo</li>'
});

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue! ' + new Date()
    }
});

var srer = [31.854814534841164, -110.85308074951173];

// eslint-disable-next-line
var mymap = L.map('map').setView(new L.LatLng(srer[0], srer[1]), 11);

// eslint-disable-next-line
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiYWNhdGVqciIsImEiOiJDTFpxOWpJIn0.1gwlWR5IcLfCAbBs0Ue27g', { maxZoom: 30, attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' + '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery &copy <a href="http://mapbox.com">Mapbox</a>', id: 'mapbox.streets'
}).addTo(mymap);
