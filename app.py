from flask import Flask, render_template, request, jsonify
import requests
import datetime
import json
from pnr import getpnrdetails

app = Flask(__name__)

class Train:
    def __init__(self, train_no='12954', date=datetime.datetime.now().strftime("%d-%m-%Y")):
        self.train_no = train_no
        self.date = date

    def gettrainlivestatus(self):
        params = {
            'train_no': str(self.train_no),
            'lang': 'en',
            'date': str(self.date),
        }
        response = requests.get('https://whereismytrain.in/cache/live_status', params=params)
        return response.json()

def gettraindelayinfo(stations, train):
    for i in range(len(train.gettrainlivestatus()["days_schedule"])):
        if train.gettrainlivestatus()["days_schedule"][i]["station_code"] == train.gettrainlivestatus()["curStn"]:
            return f"{train.gettrainlivestatus()['days_schedule'][i-1]['delay_in_arrival']} minutes at station {stations[train.gettrainlivestatus()['days_schedule'][i-1]['station_code']]} {train.gettrainlivestatus()['days_schedule'][i-1]['station_code']}"
    return 'No delay info'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getstatus", methods=["POST"])
def get_status():
    train_no = request.form.get("train_no")
    date = request.form.get("date")
    if not date:
        date = datetime.datetime.now().strftime("%d-%m-%Y")
    
    train = Train(train_no, date)
    with open('stations.json', 'r') as f:
        stations = json.load(f)

    action = request.form.get("action")
    
    if action == "1":
        status = train.gettrainlivestatus()
        return jsonify({
            "train_name": status["train_name"],
            "train_type": status["train_type"],
            "source_station": f'{stations[status["source_station"]]} {status["source_station"]}',
            "current_station": f'{stations[status["curStn"]]} {status["curStn"]}',
            "next_station": f'{status["pitstop_next_to_curstn"]["station_code"]} {stations[status["pitstop_next_to_curstn"]["station_code"]]}',
            "destination_station": f'{stations[status["destination_station"]]} {status["destination_station"]}'
        })

    elif action == "2":
        station_code = request.form.get("station_code")
        days_schedule = train.gettrainlivestatus()["days_schedule"]
        platform = next((item["platform"] for item in days_schedule if item["station_code"] == station_code), "N/A")
        return jsonify({"platform": platform})

    elif action == "3":
        delay_info = gettraindelayinfo(stations, train)
        return jsonify({"delay_info": delay_info})

    elif action == "4":
        pnr = request.form.get("pnr")
        pnr_details = getpnrdetails(pnr)
        return jsonify({"pnr_details": pnr_details})

    elif action == "5":
        return jsonify(train.gettrainlivestatus())

if __name__ == "__main__":
    app.run(debug=True)
