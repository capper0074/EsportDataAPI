from flask import Flask, request, jsonify

import Analysis
import Repo

from typing import Union

from fastapi import FastAPI

app = FastAPI()


def fetch_user_data_from_database(userid, mapname):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT id, mapname FROM placeholder WHERE id = %s AND mapname = %s"""
    cursor.execute(query, (userid, mapname))
    cursor.execute(query, (userid,))
    user_data = cursor.fetchone()  #Skal nok laves om til fetchall
    cursor.close()
    connection.close()
    return user_data

def fetch_user_map_data_from_database(userid):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT * FROM placeholder WHERE id = %s"""
    cursor.execute(query, (userid,))
    user_data = cursor.fetchone()  #Skal nok laves om til fetchall
    cursor.close()
    connection.close()
    return user_data
@app.post("/get-user_stats/{userid}")
def get_user_stats():
    # Få JSON-data fra request'en
    data = request.json

    # Kontroller om data er til stede og indeholder det nødvendige felt
    if data is None or "userid" not in data:
        return jsonify({"error": "Invalid JSON data or missing userid"}), 400

    userid = data["userid"]

    # Hent brugeroplysninger fra den simulerede database
    user_data = fetch_user_data_from_database(userid)

    # Kontroller om brugeren findes i databasen
    if user_data is None:
        return jsonify({"error": "User not found"}), 404

    # Udtræk nødvendige oplysninger fra brugeroplysningerne
    name = user_data["name"]
    kills = user_data["kills"]
    assists = user_data["assists"]
    deaths = user_data["deaths"]
    headshots = user_data["headshots"]
    match_wins = user_data["Wins"]
    match_loss = user_data["Loss"]

    # Beregn killavg
    kill_avg = Analysis.player_analysis_mean(kills)
    death_avg = Analysis.player_analysis_mean(deaths)
    assist_avg = Analysis.player_analysis_mean(assists)
    headshot_per = Analysis.player_headshot_per(kills, headshots)
    win_per = Analysis.player_match_win_per(match_wins, match_loss)

    # Opret svar-objekt med de modtagne data og beregnede data
    response_data = {
        "username": name,
        "kill_avg": kill_avg,
        "death_avg": death_avg,
        "assist_avg": assist_avg,
        "headshot_per": headshot_per,
        "win_per": win_per
    }

    # Returner data som JSON
    return jsonify(response_data), 200

@app.post("/get-user_singel_mapdata/{userid} {mapid}")
def get_user_mapdata():
    # Få JSON-data fra request'en
    data = request.json

    # Kontroller om data er til stede og indeholder det nødvendige felt
    if data is None or "userid" not in data or "map" not in data:
        return jsonify({"error": "Invalid JSON data or missing userid or map"}), 400

    userid = data["userid"]
    map_name = data["mapname"]

    # Hent brugeroplysninger fra den simulerede database
    user_data = fetch_user_map_data_from_database(userid, map_name)

    # Kontroller om brugeren findes i databasen
    if user_data is None:
        return jsonify({"error": "User not found"}), 404

    # Udtræk nødvendige oplysninger fra brugeroplysningerne
    name = user_data["name"]

    matches_played = user_data["MatchesPlayed"]
    match_wins = user_data["Wins"]
    match_loss = user_data["Losses"]
    kills = user_data["Kills"]
    deaths = user_data["Deaths"]
    assists = user_data["Assists"]

    total_rounds = user_data["TotalRoundsPlayed"]
    ct_rounds = user_data["CtRoundsPlayed"]
    t_rounds = user_data["TRoundsPlayed"]
    ct_pistol_played = user_data["CtPistolRoundsPlayed"]
    ct_pistol_won = user_data["CtPistolRoundsWins"]
    t_pistol_played = user_data["TPistolRoundsPlayed"]
    t_pistol_won = user_data["TPistolRoundsWins"]

    # Beregn data


    # Opret svar-objekt med de modtagne data og beregnede killavg
    response_data = {
        "username": name,

    }

    # Returner data som JSON
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(debug=True)
