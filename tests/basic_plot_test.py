import matplotlib.pyplot as plt
import unittest
import os

from book_modu.basic_plot.models import BasicPlot


class BasicPlotTest(object):

    instance = BasicPlot()

    """
    list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
    """
    def test_plot_show(self):
        plt.title("plotting")
        plt.plot([10, 20, 30, 40])
        plt.show()
    """
    첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
    """
    def plot_two_list_show(self):
        plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
        plt.show()

    def plot_marker(self):
        pass

    def scatter(self):
        pass

    def test_show_path(self):
        self.instance.show_path()


if __name__ == '__main__':
    unittest.main()
