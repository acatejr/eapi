from apps.srer.models import Raingage
from .geotools import utm_to_latlon

def run(*args):

    gages = Raingage.objects.all()
    if len(gages) > 0:
        Raingage.objects.all().delete()

    print("Loading SRER raingages.")
    with open('./data/srer_raingages.csv') as f:
            for i, l in enumerate(f.readlines()):
                if i > 0:
                    values = l.strip().split("|")
                    station_code = values[0]
                    current_station_name = values[1]
                    xcoord = values[2]
                    ycoord = values[3]
                    lat, lng = utm_to_latlon(12, float(xcoord), float(ycoord))
                    rg = Raingage(
                        station_code = station_code,
                        current_station_name = current_station_name,
                        latitude = lat,
                        longitude = lng
                    )
                    rg.save()

    print("Done!")

