"""Pytest module for an imaginary Automated Mouse API"""
from delayed_assert import expect, assert_expectations
import mouse as m
import time as t


class TestClick:
	# Optional performance test attribute
	max_response_time = 0.001
	# Default click attributes
	button = "left"
	clicks = 1

	def test_click(self):
		t1 = t.time()
		output = m.click(self.button, self.clicks)
		# Test returned output, assume for now that fn returns "True"
		expect(output is True)
		# Test that API mouse status reported by clicked() is as expected
		x, y, button, clicks = m.clicked()
		t2 = t.time()
		expect(x == m.pos_x())
		expect(y == m.pos_y())
		expect(button == self.button)
		expect(clicks == self.clicks)
		expect(t2 - t1 < self.max_response_time)
		assert_expectations()


class TestClickLeft(TestClick):
	button = "left"
	clicks = 1

	def test_OOR(self):
		pass


class TestClickRight(TestClick):
	button = "right"
	clicks = 1


class TestClickRightDouble(TestClick):
	button = "right"
	clicks = 2


class TestPosition:
	pass


class Test_X(TestPosition):
	def test_x_good(self):
		pass

	def test_y(self):
		pass
