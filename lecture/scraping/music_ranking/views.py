from lecture.menu.models import print_menu
from lecture.scraping.music_ranking.models import MusicRanking

if __name__ == '__main__':
    # 20210720
    # 16
    musicRanking = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        # 0- exit, 1- Bugs (URL), 2- Melon (URL) 3- output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            musicRanking.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            musicRanking.query_string = 'chartdate=20210721&charthour=09'
            musicRanking.set_html()
        elif menu == 2:
            musicRanking.tag_name = 'p'
            musicRanking.class_name.append('artist')
            musicRanking.class_name.append('title')
            musicRanking.get_raking()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass