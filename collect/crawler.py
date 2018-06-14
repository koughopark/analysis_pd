from .api import api
import os
import json
from analysis_pd.collect.api import api

RESULT_DIRECTORY = '__results__/crawling'

pagename = 'jtbcnews'
since = '2016-01-01'
until = '2017-04-31'


# url = fb_gen_url(endpoint=END_POINT, service_key=SERVICE_KEY,
#                   resultCode='',
#                   resultMsg='',
#                   numOfRows='',
#                   pageNo='',
#                   totalCount='',
#                   addrCd='',
#                   csForCnt='',
#                   scNatCnt='',
#                   gungu='',
#                   resNm='',
#                   sido='',
#                   ym='')

def pd_gen_url(endpoint, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), SERVICE_KEY)
    return url


# ------------------------------------------------------
def preprocess_tourspot_visitor(item):
    pass


def preprocess_foreign_visitor(data):
    # ed
    del data['ed']

    # edCd
    del data['edCd']

    # rnum
    del data['rnum']

    # 나라코드
    data['conutry_code'] = data['natCd']
    del data['natCd']

    # 나라이름
    data['conutry_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    # 방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년월
    if 'ym' not in data:
        data['data'] = ''
    else:
        data['data'] = data['ym']
        del data['ym']


def crawling_foreign_visitor(country, start_year, end_year):
    result = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            data = api.pd_fetch_foreign_visitor(country[1], year, month)
            if data is None:
                continue

            preprocess_foreign_visitor(data)
            result.append(data)

    # save data to file
    filename = '%s/%s(%s)_crawling_foreign_visitor_%s_%s.json' % (
        RESULT_DIRECTORY, country[0], country[1], start_year, end_year)

    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(result, indent=4, sort_keys=True,
                                 ensure_ascii=False)  # json str으로 덤프하는 과정 텝을 4정도 주고 솔팅을 해라 모두 아스키코드로 해라
        outfile.write(json_string)


if os.path.exists(RESULT_DIRECTORY) is False:  # import될때 실행됨
    os.makedirs(RESULT_DIRECTORY)  # 첫번째 디렉토리가 없으면 하나의 디렉토리가 생성됨


def crawling_tourspot_visitor(district, start_year, end_year):
    results = []
    filename = '%s/%s_%s_%s.json' % (RESULT_DIRECTORY, 'crawling_tourspot_visitor', since, until)

    for i in range(start_year, end_year):
        for j in range(1, 12):
            for items in pd_fetch_tourspot_visitor():
                for item in items:  # 10개의 개별 data를 전처리해주기 위한 과정
                    preprocess_tourspot_visitor(item)

                results += items  # 전처리 된 data가 쌓임

    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True,
                                 ensure_ascii=False)  # json str으로 덤프하는 과정 텝을 4정도 주고 솔팅을 해라 모두 아스키코드로 해라
        outfile.write(json_string)


if os.path.exists(RESULT_DIRECTORY) is False:  # import될때 실행됨
    os.makedirs(RESULT_DIRECTORY)  # 첫번째 디렉토리가 없으면 하나의 디렉토리가 생성됨
