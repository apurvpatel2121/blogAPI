from django.shortcuts import render
from rest_framework.response import Resonse
from rest_framework.views import APIView
from rest_framework import status
from posts.models import *
from rest_framework import permissions
from posts.serializers import *
# Create your views here.



class PostListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        data = {
            'user': request.user.id,
            'title': request.data.get('title'),
            'body': request.data.get('body')
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(data=posts,many=True)
        return Resonse(serializer.data,status=status.HTTP_200_OK)
    
class PostDetailView(APIView):
    permissions = [permissions.IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except:
            return None
        
    def get(self,request,pk,*args,**kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response({'errors':'Post not found!'},status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(data=post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,*args,**kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response({'errors':'Post not found!'},status=status.HTTP_404_NOT_FOUND)
        data = {
            'user':request.user.id,
            'title':request.data.get('title'),
            'body':request.data.get('body'),
            'upvote_count':post.upvote_count
        }
        
        serializer = PostSerializer(post,data=data,partial=True)
        
        pass
        