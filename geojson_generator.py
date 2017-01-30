#! python3

import os
import sys
import csv
import json


def get_geojson_features(input_file, geometry_type):
    geojson_result = []
    with open(input_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stop_name = row['stop_name']
            stop_lat_idx = float(row['stop_lat'])
            stop_lon_idx = float(row['stop_lon'])
            geojson_feature = {'type': 'Feature', 'geometry': {'type': geometry_type, 'coordinates':
                [stop_lat_idx, stop_lon_idx]}, 'properties': {'name': stop_name}}
            geojson_result.append(geojson_feature)
    
    print(geojson_result)
    return geojson_result

def get_geojson(input_file, geometry_type):
    geojson_features = get_geojson_features(input_file, geometry_type)
    geojson_collection = {'type': 'FeatureCollection', 'features': geojson_features}
    return "geojson_callback(" + json.dumps(geojson_collection, indent=4) + ");"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("USAGE: geojson_generator.py <stops.txt file path> <geometry type>")
        print("     geometry type could be: Point, Polygon")
        print("     The program output will be written to a file named stops_geojson_output.js")
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print("The given input file does not exist.")
        exit(1)

    if sys.argv[2] not in ['Point', 'Polygon']:
        print("The given geometry shape is unsupported.")
        exit(1)

    with open('stops_geojson_output.js', 'w') as outfile:
        outfile.write(get_geojson(sys.argv[1], sys.argv[2]))

