from flask import Flask, jsonify
import database_server as db

app = Flask(__name__)
db_manager = db.DatabaseManager()

@app.route("/", methods =['GET'])
def hello():
    return jsonify(status="running")

@app.route('/dataparking', methods=['GET'])
def data_parking():
    try:
        data_parking = db_manager.get_parking()
        if not data_parking:
            return jsonify(message="Data not found"), 404

        return jsonify(data_parking=data_parking)
    except Exception as e:
        return jsonify(error=str(e)), 500
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)