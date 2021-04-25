import os
from pathlib import Path
import fire
from cmds.geotools import utm_to_latlon
from app.models import WGEWRaingage, WGEWPrecipEvent
from app.database import db_session, engine

db = db_session()

def load_wgew_precipevents():
    """Loads WGEW precip event data"""
    print("Loading WGEW precip event data.")

    # Delete all precip events first
    WGEWPrecipEvent.query.delete()
    with engine.connect() as con:
        con.execute('ALTER SEQUENCE wgew_precipevent_id_seq RESTART WITH 1')
    db.commit()
    
    # ALTER SEQUENCE wgew_raingage_id_seq RESTART WITH 1


    with open('data/wgew_precip_events.csv', 'r') as f:
        current_raingage_id = None
        rg = None
        events = []

        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')
                gage = values[0]
                dt = values[1].split('/')
                tm = values[2]
                duration = values[3]
                depth = values[4]
                time_est = values[5]

                if len(dt[0]) == 1:
                    mo = '0{}'.format(dt[0])
                else:
                    mo = dt[0]

                if len(dt[1]) == 1:
                    dy = '0{}'.format(dt[1])
                else:
                    dy = dt[1]

                if len(dt[2]) == 1:
                    yr = '0{}'.format(dt[2])
                else:
                    yr = dt[2]

                dt = '{}-{}-{}'.format(yr, mo, dy)

                # Raingage 6 is not in the db os it raises exception.
                try:
                    if (current_raingage_id != gage):
                        rg = db.query(WGEWRaingage).filter_by(gage_id=gage, watershed_id=63).first()
                        current_raingage_id = gage

                    pe = WGEWPrecipEvent(
                        raingage_id=rg.id,
                        event_date = dt,
                        event_time = tm,
                        duration = duration,
                        depth = depth,
                        time_est = time_est
                    )

                    events.append(pe)
                except Exception:
                    pass

        if events:
            db.bulk_save_objects(events)

        db.commit()
        db.close()

def load_wgew_raingages():
    """Loads WGEW raingage data"""
    print("Loading WGEW raingage data.")

    # Delete all WGEWRaingage records first
    WGEWRaingage.query.delete()
    WGEWPrecipEvent.query.delete()
    with engine.connect() as con:
        con.execute('ALTER SEQUENCE wgew_raingage_id_seq RESTART WITH 1')
    db.commit()
    
    with open('data/wgew_raingages.csv', 'r') as f:
        for i, l in enumerate(f.readlines()):
            if i > 0:
                values = l.strip().split('|')                
                watershed_d = values[0]
                gage_id = values[1]
                east = values[2]
                north = values[3]
                elevation = values[4]
                err = values[5]                
                lat, lng = utm_to_latlon(12, float(east), float(north))

                rg = WGEWRaingage(
                    watershed_id = watershed_d,
                    gage_id = gage_id,
                    east = east,
                    north = north,
                    latitude = lat,
                    longitude = lng,
                    elevation = elevation,
                    err = err
                )

                db.add(rg)
        db.commit()
    db.close()

if __name__ == '__main__':
    fire.Fire({
        'load_wgew_raingages': load_wgew_raingages,
        'load_wgew_precipevents': load_wgew_precipevents
    })