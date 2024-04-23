import uuid

import Analysis
import KasperDummeDatabase
import Repo

from typing import Union

from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.post("/test")
def test():
    hej = "hej"
    hejsa = "ejsa"
    response_data = {
        "test": hej,
        "test2": hejsa
    }
    return response_data, status.HTTP_200_OK

@app.post("/get-user_stats/{userid}")
async def get_user_stats(userid: uuid.UUID):
    # Hent brugeroplysninger fra den simulerede database
    user_data = KasperDummeDatabase.fetch_team_player_stats(userid)

    # Kontroller om brugeren findes i databasen
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Udtræk nødvendige oplysninger fra brugeroplysningerne
    name = int(user_data["PlayerId"])
    kills = user_data["Kills"]
    assists = user_data["Assists"]
    deaths = user_data["Deaths"]
    headshots = user_data["Headshots"]


    # Beregn killavg
    kill_avg = Analysis.player_analysis_mean(kills)
    death_avg = Analysis.player_analysis_mean(deaths)
    assist_avg = Analysis.player_analysis_mean(assists)
    headshot_per = Analysis.player_headshot_per(kills, headshots)


    # Opret svar-objekt med de modtagne data og beregnede data
    response_data = {
        "username": name,
        "kill_avg": kill_avg,
        "death_avg": death_avg,
        "assist_avg": assist_avg,
        "headshot_per": headshot_per

    }

    # Returner data som JSON
    return response_data, status.HTTP_200_OK

@app.post("/get-user_single_mapdata/{teamid}/{mapid}")
async def get_user_mapdata(teamid: int, mapid: int):
    # Hent brugeroplysninger fra den simulerede database
    user_data = KasperDummeDatabase.fetch_team_match_stats(KasperDummeDatabase.fetch_match_id(KasperDummeDatabase.fetch_match_id(mapid), teamid), teamid)

    # Kontroller om brugeren findes i databasen
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

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
    map_kills_mean = Analysis.player_analysis_mean2(kills, matches_played)
    map_deaths_mean = Analysis.player_analysis_mean2(deaths, matches_played)
    map_assists_mean = Analysis.player_analysis_mean2(assists, matches_played)

    # Opret svar-objekt med de modtagne data og beregnede killavg
    response_data = {
        "username": name,
        "map": mapid,
        "avg_kills": map_kills_mean,
        "avg_deaths": map_deaths_mean,
        "avg_assists": map_assists_mean,
    }

    return response_data, status.HTTP_200_OK

if __name__ == "__main__":
    app.run(debug=True)
