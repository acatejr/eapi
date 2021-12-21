import os, sys

from sqlalchemy.sql.elements import not_
from app import models
from app.database import SessionLocal, engine

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def delete_wgew_raingages():
    if db.query(models.WGEWRaingage.id).count() > 0:
        count = db.query(models.WGEWRaingage.id).count()
        print(f"Deleting {count} WGWEWRaingage records")
        db.query(models.WGEWRaingage).filter(models.WGEWRaingage.id > 0).delete()
        db.execute("ALTER SEQUENCE wgew_raingages_id_seq RESTART WITH 1")
        db.commit()


def load_wgew_raingages():
    
    row = 0
    with open(f"{BASE_DIR}/data/wgew/csv/raingages.csv") as f:        
        line = f.readline()
        while line:
            
            if row > 0:
                l = line.strip('\n')
                values = l.split('|')               
                ws_id = int(values[0])
                gage_id = int(values[1])
                east = int(values[2])
                north = int(values[3])
                elev = int(values[4])
                err = float(values[5])
                if ws_id == 63:
                    rec = models.WGEWRaingage(
                        watershed_id=ws_id,
                        gage_id=gage_id,
                        east=east,
                        north=north,
                        elevation=elev,
                        err=err
                    )
                    db.add(rec)                

            line = f.readline()
            row += 1

    if row > 0:
        db.commit()

def delete_wgew_precip_events():
    if db.query(models.WGEWPrecipEvent.id).count() > 0:
        count = db.query(models.WGEWPrecipEvent.id).count()
        print(f"Deleting {count} WGWEWPrecipEvent records")
        db.query(models.WGEWPrecipEvent).filter(models.WGEWPrecipEvent.id > 0).delete()
        db.execute("ALTER SEQUENCE wgew_precip_events_id_seq RESTART WITH 1")
        db.commit()

def load_wgew_precip_events():
    
    missing = []
    row = 0
    with open(f"{BASE_DIR}/data/wgew/csv/precip.csv") as f:        
        line = f.readline()
        ws_id = 63 # Walnut Gulch's unique id
        while line:
            
            if row > 0:
                l = line.strip()
                values = l.split('|')
                gage_id = int(values[0])
                event_date = values[1]
                event_time = values[2]
                duration = int(values[3])
                depth = float(values[4])
                time_est = values[5]

                # rg = db.query(models.WGEWRaingage).filter(models.WGEWRaingage.id.in_([gage_id])).first()
                # if rg:
                rec = models.WGEWPrecipEvent(
                    # gage_id=rg.gage_id,
                    # gage_id = rg.id,
                    gage_id=gage_id,
                    watershed_id=ws_id,
                    event_date=event_date,
                    event_time=event_time,
                    duration=duration,
                    depth=depth,
                    time_est=time_est
                )
                db.add(rec)
                # else:
                #    if gage_id not in missing:
                #       missing.append(gage_id)                    

            row += 1
            line = f.readline()

    if row > 0:
        db.commit()

    if missing and len(missing) > 0:
        print(missing)

delete_wgew_precip_events()
delete_wgew_raingages()
load_wgew_raingages()
load_wgew_precip_events()
db.close()

# [384, 386, 398, 399]