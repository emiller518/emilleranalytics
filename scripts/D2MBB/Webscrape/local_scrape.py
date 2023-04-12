from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
#import D2East_MySQL as sql
import requests
from urllib.parse import urlparse


def prestoscrape(abbr, seasonname, baselink, soup):

    fulltable = soup.find("table")

    x = fulltable.find_all('tr')

    #teamID = sql.getteamidfromabvr(abbr)
    #seasonID = sql.getseasonid(seasonname)

    seasonID = 15

    for i in x[1:]:
        number = (i.find("span", text="No.:").next_sibling.strip())
        if number == '':
            continue
        year = (i.find("span", text=["Cl.:","Yr.:"]).next_sibling.strip())
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
        height = (i.find("span", text=["Ht.:", "Hgt.:"]).next_sibling.strip())
        if '-' in height:
            height = height.replace('-', '\'')
        weight = (i.find("span", text=["Wt.:", "Wgt.:"]).next_sibling.strip())

        townschoolsplit = i.find("span", text=["Hometown/High School:", "Hometown/High School/Previous College:",
                                               "Hometown/Previous School:"]) \
            .next_sibling.strip().split('/')

        if len(townschoolsplit) > 2:
            prevschool = townschoolsplit[2].strip()
        else:
            prevschool = ''

        if len(townschoolsplit) > 1:
            highschool = townschoolsplit[1].strip()
        else:
            highschool = ''

        hometown = townschoolsplit[0].strip()
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


        first = (
        i.find("th", {"class": "name"}).text.strip().replace('\t', '').replace(' ', '').replace('\n', ' ').split('  ')[
            0])
        last = (
        i.find("th", {"class": "name"}).text.strip().replace('\t', '').replace(' ', '').replace('\n', ' ').split('  ')[
            1])
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
            #imglabel = '../playerphotos/' + str(abbr) + str(seasonID) + str(playerid) + '.jpg'
            imglabel = 'playerphotos/' + str(abbr) + str(seasonID) + str(first) + str(last) + '.jpg'
            imglink = baselink + imglink['data-src']
            headers = {'User-Agent': 'Mozilla/5.0', }
            s = requests.Session()
            r = s.get(imglink, allow_redirects=True, headers=headers)
            with open(imglabel, 'wb') as f:
                f.write(r.content)




def sidearmscrape(abbr, season, baselink, soup):

    fulltable = soup.find_all("div", {"class": "sidearm-roster-player-container"})

    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')

    #teamID = sql.getteamidfromabvr(abbr)
    #seasonID = sql.getseasonid(season)

    seasonID = 15

    if len(str(seasonID)) == 1:
        seasonlabel = str(0) + str(seasonID)
    else:
        seasonlabel = str(seasonID)

    for player in fulltable:

        hometown = player.find("span", {"class": "sidearm-roster-player-hometown"}).text
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

        if player.find("span", {"class": "sidearm-roster-player-highschool"}) is not None:
            highschool = player.find("span", {"class": "sidearm-roster-player-highschool"}).text
            if '/' in highschool:
                highschool = highschool.split('/')[0]
        elif player.find("span", {"class": "sidearm-roster-player-previous-school"}) is not None:
            highschool = player.find("span", {"class": "sidearm-roster-player-previous-school"}).text
        else:
            highschool = ''

        clss = player.find("span", {"class": "sidearm-roster-player-academic-year"}).text
        newdiv = player.find("div", {"class": "sidearm-roster-player-position"})
        # position = newdiv.find("span", {"class": 'hide-on-medium'}).text.strip()
        position = newdiv.find("span", {"class": 'text-bold'}).text.strip()

        #for str2011
        test = newdiv.find("span", {"class": 'text-bold'})
        textx = test.find("span", {"class": 'hide-on-medium'})
        if textx is not None:
            position = textx.text.strip()

        if len(position) > 3:
            position = position[0]

        if newdiv.find("span", {"class": "sidearm-roster-player-height"}):
            height = newdiv.find("span", {"class": "sidearm-roster-player-height"}).text
        else:
            height = ''

        number = int(player.find("span", {"class": "sidearm-roster-player-jersey-number"}).text.strip())

        if 'fr' in clss.lower():
            classID = str(1)
        elif 'so' in clss.lower():
            classID = str(2)
        elif 'jr' in clss.lower():
            classID = str(3)
        elif 'sr' in clss.lower():
            classID = str(4)
        elif 'gr' in clss.lower():
            classID = str(5)
        else:
            classID = str(0)

        name = player.find_all("a")[1].text.title()

        if name == 'Terrence  Rountree Jr.':
            name = 'Terrence Rountree'

        if name == 'Full Bio':
            name = player.find_all("a")[0].text.title()

        if ' ' in name:
            name = name.replace("  ", " ")

        finalheight = height.replace("\"", "")

        '''
        playerexists = (sql.playeronteamindb(teamID, name))
        playeryearexists = (sql.playeryearindb(teamID, name, seasonID))

        if playerexists:
            playerid = sql.getplayernameid(teamID, name)
            sql.updateplayer(playerid, town, state, foreign, highschool)
            if playeryearexists:
                sql.updateplayeryear(playerid, seasonID, classID, finalheight, position)
            else:
                sql.insertplayeryear(playerid, teamID, seasonID, classID, number, finalheight, position)
        else:
            playerlist = [name, town, state, foreign, highschool]
            playeryearlist = [teamID, seasonID, classID, number, finalheight, position]
            sql.insertplayerfull(playerlist, playeryearlist)

        playerid = sql.getplayernameid(teamID, name)
        '''

        imglink = player.find("img", {"class": "lazyload"})

        if imglink is not None:
            # imglabel = '../playerphotos/' + str(abbr) + str(seasonID) + str(playerid) + '.jpg'
            imglabel = 'playerphotos/' + str(abbr) + str(seasonID) + str(name.split(' ')[0]) + str(name.split(' ')[1]) + '.jpg'
            imglink = baselink + imglink['data-src']
            headers = {'User-Agent': 'Mozilla/5.0', }
            s = requests.Session()
            r = s.get(imglink, allow_redirects=True, headers=headers)
            with open(imglabel, 'wb') as f:
                f.write(r.content)

        print(name + ' - ' + town + ' - ' + state + ' - ' + foreign + ' - ' + highschool + ' - ' + clss + ' - ' +
              classID + ' - ' + str(number) + ' - ' + finalheight + ' - ' + position)



def scrape(abbr, seasonname, link):
    parser = urlparse(link)
    baselink = '{uri.scheme}://{uri.netloc}'.format(uri=parser)
    print(baselink)

    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    source = urlopen(req).read()
    soup = BeautifulSoup(source, "html.parser")

    if soup.find("span", {"class": "sidearm-roster-player-hometown"}) != None:
        sidearmscrape(abbr,seasonname, baselink, soup)
    else:
        prestoscrape(abbr,seasonname, baselink, soup)

year = '2019-20'

#scrape('ASS', year, 'https://assumption.prestosports.com/sports/mbkb/2019-20/roster')
#scrape('BEN', year, 'https://www.bentleyfalcons.com/sports/mbkb/2019-20/roster')
scrape('FRA', year, 'https://www.fpuravens.com/sports/mbkb/2019-20/roster')
scrape('STM', year, 'https://www.smcathletics.com/sports/mbkb/2019-20/roster')
