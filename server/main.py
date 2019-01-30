import socketio
import eventlet
from template_matching import get_game_state

# create a Socket.IO server
sio = socketio.Server()

@sio.on('send_screenshot')
def send_screenshot(sid, screenshot):
	print(get_game_state(screenshot.replace('data:image/png;base64,', '')))
	# print('recieved screenshot', screenshot)
	# sio.emit('execute_command', 'jump')

def main():
	# wrap with a WSGI application
	app = socketio.WSGIApp(sio)
	eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

if __name__ == '__main__':
	main()
