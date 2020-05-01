from server_side import Const
from server_side.db_handler import DBHandler


def register_user(data):
    insert_new_user_credentials(**data)
    insert_new_user(**data)


def register_Arduino(data):
    insert_new_arduino(**data)


def get_heartbeat(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_pulse_data_for_user_from_db(user_id, 1)


def get_heartbeat_history(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_pulse_data_for_user_from_db(user_id)


def get_fall(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_fall_data_for_user_from_db(user_id, 1)


# --------------- getting history db functions: -------------------

def get_fall_history(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_fall_data_for_user_from_db(user_id)


def get_fall_data_for_user_from_db(user_id, limit=None):
    query = f"""select * from {Const.FALL_TABLE} 
                where {Const.ARDUINO_ID_FIELD} = {user_id} 
                order by {Const.DATE_FIELD} asc"""
    if limit:
        query += f" limit {limit}"

    db = DBHandler()
    return db.getData(query)


def get_pulse_data_for_user_from_db(user_id, limit=None):
    query = f"""select * from {Const.FALL_TABLE} 
                where {Const.ARDUINO_ID_FIELD} = {user_id} 
                order by {Const.DATE_FIELD} asc"""
    if limit:
        query += f" limit {limit}"

    db = DBHandler()
    return db.getData(query)


# --------------- user-related db functions: -------------------

def insert_new_user_credentials(**fields):
    query = f"""INSERT INTO {Const.PASS_TABLE}({Const.EMAIL_FIELD},{Const.PASSWORD_FIELD}) 
            VALUES ({fields.get(Const.EMAIL_FIELD)},{fields.get(Const.PASSWORD_FIELD)});"""
    db = DBHandler()
    db.execute(query)


def insert_new_user(**fields):
    query = f"""INSERT INTO {Const.USER_TABLE}
                            ({Const.EMAIL_FIELD},{Const.ARDUINO_ID_FIELD}, {Const.NAME_FIELD},{Const.PHONE_FIELD}) 
            VALUES ({fields.get(Const.EMAIL_FIELD)},{fields.get(Const.ARDUINO_ID_FIELD)}, 
                    {fields.get(Const.NAME_FIELD)}, {fields.get(Const.PHONE_FIELD)});"""
    db = DBHandler()
    db.execute(query)


def insert_new_arduino(**fields):
    query = f"""INSERT INTO {Const.ARDUINO_USER_TABLE}
            ({Const.ARDUINO_ID_FIELD}, {Const.NAME_FIELD}, {Const.AGE_FIELD}) VALUES 
            ({fields.get(Const.ARDUINO_ID_FIELD)}, {fields.get(Const.NAME_FIELD)}, {fields.get(Const.AGE_FIELD)});"""
    db = DBHandler()
    db.execute(query)
