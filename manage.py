#!/usr/bin/env python
import math, os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from data.convert_coords import utm_to_latlon

app.config.from_object(os.environ['APP_SETTINGS'])
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# Import models here
from models import Raingage, PrecipEvent

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
station_name_map = [
    {"id": "white", "name": "Whitehouse"},
    {"id": "watre", "name": "Water Retention"},
    {"id": "sw", "name": "Southwest"},
    {"id": "scs5n", "name": "SCS-5N"},
    # {"id": "scs#1", "name": "SCS" },
    {"id": "scs#1", "name": "SCS #1"},
    {"id": "ruela", "name": "Ruelas"},
    {"id": "roden", "name": "Rodent"},
    {"id": "robin", "name": "Robinson"},
    {"id": "road", "name": "Road"},
    {"id": "past3", "name": "Pasture 3"},
    {"id": "parke", "name": "Parker"},
    {"id": "pa11a", "name": "Pasture 11A"},
    {"id": "nw", "name": "Northwest"},
    {"id": "nrnch", "name": "North Ranch"},
    {"id": "ne", "name": "Northeast"},
    {"id": "muhle", "name": "Muhlenbergia"},
    {"id": "mcgib", "name": "McGibbon"},
    {"id": "limst", "name": "Limestone"},
    {"id": "johns", "name": "Johnson Ranch"},
    {"id": "ibp", "name": "IBP"},
    {"id": "hughe", "name": "Hughes"},
    {"id": "huerf", "name": "Huerfano"},
    {"id": "grari", "name": "Gravelly Ridge"},
    {"id": "fores", "name": "Forest"},
    {"id": "flori", "name": "Florida"},
    {"id": "fagan", "name": "Fagan"},
    {"id": "eriop", "name": "Eriopoda"},
    {"id": "desst", "name": "Desert Station"},
    {"id": "desri", "name": "Desert Rim"},
    {"id": "desgr", "name": "Desert Grassland"},
    {"id": "choll", "name": "Cholla"},
    {"id": "box", "name": "Box"},
    {"id": "amado", "name": "Amado"},
    {"id": "airst", "name": "Airstrip"},
    {"id": "164", "name": "Enclosure 164"},
    {"id": "45", "name": "Enclosure 45"},
    {"id": "41", "name": "Enclosure 41"},
    {"id": "205", "name": "Enclosure 205"},
    {"id": "18", "name": "Enclosure 18"},
    {"id": "131", "name": "Encl. No. 131"},
]

def precip_values(values):
    output = []

    for k, v in enumerate(values):
        if v in ['-9999', '']:
            output.append(None)
        else:
            output.append(float(int(v) / 100.00))

    return output



def find_station_name(name):
    station_name = None

    for s in station_name_map:
        if s['id'] == name:
            station_name = s['name']

    return station_name

@manager.command
def load_precip_events():
    PrecipEvent.query.delete()
    print("Loading precip event data.")
    l = 0
    with open('./data/precip.csv', 'r') as f:
        for line in f.readlines():
            if l > 0:
                values = line.strip().split('|')
                station = values[0].lower()
                year = values[1]
                station_name = None
                station_id_list = list(i['id'] for i in station_name_map)
                if station in station in station_id_list:
                    station_name = find_station_name(station)
                else:
                    station_name = station

                rg = Raingage.query.filter_by(name=station_name).first()
                precip_vals = precip_values(values[2:])

                for k, v in enumerate(precip_vals):
                    month = k
                    precip_event = PrecipEvent(
                        raingage_id = rg.id,
                        year = year,
                        month = month,
                        precip = v
                    )

                    db.session.add(precip_event)
            l += 1

    db.session.commit()
    print("Done!")

@manager.command
def load_raingages():
    """ Script commmand for loading raingage data.
    """

    # Delete all raingage data first
    Raingage.query.delete()
    print("Loading raingage data.")

    with open('data/raingages.csv', 'r') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')
                # STATION CODE CURRENT STATION NAME X-COORD Y-COORD
                station_code = values[0]
                current_station_name = values[1]
                xcoord = values[2]
                ycoord = values[3]
                lat, lng = utm_to_latlon(12, float(xcoord), float(ycoord))
                rg = Raingage(
                    code = station_code,
                    name = current_station_name,
                    longitude = lng,
                    latitude = lat
                )
                db.session.add(rg)

    db.session.commit()

    print("Done!")

if __name__ == '__main__':
    manager.run()
