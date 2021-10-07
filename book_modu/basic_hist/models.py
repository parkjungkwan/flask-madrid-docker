import matplotlib.pyplot as plt
import random
import csv

class BasicHist(object):

    def hist_show(ls: []):
        plt.hist(ls, bins=6, color='lightpink')
        plt.show()


    def dice(n: int) -> []:
        ls = []
        [ls.append(random.randint(1, 6)) for i in range(n)]
        return ls


    def highest_temperature(month: str) -> []:
        # month = (str('0'+month) if len(month) == 1 else month)
        birth = ChangedTemperaturesOnMyBirthday()
        birth.read_data()
        mon = []
        [mon.append(float(i[-1])) for i in birth.data if i[-1] != '' if month == i[0].split('-')[1]]
        return mon


    def hist_show_many(ls):
        [plt.hist(i, bins=100) for i in ls]
        plt.show()


    def show_hist_about(arr: [], month: str):
        plt.hist(arr, bins=100, color='pink', label=month)
        plt.legend()
        plt.show()
