from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request



SERVICE_KEY = 'bpU9ConJZs44J4b%2FbIStu29uOgtlQ%2Fvl%2BMma1RXL5c2vz8Wdayhg33wAmEqn51Mf2loTqXUr%2BGI9QsfMdFjKXQ%3D%3D'


def pd_gen_url(endpoint, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), SERVICE_KEY)
    return url


def pd_fetch_foreign_visitor(country_code, year, month):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(
        endpoint,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        ED_CD='E',
        _type='json'
        )
    json_result = json_request(url=url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None



def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0): # 위에 형식처럼 고쳐보장
    endpoint = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
    url = pd_gen_url(endpoint,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     SIDO=district1,
                     GUNGU=district2,
                     tourspot='',
                     RES_NM='',
                     numOfRows=10,
                     pageNo='',
                     _type='json',
                     )

    isnext = True
    while isnext is True:
        json_result = json_request(url)

        item = None if json_result is None else json_result.get('response').get('body').get('items').get('item')

        isnext = None if json_result.get('response').get('body').get('items').get('item') is None else json_result.get('response').get('body').get('pageNo')+1
        if isnext is None:
            break

        yield item

    # json_result = json_request(url=url)
    # return json_result.get('response').get('body').get('items').get('item')
