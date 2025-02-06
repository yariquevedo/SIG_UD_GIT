// Inicializar el mapa
var map = L.map('map').setView([4.616688555906419, -74.15938380177191], 13);

// Cargar los tiles de OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Definir las ubicaciones de los marcadores
var locations = [
    [4.618207105957917, -74.15762427270163],
    [4.617565465487658, -74.15786030708911],
    [4.61665647382802, -74.1594052594435],
    [4.618466682240845, -74.15665267958006],
    [4.61833629031914, -74.15873672451828]
];

// Agregar los marcadores al mapa
locations.forEach(function(location) {
    L.marker(location).addTo(map);
});
