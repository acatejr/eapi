from apps.wgew.models import Raingage
from .geotools import utm_to_latlon

def run(*args):

    gages = Raingage.objects.all()
    if len(gages) > 0:
        Raingage.objects.all().delete()

    print("Loading WGEW raingages.")
    with open('./data/wgew_raingages.csv') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split("|")
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
                    east = east,
                    north = north,
                    elevation = elevation,
                    err = err,
                    latitude = lat,
                    longitude = lng
                )
                rg.save()
    f.close()
    print("Done!")
