#!/usr/bin/env python3

codes = []

text = 'Hello, world!'
for c in text:
    codes.append('{0:08b}'.format(ord(c)))

margin_left = 0
margin_top = 0

radius = 8
gap = 5
stroke_width = 3
color = '#ffffff'


def circle(x, y):
    print("""<ellipse
       style="fill:none;stroke:{};stroke-width:{};stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
       id="path817"
       cx="{}"
       cy="{}"
       rx="{}"
       ry="{}"
       />""".format(color, stroke_width, x, y, radius, radius))


def vertical_stroke(cx, cy):
    x = cx
    y = cy - radius
    height = 2 * radius
    print("""<rect
   style="fill:none;fill-opacity:1;stroke:{};stroke-width:{};stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
   width="1"
   height="{}"
   x="{}"
   y="{}" />""".format(color, stroke_width, height, x, y))


for i, c in enumerate(codes):
    for j, d in enumerate(c):
        x = margin_left + gap + radius + j * (gap + 2 * radius)
        y = margin_top + gap + radius + i * (gap + 2 * radius)
        if d == '0':
            circle(x, y)
        if d == '1':
            vertical_stroke(x, y)
