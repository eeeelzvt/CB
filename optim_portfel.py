from matplotlib import pyplot as plt
import numpy as np

def krug_portfel(data =[], money = []):
    money = ['USD', 'EURO', 'RUB','CNY', 'JAGUAR', 'MERCEDES']

    data = [23, 17, 35, 29, 12, 41]

    # Creating plot
    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=money)

    # show plot
    plt.show()

krug_portfel()