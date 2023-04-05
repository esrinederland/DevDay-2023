import { Component, Element, Prop, h } from '@stencil/core';
import Map from "@arcgis/core/Map";
import WebMap from "@arcgis/core/WebMap";
import MapView from "@arcgis/core/views/MapView";

@Component({
  tag: 'arcgis-map',
  styleUrl: 'arcgis-map.css',
  shadow: true,
})
export class ArcGISMap {

  @Element() private el: HTMLElement;

  @Prop() webmapId: string; // as the webmap-id prop in the web component <arcgis-map webmap-id="..."

  componentDidRender() {
    this.createMap(); 
  }

  private createMap() : void {
    // To have the font in Map like the +/- zoom buttons
    const font = document.createElement("link");
    font.href = "https://js.arcgis.com/4.26/@arcgis/core/assets/esri/themes/light/main.css";
    font.rel = "stylesheet"
    document.head.appendChild(font);

    let map;
    if(this.webmapId) {
      map = new WebMap({
        portalItem: {
          id: this.webmapId
        }
      });
    }
    else {
      map = new Map({
        basemap: "streets-vector"
      });
    }

    // Create a MapView instance (for 2D viewing) and reference the map instance
    new MapView({
      map: map,
      container: this.el.shadowRoot?.querySelector('#viewDiv') as HTMLDivElement
    });
  }

  render() {
    return <div style={{height: '100%', width: '100%'}}>
      <style> @import "https://js.arcgis.com/4.26/@arcgis/core/assets/esri/themes/light/main.css"; </style>
      <div id="viewDiv"></div>
    </div>;
   
  }
}
