#!/usr/bin/env python3

codes = []

for c in 'Hello, world!':
    codes.append('{0:08b}'.format(ord(c)))

radius = 8
gap = 5
stroke_width = 3


def circle(x, y):
    print("""<ellipse
       style="fill:none;stroke:#fffffe;stroke-width:{};stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       id="path817"
       cx="{}"
       cy="{}"
       rx="{}"
       ry="{}"
       />""".format(stroke_width, x, y, radius, radius))


for i, c in enumerate(codes):
    for j, d in enumerate(c):
        x = gap + radius + j * (gap + 2 * radius)
        y = gap + radius + i * (gap + 2 * radius)
        circle(x, y)
