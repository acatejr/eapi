import datetime
from datetime import timedelta

import pytest
from app.models import WGEWRaingage, WGEWPrecipEvent
from app.database import SessionLocal, engine

db = SessionLocal()

def test_create_raingage():
    wgew_rg = WGEWRaingage()
    db.add(wgew_rg)
    db.commit()
    rg = db.query(WGEWRaingage).filter_by(id=wgew_rg.id).first()
    assert rg.id == wgew_rg.id

def test_read_raingage():
    db.add(WGEWRaingage())
    db.commit()
    rg = db.query(WGEWRaingage).all()[0]
    assert rg is not None

def test_update_raingage():
    rg = WGEWRaingage()
    db.add(rg)
    db.commit()
    id = rg.id

    rg = db.query(WGEWRaingage).filter_by(id=id).first()
    rg.updated = datetime.datetime.utcnow()
    db.add(WGEWRaingage())
    db.commit()
    assert rg.updated is not None

def test_delete_raingage():
    rg = WGEWRaingage()
    db.add(rg)
    db.commit()

    target_id = rg.id
    db.query(WGEWRaingage).filter(WGEWRaingage.id == target_id).delete()
    target_rg = db.query(WGEWRaingage).filter_by(id=target_id).first()
    assert target_rg is None

def test_create_precip_event():
    wgew_pe = WGEWPrecipEvent()
    db.add(wgew_pe)
    db.commit()
    pe = db.query(WGEWPrecipEvent).filter_by(id=wgew_pe.id).first()
    assert pe.id == wgew_pe.id

def test_read_precip_event():
    pytest.fail("Implement me!")

def test_update_precip_event():
    pytest.fail("Implement me!")

def test_delete_precip_event():
    pytest.fail("Implement me!")


