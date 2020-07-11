from server_side import Const
from server_side.db_handler import DBHandler


def register_user(data):
    pk = insert_new_user(**data)
    data['pk'] = pk
    insert_new_user_credentials(**data)


def signin_user(data):
    user_id = check_user_credentials(**data)
    user_data = get_user_data(user_id)
    return _format_user_data(user_data)


def _format_user_data(user_data):
    return f"{user_data.get(Const.NAME_FIELD,'')} {user_data.get(Const.ARDUINO_ID_FIELD,'')}"


def register_arduino(data):
    insert_new_arduino(**data)


def get_heartbeat(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    #return get_pulse_data_for_user_from_db(user_id, 1)
    return '180'


def get_heartbeat_history(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_pulse_data_for_user_from_db(user_id)


def get_fall(data):
    user_id = data.get(Const.ARDUINO_ID_FIELD)
    return get_fall_data_for_user_from_db(user_id, 1)


# --------------- getting history db functions: -------------------

def get_fall_history(data):
    # user_id = data.get(Const.ARDUINO_ID_FIELD)
    # return get_fall_data_for_user_from_db(user_id)
    return 180


def get_fall_data_for_user_from_db(user_id, limit=None):
    query = f"""select * from {Const.FALL_TABLE} 
                where {Const.ARDUINO_ID_FIELD} = {user_id} 
                order by {Const.DATE_FIELD} desc"""
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
    query = f"""INSERT INTO {Const.PASS_TABLE}(pk, {Const.EMAIL_FIELD},{Const.PASSWORD_FIELD}) 
            VALUES ({fields.get('pk')}, '{fields.get(Const.EMAIL_FIELD)}','{fields.get(Const.PASSWORD_FIELD)}');"""
    db = DBHandler()
    db.execute(query)


def insert_new_user(**fields):
    query = f"INSERT INTO {Const.USER_TABLE} ({Const.EMAIL_FIELD},{Const.ARDUINO_ID_FIELD}, " \
            f"{Const.NAME_FIELD},{Const.PHONE_FIELD}) " \
            f"VALUES ('{fields.get(Const.EMAIL_FIELD)}','{fields.get(Const.ARDUINO_ID_FIELD)}', " \
            f"'{fields.get(Const.NAME_FIELD)}', '{fields.get(Const.PHONE_FIELD)}');"
    db = DBHandler()
    db.execute(query)
    get_pk_query = "SELECT LAST_INSERT_ID() as pk;"
    pk = db.getData(get_pk_query)
    return pk.pk.values[0]


def insert_new_arduino(**fields):
    query = f"""INSERT INTO {Const.ARDUINO_USER_TABLE}
            ({Const.ARDUINO_ID_FIELD}, {Const.NAME_FIELD}, {Const.AGE_FIELD}) VALUES 
            ('{fields.get(Const.ARDUINO_ID_FIELD)}', '{fields.get(Const.NAME_FIELD)}', 
            '{fields.get(Const.AGE_FIELD)}');"""
    db = DBHandler()
    db.execute(query)


def check_user_credentials(**fields):
    query = f"""Select pk FROM {Const.PASS_TABLE} WHERE  '{fields.get(Const.EMAIL_FIELD)}' = {Const.EMAIL_FIELD}
                        and {Const.PASSWORD_FIELD} = '{fields.get(Const.PASSWORD_FIELD)}'
            ;"""
    db = DBHandler()
    user_data = db.getData(query)
    if user_data.empty:
        return -1
    else:
        return user_data.pk.values[0]  # assuming unique emails


def get_user_data(user_id):
    query = f"""Select * FROM {Const.USER_TABLE} WHERE  {Const.USER_ID_FIELD} = {user_id}
            ;"""
    db = DBHandler()
    user_data = db.getData(query)
    if user_data.empty:
        return -1
    else:
        return user_data.iloc[0]  # assuming unique users
