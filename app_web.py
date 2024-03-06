from flask import Flask, request, jsonify

app = Flask(__name__)

data = ""
@app.route('/post-number', methods=['POST', 'GET'])
def fun():
    global data
    if request.method == 'POST':
        data = request.json
        cas = data.get('cas')
        print(cas)
        return cas

    elif request.method == 'GET':
        return data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
