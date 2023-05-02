// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 50.4657358, lng: 30.4468069 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerView } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map-kyiv"), {
    zoom: 13,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  let marker = new google.maps.Marker({
    position: position,
    map: map,
    title: 'Karat-avto Kyiv'
  });

  marker.setMap(map);

}

initMap();
