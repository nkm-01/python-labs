#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(a: int | sd.Point, # x or center
               b: int | tuple[int, int, int], # y or color
               c: tuple[int, int, int] | None = None): # color if a, b is x, y, else None
	"""
	draw_smile(center, color) OR draw_smile(center_x, center_y, color)
	Draws a smile face
	"""
	center = a if not c else sd.Point(a, b)
	color = b if not c else c

	left_eye = sd.Point(center.x - 17, center.y + 20)
	right_eye = sd.Point(center.x + 17, center.y + 20)
	smile = [
		sd.Point(center.x - 25, center.y - 5 ),
		sd.Point(center.x - 15, center.y - 15),
		sd.Point(center.x + 0 , center.y - 20),
		sd.Point(center.x + 15, center.y - 15),
		sd.Point(center.x + 25, center.y - 5 ),
	]

	sd.circle(center, 50, color)
	sd.circle(left_eye, 10, color)
	sd.circle(right_eye, 10, color)
	sd.lines(smile, color)

for _ in range(10):
	draw_smile(sd.random_point(), sd.random_color())
sd.pause()
