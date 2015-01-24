# SUPERSHAPE - last updated for NodeBox 1.9.4
# Author: Frederik De Bleser <frederik@pandora.be>
# Copyright (c) 2006 by Frederik De Bleser.
# See LICENSE.txt for details.

# The superformula was published by Johan Gielis,
# you may use it in NodeBox for non-commercial purposes.

from math import pi, sin, cos, pow
from nodebox.graphics import Path
_range = range

TWOPI = pi * 2


# Else, use the native python
# calculation of supershapes.
def supercalc(m, n1, n2, n3, phi):
    a = 1.0
    b = 1.0

    t1 = cos(m * phi / 4) / a
    t1 = abs(t1)
    t1 = pow(t1, n2)

    t2 = sin(m * phi / 4) / b
    t2 = abs(t2)
    t2 = pow(t2, n3)

    r = pow(t1 + t2, 1 / n1)
    if abs(r) == 0:
        return (0, 0)
    else:
        r = 1 / r
        return (r * cos(phi), r * sin(phi))


def path(position, width, height, m, n1, n2, n3, points=1000, percentage=1.0, range=TWOPI):
    path = Path()
    for i in _range(points):
        if i > points*percentage:
            continue
        phi = i * range / points
        dx, dy = supercalc(m, n1, n2, n3, phi)
        dx = (dx * width / 2) + position.x
        dy = (dy * height / 2) + position.y
        path.addPoint(dx, dy)
    return path


def transform(path, m, n1, n2, n3, scale=1.0, points=100, range=TWOPI):
    new_path = Path()
    for i in _range(points):
        pt = path.pointAt(float(i) / points)
        phi = i * range / points
        dx, dy = supercalc(m, n1, n2, n3, phi)
        new_path.addPoint(pt.x + dx * scale, pt.y + dy * scale)
    return new_path
