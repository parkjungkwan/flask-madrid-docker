from book_modu.population.models \
    import Population, PopulationWithPandas

if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    pop.show_plot(pop.pop_per_dong('역삼2동'))

    pop2 = PopulationWithPandas()
    pop2.read_data()
    # name = input('인구구조가 알고 싶은 지역의 이름(읍면동 단위)를 입력해 주세요')
    pop2.find_home('필동')
    pop2.home = pop2.list_to_array(pop2.home)
    pop2.find_similar_area('필동')
    pop2.show_plot_similar_two_cities('필동', pop2.home, pop2.away)