from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import D2East_MySQL as sql
import requests

from urllib.parse import urlparse

link = 'https://lemoynedolphins.com/sports/mens-basketball/roster'
parser = urlparse(link)
baselink = '{uri.scheme}://{uri.netloc}'.format(uri=parser)
print(baselink)

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(req).read()
soup = BeautifulSoup(source, "html.parser")

fulltable = soup.find("table")

x = fulltable.find_all('tr')


opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')


abbr = 'LEM'
seasonname = '2019-20'

teamID = sql.getteamidfromabvr(abbr)
seasonID = sql.getseasonid(seasonname)


for i in x[1:]:
    number = (i.find("span", text="No.:").next_sibling.strip())
    if number == '':
        continue
    year = (i.find("span", text="Cl.:").next_sibling.strip())
    if 'fr' in year.lower():
        classID = str(1)
    elif 'so' in year.lower():
        classID = str(2)
    elif 'jr' in year.lower():
        classID = str(3)
    elif 'sr' in year.lower():
        classID = str(4)
    elif 'gr' in year.lower():
        classID = str(5)
    else:
        classID = str(0)
    position = (i.find("span", text="Pos.:").next_sibling.strip())
    height = (i.find("span", text="Ht.:").next_sibling.strip())
    if '-' in height:
        height = height.replace('-', '\'')
    weight = (i.find("span", text="Wt.:").next_sibling.strip())
    hometown = (i.find("span", text="Hometown/High School:").next_sibling.strip().split('/')[0].strip())
    town = hometown.split(", ")[0]
    state = hometown.split(", ")[1]
    state = state.replace('.', '')

    if state == 'Conn':
        state = 'CT'
    if state == 'Calif':
        state = 'CA'
    if state == 'Mass':
        state = 'MA'
    if state == 'Fla':
        state = 'FL'
    if state == 'Ontario':
        state = 'Canada'
    if state == 'Ind':
        state = 'IN'
    if state == 'Mich':
        state = 'MI'
    if state == 'Ohio':
        state = 'OH'
    if state == 'WVa':
        state = 'WV'
    if state == 'Maine':
        state = 'ME'
    if state == 'Ill':
        state = 'IL'

    if len(state) > 2:
        foreign = str(1)
    else:
        foreign = str(0)
        state = state.upper()

    highschool = (i.find("span", text="Hometown/High School:").next_sibling.strip().split('/')[1].strip())
    prevschool = (i.find("span", text="Hometown/High School:").next_sibling.strip().split('/')[2].strip())
    first = (i.find("th", {"class": "name"}).text.strip().replace('\t','').replace(' ','').replace('\n', ' ').split('  ')[0])
    last = (i.find("th", {"class": "name"}).text.strip().replace('\t', '').replace(' ', '').replace('\n', ' ').split('  ')[1])
    name = first + ' ' + last

    playerlist = [name, number, classID, position, height, weight, hometown, highschool, prevschool]

    print(playerlist)

    '''

    playerexists = (sql.playeronteamindb(teamID, name))
    playeryearexists = (sql.playeryearindb(teamID, name, seasonID))

    if playerexists:
        playerid = sql.getplayernameid(teamID, name)
        sql.updateplayer(playerid, town, state, foreign, highschool)
        if playeryearexists:
            sql.updateplayeryear(playerid, seasonID, classID, height, position)
        else:
            sql.insertplayeryear(playerid, teamID, seasonID, classID, number, height, position)
    else:
        playerlist = [name, town, state, foreign, highschool]
        playeryearlist = [teamID, seasonID, classID, number, height, position]
        sql.insertplayerfull(playerlist, playeryearlist)

    playerid = sql.getplayernameid(teamID, name)
    '''

    imglink = i.find("img", {"class": "lazyload"})

    if imglink is not None:
        imglabel = '../playerphotos/' + str(abbr) + str(15) + str(1) + '.jpg'
        imglink = baselink + imglink['data-src']
        headers = {'User-Agent': 'Mozilla/5.0', }
        s = requests.Session()
        r = s.get(imglink, allow_redirects=True, headers=headers)
        with open(imglabel, 'wb') as f:
            f.write(r.content)



