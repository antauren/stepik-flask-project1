from flask import Flask, render_template

from data import tours, departures, title, subtitle, description

tours_dict = tours.copy()
for id_, tour in tours_dict.items():
    tour['id'] = id_

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',

                           tours=list(tours_dict.values()),
                           departures=departures,

                           title=title,
                           subtitle=subtitle,
                           description=description,
                           tour=False
                           )


@app.route('/departures/<departure>/')
def render_departures(departure):
    request_tours = [tour for tour in tours_dict.values() if tour['departure'] == departure]

    return render_template('departure.html',

                           tours=request_tours,
                           departures=departures,
                           departure=departures[departure],
                           tour=False
                           )


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html',

                           tour=tours_dict[id],
                           departures=departures
                           )


if __name__ == '__main__':
    app.run()
