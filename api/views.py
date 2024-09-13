from rest_framework.views import APIView
from django.contrib.auth.models import User
from . import serializer
from rest_framework.response import Response

class UserApiView( APIView):
    def get(self, request):
        all_users = User.objects.all() #queryset (object)
        # to cover in json we will use serializer
        serialized = serializer.UserSerializer(all_users, many=True)
        return Response( data = serialized.data)
    
    def post(self, request):
        # get data from request and serialize it
        sr = serializer.UserCreateSerializer(data = request.data )

        if sr.is_valid():
            # if serialized data id valid save
            sr.save()
            return Response( data = {"details": "user created successfully"} )
        else:
            # if validation fails return response with error messages returned by serializer
            return Response(data= sr.errors)



class GetUserFromId(APIView):

    def get(self, request, id):
        # get user with id

        try:
            user = User.objects.get(id=id)
        except: 
            user = None

        # we have two case user exits with id and does not exist
        if user is None:
            # user does not exist
            return Response( data = {"details": f"user not found with give id {id}"} )
        else:
            # user exists
            # serialize user  ( convert from queryset to json)\
            sr = serializer.UserSerializer(user) #no need to mention many=True as single user will be returned
            return Response(data = sr.data )