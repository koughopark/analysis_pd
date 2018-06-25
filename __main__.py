import collect
import analyze
import visualize
import pandas as pd
from config import CONFIG
import matplotlib.pyplot as plt

if __name__ == '__main__':
    resultfiles = dict()

    # collect
    # crawling_tourspot_visitor 하기
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        **CONFIG['common']
    )
    # crawling_foreign_visitor 하기
    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

        # collect.crawling_tourspot_visitor('서울특별시', start_year=2017, end_year=2017)
        # for country in [('중국', 112), ('일본', 130), ('미국', 275)]:
        #     collect.crawling_foreign_visitor(country, start_year=2017, end_year=2017)

    # 1. analysis and visualize
    # result_analysis = analyze.analysis_correlation(resultfiles)
    # visualize.graph_scatter(result_analysis)

    # 2. analysis and visualize
    # 함수 만들어야됨됨
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    # print(result_analysis)
    #visualize.graph_scatter(result_analysis)

    graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tourspot')

    graph_table.plot(kind='bar')
    plt.show()

# tourspot r_중국 r_일본 r_미국
#  경복국   0.2    0.4    0.5
#   종묘    0.2    0.4    0.5
