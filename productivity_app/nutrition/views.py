from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from pprint import pprint

import requests

# Create your views here.
def search_food(request):

    search_term = 'milk'  

    r = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?app_id={settings.EDAMAM_APP_ID}&app_key={settings.EDAMAM_API_KEY}&ingr={search_term}&nutrition-type=logging&calories=0-1000&category=generic-foods')
    foods = r.json()
    print('Status: {}'.format(r.status_code))

    return render(request, 'nutrition/food_list.html', {'foods': foods})