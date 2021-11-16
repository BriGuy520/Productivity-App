from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

from pprint import pprint

import requests

# Create your views here.
def search_food(request):

    search_term = 'cheddar cheese'  

    r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + settings.API_KEY + '&query=' + search_term)
    foods = r.json()
    print('Status: {}'.format(r.status_code))

    return render(request, 'nutrition/food_list.html', {'foods': foods})