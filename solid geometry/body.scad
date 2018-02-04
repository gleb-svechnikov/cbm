$fn=50;

cylinder(500,50,50,true);

cube([500,150,100],true);

translate([0,0,300]) 
    sphere(150, true);

rotate([0,30,0]) 
    translate([90,0,-450])  
        cylinder(500,50,50,true);
 
translate([150,0,-450])
    rotate([0,-30,0])
        cylinder(500,50,50,true);
