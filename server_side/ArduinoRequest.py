from server_side import Const
from datetime import datetime

from server_side.db_handler import DBHandler


def set_fall(data):
    write_fall_to_db(**data)
    # alert to app


def set_heartbeat(data):
    data[Const.DATE_FIELD] = datetime.now()
    data[Const.NORMAL_FIELD] = 1
    write_heartbeat_to_db(**data)


def set_anomaly_heartbeat(data):
    data[Const.DATE_FIELD] = datetime.now()
    data[Const.NORMAL_FIELD] = 0
    write_heartbeat_to_db(**data)
    # alert to app


def write_fall_to_db(**fields):
    query = f"""INSERT INTO {Const.FALL_TABLE}
            ({Const.ARDUINO_ID_FIELD}, {Const.DATE_FIELD}, {Const.LATITUDE_FIELD}, {Const.LONGITUDE_FIELD}) VALUES 
            ({fields.get(Const.ARDUINO_ID_FIELD)}, {fields.get(Const.DATE_FIELD)}, {fields.get(Const.LATITUDE_FIELD)},
            {fields.get(Const.LONGITUDE_FIELD)});"""
    db = DBHandler()
    db.execute(query)


def write_heartbeat_to_db(**fields):
    query = f"""INSERT INTO {Const.FALL_TABLE}
            ({Const.ARDUINO_ID_FIELD}, {Const.DATE_FIELD},{Const.NORMAL_FIELD}) VALUES 
            ({fields.get(Const.ARDUINO_ID_FIELD)}, {fields.get(Const.DATE_FIELD)}, {fields.get(Const.NORMAL_FIELD)});"""
    db = DBHandler()
    db.execute(query)
