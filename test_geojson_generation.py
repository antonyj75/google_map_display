#! python3

import unittest
import os
import json

import geojson_generator


class TestGeoJsonGeneration(unittest.TestCase):

    def test_geojson_with_single_coordinate(self):
        input_stops = """stop_id,stop_code,platform_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone
        9673,,,Albany (Phoenix Inn Suites),,44.6294281206632,-123.060811758041,110,,0,,"""
        expected_output = [{'type': 'Feature', 'geometry': {'type': 'Point',
            'coordinates': [44.6294281206632,-123.060811758041]}, 'properties': {'name': 'Albany (Phoenix Inn Suites)'}}]
        
        with open('test_stops.txt', 'w') as f:
            f.write(input_stops)
        
        output = geojson_generator.get_geojson_features('test_stops.txt')
        self.assertEqual(output, expected_output)
        os.remove('test_stops.txt')

    def test_geojson_with_two_coordinates(self):
        input_stops = """stop_id,stop_code,platform_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone
        9673,,,Albany (Phoenix Inn Suites),,44.6294281206632,-123.060811758041,110,,0,,
        9671,,,Woodburn (Best Western Hotel),,45.1523849374081,-122.877241373062,112,,0,,"""
        expected_output = [{'type': 'Feature', 'geometry': {'type': 'Point',
            'coordinates': [44.6294281206632,-123.060811758041]}, 'properties': {'name': 'Albany (Phoenix Inn Suites)'}},
            {'type': 'Feature', 'geometry': {'type': 'Point',
                            'coordinates': [45.1523849374081,-122.877241373062]}, 'properties': {'name': 'Woodburn (Best Western Hotel)'}}]

        with open('test_stops.txt', 'w') as f:
            f.write(input_stops)

        output = geojson_generator.get_geojson_features('test_stops.txt')
        self.assertEqual(output, expected_output)
        os.remove('test_stops.txt')

    def test_complete_geojson(self):
        input_stops = """stop_id,stop_code,platform_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone
        9673,,,Albany (Phoenix Inn Suites),,44.6294281206632,-123.060811758041,110,,0,,"""
        expected_output_json = {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point',
            'coordinates': [44.6294281206632,-123.060811758041]}, 'properties': {'name': 'Albany (Phoenix Inn Suites)'}}]}

        with open('test_stops.txt', 'w') as f:
            f.write(input_stops)

        output = geojson_generator.get_geojson('test_stops.txt')
        expected_output = "geojson_callback(" + json.dumps(expected_output_json, indent=4) + ");"
        print(expected_output)
        print(output)
        self.assertEqual(output, expected_output)
        os.remove('test_stops.txt')

