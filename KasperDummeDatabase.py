import Repo
import uuid

def fetch_match_id(map_name):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT Id FROM Match WHERE id = %s AND mapname = ?"""
    cursor.execute(query, (map_name))
    match_id = cursor.fetchall()  #Skal nok laves om til fetchall
    cursor.close()
    connection.close()
    return match_id


def fetch_match_id_for_team(matchid, teamid):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT MatchesId FROM MatchTeam WHERE MatchId = ? AND TeamsId = ?"""
    cursor.execute(query, (matchid, teamid))
    team_match_id = cursor.fetchall()
    cursor.close()
    connection.close()
    return team_match_id


def fetch_team_match_stats(matchid, teamid):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT * FROM placeholder WHERE id = %s AND mapname = ?"""
    cursor.execute(query, (matchid, teamid))
    team_stats = cursor.fetchall()
    cursor.close()
    connection.close()
    return team_stats


def fetch_player_stats(userid): #Denne tag ikke højte for mappet, men tag istedet for hele lortet.
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT * FROM PLAYERMATCHSTATS WHERE FKPlayerId = ?"""
    cursor.execute(query, userid)

    user_stats = cursor.fetchall()
    cursor.close()
    connection.close()
    return user_stats

def fetch_player_team_stats(userid, teamid): #Denne tag ikke højte for mappet, men tag istedet for hele lortet.
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT * FROM PLAYERMATCHSTATS WHERE FKPlayerId = ? AND TeamsId = ?"""
    cursor.execute(query, userid, teamid)

    user_stats = cursor.fetchall()
    cursor.close()
    connection.close()
    return user_stats