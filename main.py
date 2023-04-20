from flask_socketio import SocketIO
from server.views import app
from server.logcolors import Color


socketio = SocketIO(app, cors_allowed_origins="*", static_url_path='/server/static')

@socketio.on('connect')
def handle_connect():
    print(Color('green', 'User connected'))

@socketio.on('disconnect')
def handle_disconnect():
    print(Color('green', 'User disconnected'))

@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data)
    print(Color('green', data['username'] + ": " + data['message']))

if __name__ == '__main__':
    socketio.run(app)
    print(Color('green', 'Server successfully disabled'))