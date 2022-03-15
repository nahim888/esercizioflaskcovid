from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")

@app.route('/', methods=['GET'])
def index():
    reg = df['nome_area'].drop_duplicates().to_list()
    return render_template('indexes1.html', reg=reg)

@app.route('/risp', methods=['GET', 'POST'])
def risp():
    regioni = request.form.getlist('check')
    df3 = []
    for regione in regioni:
        df2 = df[df['nome_area']== regione]
        df3.append(df2)
    df3 = pd.concat(df3)
    return render_template('indexes2.html', tables=[df3.to_html()], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)
