from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import D2East_MySQL as sql
import requests
from urllib.parse import urlparse



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
        print('prestooo')



def prestoscrape(abbr, seasonname, baselink, soup):
    fulltable = soup.find("table")

    x = fulltable.find_all('tr')

    teamID = sql.getteamidfromabvr(abbr)
    seasonID = sql.getseasonid(seasonname)

    for i in x[1:]:

        name = (" ".join(i.findAll('a')[0].text.replace('\t', '').replace('\n', '').replace('\r', '').split()))

        '''

        # Get variables by searching through text or class names
        number = int(i.find("span", text=[" No.:", "No.:"]).next_sibling.strip())
        year = (i.find("span", text=["Cl.:","Yr.:"]).next_sibling.strip())
        position = (i.find("span", text="Pos.:").next_sibling.strip())
        hometown = i.find("span", text=["Hometown:", " Hometown:"]).next_sibling.strip()
        height = (i.find("span", text=["Ht.:", "Hgt.:"]).next_sibling.strip())
        weight = (i.find("span", text=["Wt.:", "Wgt.:"]).next_sibling.strip())
        first = (i.find("th", {"class": "name"}).text.strip().replace('\t', '').replace(' ', '').replace('\n', ' ').split('  ')[0])
        last = (i.find("th", {"class": "name"}).text.strip().replace('\t', '').replace(' ', '').replace('\n', ' ').split('  ')[1])
        name = first + ' ' + last


        # if hometown and high school are combined:
        if i.find("span", text=["Hometown/High School:", "Hometown/High School/Previous College:", "Hometown/Previous School:","Hometown/High School/Previous School:","Hometown/High School (Last College):"]):
            townschoolsplit = i.find("span", text=["Hometown/High School:", "Hometown/High School/Previous College:",
                                                   "Hometown/Previous School:", "Hometown/High School/Previous School:",
                                                   "Hometown/High School (Last College):"]).next_sibling.strip().split('/')
            if len(townschoolsplit) > 2:
                prevschool = townschoolsplit[2].strip()
            else:
                prevschool = ''

            if len(townschoolsplit) > 1:
                highschool = townschoolsplit[1].strip()
            else:
                highschool = ''

            hometown = townschoolsplit[0].strip()

        else:
            hometown = (" ".join(i.findAll('td')[5].text.replace('\t', '').replace('\n', '').replace('\r', '').split('Hometown:')[-1].split()))

            prevschool = ''

            highschool = ''
        '''

        try:
            number = \
            i.findAll('td')[0].text.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '').split(
                'No.:')[-1]
        except ValueError:
            continue
        except AttributeError:
            continue

        year = \
        i.findAll('td')[1].text.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '').split('Yr.:')[-1]
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

        position = \
        i.findAll('td')[2].text.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '').split('Pos.:')[
            -1]

        if position == 'Point Guard' or position == 'Guard':
            position = 'G'
        elif position == 'Forward':
            position = 'F'
        elif position == 'Forward/Guard':
            position = 'G/F'

        height = \
        i.findAll('td')[3].text.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '').split('Ht.:')[-1]

        if '-' in height:
            height = height.replace('-', '\'')

        weight = \
        i.findAll('td')[4].text.replace('\t', '').replace('\n', '').replace('\r', '').replace(' ', '').split('Wgt.:')[
            -1].split('Wt.')[-1].replace(u'\xa0', u'')

        hometown = (" ".join(
            i.findAll('td')[5].text.replace('\t', '').replace('\n', '').replace('\r', '').split('Hometown:')[
                -1].split()))

        if len(i.findAll('td')) >= 7:
            highschool = (" ".join(
                i.findAll('td')[6].text.replace('\t', '').replace('\n', '').replace('\r', '').split('High School:')[
                    -1].split()))
        elif len(hometown.split('/')) > 0:
            highschool = hometown.split('/')[1]
            hometown = hometown.split('/')[0]
        else:
            highschool = ''

        town = hometown.split(", ")[0]

        try:
            state = hometown.split(", ")[1]
        except IndexError:
            state = ''

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
        if state == 'Minn':
            state = 'MN'

        if len(state) > 2:
            foreign = str(1)
        else:
            foreign = str(0)
            state = state.upper()

        playerlist = [name, number, classID, position, height, weight, town, state, highschool]

        print(playerlist)

        playerexists = (sql.playeronteamindb(teamID, name))
        playeryearexists = (sql.playeryearindb(teamID, name, seasonID))

        if playerexists:
            print('player exists')
            playerid = sql.getplayernameid(teamID, name)
            sql.updateplayer(playerid, town, state, foreign, highschool)
            if playeryearexists:
                print('update player year')
                sql.updateplayeryear(playerid, seasonID, classID, height, position)
            else:
                print('adding player year')
                sql.insertplayeryear(playerid, teamID, seasonID, classID, number, height, position)
        else:
            print('player does not exist')
            playerlist = [name, town, state, foreign, highschool]
            playeryearlist = [teamID, seasonID, classID, number, height, position]
            sql.insertplayerfull(playerlist, playeryearlist)

        playerid = sql.getplayernameid(teamID, name)

        imglink = i.find("img", {"class": "lazyload"})

        if imglink is not None:
            imglabel = '../static/playerphotos/' + str(abbr) + str(seasonID) + str(playerid) + '.jpg'
            # imglabel = 'playerphotos/' + str(abbr) + str(seasonID) + str(first) + str(last) + '.jpg'
            imglink = baselink + imglink['data-src'].split('.jpg')[0] + '.jpg'
            headers = {'User-Agent': 'Mozilla/5.0', }
            s = requests.Session()
            r = s.get(imglink, allow_redirects=True, headers=headers)
            with open(imglabel, 'wb') as f:
                f.write(r.content)




