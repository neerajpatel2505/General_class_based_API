from django.shortcuts import render

# Create your views here.
from api.models import Movie 
from api.serializers import MovieSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

class MovieList(APIView): 
    def get(self, request): 
        movies = Movie.objects.all() 
        serializer=MovieSerializer(movies,many=True) 
        return Response(serializer.data) 
    def post(self, request): 
        serializer=MovieSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

class MovieDetail(APIView): 
    def get(self, request,pk): 
        try: 
            movie=Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return Response({'error':'Detail not found'},status=status.HTTP_404_NOT_FOUND) 
        serializer = MovieSerializer(movie) 
        return Response(serializer.data) 
    def put(self,request,pk): 
        movie=Movie.objects.get(pk=pk) 
        serializer = MovieSerializer(movie,data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors) 
    def delete(self,request,pk): 
        movie=Movie.objects.get(pk=pk) 
        movie.delete() 
        return Response({'error':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)