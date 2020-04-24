from server import Const


def get_heartbeat(data):
    pass


def get_heartbeat_history(data):
    pass


def get_fall(data):
    user_id = data.get(Const.USER_ID)
    get_fall_data_for_user_from_db(user_id, 1)
    pass


def get_fall_history(data):
    user_id = data.get(Const.USER_ID)
    get_fall_data_for_user_from_db(user_id)
    pass


def get_fall_data_for_user_from_db(user_id, limit=None):
    query = f"""select * from {Const.FALL_TABLE} where {Const.USER_ID} = {user_id} """
    if limit:
        query += f" limit {limit}"

    # return results