from flask import Flask, render_template
import pandas as pd
from database import df


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/dataprocessing')
def dataprocessing():
    return render_template('dataprocessing.html')


@app.route('/dataset')
def dataset():
    df = pd.read_csv('loan_data.csv')
    dataset = df.head(50).to_dict(orient='records')
    return render_template('dataset.html', dataset=dataset)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





