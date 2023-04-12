from D2East_MySQL import updateshotcoordinates
from selenium import webdriver
import time
from bs4 import BeautifulSoup


def getshotchart(gameid, linkseg, finalscore):

    link = 'https://' + linkseg + '/sidearmstats/mbball/shot-chart'
    print(link)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('window-size=1920x1080');

    driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver", chrome_options=chrome_options)

    driver.implicitly_wait(30)
    time.sleep(5)
    driver.get(link)
    time.sleep(5)

    tutorial_soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    awayscore = tutorial_soup.find('div', {'class': ['c-scoreboard__team--away']}).text
    homescore = tutorial_soup.find('div', {'class': ['c-scoreboard__team--home']}).text

    totalshots = []

    if (int(finalscore[0]) != int(homescore)) or (int(finalscore[1]) != int(awayscore)):
        print('Score in DB ' + str(finalscore[1]) + '@' + str(finalscore[0]) + ' does not match score on website, ' + str(awayscore) + '@' + str(homescore))
        print('Skipping...')
        pass
    else:
        homeshots = tutorial_soup.find_all('div', {'class': ['c-shot-chart__shot--home']})
        awayshots = tutorial_soup.find_all('div', {'class': ['c-shot-chart__shot--away']})

        for i in homeshots:
            if i.has_attr('style'):
                sidearm_y = round(float(i.get('style').split('top: ')[1].split('%')[0]), 2)
                sidearm_x = round(float(i.get('style').split('left: ')[1].split('%')[0]), 2)

                x_rect = round((sidearm_x * .94),2)
                y_rect = round(((100-sidearm_y)*.5),2)

                x_square = round(((100-sidearm_y)*.5),2)
                y_square = round(((100-sidearm_x)*.94),2)

            else:
                x_rect = 0
                y_rect = 0
                x_square = 0
                y_square = 0

            timehalf = i.find('div', {'class': ['c-shot-chart__shot-time']}).text
            timeleft = timehalf.split(' - ')[0]
            half = int(timehalf.split(' - ')[1][0])

            if half == 1:
               seconds = int(timeleft.split(':')[0])*60 + int(timeleft.split(':')[1])
            else:
                seconds = int(timeleft.split(':')[0]) * 60 + int(timeleft.split(':')[1])

            shot = [half, seconds, x_rect, y_rect, x_square, y_square]
            totalshots.append(shot)


        for i in awayshots:
            if i.has_attr('style'):

                sidearm_y = round(float(i.get('style').split('top: ')[1].split('%')[0]), 2)
                sidearm_x = round(float(i.get('style').split('left: ')[1].split('%')[0]), 2)

                x_rect = round((sidearm_x * .94), 2)
                y_rect = round(((100 - sidearm_y) * .5), 2)

                x_square = round(((sidearm_y) * .5), 2)
                y_square = round(((sidearm_x) * .94), 2)

            else:
                x_rect = 0
                y_rect = 0
                x_square = 0
                y_square = 0

            timehalf = i.find('div', {'class': ['c-shot-chart__shot-time']}).text
            timeleft = timehalf.split(' - ')[0]
            half = int(timehalf.split(' - ')[1][0])

            if half == 1:
                seconds = int(timeleft.split(':')[0])*60 + int(timeleft.split(':')[1])
            else:
                seconds = int(timeleft.split(':')[0]) * 60 + int(timeleft.split(':')[1])

            shot = [half, seconds, x_rect, y_rect, x_square, y_square]
            totalshots.append(shot)

        for i in totalshots:
            print(i)
            updateshotcoordinates(gameid, i[0], i[1], i[4], i[5], i[2], i[3])



