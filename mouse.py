"""Dummy mouse automation API."""


def click(button, clicks):
	return True


def move_to():
	return True


def scroll():
	return True


def clicked():
	"""Returns clicked status: x, y, button type and no_clicks of last click performed"""
	x = 0
	y = 0
	button = "left"
	clicks = 1
	return (x, y, button, clicks)


def pos_x():
	x = 0
	return x


def pos_y():
	y = 0
	return y
