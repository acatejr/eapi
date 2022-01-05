from sqlalchemy.orm import Session

from . import models, schemas

def get_wgew_raingages(db: Session):
    return db.query(models.WGEWRaingage).all()

def get_wgew_watershed_raingage(db: Session, wsid: int, gageid: int):

    return db.query(models.WGEWRaingage).filter(
            models.WGEWRaingage.watershed_id == wsid
        ).filter(
            models.WGEWRaingage.gage_id == gageid
        ).first()

def get_wgew_watershed_gage_precip(db: Session, wsid: int, gageid: int):
    """Retrieve all precip events for given watershed and raingage.
    """

    return db.query(models.WGEWPrecipEvent).filter(
            models.WGEWPrecipEvent.gage_id == gageid
        ).filter(
            models.WGEWPrecipEvent.watershed_id == wsid
        ).all()
