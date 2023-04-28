from flask import Flask,render_template,jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/getweatherdata')
def getdate():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": 44.34,
        "lon": 10.99,
        "appid": ""
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
        print("Weather data:", data)
    else:
        return "error"
        print(f"Error {response.status_code}: {response.text}")

def get_weather_data(lat, lon, appid):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": appid
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/weather_data/<float:lat>/<float:lon>')
def weather_data(lat, lon):
    appid = "356ebba58f9edb6a663e344d7fd81b43"
    data = get_weather_data(lat, lon, appid)

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch weather data."}), 500


def hello_world():
    return 'Hello World'

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

if __name__ == "__main__":
    app.run()
