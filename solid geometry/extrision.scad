linear_extrude(height = 15, center = false, convexity = 10, twist = 960, $fn = 100)
translate([1, 0, 0]) circle(r = 1);



scale([2,2,2]) rotate_extrude(convexity = 10, $fn = 100)
translate([2, 0, 0]) circle(r = 1, $fn = 100);


linear_extrude(height = fanwidth, center = true, convexity = 10)
import (file = "decor.dxf");