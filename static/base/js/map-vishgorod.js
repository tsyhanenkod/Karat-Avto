// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 50.5916367, lng: 30.4837752 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerView } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map-vishgorod"), {
    zoom: 14,
    center: position,
    mapId: "KYIV-MAP",
  });

  // The marker, positioned at Uluru
  let marker = new google.maps.Marker({
    position: position,
    map: map,
    title: 'Karat-avto Vishgorod'
  });

  marker.setMap(map);
}

initMap();