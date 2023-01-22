from requests import get
from json import loads
from flask import Flask, render_template, url_for, request, redirect
# dodać odswieżanie i dodawanie do html


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def weather():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        url = 'https://danepubliczne.imgw.pl/api/data/synop'
        response = get(url)
        for row in loads(response.text):
            if request.form.get('miasto') not in row['stacja']:
                cities = [row['stacja'] for row in loads(response.text)]
                return render_template('error.html', cities=cities)

            if row['stacja'] == request.form.get('miasto'):
                miasto = row['stacja']
                data = row['data_pomiaru']
                godzina = row['godzina_pomiaru']
                temperatura = row['temperatura']
                cisnienie = row['cisnienie']

                return render_template('index.html', miasto=miasto, data=data, godzina=godzina,
                                       temperatura=temperatura, cisnienie=cisnienie)


if __name__ == '__main__':
    app.run(debug=True)
