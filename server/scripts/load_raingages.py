# scripts/load_raingages.py
import os
from appsrer.models import Raingage
from .convert_coords import utm_to_latlon

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run():
    print("Loading raingage data.")
    with open(BASE_DIR + '/scripts/raingages.csv', 'r') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')
                # STATION CODE CURRENT STATION NAME X-COORD Y-COORD
                station_code = values[0]
                current_station_name = values[1]
                xcoord = values[2]
                ycoord = values[3]
                lat, lng = utm_to_latlon(12, float(xcoord), float(ycoord))
                rg = Raingage(code=station_code, name=current_station_name, latitude=lat, longitude=lng)
                rg.save()

    print("Done!")