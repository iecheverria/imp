import IMP
import IMP.test
import IMP.algebra
import IMP.core


class Tests(IMP.test.TestCase):

    """Test the symmetry restraint"""

    def test_symmetry(self):
        """Test the box score"""
        m = IMP.Model()
        p = IMP.Particle(m)
        d = IMP.core.XYZ.setup_particle(p)
        bbi = IMP.algebra.BoundingBox3D(IMP.algebra.Vector3D(10, 10, 10),
                                        IMP.algebra.Vector3D(20, 20, 20))
        bbo = IMP.algebra.BoundingBox3D(IMP.algebra.Vector3D(0, 0, 0),
                                        IMP.algebra.Vector3D(30, 30, 30))

        d.set_coordinates(IMP.algebra.get_random_vector_in(bbo))
        d.get_coordinates().show()
        d.set_coordinates_are_optimized(True)
        s = IMP.core.BoundingBox3DSingletonScore(IMP.core.Harmonic(0, 1), bbi)
        r = IMP.core.SingletonRestraint(m, s, p)
        sf = IMP.core.RestraintsScoringFunction([r])
        o = IMP.core.ConjugateGradients(m)
        o.set_scoring_function(sf)
        o.optimize(100)
        for i in range(0, 3):
            self.assertGreater(d.get_coordinate(i), 9.9)
            self.assertLess(d.get_coordinate(i), 20.1)
        d.get_coordinates().show()

if __name__ == '__main__':
    IMP.test.main()
