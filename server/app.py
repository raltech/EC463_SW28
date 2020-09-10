from flask import Flask, jsonify, request
import db

app = Flask(__name__)


@app.route('/user/<string:user_id>/sensors', methods=['GET'])
def get_sensors(user_id: str):
    conn = db.getConnection()
    print(db.getSensors(conn, user_id))
    return jsonify(success=True)


@app.route('/user/<string:user_id>/sensors', methods=['POST'])
def add_sensor(user_id: str):
    conn = db.getConnection()
    try:
        db.addSensor(
            conn, user_id, request.json['sensorType'], request.json['name'])
    except:
        return "Need to supply sensorType: {'temperature', 'humidity} and name", 400
    return jsonify(success=True)


if __name__ == "__main__":
    app.run()
