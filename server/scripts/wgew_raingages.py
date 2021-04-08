# scripts/wgew_raingages.py

import os, sys
from scripts.geo_utils import utm_to_latlon
from apps.wgew.models import Raingage

def run():
    """Run wgew raingages."""

    sys.stdout.write("Retrieving WGEW raingages.\n")
    delete_raingages()

    with open('../data/wgew_raingages.csv', 'r') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')
                watershed_id = values[0]
                gage_id = values[1]
                east = values[2]
                north = values[3]
                elevation = values[4]
                err = values[5]

                lat, lng = utm_to_latlon(12, float(east), float(north))
                rg = Raingage(
                    watershed_id = watershed_id,
                    gage_id = gage_id,
                    latitude = lat,
                    longitude = lng,
                    elevation = elevation,
                    err = err
                )
                rg.save()

def delete_raingages():
    raingages = Raingage.objects.all()
    if (len(raingages) > 0):
        raingages.delete()
