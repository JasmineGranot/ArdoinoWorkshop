from server_side import Const
from server_side.db_handler import DBHandler


def register_user(data):
    pass


def get_heartbeat(data):
    print(f"got heartbeat data")


def get_heartbeat_history(data):
    print(f"got heartbeat history data")


def get_fall(data):
    user_id = data.get(Const.USER_ID)
    get_fall_data_for_user_from_db(user_id, 1)
    pass


def get_fall_history(data):
    user_id = data.get(Const.USER_ID)
    get_fall_data_for_user_from_db(user_id)


def get_fall_data_for_user_from_db(user_id, limit=None):
    query = f"""select * from {Const.FALL_TABLE} where {Const.ARDUINO_ID} = {user_id} """
    if limit:
        query += f" limit {limit}"

    db = DBHandler()
    data = db.execute(query)
    print(f"got fall data")

    # return results
