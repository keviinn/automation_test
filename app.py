from flask import Flask, request
import pickle
app = Flask(__name__)
MODEL = pickle.load(open('a_model', 'rb'))
@app.route('/', methods=['POST'])
def post_route():
    if request.method == 'POST':
        data = request.get_json()
        results = MODEL.predict(data)
        return str(results) + '\n\n'
app.run(host="0.0.0.0")
