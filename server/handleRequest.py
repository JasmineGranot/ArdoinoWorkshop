from server import Const, ArduinoRequest as Ard, AppRequest as App

PROTOCOL_DICT = {Const.GET_HEARTBEAT: [Const.REQUEST_TYPE, Const.USER_ID],
                 Const.SET_HEARTBEAT: [Const.REQUEST_TYPE, Const.USER_ID, Const.HEARTBEAT_VAL],
                 Const.GET_HEARTBEAT_HISTORY: [Const.REQUEST_TYPE, Const.USER_ID],
                 Const.GET_LAST_FALL: [Const.REQUEST_TYPE, Const.USER_ID],
                 Const.SET_LAST_FALL: [Const.REQUEST_TYPE, Const.USER_ID, Const.FALL_LOC, Const.TIME],
                 Const.GET_FALL_HISTORY: [Const.REQUEST_TYPE, Const.USER_ID]
                 }

FUNCTION_BY_PROTOCOL = {Const.GET_HEARTBEAT: App.get_heartbeat,
                        Const.SET_HEARTBEAT: Ard.set_heartbeat,
                        Const.GET_HEARTBEAT_HISTORY: App.get_heartbeat_history,
                        Const.GET_LAST_FALL: App.get_fall,
                        Const.SET_LAST_FALL: Ard.set_fall,
                        Const.GET_FALL_HISTORY: App.get_fall_history
                        }


def parse_data(msg):
    data = msg.split()  # msg = "setHeartbeat 100 180" -> data = ['setHeartbeat', '100', '180']
    protocol_fields = PROTOCOL_DICT[
        data[0]]  # PROTOCOL_DICT['setHeartbeat'] = ['protocol_type', 'user_id', 'heartbeat']
    return get_dict_by_protocol(data, protocol_fields)


def get_dict_by_protocol(data, protocol):
    return dict(zip(protocol, data))  # [('protocol_type', 'setHeartbeat'), ('user_id', '100'), ('heartbeat','180')]
                                      # {'protocol_type': 'setHeartbeat', 'user_id': '100' ....}


def handle_request(msg):  # msg = "setHeartbeat 100 180"
    data = parse_data(msg)  # data = {'user_id': 100, 'protocol': Const.SET_HEARTBEAT, 'val': 180}
    protocol_type = data.get(Const.REQUEST_TYPE)
    return FUNCTION_BY_PROTOCOL[protocol_type](data)