def sidearmscrape(abbr, season, baselink, soup):

    fulltable = soup.find_all("div", {"class": "sidearm-roster-player-container"})

    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')

    teamID = sql.getteamidfromabvr(abbr)
    seasonID = sql.getseasonid(season)

    #seasonID = 15

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
        if state == 'Fla' or state == 'Fla.':
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

        try:
            position = newdiv.find("span", {"class": 'text-bold'}).text.strip()
        except AttributeError:
            position = ''

        #for str2011
        '''
        test = newdiv.find("span", {"class": 'text-bold'})
        textx = test.find("span", {"class": 'hide-on-medium'})
        if textx is not None:
            position = textx.text.strip()
        '''

        if len(position) > 3:
            position = position[0]

        if newdiv.find("span", {"class": "sidearm-roster-player-height"}):
            height = newdiv.find("span", {"class": "sidearm-roster-player-height"}).text
        else:
            height = ''

        try:
            number = int(player.find("span", {"class": "sidearm-roster-player-jersey-number"}).text.strip())
        except ValueError:
            continue
        except AttributeError:
            continue

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


        playerexists = (sql.playeronteamindb(teamID, name))
        playeryearexists = (sql.playeryearindb(teamID, name, seasonID))

        if playerexists:
            print('player exists')
            playerid = sql.getplayernameid(teamID, name)
            sql.updateplayer(playerid, town, state, foreign, highschool)
            if playeryearexists:
                print('update player year')
                sql.updateplayeryear(playerid, seasonID, classID, finalheight, position)
            else:
                print('addingplayeryear')
                sql.insertplayeryear(playerid, teamID, seasonID, classID, number, finalheight, position)
        else:
            print('player does not exist')
            playerlist = [name, town, state, foreign, highschool]
            playeryearlist = [teamID, seasonID, classID, number, finalheight, position]
            sql.insertplayerfull(playerlist, playeryearlist)

        playerid = sql.getplayernameid(teamID, name)

        imglink = player.find("img", {"class": "lazyload"})

        if imglink is not None:
            imglabel = '../static/playerphotos/' + str(abbr) + str(seasonID) + str(playerid) + '.jpg'
            # imglabel = 'playerphotos/' + str(abbr) + str(seasonID) + str(name.split(' ')[0]) + str(name.split(' ')[1]) + '.jpg'
            imglink = baselink + imglink['data-src'].split('.jpg')[0] + '.jpg'
            headers = {'User-Agent': 'Mozilla/5.0', }
            s = requests.Session()
            r = s.get(imglink, allow_redirects=True, headers=headers)
            with open(imglabel, 'wb') as f:
                f.write(r.content)

        #print(name + ' - ' + town + ' - ' + state + ' - ' + foreign + ' - ' + highschool + ' - ' + clss + ' - ' +
        #      classID + ' - ' + str(number) + ' - ' + finalheight + ' - ' + position)




scrapeyears = ['2020-21']

