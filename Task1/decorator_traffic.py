def traffic_signal(func):
    def wrapper(signal):
        if signal == 'RED':
            print('RED : STOP')
        elif signal == 'YELLOW':
            print('YELLOW : SLOW DOWN')
        elif signal == 'GREEN':
            print('GREEN : GO')
        else:
            print('Invalid signal')
        func(signal)
    return wrapper

@traffic_signal
def message(signal):
    pass

message('RED')
message('YELLOW')
message('GREEN')

