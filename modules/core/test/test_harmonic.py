import IMP
import IMP.test
import IMP.core


def _harmonicfunc(val, mean, force_constant):
    """Python implementation of harmonic function and first derivative"""
    diff = val - mean
    score = 0.5 * force_constant * diff * diff
    deriv = force_constant * diff
    return score, deriv


class Tests(IMP.test.TestCase):

    """Tests for harmonic unary function"""

    def test_values(self):
        """Test that harmonic values are correct"""
        force_constant = 100.0
        mean = 10.0
        func = IMP.core.Harmonic(mean, force_constant)
        func.set_was_used(True)
        for i in range(15):
            val = 5.0 + i
            expscore, expderiv = _harmonicfunc(val, mean, force_constant)
            score, deriv = func.evaluate_with_derivative(val)
            scoreonly = func.evaluate(val)
            self.assertEqual(score, scoreonly)
            self.assertAlmostEqual(expscore, score, delta=0.1)
            self.assertAlmostEqual(expderiv, deriv, delta=0.1)

    def test_accessors(self):
        """Test Harmonic accessors"""
        func = IMP.core.Harmonic(10.0, 1.0)
        func.set_was_used(True)
        self.assertEqual(func.get_mean(), 10.0)
        self.assertEqual(func.get_k(), 1.0)
        func.set_mean(5.0)
        func.set_k(2.0)
        self.assertEqual(func.get_mean(), 5.0)
        self.assertEqual(func.get_k(), 2.0)

    def test_show(self):
        """Check Harmonic::show() method"""
        for func in (IMP.core.Harmonic(10.0, 1.0),
                     IMP.core.HarmonicLowerBound(10.0, 1.0),
                     IMP.core.HarmonicUpperBound(10.0, 1.0)):
            func.set_was_used(True)
            func.show()

if __name__ == '__main__':
    IMP.test.main()
