from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
import json


# Create your views here.
def test(request):
    return render('<h1>ahahhahaha</h1>')


@api_view(["GET"])
@csrf_exempt
def welcome(request):
    content = {"message": "Test works"}
    return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
def get_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    if books:
        content = {'status': '200', "message": "Books found", 'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error', "message": "Books not found", 'data': 0}
        return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
def get_all_authors(request):
    author = Author.objects.all()
    serializer = AuthorSerializer(author, many=True)
    if author:
        content = {'status': '200', "message": "Authors found", 'data': serializer.data}
        return JsonResponse(content)
    else:
        content = {'status': 'error', "message": "Authors not found", 'data': 0}
        return JsonResponse(content)
