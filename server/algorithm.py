def get_distance(trex, obstacle):
	return obstacle['top_left'][0] - trex['top_left'][0]

def get_command(trex, obstacles):
	if (not trex):
		return ''

	infront_obstacles = [o for o in obstacles if get_distance(trex, o) > 0]

	if (len(infront_obstacles) == 0):
		return ''

	nearest_obstacle = min(infront_obstacles, key=lambda o:o['top_left'][0])
	nearest_distance = get_distance(trex, nearest_obstacle)

	if (nearest_obstacle['bottom_right'][1] < trex['top_left'][1]):
		return ''

	if (nearest_distance < 400):
		return 'jump'

	return ''
