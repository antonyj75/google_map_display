#! python3

import os
import sys
import csv
import json


def get_geojson_features(input_file):
    geojson_result = []
    coordinates = []
    with open(input_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stop_name = row['stop_name']
            stop_lat_idx = float(row['stop_lat'])
            stop_lon_idx = float(row['stop_lon'])
            coordinates.append([stop_lat_idx, stop_lon_idx])
            geojson_feature = {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates':
                [stop_lat_idx, stop_lon_idx]}, 'properties': {'name': stop_name}}
            geojson_result.append(geojson_feature)

    if len(coordinates) > 2:
        print("Creating convex hull for drawing polygon...")
        polygon_vertices = []
        from scipy.spatial import ConvexHull
        hull = ConvexHull(coordinates)
        for coordinate_idx in hull.vertices:
            polygon_vertices.append(coordinates[coordinate_idx])
        print("Convex hull vertices are ", polygon_vertices)
        geojson_polygon = {'type': 'Feature', 'geometry': {'type': 'Polygon',
            'coordinates': polygon_vertices}, 'properties': {}}
        geojson_result.append(geojson_polygon)
    return geojson_result

def get_geojson(input_file):
    geojson_features = get_geojson_features(input_file)
    geojson_collection = {'type': 'FeatureCollection', 'features': geojson_features}
    return "geojson_callback(" + json.dumps(geojson_collection, indent=4) + ");"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("USAGE: geojson_generator.py <stops.txt file path>")
        print("     The program output will be written to a file named stops_geojson_output.js")
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print("The given input file does not exist.")
        exit(1)

    print("Processing %s file..." % sys.argv[1])
    with open('stops_geojson_output.js', 'w') as outfile:
        outfile.write(get_geojson(sys.argv[1]))

