from sqlalchemy.orm import Session

from . import models, schemas

def get_wgew_raingages(db: Session):
    return db.query(models.WGEWRaingage).all()

def get_wgew_watershed_raingage(db: Session, wsid: int, gageid: int):
    print(wsid, gageid)
    return db.query(models.WGEWRaingage).filter(
            models.WGEWRaingage.watershed_id == wsid
        ).filter(
            models.WGEWRaingage.gage_id == gageid
        ).first()