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
from models import Raingage

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
