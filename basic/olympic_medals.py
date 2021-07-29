import pandas
import pandas as pd


class Olympic(object):
    pass

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
        print(df)
        return df

if __name__ == '__main__':
    obj = Olympic()
    obj.read_wiki()