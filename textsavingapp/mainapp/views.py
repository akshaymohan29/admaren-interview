from django.shortcuts import render
from .serializer import TextSnippetSerializer,TagsSerializer
from rest_framework.views import APIView
from rest_framework import  status
from rest_framework.response import Response
from .models import User,Text_Snippet,Tags
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create To Display All.

class SnippetOverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        text_snippets = Text_Snippet.objects.all()
        text_count = text_snippets.count()
        print(text_snippets,request.user)
        serializer = TextSnippetSerializer(text_snippets,many =True)
        response_data = {
            'total_count': text_count,
            'snippets': serializer.data
        }
        return Response(response_data)

# Create Api 

class CreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        data['created_user'] = request.user.id  
        print(data)
        serializer = TextSnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
# Details Api
    
class DetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request ,id ):
        print(id)
        details = Text_Snippet.objects.get(id=id)
        serializer = TextSnippetSerializer(details)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Update Api
 
class UpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            snippet = Text_Snippet.objects.get(id=id)
        except Text_Snippet.DoesNotExist:
            return Response({'detail': 'data not found.'}, status=status.HTTP_404_NOT_FOUND)

        if snippet.created_user != request.user:
            raise PermissionDenied("You are not allowed to update .")

        data = request.data
        serializer = TextSnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Api
   
class DeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            snippet = Text_Snippet.objects.get(id=id)
        except Text_Snippet.DoesNotExist:
            return Response({'detail': 'Snippet not found.'}, status=status.HTTP_404_NOT_FOUND)

        snippet.delete()

        response_data = {
            'message': 'Snippet deleted successfully.',
            'id': id
        }

        return Response(response_data, status=status.HTTP_200_OK)  

# Tag List Api 
 
class TagListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tags = Tags.objects.all()
        serializer = TagsSerializer(tags, many=True)
        return Response(serializer.data)     

# Tag Detail Api
 
class TagDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        print('hediuewdi')
        try:
            tag = Tags.objects.get(id=id)
        except Tags.DoesNotExist:
            return Response({'detail': 'Tag not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        snippets = Text_Snippet.objects.filter(tags=tag)
        serializer = TextSnippetSerializer(snippets, many=True)
        return Response(serializer.data)   