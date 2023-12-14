from flask import Flask
import pickle
import numpy as np
import pandas as pd
import locale

model_2 = pickle.load(open('project_app\website\model.pkl', 'rb'))

def create_app():
    app = Flask(__name__)
    return app

def predict_prices(inputs):
    input_data = np.array(inputs).reshape(1, -1)
    columns = ['bedrooms', 'bathrooms', 'toilets', 'parking_space', 'title', 'town']
    input_df = pd.DataFrame(input_data, columns=columns)
    result = model_2.predict(input_df)
    return int(result)

def formatting_price(amount):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
     #Format the number as currency (Naira) and append the Naira symbol manually
    formatted_amount = f"₦ {locale.format_string('%.2f', amount, grouping=True)}"
    return formatted_amount