from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
# from rest_framework import permissions
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from . import models
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
import json
from django.http import HttpResponse
from .target_identify_socket import get_target_data,TargetIdentifySocialMedia
import threading
# import socketio
# sio = socketio.Client()

# @sio.on('connect', namespace='/test')
# def on_connect():
#     print("I'm connected to the server")
    
# @sio.event
# def connect():
#     print('[INFO] Successfully connected to server.')


# @sio.event
# def connect_error():
#     print('[INFO] Failed to connect to server.')


# @sio.event
# def disconnect():
#     print('[INFO] Disconnected from server.')
    
# data1 = ""
# import json

# @sio.event
# def message(data):
#     print('I received a message!')
#     print(data)
#     data1 = ""
#     data1 = data
#     # return data1
#     with open('data.json','w') as f:
#         json.dump(data,f,indent=4)
        
class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request, format=None):
        responseData = TargetIdentifySocialMedia().start_targetidentify(target="twitter",query="ali")
        
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get(self, request, format=None):
        responseData = TargetIdentifySocialMedia().start_targetidentify(target="facebook",query="faisal")
        # x = threading.Thread(target=get_target_data,args=("reddit","ali",))
        # x.start()
        # x.join()
        # print(x)
        # responseData = get_target_data(target="facebook",query="ali")
        # print(request)
        # def message1():
        #     print("crawled")
        #     sio.disconnect()
        # # pass
        # try:
        #     sio.disconnect()
        # except:
        #     pass
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"twitter","query":"ali"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- twitter data -----")     
        # print(w)
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"facebook","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- facebook data -----")    
        # print(w)
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"linkedin","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- linkedin data -----")    
        # print(w)
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"instagram","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- instagram data -----")    
        # print(w)
        
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"youtube","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- youtube data -----")    
        # print(w)
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"reddit","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- reddit data -----")    
        # print(w)
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"tiktok","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- tiktok data -----")    
        # print(w)
        
        # sio.connect('http://192.168.18.240:8000')
        # sio.emit('message', {'social_media':"tumblr","query":"faisal"},callback=message1)
        # sio.wait()
        # print("data")
        # with open('data.json') as f:
        #     w = json.load(f)
        
        # print("--------- tumblr data -----")    
        # print(w)
        
        # responseData = {
        # 'id': 4,
        # 'name': 'Test Response',
        # 'roles' : ['Admin','User']
        # }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        # return Response(serializer.data)

    def post(self, request, format=None):
        print(request)
        pass
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Example(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
    

# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def example_view1(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)