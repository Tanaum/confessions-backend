from flask import Flask, request, jsonify
from dbCode import StoreNewConfession, RetrieveConfessions

app = Flask(__name__)

#POST NEW CONFESSION
@app.route("/new-confession/<ConfessorName>/<ConfessionData>", methods=["POST"])
def NewConfession(ConfessorName,ConfessionData):
    IPAddr = request.remote_addr
    print(IPAddr)

    value = StoreNewConfession(ConfessorName, ConfessionData, IPAddr)

    if value["Value"] == True:
        return jsonify(value), 200
    elif value["Value"] == False:
        return jsonify(value), 400


#GET ALL CONFESSIONS
@app.route("/all-confessions", methods=["GET"])
def AllConfessions():
    value = RetrieveConfessions()
    return jsonify(value), 200

if __name__ == "__main__":
    app.run(debug=True)