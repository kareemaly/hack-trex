import cv2
import numpy as np
import base64

def find_piece(screenshot, piece):
	width, height = piece.shape[::-1]

	result = cv2.matchTemplate(screenshot, piece, cv2.TM_CCOEFF_NORMED)
	locations = []

	while True:
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		if (max_val > 0.9):
			top_left = max_loc
			bottom_right = (top_left[0]+width, top_left[1]+height)
			locations.append({
				'top_left': top_left,
				'bottom_right': bottom_right,
			})
			result[max_loc[::-1]] = 0
		else:
			break

	return locations

def get_cropped_piece(pieces, x, y, width, height):
	return pieces[y:y+height, x:x+width]

def from_base64(base64_data, flags):
    nparr = np.frombuffer(base64.b64decode(base64_data), np.uint8)
    return cv2.imdecode(nparr, flags)

def get_game_state(base64_screenshot):
	screenshot = from_base64(base64_screenshot, cv2.IMREAD_GRAYSCALE)
	pieces = cv2.imread('./images/pieces.png', cv2.IMREAD_GRAYSCALE)

	trex = get_cropped_piece(pieces, 1678, 0, 87, 87)

	obstacles = [
		get_cropped_piece(pieces, 652, 0, 50, 80),
		get_cropped_piece(pieces, 652 + 50, 0, 50, 80),
		get_cropped_piece(pieces, 652 + 100, 0, 50, 80),
		get_cropped_piece(pieces, 652 + 150, 0, 48, 80),
		get_cropped_piece(pieces, 652 + 198, 0, 100, 80),
		get_cropped_piece(pieces, 446, 0, 34, 60),
		get_cropped_piece(pieces, 446+34, 0, 34, 60),
		get_cropped_piece(pieces, 446+34*2, 0, 34, 60),
		get_cropped_piece(pieces, 446+34*3, 0, 34, 60),
		get_cropped_piece(pieces, 446+34*4, 0, 34, 60),
		get_cropped_piece(pieces, 446+34*5, 0, 34, 60),
	]

	trex_location = find_piece(screenshot, trex)
	obstacle_locations = [location for obstacle in obstacles for location in find_piece(screenshot, obstacle)]
	obstacle_locations = list({ o['top_left']:o for o in obstacle_locations }.values())

	return {
		'trex_location': trex_location,
		'obstacle_locations': obstacle_locations,
	}
