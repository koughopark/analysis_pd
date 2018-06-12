from urllib.request import Request, urlopen
from datetime import *
import sys
import json


def print_error(e):
    print('%s %s' % (e, datetime.now()), file=sys.stderr)


# def html_request(url='', encoding='utf-8', success=None,
#                  error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
#     try:
#         request = Request(url)
#         resp = urlopen(request)
#         html = resp.read().decode(encoding)
#
#         print('%s : success for request[%s]' % (datetime.now(), url))
#
#         if callable(success) is False:
#             return html
#
#         success(html)
#
#     except Exception as e:
#         if callable(error) is True:
#             error(e)


def json_request(url='', encoding='utf-8', success=None,
                 error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)  # 리퀘스트 객체 생성
        resp = urlopen(request)  # 응답 받기
        resp_body = resp.read().decode(encoding)  # 응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함

        json_result = json.loads(resp_body)

        # print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

        return json_result


    except Exception as e:
        if callable(error) is True:
            error(e)
