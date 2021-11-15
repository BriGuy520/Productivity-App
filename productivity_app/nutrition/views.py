from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from pprint import pprint

import requests

# Create your views here.
def search_food(request):
  

  r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?api_key=' + settings.API_KEY)
  foods = r.json()
  print('Status: {}'.format(r.status_code))
  
  return render(request, 'nutrition/food_list.html', {'foods': foods})

    

