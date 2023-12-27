from flask import Flask
import pickle
import numpy as np
import pandas as pd
import locale
# from flask_ngrok import run_with_ngrok

model = pickle.load(open('project_app\website\static\model.pkl', 'rb'))
scaler_X = pickle.load(open('project_app\website\static\scaler_x', 'rb'))
scaler_y = pickle.load(open('project_app\website\static\scaler_y', 'rb'))

def create_app():
    app = Flask(__name__)
    return app

def formatting_price(amount):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
     #Format the number as currency (Naira) and append the Naira symbol manually
    formatted_amount = f"₦ {locale.format_string('%.2f', amount, grouping=True)}"
    return formatted_amount



slot_numbers = ['bedrooms', 'bathrooms', 'toilets', 'parking_space']

towns = ['Agbara-Igbesa', 'Agege', 'Ajah', 'Alimosho', 'Amuwo Odofin', 'Apapa',
       'Ayobo', 'Badagry', 'Egbe', 'Ejigbo', 'Eko Atlantic City', 'Epe',
       'Gbagada', 'Ibeju', 'Ibeju Lekki', 'Idimu', 'Ifako-Ijaiye', 'Ijaiye',
       'Ijede', 'Ijesha', 'Ikeja', 'Ikorodu', 'Ikotun', 'Ikoyi', 'Ilupeju',
       'Imota', 'Ipaja', 'Isheri', 'Isheri North', 'Isolo', 'Ketu', 'Kosofe',
       'Lagos Island', 'Lekki', 'Magodo', 'Maryland', 'Mushin', 'Ogudu', 'Ojo',
       'Ojodu', 'Ojota', 'Oke-Odo', 'Orile', 'Oshodi', 'Shomolu', 'Surulere',
       'Victoria Island (VI)', 'Yaba']

building_types = ['Block of Flats', 'Detached Bungalow', 'Detached Duplex',
       'Semi Detached Bungalow', 'Semi Detached Duplex', 'Terraced Bungalow',
       'Terraced Duplexes']

# scaler_X = StandardScaler()
# scaler_y = StandardScaler()
def create_dataframe(input_list):
    data = {'bedrooms':input_list['bedrooms'], 'bathrooms':input_list['bathrooms'], 'toilets':input_list['toilets'], 'parking_space':input_list['parking_space']}
    data.update({title: title == input_list['title'] for title in building_types})
    data.update({town: town == input_list['town'] for town in towns})
    df = pd.DataFrame([data])
    return df

def make_pred(input):
    input_scaled = scaler_X.transform(input)
    y_pred = model.predict(input_scaled)
    y_pred_unscaled = scaler_y.inverse_transform(y_pred).flatten()
    return y_pred_unscaled.astype('int64')

# trying = create_dataframe({'bedrooms': '2', 'bathrooms': '2', 'toilets': '1', 'parking_space': '2', 'title': 'Detached Duplex', 'town': 'Ibeju Lekki'})
# print(make_pred(trying))



