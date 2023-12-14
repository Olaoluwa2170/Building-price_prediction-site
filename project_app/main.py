from flask.json import jsonify
from website import create_app, predict_prices, formatting_price
from flask import render_template, request, url_for


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
    inputs = list(data.values())
    predicted_price  = formatting_price(predict_prices(inputs))
    response_data = { 'message': 'Message received', 'status': 200, 'data': predicted_price }
    return jsonify(response_data)




if __name__ == '__main__':
    app.run(debug=True)