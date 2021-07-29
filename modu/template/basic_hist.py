import random
# random.randint(1, 6)
# range(5)
import matplotlib.pyplot as plt

from modu.template import ChangedTemperaturesOnMyBirthday


def random_dice(count):
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(count)]
    return ls

def show_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()

def highest_temperature(month: str) -> []:
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    arr = []
    [arr.append(float(i[-1])) for i in birth.data if i[-1] != ''  if i[0].split('-')[1] == month]
    return arr

def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color = 'r', label=f'{month} Month')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    show_hist_about(highest_temperature('01'), month='01')