from flask.json import jsonify
from website import create_app, formatting_price, create_dataframe, make_pred
from flask import render_template, request, url_for, Flask
# from flask_ngrok import run_with_ngrok


# , render_template, request, url_for

app = create_app()



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def predict():
    data = request.form.to_dict()
    return render_template('index.html')
 

@app.route('/getformdata', methods=['POST'])
def getformdata():
    data = request.get_json()
    predicted_price = make_pred(create_dataframe(data))
    formated_price = formatting_price(predicted_price[0])
    response_data = { 'message': 'Message received', 'status': 200, 'data': formated_price }
    return jsonify(response_data)




if __name__ == '__main__':
    app.run()