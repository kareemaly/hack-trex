import socketio
import eventlet
from template_matching import get_game_state
from algorithm import get_command

# create a Socket.IO server
sio = socketio.Server()

@sio.on('send_screenshot')
def send_screenshot(sid, screenshot):
	game_state = get_game_state(screenshot.replace('data:image/png;base64,', ''))
	trex = game_state['trex_location']
	obstacles = game_state['obstacle_locations']
	command = get_command(trex, obstacles)
	sio.emit('execute_command', command)

def main():
	# wrap with a WSGI application
	app = socketio.WSGIApp(sio)
	eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

if __name__ == '__main__':
	main()
