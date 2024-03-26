from flask import Flask, request, jsonify

import Analysis
import Repo

app = Flask(__name__)


def fetch_user_data_from_database(userid):
    connection = Repo.connect_to_database()
    cursor = connection.cursor()
    query = """SELECT * FROM placeholder WHERE id = %s"""
    cursor.execute(query, (userid,))
    user_data = cursor.fetchone()  #Skal nok laves om til fetchall
    cursor.close()
    connection.close()
    return user_data
@app.route("/get-user", methods=["POST"])
def get_user():
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

    # Beregn killavg
    killavg = Analysis.player_analysis_mean(kills)

    # Opret svar-objekt med de modtagne data og beregnede killavg
    response_data = {
        "killavg": killavg
    }

    # Returner data som JSON
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(debug=True)
