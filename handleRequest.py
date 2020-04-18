import ArduinoRequest as ard
import AppRequest as app

TYPE = 'protocol_type'
USER = 'user_id'


PROTOCOL_DICT = {'getHeartbeat': [TYPE, USER],
                 'setHeartbeat': [TYPE, USER, 'heartbeat'],
                 'getHeartbeatHistory': [TYPE, USER],
                 'getFall': [TYPE, USER],
                 'setFall': [TYPE, USER, 'fall_location', 'fall_time'],
                 'getFallHistory': [TYPE, USER]
                 }

FUNCION_BY_PROTOCOL = {'getHeartbeat': app.getHeartbeat,
                       'setHeartbeat': ard.setHeartbeat,
                       'getHeartbeatHistory': app.getHeartbeatHistory,
                       'getFall': app.getFall,
                       'setFall': ard.setFall,
                       'getFallHistory': app.getFallHistory
                       }


def parse_data(msg):
    data = msg.split()  # msg = "setHeartbeat 100 180" -> data = ['setHeartbeat', '100', '180']
    protocol_fields = PROTOCOL_DICT[
        data[0]]  # PROTOCOL_DICT['setHeartbeat'] = ['protocol_type', 'user_id', 'heartbeat']
    return get_dict_by_protocol(data, protocol_fields)


def get_dict_by_protocol(data, protocol):
    return dict(zip(protocol, data))  # [('protocol_type', 'setHeartbeat'), ('user_id', '100'), ('heartbeat','180')]


def handle_request(msg):
    data = parse_data(msg)
    protocol_type = data.get(TYPE)
    return FUNCION_BY_PROTOCOL[protocol_type](data)
