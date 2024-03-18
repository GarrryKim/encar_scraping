from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from pprint import pprint

# Create your views here.
def index(request):
    
    return render(request, 'encarscraper/index.html')


def search_cars(request):
    
    encar_url = 'http://api.encar.com/search/car/list/premium'
    
    param = {
            "count": "True",
            "q": "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.(C.ModelGroup.그랜저._.Model.그랜저 IG.))))",
            "sr": "|ModifiedDate|0|20"
        }

    response = requests.get(encar_url, params= param, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}).json()
    search_results = response['SearchResults']
    pprint(search_results)
    
    context = {
        
    }
    return render(request, 'encarscraper/soup.html', context)

