"""Dummy mouse automation module"""
import tkinter as tk


class Mouse:

	def __init__(self, x, y, scroll):
		# Initial mouse position
		self.x = 0
		self.y = 0
		self.scroll = 0
		self.logger = []

	def get_screen_width(self):
		root = tk.Tk()
		return root.winfo_screenwidth()

	def validate(self, posn):
		# some basic validation
		if posn > self.get_screen_width() or posn < 0 or type(posn) is not int:
			return False
		else:
			return True

	def log_a_warning(self):
		self.logger.append("'User warning: Please input a valid mouse position.'")
		print(self.logger[-1])

	def move_to(self, x, y):
		# move cursor to x, y

		if self.validate(x):
			self.x = x
		else:
			self.log_a_warning()
			return False

		# validate y here
		#

		print(f"'User info: Mouse moved to {x}, {y}!'")
		return True

	def click(self, button, clicks):
		# perform a click with L or R button and single or dbl click
		self.button = button
		self.clicks = clicks
		return True

	def select(self, x, y, button, clicks):
		# move mouse cursor and perform a click
		self.move_to(x, y)
		self.click(button, clicks)
		return True

	def scroll(self, x, y, z):
		# perform a vertical scroll at x,y posn by amount z
		self.scroll += z
		return True

	def clicked(self):
		"""Get click status: x, y, button type and no_clicks of last click performed"""
		return self

	def pos_x(self):
		# get cursor pos x
		return True

	def pos_y(self):
		# get cursor pos y
		return True


def main():
	# example
	m = Mouse(0, 0)
	m.click("left", 1)
	m.select(1000, 150, "right", 2)


if __name__ == '__main__':
	main()
