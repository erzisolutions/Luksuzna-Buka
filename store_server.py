from flask import Flask, jsonify, request

app = Flask(__name__, static_folder='webapp')

PIES = [
    {"id": 1, "name": "Drugarica sa sirom", "price": 350},
    {"id": 2, "name": "Drugarica sa mesom", "price": 400},
    {"id": 3, "name": "Drugarica sa zeljem", "price": 360},
    {"id": 4, "name": "Drugarica sa krompirom", "price": 340},
]

@app.route('/')
def index():
    return app.send_static_file('drugarica_store.html')

@app.route('/pies')
def pies():
    return jsonify(PIES)

@app.route('/checkout', methods=['POST'])
def checkout():
    order = request.get_json(force=True)
    total = 0
    for item in order.values():
        total += item.get('qty', 1) * item.get('price', 0)
    return jsonify({'status': 'ok', 'total': total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
