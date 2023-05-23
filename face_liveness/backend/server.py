from flask import Flask, jsonify, request

from face_liveness.backend.aws import create_session, get_session_results

app = Flask(__name__)


@app.route('/getsessionid')
def getsessionid():
    session_id = create_session()
    return jsonify({'sessionId': session_id})


@app.route('/processended')
def processended():
    session_id = request.args.get('sessionId')
    status = get_session_results(session_id)
    return jsonify({'status': status})


if __name__ == '__main__':
    app.run(port=4242)
