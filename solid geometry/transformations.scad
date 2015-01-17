$fn = 100;
//color("red") resize(newsize=[3,6,1]) sphere(r=1);  

scale([1,1,1]){
	translate([0,0,5]) sphere(r = 1.5);
	resize([1,1,1]) cube([2,2,2], center = true);
	rotate([0,0,0]) cylinder(h = 4, d1 = 2, d2 = 0, center = true);
}

