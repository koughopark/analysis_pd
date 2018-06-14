import collect

if __name__ == '__main__':

    # collect

    # collect.crawling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)
    for country in [('중국', 112), ('일본', 130), ('미국', 275)]:
        collect.crawling_foreign_visitor(country, start_year=2017, end_year=2017)

    # analysis

    # visualize

