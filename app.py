from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app) 

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    print(f"Received message, {data}")
    emit('new_notification', {'message': 'u got a new mesage'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
