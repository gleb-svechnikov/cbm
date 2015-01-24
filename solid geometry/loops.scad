//for (z = [-10,-5]) 
//{
//    translate([0, 0, z])
//    cube(size = 1, center = false);
//}
//
//for ( i = [0 : 5] )
//{
//    rotate( i * 360 / 6, [1, 0, 0])
//    translate([0, 10, 0])
//    sphere(r = 1);
//}
//
// for(i = [ [ 0,  0,  0],
//           [10, 12, 10],
//           [20, 24, 20],
//           [30, 36, 30],
//           [40, 48, 40],
//           [50, 60, 50] ])
//{
//    translate(i)
//    cube([50, 15, 10], center = false);
//}
intersection_for(n = [1 : 6])
{
    rotate([0, 0, n * 60])
    {
        translate([5,0,0])
        sphere(r=12);
    }
}


