
import matplotlib.pyplot as plt
import numpy as np
from django.http import response
from django.shortcuts import render


def test_matplotlib(response):
    t = np.arange(1.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)
    plt.plot(t, s)
    # plt.bar(t, s)

    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.title('testing')
    plt.savefig("static/image/test.png") # save pic in the given location
    # plt.show() display figure with dailog box pop up

    # return render(request, template_name='matplotLib_figure.html')
    return render(response, template_name='matplotLib_figure.html')


def circle_area(request):
    radius = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    area = [3.14159, 12.56636, 28.27431, 50.26544, 78.53975, 113.09724]
    plt.plot(radius, area)
    # plt.show()
    plt.xlabel('radius')
    plt.ylabel('area')
    plt.figlegend(radius, area)
    plt.savefig("static/image/area.png")
    # plt.show()
    return render(request, template_name='matplotLib_figure.html')