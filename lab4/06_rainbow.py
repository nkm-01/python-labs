#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start = sd.Point(50, 50)
end = sd.Point(350, 450)
for color in rainbow_colors:
    sd.line(start, end, color, 4)
    start = sd.Point(start.x + 5, start.y)
    end = sd.Point(end.x + 5, end.y)
sd.sleep(5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
sd.clear_screen()

center = sd.Point(400, -100)
radius = 500
for color in rainbow_colors:
    sd.circle(center, radius, color, 4)
    radius -= 5

sd.pause()
