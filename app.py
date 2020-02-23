import pickle
from flask import Flask, request, jsonify
import sklearn

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
print(model)
labels = {0: "versicolor",  1: "setosa", 2: "virginica"}


@app.route('/api', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict = model.predict(data['X'])
    return jsonify([labels[i] for i in predict])

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
