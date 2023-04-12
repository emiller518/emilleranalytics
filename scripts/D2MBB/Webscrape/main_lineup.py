import D2East_MySQL as sql


def calculatelineups(gameid):

    seasonid = sql.getseasonidfromgameid(gameid)

    current_home_players = sql.gethomestarters(gameid, seasonid)
    print(current_home_players)
    current_away_players = sql.getawaystarters(gameid, seasonid)
    print(current_away_players)

    old_home_lineup = []
    current_home_lineup = (sql.returnlineup(current_home_players))
    old_away_lineup = []
    current_away_lineup = (sql.returnlineup(current_away_players))

    gamelist = sql.getpbp(gameid)

    skip = []

    for key, event in enumerate(gamelist):

        if event[1] == 2 and event[2] == 1 and event[6] not in [23,24]:
            current_home_players = sql.gethomestarters(gameid, seasonid)
            current_away_players = sql.getawaystarters(gameid, seasonid)
            current_home_lineup = (sql.returnlineup(current_home_players))
            current_away_lineup = (sql.returnlineup(current_away_players))

        if event[2] == 1:
            seconds = 1200 - event[4]
        else:
            seconds = gamelist[key - 1][4] - event[4]

        if key in skip:
            pass

        else:

            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ----START OF 'SUB OUT' LISTED FIRST-------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # if id for sub out
            if event[6] == 23 and event[9] == 'A':

                # if it's the first time coming across sub out
                if gamelist[key - 1][6] != 23:

                    # 4 alternating subs, away team
                    if gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 6][6] == 23 and gamelist[key + 7][6] == 24 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and gamelist[key + 6][9] == 'A' and gamelist[key + 7][9] == 'A' \
                            and (gamelist[key + 8][6] not in [23, 24] or gamelist[key + 8][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_players.remove(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_players.remove(gamelist[key + 6][5])
                        current_away_players.append(gamelist[key + 7][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    # 3 alternating subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_players.remove(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    # 2 alternating subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][9] == 'A' \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    # single sub, away team
                    elif gamelist[key + 1][6] == 24 \
                            and (gamelist[key + 2][6] not in [23, 24] or gamelist[key + 2][9] == 'H'):
                        skip.append(key + 1)
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)

                    # 2 consecutive subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    # 3 consecutive subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24:
                        # print('-------------3 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_players.append(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    # 4 consecutive subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24:
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_players.append(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_players.append(gamelist[key + 6][5])
                        current_away_players.append(gamelist[key + 7][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    # 5 consecutive subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24:
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7, key + 8, key + 9])
                        old_away_lineup = current_away_lineup
                        current_away_players = []
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_players.append(gamelist[key + 6][5])
                        current_away_players.append(gamelist[key + 7][5])
                        current_away_players.append(gamelist[key + 8][5])
                        current_away_players.append(gamelist[key + 9][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 8], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 9], seconds, current_home_lineup, current_away_lineup)

                    # 3 in weird saint rose order, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_players.remove(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.remove(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_players.append(gamelist[key + 4][5])
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    else:
                        print(event)
                        print('error')

            # ------------------------------------------------------------------------------------------------------
            # -----------------------START OF HOME LOGIC---------------------------------------------------
            # ------------------------------------------------------------------------------------------------------

            elif event[6] == 23 and event[9] == 'H':

                # if it's the first time coming across sub out
                if gamelist[key - 1][6] != 23:

                    if gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 6][6] == 23 and gamelist[key + 7][6] == 24 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][9] == 'H' \
                            and gamelist[key + 4][9] == 'H' and gamelist[key + 5][9] == 'H' \
                            and gamelist[key + 6][9] == 'H' and gamelist[key + 7][9] == 'H' \
                            and (gamelist[key + 8][6] not in [23, 24] or gamelist[key + 8][9] == 'A'):
                        # print('----------4 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_players.remove(gamelist[key + 4][5])
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_players.remove(gamelist[key + 6][5])
                        current_home_players.append(gamelist[key + 7][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][9] == 'H' \
                            and gamelist[key + 4][9] == 'H' and gamelist[key + 5][9] == 'H' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'A'):
                        # print('--------- 3 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_players.remove(gamelist[key + 4][5])
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][9] == 'H' \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'A'):
                        # print('-----------2 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 \
                            and (gamelist[key + 2][6] not in [23, 24] or gamelist[key + 2][9] == 'A'):
                        # print('------------1 sub')
                        skip.append(key + 1)
                        old_home_lineup = current_home_lineup
                        print('player remove: ' + str(gamelist[key][5]))
                        print('player add: ' + str(gamelist[key + 1][5]))
                        print(current_home_players)
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        print('change made:')
                        print(current_home_players)
                        current_home_lineup = sql.returnlineup(current_home_players)
                        print('lineup:' + str(current_away_lineup))
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'A'):
                        # print('-------------2 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 24:
                        # print('-------------3 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_players.append(gamelist[key + 4][5])
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24:
                        # print('--------------4 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_home_lineup = current_home_lineup
                        current_home_players.remove(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_players.append(gamelist[key + 4][5])
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_players.append(gamelist[key + 6][5])
                        current_home_players.append(gamelist[key + 7][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 23 and gamelist[key + 5][6] == 24:
                        # print('--------------group consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7, key + 8, key + 9])
                        old_home_lineup = current_home_lineup
                        current_home_players = []
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_players.append(gamelist[key + 6][5])
                        current_home_players.append(gamelist[key + 7][5])
                        current_home_players.append(gamelist[key + 8][5])
                        current_home_players.append(gamelist[key + 9][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 8], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 9], seconds, current_home_lineup, current_away_lineup)

                    else:
                        print(event)
                        print('error')


            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ----START OF 'SUB IN' LISTED FIRST-------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # if id for sub out
            elif event[6] == 24 and event[9] == 'A':

                # if it's the first time coming across sub out
                if gamelist[key - 1][6] != 24:

                    # 4 alternating subs, away team
                    if gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23 \
                            and gamelist[key + 6][6] == 24 and gamelist[key + 7][6] == 23 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][
                        9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and gamelist[key + 6][9] == 'A' and gamelist[key + 7][9] == 'A' \
                            and (gamelist[key + 8][6] not in [23, 24] or gamelist[key + 8][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_players.append(gamelist[key + 4][5])
                        current_away_players.remove(gamelist[key + 5][5])
                        current_away_players.append(gamelist[key + 6][5])
                        current_away_players.remove(gamelist[key + 7][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    # 3 alternating subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][
                        9] == 'A' \
                            and gamelist[key + 4][9] == 'A' and gamelist[key + 5][9] == 'A' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_players.append(gamelist[key + 4][5])
                        current_away_players.remove(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    # 2 alternating subs, away team
                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 1][9] == 'A' and gamelist[key + 2][9] == 'A' and gamelist[key + 3][
                        9] == 'A' \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    # single sub, away team
                    elif gamelist[key + 1][6] == 23 \
                            and ((gamelist[key + 2][6] not in [23, 24]) or (gamelist[key + 2][9] == 'H')):
                        skip.append(key + 1)
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.remove(gamelist[key + 1][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)

                    # 2 consecutive subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'H'):
                        skip.extend([key + 1, key + 2, key + 3])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.remove(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    # 3 consecutive subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23:
                        # print('-------------3 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.remove(gamelist[key + 3][5])
                        current_away_players.remove(gamelist[key + 4][5])
                        current_away_players.remove(gamelist[key + 5][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    # 4 consecutive subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23:
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_away_lineup = current_away_lineup
                        current_away_players.append(gamelist[key][5])
                        current_away_players.append(gamelist[key + 1][5])
                        current_away_players.append(gamelist[key + 2][5])
                        current_away_players.append(gamelist[key + 3][5])
                        current_away_players.remove(gamelist[key + 4][5])
                        current_away_players.remove(gamelist[key + 5][5])
                        current_away_players.remove(gamelist[key + 6][5])
                        current_away_players.remove(gamelist[key + 7][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    # 5 consecutive subs, away team
                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23:
                        skip.extend(
                            [key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7, key + 8, key + 9])
                        old_away_lineup = current_away_lineup
                        current_away_players = []
                        current_away_players.append(gamelist[key + 5][5])
                        current_away_players.append(gamelist[key + 6][5])
                        current_away_players.append(gamelist[key + 7][5])
                        current_away_players.append(gamelist[key + 8][5])
                        current_away_players.append(gamelist[key + 9][5])
                        current_away_lineup = sql.returnlineup(current_away_players)
                        sql.updatepbp(gamelist[key + 0], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, old_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 8], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 9], seconds, current_home_lineup, current_away_lineup)

                    else:
                        print(event)
                        print('error')

            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------
            # ------------------------------------------------------------------------------------------------------

            elif event[6] == 24 and event[9] == 'H':

                # if it's the first time coming across sub out
                if gamelist[key - 1][6] != 24:

                    if gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23 \
                            and gamelist[key + 6][6] == 24 and gamelist[key + 7][6] == 23 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][
                        9] == 'H' \
                            and gamelist[key + 4][9] == 'H' and gamelist[key + 5][9] == 'H' \
                            and gamelist[key + 6][9] == 'H' and gamelist[key + 7][9] == 'H' \
                            and (gamelist[key + 8][6] not in [23, 24] or gamelist[key + 8][9] == 'A'):
                        # print('----------4 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_players.append(gamelist[key + 4][5])
                        current_home_players.remove(gamelist[key + 5][5])
                        current_home_players.append(gamelist[key + 6][5])
                        current_home_players.remove(gamelist[key + 7][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][
                        9] == 'H' \
                            and gamelist[key + 4][9] == 'H' and gamelist[key + 5][9] == 'H' \
                            and (gamelist[key + 6][6] not in [23, 24] or gamelist[key + 6][9] == 'A'):
                        # print('--------- 3 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_players.append(gamelist[key + 4][5])
                        current_home_players.remove(gamelist[key + 5][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23 \
                            and gamelist[key + 1][9] == 'H' and gamelist[key + 2][9] == 'H' and gamelist[key + 3][
                        9] == 'H' \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'A'):
                        # print('-----------2 subs alternate')
                        skip.extend([key + 1, key + 2, key + 3])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 23 \
                            and ((gamelist[key + 2][6] not in [23, 24]) or (gamelist[key + 2][9] != gamelist[key][9])):
                        # print('------------1 sub')
                        skip.append(key + 1)
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.remove(gamelist[key + 1][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 23 and gamelist[key + 3][6] == 23 \
                            and (gamelist[key + 4][6] not in [23, 24] or gamelist[key + 4][9] == 'A'):
                        # print('-------------2 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.remove(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 23:
                        # print('-------------3 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.remove(gamelist[key + 3][5])
                        current_home_players.remove(gamelist[key + 4][5])
                        current_home_players.remove(gamelist[key + 5][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 23:
                        # print('--------------4 subs consecutive')
                        skip.extend([key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7])
                        old_home_lineup = current_home_lineup
                        current_home_players.append(gamelist[key][5])
                        current_home_players.append(gamelist[key + 1][5])
                        current_home_players.append(gamelist[key + 2][5])
                        current_home_players.append(gamelist[key + 3][5])
                        current_home_players.remove(gamelist[key + 4][5])
                        current_home_players.remove(gamelist[key + 5][5])
                        current_home_players.remove(gamelist[key + 6][5])
                        current_home_players.remove(gamelist[key + 7][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)

                    elif gamelist[key + 1][6] == 24 and gamelist[key + 2][6] == 24 and gamelist[key + 3][6] == 24 \
                            and gamelist[key + 4][6] == 24 and gamelist[key + 5][6] == 23:
                        # print('--------------group consecutive')
                        skip.extend(
                            [key + 1, key + 2, key + 3, key + 4, key + 5, key + 6, key + 7, key + 8, key + 9])
                        old_home_lineup = current_home_lineup
                        current_home_players = []
                        current_home_players.append(gamelist[key + 5][5])
                        current_home_players.append(gamelist[key + 6][5])
                        current_home_players.append(gamelist[key + 7][5])
                        current_home_players.append(gamelist[key + 8][5])
                        current_home_players.append(gamelist[key + 9][5])
                        current_home_lineup = sql.returnlineup(current_home_players)
                        sql.updatepbp(gamelist[key + 0], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 1], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 2], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 3], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 4], seconds, old_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 5], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 6], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 7], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 8], seconds, current_home_lineup, current_away_lineup)
                        sql.updatepbp(gamelist[key + 9], seconds, current_home_lineup, current_away_lineup)

                    else:
                        print(event)
                        print('error')

            else:
                sql.updatepbp(event, seconds, current_home_lineup, current_away_lineup)

        print(event)
        print(str(current_home_lineup) + ' ' + str(current_away_lineup))

    sql.marklineupcomplete(gameid)


'''
for gameid in sql.getgameidsforlineup():
    calculatelineups(gameid)
'''




