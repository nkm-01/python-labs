#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
def bubble():
	center = sd.Point()
	sd.circle(center, 50)
	sd.circle(center, 45)
	sd.circle(center, 40)
bubble()
sd.sleep(5)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_bubble(center: sd.Point = sd.Point(),
                radius: int = 50,
                step: int = 5,
                color: (int, int, int) = sd.random_color()) -> None:
	sd.circle(center, radius, color)
	sd.circle(center, radius - step, color)
	sd.circle(center, radius - step * 2, color)

# Нарисовать 10 пузырьков в ряд
sd.clear_screen()
for i in range(1, 11):
	draw_bubble(sd.Point(100 * i, 100))
sd.sleep(5)

# Нарисовать три ряда по 10 пузырьков
sd.clear_screen()
for y in range(1, 4):
	for x in range(1, 11):
		draw_bubble(sd.Point(100 * x, 100 * y))
sd.sleep(5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.clear_screen()
for _ in range(100):
	draw_bubble(center=sd.Point(), color=sd.random_color())
sd.pause()
