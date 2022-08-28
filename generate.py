#!/usr/bin/env python3

codes = []

for c in 'Hello, world!':
    codes.append('{0:08b}'.format(ord(c)))

for c in codes:
    print(c)

radius = 8
gap = 2

for i, c in enumerate(codes):
    for j, d in enumerate(c):
        x = gap + radius + j * (gap + 2 * radius)
        y = gap + radius + i * (gap + 2 * radius)
        print("""<ellipse
           style="fill:none;stroke:#fffffe;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path817"
           cx="{}"
           cy="{}"
           rx="{}"
           ry="{}"
           />""".format(x, y, radius, radius))