'''

for year in scrapeyears:

    yearext = year[0:-2] + '20' + year[-2:]
    
    # NE10 Scrape
    scrape('PAC', year, 'https://paceuathletics.com/sports/mens-basketball/roster/'+year)
    scrape('NEW', year, 'https://newhavenchargers.com/sports/mens-basketball/roster/'+year)
    scrape('ADE', year, 'https://aupanthers.com/sports/mens-basketball/roster/'+year)
    scrape('AME', year, 'https://aicyellowjackets.com/sports/mens-basketball/roster/'+year)
    scrape('STR', year, 'https://gogoldenknights.com/sports/mens-basketball/roster/'+year)
    scrape('SCT', year, 'https://scsuowls.com/sports/mens-basketball/roster/'+year)
    scrape('ASS', year, 'https://assumption.prestosports.com/sports/mbkb/'+year+'/roster')
    scrape('BEN', year, 'https://www.bentleyfalcons.com/sports/mbkb/'+year+'/roster')
    scrape('FRA', year, 'https://www.fpuravens.com/sports/mbkb/'+year+'/roster')
    scrape('STM', year, 'https://www.smcathletics.com/sports/mbkb/'+year+'/roster')
    scrape('STA', year, 'https://www.saintanselmhawks.com/sports/mbkb/'+year+'/roster')
    scrape('SNH', year, 'https://www.snhupenmen.com/sports/mbkb/'+year+'/roster')
    scrape('STO', year, 'https://www.stonehillskyhawks.com/sports/mbkb/'+year+'/roster')
    scrape('LEM', year, 'https://lemoynedolphins.com/sports/mens-basketball/roster/'+year)
    
    # CACC Scrape
    scrape('BLO', year, 'https://bcbearsathletics.com/sports/mens-basketball/roster/' + yearext)
    scrape('CAL', year, 'https://caldwellathletics.com/sports/mens-basketball/roster/' + year)
    scrape('CON', year, 'https://www.concordiaclippers.com/sports/mbkb/' + year + '/roster/')
    scrape('DOM', year, 'https://www.chargerathletics.com/sports/mbkb/' + year + '/roster/')
    scrape('FEL', year, 'https://www.felicianathletics.com/sports/mbkb/' + year + '/roster/')
    scrape('NYA', year, 'https://athletics.nyack.edu/sports/mbkb/' + year + '/roster/')
    scrape('POS', year, 'https://posteagles.com/sports/mens-basketball/roster/' + year)
    scrape('CHE', year, 'https://griffinathletics.com/sports/mens-basketball/roster/' + yearext)
    scrape('GEO', year, 'https://gculions.com/sports/mens-basketball/roster/' + year)
    scrape('GOL', year, 'https://www.gbcathletics.com/sports/mens-basketball/roster/' + yearext)
    scrape('HOL', year, 'https://athletics.holyfamily.edu/sports/mens-basketball/roster/' + year)
    scrape('JEF', year, 'http://www.jeffersonrams.com/sports/mbkb/' + year + '/roster/')
    scrape('USC', year, 'https://www.devilsathletics.com/sports/mbkb/' + year + '/roster/')
    scrape('WIL', year, 'https://wildcats.athletics.wilmu.edu/sports/mbkb/' + year + '/roster/')

    # ECC Scrape
    scrape('BRI', year, 'https://www.ubknights.com/sports/mbkb/' + year + '/roster')
    scrape('DIS', year, 'https://www.udcfirebirds.com/sports/mbkb/' + year + '/roster')
    scrape('STQ', year, 'https://www.stacathletics.com/sports/mbkb/' + year + '/roster')
    scrape('DAE', year, 'https://daemenwildcats.com/sports/mens-basketball/roster/' + year)
    scrape('MER', year, 'https://mercyathletics.com/sports/mens-basketball/roster/' + year)
    scrape('MOL', year, 'https://molloylions.com/sports/mens-basketball/roster/' + year)
    scrape('NYI', year, 'https://nyitbears.com/sports/mens-basketball/roster/' + year)
    scrape('QUE', year, 'https://queensknights.com/sports/mens-basketball/roster/' + year)
    scrape('ROB', year, 'https://robertsredhawks.com/sports/mens-basketball/roster/' + yearext)

'''


for year in scrapeyears:
    #scrape('MOL', year, 'https://molloylions.com/sports/mens-basketball/roster/' + year)
    scrape('STQ', year, 'https://www.stacathletics.com/sports/mbkb/' + year + '/roster')
    #scrape('AME', year, 'https://aicyellowjackets.com/sports/mens-basketball/roster/'+year)
    #scrape('STR', year, 'https://gogoldenknights.com/sports/mens-basketball/roster/' + year)
    scrape('FRA', year, 'https://www.fpuravens.com/sports/mbkb/'+year+'/roster')
