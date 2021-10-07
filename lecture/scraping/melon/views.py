from lecture.scraping.melon.models import Melon

if __name__ == '__main__':
    melon = Melon('https://www.melon.com/chart/index.htm?dayTime=2021072016')
    melon.scrap()