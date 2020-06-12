from server_side import Const, ArduinoRequest as Ard, AppRequest as App

PROTOCOL_DICT = {Const.GET_HEARTBEAT: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD],
                 Const.SET_HEARTBEAT: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD, Const.HEARTBEAT_VAL],
                 Const.SET_ANOMALY_HEARTBEAT: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD, Const.HEARTBEAT_VAL],
                 Const.GET_HEARTBEAT_HISTORY: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD],
                 Const.GET_LAST_FALL: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD],
                 Const.SET_LAST_FALL: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD, Const.LATITUDE_FIELD,
                                       Const.LONGITUDE_FIELD, Const.DATE_FIELD],
                 Const.GET_FALL_HISTORY: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD],
                 Const.ADD_ARDUINO: [Const.REQUEST_TYPE, Const.ARDUINO_ID_FIELD, Const.AGE_FIELD],
                 Const.ADD_USER: [Const.REQUEST_TYPE, Const.NAME_FIELD, Const.EMAIL_FIELD,
                                  Const.PHONE_FIELD, Const.ARDUINO_ID_FIELD,
                                  Const.PASSWORD_FIELD],
                 Const.SIGN_IN: [Const.REQUEST_TYPE, Const.EMAIL_FIELD, Const.PASSWORD_FIELD]
                 }

FUNCTION_BY_PROTOCOL = {Const.GET_HEARTBEAT: App.get_heartbeat,
                        Const.SET_HEARTBEAT: Ard.set_heartbeat,
                        Const.SET_ANOMALY_HEARTBEAT: Ard.set_anomaly_heartbeat,
                        Const.GET_HEARTBEAT_HISTORY: App.get_heartbeat_history,
                        Const.GET_LAST_FALL: App.get_fall,
                        Const.SET_LAST_FALL: Ard.set_fall,
                        Const.GET_FALL_HISTORY: App.get_fall_history,
                        Const.ADD_USER: App.register_user,
                        Const.ADD_ARDUINO: App.register_arduino,
                        Const.SIGN_IN: App.signin_user
                        }


def parse_data(msg):
    data = msg.decode('utf-8').split(Const.DELIMETER)  # msg = "setHeartbeat 100 180" -> data = ['setHeartbeat', '100', '180']
    protocol_fields = PROTOCOL_DICT.get(data[0], Const.NOT_FOUND)  # PROTOCOL_DICT['setHeartbeat'] = ['protocol_type', 'user_id', 'heartbeat_val']
    if protocol_fields != Const.NOT_FOUND and len(data) == len(protocol_fields):
        return get_dict_by_protocol(data, protocol_fields)


def get_dict_by_protocol(data, protocol):
    return dict(zip(protocol, data))  # [('protocol_type', 'setHeartbeat'), ('user_id', '100'), ('heartbeat','180')]
    # {'protocol_type': 'setHeartbeat', 'user_id': '100' ....}


def handle_request(msg):  # msg = "setHeartbeat 100 180"
    data = parse_data(msg)  # data = {'user_id': 100, 'protocol': Const.SET_HEARTBEAT, 'val': 180}
    protocol_type = data.get(Const.REQUEST_TYPE)
    return FUNCTION_BY_PROTOCOL[protocol_type](data)
