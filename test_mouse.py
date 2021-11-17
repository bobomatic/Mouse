"""Pytest module for an imaginary Automated Mouse module"""
from mouse import Mouse
import tkinter as tk


class Helper:
	def get_screen_width():
		root = tk.Tk()
		return root.winfo_screenwidth()

	def get_screen_height():
		pass


class TestMoveTo:
	# Default mouse test attributes
	x = 1000
	y = 500

	def test_x_good(self):
		# Test the returned output. Assume for now that fn returns "True". 
		m = Mouse(0, 0, 0)
		output = m.move_to(self.x, self.y)
		assert output is True

	def test_x_zero(self):
		m = Mouse(400, 500, 0)
		self.x = 0
		output = m.move_to(self.x, self.y)
		assert output is True

	def test_x_max(self):
		# x equals the screen size
		m = Mouse(0, 0, 0)
		self.x = Helper.get_screen_width()
		print(f"[x = {self.x} pixels]", end=' ')
		output = m.move_to(self.x, self.y)
		assert output is True

	def test_x_OOR_pos(self):
		# what if x is larger than the screen size
		m = Mouse(0, 0, 0)
		self.x = Helper.get_screen_width() + 1
		print(f"[x = {self.x} pixels (off screen)]", end=' ')
		output = m.move_to(self.x, self.y)
		assert output is False

	def test_x_OOR_pos_check_error_msg(self):
		# example of checking a warning message
		m = Mouse(0, 0, 0)
		self.x = Helper.get_screen_width() + 1
		print(f"[x = {self.x} pixels (off screen)]", end='')
		m.move_to(self.x, self.y)
		assert m.logger[-1] == "'User warning: Please input a valid mouse position.'"

	def test_x_OOR_neg(self):
		m = Mouse(0, 0, 0)
		self.x = -1
		output = m.move_to(self.x, self.y)
		assert output is False

	def test_x_wrong_type(self):
		# Demo of a fail
		m = Mouse(0, 0, 0)
		print("[Example of application not handling an error]")
		self.x = "I AM A WRONG TYPE!"
		output = m.move_to(self.x, self.y)
		assert output is False

	# Test y inputs here
	#
	#
	#


class TestClickLeft:
	def test_something(self):
		pass

	def test_something_else(self):
		pass


class TestClickRight:
	def test_something(self):
		pass

	def test_something_else(self):
		pass


# More test groupings below
#
#
#
