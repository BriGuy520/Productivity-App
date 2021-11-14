from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

import requests

# Create your views here.
def search_food(request):
  
  response = requests.get('https://www.foodrepo.org/api/v3')

  return JsonResponse(response.json())

