from flask import Flask, render_template
from flask_socketio import SocketIO,  emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_cube_rotation')
def handle_cube_rotation(data):
    emit('update_cube_rotation', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
