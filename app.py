from flask import Flask, render_template

from data import tours, departures

tours_dict = tours.copy()
for id_, tour in tours_dict.items():
    tour['id'] = id_

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', tours=tours_dict.values())


@app.route('/departures/<departure>/')
def render_departures(departure):
    request_tours = [tour for tour in tours_dict.values() if tour['departure'] == departure]

    return render_template('departure.html',

                           tours=request_tours,
                           departures=departures,
                           departure=departures[departure],

                           price_list=[tour['price'] for tour in request_tours],
                           nights_list=[tour['nights'] for tour in request_tours]
                           )


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html',

                           tour=tours_dict[id],
                           departures=departures)


app.run(debug=True)
