
function initMap() {
  const myLatlng = { lat: 38.870947770787254, lng: -105.14251562500002 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: myLatlng,
  });
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({});

  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    // Close the current InfoWindow.
    infoWindow.close();
    $('#id_latitude').val(mapsMouseEvent.latLng.lat().toPrecision(7));
    $('#id_longitude').val(mapsMouseEvent.latLng.lng().toPrecision(7));

    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
      JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    );
    infoWindow.open(map);
  });
}