 function get_cylinder_h(p) = lookup(p, [
 		[ -200, 5 ],
 		[ -50, 20 ],
 		[ -20, 18 ],
 		[ +80, 25 ],
 		[ +150, 2 ]
 	]);
 
// for (i = [-100:5:+100]) {
// 	// echo(i, get_cylinder_h(i));
// 	translate([ i, 0, -30 ]) cylinder(r1 = 6, r2 = 2, h = get_cylinder_h(i)*3);
// }

// for(i=[0:36])
//    translate([i*10,0,0])
//       cylinder(r=5,h=cos(i*10)*50+60, center  = true);


 for(i=[0:36])
    translate([i*10,0,0])
       cylinder(r=5,h=sin(i*10)*50+60);

