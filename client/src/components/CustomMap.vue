<template>
  <div id="leaflet-map"></div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { map, tileLayer, geoJSON,popup } from 'leaflet';
import 'leaflet/dist/leaflet.css';



// fetch geojson data
const geojson = await fetch('http://127.0.0.1:3000/api/geodata/').then(res => res.json())
// Créer une référence à l'élément du template qui contiendra la carte
const mapContainer = ref(null);

// Initialiser la carte au montage du composant
onMounted(() => {
  // Créer la carte
  mapContainer.value = map('leaflet-map').setView([-21.340443885135485, 55.49113642891109], 17)

  // Ajouter une couche de tuiles 
  tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(mapContainer.value);

  // ADD GEOJSON DATA
  const geojsonLayer = geoJSON(geojson)
  geojsonLayer.addTo(mapContainer.value)
  
  // ADD POPUP for properties tta for each feature
  geojsonLayer.bindPopup(function (layer: any) {
    const props = layer.feature.properties;
    const popupContent = Object.keys(props).map((key) => {
      return `<tr><td><strong>${key}</strong></td><td>${props[key]}</td></tr>`
    }).join('');
    return `<table>${popupContent}</table>`
  });

  // ADD HIGHLIGHT on mouse in/out
  function highlightFeature(e: any) {
    const layer = e.target;
    layer.setStyle({
      weight: 5,
      fillOpacity: 0.7,
    });

  }

  function resetHighlight(e: any) {
    geojsonLayer.resetStyle(e.target);
  }



  // mouse hover
  geojsonLayer.eachLayer(function (layer: any) {
    layer.on({
      mouseover: highlightFeature,
      mouseout: resetHighlight,
    });
  });




});



</script>

<style scoped>
#leaflet-map {
  height: 100vmax;
}
</style>
