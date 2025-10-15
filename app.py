# from flask import Flask, request, jsonify
# import psycopg2
# from psycopg2.extras import RealDictCursor

# app = Flask(__name__)

# # Database connection details
# DB_CONFIG = {
#     'host': 'localhost',
#     'database': 'iot_dashboard',
#     'user': 'postgres',
#     'password': 'Dharsri*22'
# }

# def get_connection():
#     return psycopg2.connect(**DB_CONFIG)

# @app.route('/')
# def home():
#     return "IoT Backend is running"

# @app.route('/api/sensor-data', methods=['POST'])
# def insert_sensor_data():
#     data = request.get_json()
#     village_id = data.get('village_id', 1)  # Default: 1
#     value1 = data.get('ph')
#     value2 = data.get('turbidity')

#     try:
#         conn = get_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO sensor_data (village_id, value1, value2) VALUES (%s, %s, %s)",
#             (village_id, value1, value2)
#         )
#         conn.commit()
#         cur.close()
#         conn.close()
#         return jsonify({"message": "Data inserted successfully"})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route('/api/latest', methods=['GET'])
# def get_latest_data():
#     try:
#         conn = get_connection()
#         cur = conn.cursor(cursor_factory=RealDictCursor)
#         cur.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 1")
#         row = cur.fetchone()
#         cur.close()
#         conn.close()
#         return jsonify(row)
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------
# Routes
# ------------------------------

@app.route('/')
def home():
    return "IoT Backend is running"

# POST route (optional, will just return success without DB for demo)
@app.route('/api/sensor-data', methods=['POST'])
def insert_sensor_data():
    data = request.get_json()
    village_id = data.get('village_id', 1)  # Default: 1
    ph = data.get('ph')
    turbidity = data.get('turbidity')

    # For demo, we are not storing in DB
    return jsonify({
        "message": "Data received successfully",
        "village_id": village_id,
        "ph": ph,
        "turbidity": turbidity
    })

# GET route for latest data (mock data for both villages)
@app.route('/api/latest', methods=['GET'])
def get_latest_data():
    return jsonify({
        "villages": [
            {"village_id": 1, "name": "Chennai", "lat": 13.0843, "lon": 80.2705, "ph": 7.3, "turbidity": 4.8},
            {"village_id": 2, "name": "Coimbatore", "lat": 10.9974, "lon": 76.9589, "ph": 7.1, "turbidity": 5.0}
        ]
    })

# ------------------------------
# Main
# ------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
