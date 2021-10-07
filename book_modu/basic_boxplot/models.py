import random

from modu.template import ChangedTemperaturesOnMyBirthday
from modu.template.basic_hist import highest_temperature
import matplotlib.pyplot as plt

class BasicBoxplot(object):

    def show_boxplot(month: str):
        arr = highest_temperature(month)
        plt.boxplot(arr)
        plt.show()


    def sorted_random_arr() -> []:
        arr = []
        [arr.append(random.randint(1, 1000)) for i in range(13)]
        return arr


    def show_boxplot_all_month():
        # arr = ChangedTemperaturesOnMyBirthday()
        # arr.read_data()
        # month_ls = []
        # [month_ls.append([]) for i in range(12)]
        # print(month_ls)
        # [month_ls[int(i[0].split('-')[1])-1].append(float(i[-1])) for i in arr.data if i[-1] != '']
        # plt.boxplot(month_ls)
        # plt.show()
        arr = []
        [arr.append(highest_temperature((str(i + 1)
                                         if len(str(i+1)) == 2
                                            else str('0'+str(i + 1)))))
                                                for i in range(12)]
        plt.boxplot([i for i in arr])
        plt.show()


    def show_boxplot_per_date():
        arr = ChangedTemperaturesOnMyBirthday()
        arr.read_data()
        date = []
        [date.append([]) for i in range(31)]
        [date[int(i[0].split('-')[2])-1].append(float(i[-1])) for i in arr.data if i[-1] != '' if i[0].split('-')[1] == '08']
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.boxplot(date, showfliers=False)
        plt.show()