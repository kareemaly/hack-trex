const io = require('socket.io-client');

const socket = io('localhost:8000');

const dispatchKeyboardEvent = (keyCode) => {
	const event = new KeyboardEvent('keydown', { keyCode });
	document.dispatchEvent(event);
}

socket.on('execute_command', (command) => {
	switch(command) {
		case 'jump':
			dispatchKeyboardEvent(32);
			break;
		case 'duck':
			dispatchKeyboardEvent(40);
			break;
	}
})

setInterval(() => {
	const element = document.getElementsByClassName('runner-canvas')[0];
	const screenshot = element.toDataURL();
	socket.emit('send_screenshot', screenshot);
}, 1000);

