import os, sys
from app import models
from app.database import SessionLocal, engine

db = SessionLocal()
models.Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def load_wgew_raingages():

    if db.query(models.WGEWRaingage.id).count() > 0:
        count = db.query(models.WGEWRaingage.id).count()
        print(f"Deleting {count} WGWEWRaingage records")
        db.query(models.WGEWRaingage).filter(models.WGEWRaingage.id > 0).delete()
        db.execute("ALTER SEQUENCE wgew_raingages_id_seq RESTART WITH 1")
        db.commit()

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

load_wgew_raingages()
db.close()


# watershed_id|gage_id|east|north|elevation|err ['watershed_id', 'gage_id', 'east', 'north', 'elevation', 'err']
# 63|1|580177|3510850|1222|9 ['63', '1', '580177', '3510850', '1222', '9']
# 63|2|581187|3512053|1254|9 ['63', '2', '581187', '3512053', '1254', '9']
# 63|3|581204|3509768|1246|18 ['63', '3', '581204', '3509768', '1246', '18']
# 63|4|582932|3512517|1278|8.7 ['63', '4', '582932', '3512517', '1278', '8.7']
