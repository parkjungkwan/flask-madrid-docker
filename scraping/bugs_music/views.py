from menu.models import print_menu
from scraping.bugs_music.models import MusicRanking

if __name__ == '__main__':
    # 20210720
    # 16
    mr = MusicRanking()
    while 1:
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict To Dataframe', 'Dataframe to CSV'])
        # 0- exit, 1- Bugs (URL), 2- Melon (URL) 3- output, 4-print dict,
        # 5-dict to dataframe, 6-df to csv
        if menu == 0:
            break
        elif menu == 1:
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=09'
            mr.set_html()
        elif menu == 2:
            mr.tag_name = 'p'
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_raking()
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass