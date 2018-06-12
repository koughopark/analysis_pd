# facebook api Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

END_POINT = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
SERVICE_KEY = 'bpU9ConJZs44J4b%2FbIStu29uOgtlQ%2Fvl%2BMma1RXL5c2vz8Wdayhg33wAmEqn51Mf2loTqXUr%2BGI9QsfMdFjKXQ%3D%3D'


def pd_gen_url(endpoint= END_POINT, service_key = SERVICE_KEY, **params):
    url = '%s?serviceKey=%s&%s' % (endpoint, service_key, urlencode(params))
    print(url)
    return url


def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):

    url = pd_gen_url(endpoint=END_POINT,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     SIDO=district1,
                     GUNGU=district2,
                     RES_NM='',
                     numOfRows=10,
                     _type='json'
                     )
    # print(district1)
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        pos = None if json_result is None else json_result.get('response').get('body').get('items')
        posts = None if json_result is None else json_result.get('response').get('body').get('items').get('item')

        url = None if posts is None else pos.get("totalCount")
        isnext = url is not None
        yield posts

    # json_result = json_request(url=url)
    # return json_result.get('response').get('body').get('items').get('item')


