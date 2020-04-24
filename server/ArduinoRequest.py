from server import Const
from datetime import datetime


def set_fall(data):
    user_id = data.get(Const.USER_ID)
    time = datetime.now()
    data[Const.TIME] = time
    loc = data.get(Const.FALL_LOC)
    write_fall_to_db(user_id, time, loc)
    # alert to app


def set_heartbeat(data):
    user_id = data.get(Const.USER_ID)
    time = datetime.now()
    val = data.get(Const.HEARTBEAT_VAL)
    write_heartbeat_to_db(user_id, time, val)


def set_anomaly_heartbeat(data):
    user_id = data.get(Const.USER_ID)
    time = datetime.now()
    val = data.get(Const.HEARTBEAT_VAL)
    write_heartbeat_to_db(user_id, time, val)
    # alert to app


def write_fall_to_db(user_id, fall_time, fall_location):
    query = f"""
    INSERT INTO {Const.FALL_TABLE} ({Const.USER_ID, Const.TIME, Const.FALL_LOC})
    VALUES 
       ({user_id},{fall_time}, {fall_location});
    """
    return query


def write_heartbeat_to_db(user_id, time, heartbeat_val):
    query = f"""
    INSERT INTO {Const.HEARTBEAT_TABLE} ({Const.USER_ID, Const.TIME, Const.HEARTBEAT_VAL})
    VALUES 
       ({user_id}, {time}, {heartbeat_val});
    """
    return query
