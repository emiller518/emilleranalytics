from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import csv

link = 'https://gogoldenknights.com/sidearmstats/mbball/shot-chart'

driver = webdriver.Chrome(executable_path=r"/Users/ethanmiller/Desktop/chromedriver")
driver.implicitly_wait(30)
time.sleep(5)
driver.get(link)
time.sleep(5)

tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')

homeshots = tutorial_soup.find_all('div', {'class': ['c-shot-chart__shot--home']})
awayshots = tutorial_soup.find_all('div', {'class': ['c-shot-chart__shot--away']})
totalshots = [['Player','Time','Half','Seconds','X_square','Y_square','X_rect','Y_rect','Result','Type','Team']]

for i in homeshots:
    if i.has_attr('style'):
        y_rect = round(100-float(i.get('style').split('top: ')[1].split('%')[0]), 2)
        x_rect = round(float(i.get('style').split('left: ')[1].split('%')[0]), 2)
        x_square = round(100 - float(i.get('style').split('top: ')[1].split('%')[0]), 2)
        y_square = round(100 - ((float(i.get('style').split('left: ')[1].split('%')[0])) - 50) * 2,2)
    else:
        x_rect = 0
        x_square = 0
        y_rect = 0
        y_square = 0

    if 'c-shot-chart__shot--miss' in i.get('class'):
        success = 0
    else:
        success = 1

    timehalf = i.find('div', {'class': ['c-shot-chart__shot-time']}).text
    timeleft = timehalf.split(' - ')[0]
    half = int(timehalf.split(' - ')[1][0])
    number = int(i.find('button').text)

    playtype = i.find('div', {'class': ['c-shot-chart__shot-narrative']}).text.split(' ')
    playtypelist = ''
    for i in playtype:
        if i.isupper():
            playtypelist += i + ' '
    playtypelist = playtypelist[:-1].title().split(' ')[0]

    if ';' in playtypelist:
        playtypelist = playtypelist.split(';')[0]

    if half == 1:
       seconds = int(timeleft.split(':')[0])*60 + int(timeleft.split(':')[1]) + (20*60)
    else:
        seconds = int(timeleft.split(':')[0]) * 60 + int(timeleft.split(':')[1])

    shot = [number, timeleft, half, seconds, x_square, y_square, x_rect, y_rect, success, playtypelist, 'Home']
    totalshots.append(shot)


for i in awayshots:
    if i.has_attr('style'):
        y_rect = round(100-float(i.get('style').split('top: ')[1].split('%')[0]), 2)
        x_rect = round(float(i.get('style').split('left: ')[1].split('%')[0]), 2)
        x_square = round(100-(100 - float(i.get('style').split('top: ')[1].split('%')[0])), 2)
        y_square = round(200-(100-(float(i.get('style').split('left: ')[1].split('%')[0]) - 50)* 2),2)
    else:
        x_rect = 0
        x_square = 0
        y_rect = 0
        y_square = 0

    if 'c-shot-chart__shot--miss' in i.get('class'):
        success = 0
    else:
        success = 1

    timehalf = i.find('div', {'class': ['c-shot-chart__shot-time']}).text
    timeleft = timehalf.split(' - ')[0]
    half = int(timehalf.split(' - ')[1][0])
    number = int(i.find('button').text)

    playtype = i.find('div', {'class': ['c-shot-chart__shot-narrative']}).text.split(' ')
    playtypelist = ''
    for i in playtype:
        if i.isupper():
            playtypelist += i + ' '
    playtypelist = playtypelist[:-1].title().split(' ')[0]

    if ';' in playtypelist:
        playtypelist = playtypelist.split(';')[0]

    if half == 1:
        seconds = int(timeleft.split(':')[0])*60 + int(timeleft.split(':')[1]) + (20*60)
    else:
        seconds = int(timeleft.split(':')[0]) * 60 + int(timeleft.split(':')[1])

    shot = [number, timeleft, half, seconds, x_square, y_square, x_rect, y_rect, success, playtypelist, 'Away']
    totalshots.append(shot)


for i in totalshots:
    print(i)

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(totalshots)