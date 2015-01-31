$fn=50;
minkowski()
{
 cube([10,10,1]);
 cylinder(r=2,h=1);
}

hull() {
   translate([15,10,0]) circle(10);
   circle(2);
}
