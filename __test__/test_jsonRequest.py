from analysis_pd.collect.api import web_request as wr

url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList?serviceKey=bpU9ConJZs44J4b%2FbIStu29uOgtlQ%2Fvl%2BMma1RXL5c2vz8Wdayhg33wAmEqn51Mf2loTqXUr%2BGI9QsfMdFjKXQ%3D%3D&YM=201701&SIDO=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&GUNGU=&RES_NM=&numOfRows=10&_type=json&pageNo=1'

def success_fetch_user_list(response):
    print(response)

def error_fetch_user(e):
    print(e)


wr.json_request(url=url, success=success_fetch_user_list, error=error_fetch_user)

'''
json_result = wr.json_request(url)
print(json_result)
'''

# https://graph.facebook.com/v3.0/jtbcnews/posts/?access_token=(토큰을 넣어라 가로도 지우고)&since=20170101&untill=20171231&limit=50