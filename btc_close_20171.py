import json

# loading data to a list
filename = 'btc_close_2017_requests.json'
with open(filename) as f:
    btc_data = json.load(f)
# print everyday's message
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    #print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))

# create 5 list, stored date and close price
dates = []
months = []
weeks = []
weekdays = []
close = []
# everyday's masseage
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

import pygal
import math

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价 （¥）'
line_chart.x_labels = dates
N = 20 # x axis every 20 day show once
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价折线图 (¥).svg')

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
        x_unique, y_mean = [*zip(*xy_map)]
        line_chart = pygal.Line()
        line_chart.title = title
        line_chart.x_labels = x_unique
        line_chart.add(y_legend, y_mean)
        line_chart.render_to_file('收盘价月日均值(¥).svg')
        return line_chart
    idx_month = dates.index('2017-12-01')
    line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值(¥)', '月日均值')
    line_chart_month
