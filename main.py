import base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/pubsub", methods=["POST"])
def pubsub_handler():
    """Receive and parse Pub/Sub messages."""
    received_request = request.get_json()
    if not received_request:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(received_request, dict) or "message" not in received_request:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    received_message = received_request["message"]

    data = "default message is empty"
    if isinstance(received_message, dict) and "data" in received_message:
        data = base64.b64decode(received_message["data"]).decode("utf-8").strip()

    if data is not None:
        print(f"Received message: {data}")
        # Add custom message processing logic.
        
    return ("", 204)

if __name__ == "__main__":
    app.run(debug=True)
