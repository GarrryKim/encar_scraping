import requests
from pprint import pprint
from bs4 import BeautifulSoup

def request_json():
    
    encar_url = 'http://api.encar.com/search/car/list/premium'
    param = {
            "count": "True",
            "q": "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.르노코리아(삼성_)._.(C.ModelGroup.SM6._.Model.SM6.))))",
            "sr": "|ModifiedDate|0|20"
        }

    response = requests.get(encar_url, params= param, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}).json()
    
    return response


def get_id():
    json_data = request_json()
    search_results = json_data['SearchResults']
    info_list = []
    for result in search_results:
        
        car_info = {
            'Id': result['Id'],
            'Manufacturer': result['Manufacturer'],
            'Model': result['Model']+' '+result['Badge']+' '+result['FuelType'],
        }
        
        info_list.append(car_info)
    pprint(info_list)
    return info_list


def get_product_results():
    
    car_ids = get_id()
    
    for id in car_ids:
        detail_url = f'http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=normal&carid={id}'
        html = requests.get(url = detail_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
        soup = BeautifulSoup(html.text, "html.parser")
        element = soup.select('body > div.container > div.body > div > div.section.sample > div.rreport > div.summary > p')
        break
    return

get_product_results()


