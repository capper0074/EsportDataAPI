from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-user", methods=["POST"])
def get_user():
    # Få JSON-data fra request'en
    data = request.json

    # Kontroller om data er til stede og indeholder de nødvendige felter
    if data is None or "name" not in data or "kills" not in data or "assists" not in data or "deaths" not in data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Udtræk nødvendige oplysninger fra JSON-data
    name = data["name"]
    kills = data["kills"]
    assists = data["assists"]
    deaths = data["deaths"]

    # Behandling af data (her kan du tilføje din egen logik)
    # I dette eksempel oprettes der bare et svar-objekt med de modtagne data
    response_data = {
        "name": name,
        "kills": kills,
        "assists": assists,
        "deaths": deaths,
    }

    # Returner data som JSON
    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(debug=True)