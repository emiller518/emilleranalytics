import D2East_MySQL as sql, D2EastWebScrape as scrape


def insertpbp(conf,season):
    schedsoup = scrape.schedulesoup(season, conf)
    for link in scrape.getlinks(schedsoup, season, conf):
        print(link)
        if sql.pbpindb(link) == 2:
            sql.markpbpcomplete(link)
            gamesoup = scrape.gamesoup(link, season, conf)
            gameid = sql.getgameidfromlink(link)

            try:
                scrape.parsepbp(gamesoup, gameid, season)

            except IndexError:
                print('DID NOT WORK!!!!!!!!!!!')
                sql.markpbperror(link)


        else:
            pass



seasons = ['2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14']

for i in seasons:

    insertpbp('NE10', i)
    insertpbp('CACC', i)
    insertpbp('ECC', i)



