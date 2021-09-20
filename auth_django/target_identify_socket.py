import socketio
import json
sio = socketio.Client()

@sio.on('connect', namespace='/test')
def on_connect():
    print("I'm connected to the server")
    
@sio.event
def connect():
    print('[INFO] Successfully connected to server.')


@sio.event
def connect_error():
    print('[INFO] Failed to connect to server.')


@sio.event
def disconnect():
    print('[INFO] Disconnected from server.')
    
@sio.event
def message(data):
    print('I received a message!')
    with open('data.json','w') as f:
        json.dump(data,f,indent=4)

def message1():
    print("crawled")
    sio.disconnect()
                    
def get_target_data(target,query):
    try:
        sio.disconnect()
    except:
        pass
    sio.connect('http://192.168.18.240:8000')
    sio.emit('message', {'social_media':target,"query":query},callback=message1)
    sio.wait()
    print("data")
    with open('data.json') as f:
        data = json.load(f)
    
    print("--------- {} data crawled -----".format(target))     
    return data