import socketio
import json
import threading
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
def user_disconnected(data):
    print("this is disconnected")
    print(data)
    sio.disconnect()
        
@sio.event
def message(data):
    print('I received a message!')
    with open('data.json','w') as f:
        json.dump(data,f,indent=4)


                    
def get_target_data(target,query):
    
    sio.disconnect()
    sio.connect('http://192.168.18.240:8000')
    sio.emit('message', {'social_media':target,"query":query},callback=message1)
    sio.wait()
    print("data")
    with open('data.json') as f:
        data = json.load(f)
    
    print("--------- {} data crawled -----".format(target))     
    return data

import time
class TargetIdentifySocialMedia():
    def __init__(self):
        self.target_data = []

        sio.disconnect()
        time.sleep(3)
        sio.connect('http://192.168.18.240:8000',transports='polling')
    
    def message1(self):
        print("crawled")
        sio.disconnect()
    
    def get_target_data(self,target,query):
        try:
            sio.emit('message_{}'.format(target), {'social_media':target,"query":query},callback=self.message1)
            sio.wait()
            with open('data.json') as f:
                data = json.load(f)
            
            print("--------- {} data crawled -----".format(target))     
            self.target_data = data
        except:
            self.target_data = []
        return data
    
    def create_new_json(self):
        with open('data.json','w') as f:
            json.dump([{}],f,indent=4)
            
    def start_targetidentify(self,target,query):
        self.create_new_json()
        data = self.get_target_data(target=target,query=query)
        return data
