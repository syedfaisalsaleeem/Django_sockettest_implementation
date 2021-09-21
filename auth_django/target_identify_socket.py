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
def facebook_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("facebook"),'w') as f:
        json.dump(data,f,indent=4)
    print(data)
    # sio.disconnect()
        
@sio.event
def twitter_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("twitter"),'w') as f:
        json.dump(data,f,indent=4)
        
@sio.event
def instagram_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("instagram"),'w') as f:
        json.dump(data,f,indent=4)
    # sio.disconnect()

@sio.event
def reddit_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("reddit"),'w') as f:
        json.dump(data,f,indent=4)
        
@sio.event
def youtube_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("youtube"),'w') as f:
        json.dump(data,f,indent=4)
        
@sio.event
def linkedin_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("linkedin"),'w') as f:
        json.dump(data,f,indent=4)
        
@sio.event
def tiktok_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("tiktok"),'w') as f:
        json.dump(data,f,indent=4)
@sio.event
def tumblr_message(data):
    print('I received a message!')
    with open('{}_data.json'.format("tumblr"),'w') as f:
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

        try:
            sio.connect('http://192.168.18.240:8000',transports='polling')
        except:
            pass
        
    def message1(self):
        print("crawled")
        # sio.disconnect()
    
    def message2(self):
        print("crawled")
        # sio.disconnect()
    
    def get_target_data(self,target,query):
        data = [{}]
        try:
            sio.emit('message', {'social_media':target,"query":query},callback=self.message1)
            sio.wait()

            with open('{}_data.json'.format(target)) as f:
                data = json.load(f)
            
            print("--------- {} data crawled -----".format(target))     
            self.target_data = data
        except:
            self.target_data = []
        return data
        # if target == "facebook":
        #     try:
        #         sio.emit('message', {'social_media':target,"query":query},callback=self.message1)
        #         sio.wait()
    
        #         with open('{}_data.json'.format(target)) as f:
        #             data = json.load(f)
                
        #         print("--------- {} data crawled -----".format(target))     
        #         self.target_data = data
        #     except:
        #         self.target_data = []
        #     return data
        
        # elif target == "twitter":
        #     try:
        #         sio.emit('message'.format(target), {'social_media':target,"query":query},callback=self.message1)
        #         sio.wait()
        #         with open('{}_data.json'.format(target)) as f:
        #             data = json.load(f)
                
        #         print("--------- {} data crawled -----".format(target))     
        #         self.target_data = data
        #     except:
        #         self.target_data = []
        #     return data
    
    def create_new_json(self, target):
        with open('{}_data.json'.format(target),'w') as f:
            json.dump([{}],f,indent=4)
            
    def start_targetidentify(self,target,query):
        import threading
        d = threading.Thread(target=self.get_target_data,args=(target,query))
        d.start()
        d.join()
        # self.create_new_json(target)
        # data = self.get_target_data(target=target,query=query)
        return self.target_data
