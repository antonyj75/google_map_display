# Display public transport stops on Google Maps

A simple application that reads public transit stops from a given [stops.txt file](https://developers.google.com/transit/gtfs/reference/stops-file), creates a GeoJson file, and plots them on Google Maps.



Step 1. Processing stops.txt file
---------------------------------

Run the `geojson_generator.py` script to generate `stops_geojson_output.js` file.

```
python geojson_generator.py stops.txt
```


#### Prerequisites for running the geojson_generator Python script

1. Python3
2. [SciPy](http://scipy.github.io/devdocs/index.html) package


Step 2. Open the display_geojson_in_map.html in browser
-------------------------------------------------------

Once the `stops_geojson_output.js` is generated successfully by the Python script, just open the `display_geojson_in_map.html` file in a browser.
You should see a google map with stops marked and a Polygon drawn around the marked stops.


Next steps
----------

A number of improvements could be done. For example, instead of [loading GeoJson as a JavaScript callback](https://developers.google.com/maps/documentation/javascript/importing_data#try-it-yourself), we could [load it as plain GeoJson](https://developers.google.com/maps/documentation/javascript/datalayer#load_geojson).

