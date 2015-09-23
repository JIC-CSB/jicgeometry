"""Unit tests for the Point3D class."""

import unittest

class Point3DUnitTests(unittest.TestCase):
    
    def test_import(self):
        # This throws an error if the class cannot be imported.
        from jicgeometry import Point3D

    def test_initialisation_with_tuple(self):
        from jicgeometry import Point3D
        p = Point3D( (1, 2, 3) )
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)
        
    def test_initialisation_with_x_y_z_values(self):
        from jicgeometry import Point3D
        p = Point3D( 1, 2, 3 )
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.z, 3)
        
    def test_intialisation_raises(self):
        from jicgeometry import Point3D
        with self.assertRaises(TypeError):
            p = Point3D( 1, 2 )
    
    def test_repr_int(self):
        from jicgeometry import Point3D
        p = Point3D( 1, 2, 3 )
        self.assertEqual(repr(p), "<Point3D(x=1, y=2, z=3, dtype=int)>")
        
    def test_repr_float(self):
        from jicgeometry import Point3D
        p = Point3D( 1.33333333333333 , 2.66666666667, 3.0 )
        self.assertEqual(repr(p), "<Point2D(x=1.33, y=2.67, z=3.00, dtype=float)>")
        
    def test_dtype_int(self):
        from jicgeometry import Point3D
        p = Point3D( 1 , 2, 3 )
        self.assertEqual(p.dtype, "int")
        self.assertTrue(isinstance(p.x, int))
        self.assertTrue(isinstance(p.y, int))
        self.assertTrue(isinstance(p.z, int))

    def test_dtype_float(self):
        from jicgeometry import Point3D
        p = Point3D( 1.0 , 2.0, 3.0 )
        self.assertEqual(p.dtype, "float")
        self.assertTrue(isinstance(p.x, float))
        self.assertTrue(isinstance(p.y, float))
        self.assertTrue(isinstance(p.z, float))

    def test_dtype_mixed(self):
        from jicgeometry import Point3D
        p = Point3D( 1 , 2.0, 3 )
        self.assertEqual(p.dtype, "float")
        self.assertTrue(isinstance(p.x, float))
        self.assertTrue(isinstance(p.y, float))
        self.assertTrue(isinstance(p.z, float))

    def test_assert_non_numeric_raises_runtime_error(self):
        from jicgeometry import Point3D
        with self.assertRaises(RuntimeError):
            p = Point3D( "1" , 2.0, 3 )
        
    def test_equal(self):
        from jicgeometry import Point3D
        p1 = Point3D(1, 2, 4)
        p2 = Point3D(1, 2, 4)
        self.assertTrue(p1 == p2) 

    def test_Point3D_of_different_dtypes_not_equal(self):
        from jicgeometry import Point3D
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(1.0, 2.0, 3.0)
        self.assertFalse(p1 == p2) 

    def test_add(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 5)
        self.assertEqual(p+p, Point3D(4, 6, 10))

    def test_add_int_float_mixed(self):
        from jicgeometry import Point3D
        p1 = Point3D(2, 3, 5)
        p2 = Point3D(2.0, 3.0, 5.0)
        self.assertEqual(p1+p2, Point3D(4.0, 6.0, 10.))

    def test_sub(self):
        from jicgeometry import Point3D
        p1 = Point3D(2, 3, 4)
        p2 = Point3D(3, 1, 4)
        self.assertEqual(p1-p2, Point3D(-1, 2, 0))

    def test_sub_int_float_mixed(self):
        from jicgeometry import Point3D
        p1 = Point3D(2, 3, 4)
        p2 = Point3D(3.0, 1.0, 4.0)
        self.assertEqual(p1-p2, Point3D(-1.0, 2.0, 0.0))
        
    def test_mul_with_int(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(p*3, Point3D(6, 9, 12))
        
    def test_mul_with_float(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(p*3.0, Point3D(6.0, 9.0, 12.0))
        
    def test_div_with_int(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(p.dtype, 'int')
        new_p = p / 3
        self.assertEqual(new_p.dtype, 'float')
        self.assertEqual(new_p, Point3D(2/3.0, 3/3.0, 4/3.0))

    def test_div_with_float(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(p/3.0, Point3D(2/3.0, 3/3.0, 4/3.0))

    def test_len(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(len(p), 3)
        
    def test_getitem(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(p[0], 2)
        self.assertEqual(p[1], 3)
        self.assertEqual(p[2], 4)
        with self.assertRaises(IndexError):
            p[3]

    def test_iter(self):
        from jicgeometry import Point3D
        import numpy as np
        p = Point3D(2, 3, 4)
        ar = np.array(p)
        self.assertEqual(ar[0], 2)
        self.assertEqual(ar[1], 3)
        self.assertEqual(ar[2], 4)

    def test_magnitude_property(self):
        from jicgeometry import Point3D
        import math
        p = Point3D(2, 3, 4)
        self.assertEqual(p.magnitude, math.sqrt(29))

    def test_unit_vector(self):
        from jicgeometry import Point3D
        p = Point3D(2, 3, 4)
        self.assertEqual(repr(p.unit_vector),
            "<Point2D(x=0.37, y=0.56, z=0.74, dtype=float)>")
        x2 = p.unit_vector.x**2
        y2 = p.unit_vector.y**2
        z2 = p.unit_vector.z**2
        self.assertEqual(x2 + y2 + z2, 1.)
        
    def test_distance(self):
        from jicgeometry import Point3D
        p1 = Point3D(6, 0, 8)
        p2 = Point3D(3, 0, 4)
        self.assertEqual(p1.distance(p2), 5.0)

    def test_astype_int(self):
        from jicgeometry import Point3D
        p = Point3D(5.9, 8.2, 9.5)
        p = p.astype("int")
        self.assertEqual(p, Point3D(6, 8, 10))
        
    def test_astype_float(self):
        from jicgeometry import Point3D
        p = Point3D(5, 8, 10)
        p = p.astype("float")
        self.assertEqual(p, Point3D(5.0, 8.0, 10.0))

    def test_astype_invalid_type(self):
        from jicgeometry import Point3D
        p = Point3D(5, 8, 10)
        with self.assertRaises(RuntimeError):
            p.astype("Idontexist")
        
    def test_astuple(self):
        from jicgeometry import Point3D
        p = Point3D(5, 8, 10)
        t = p.astuple()
        self.assertTrue(isinstance(t, tuple))
        self.assertEqual(t[0], 5)
        self.assertEqual(t[1], 8)
        self.assertEqual(t[2], 10)
        
    def test_iter(self):
        from jicgeometry import Point3D
        p = Point3D(5, 8, 10)
        for expected, got in zip(p, (5, 8, 10)):
            self.assertEqual(expected, got)
        
if __name__ == '__main__':
    unittest.main()
