#!/usr/bin/env python

# general imports
from numpy import *
from random import uniform

# imp general
import IMP

# our project
from IMP.isd import Scale, vonMisesKappaConjugateRestraint

# unit testing framework
import IMP.test


class Tests(IMP.test.TestCase):

    def setUp(self):
        IMP.test.TestCase.setUp(self)
        # IMP.set_log_level(IMP.MEMORY)
        IMP.set_log_level(0)
        self.m = IMP.Model()
        self.kappa = Scale.setup_particle(IMP.Particle(self.m), 1.0)
        self.DA = IMP.DerivativeAccumulator()

    def testValuePKappa(self):
        "Test vonMisesKappaConjugate probability by changing kappa"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(
            self.m, self.kappa, c, R0)
        for i in range(100):
            no = uniform(0.1, 60)
            self.kappa.set_scale(no)
            ratio = i1(no) / i0(no)
            py = exp(no * R0) / i0(no) ** c
            cpp = self.J.get_probability()
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testValuePc(self):
        "Test vonMisesKappaConjugate probability by changing c"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        R0 = 1.0
        no = 1.0
        self.kappa.set_scale(no)
        for i in range(100):
            c = uniform(2.0, 75)
            self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                             self.kappa, c, R0)
            ratio = i1(no) / i0(no)
            py = exp(no * R0) / i0(no) ** c
            cpp = self.J.get_probability()
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testValuePR0(self):
        "Test vonMisesKappaConjugate probability by changing R0"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        c = 10.0
        no = 1.0
        self.kappa.set_scale(no)
        for i in range(100):
            R0 = uniform(0.0, 10.0)
            self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                             self.kappa, c, R0)
            ratio = i1(no) / i0(no)
            py = exp(no * R0) / i0(no) ** c
            cpp = self.J.get_probability()
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testValueEKappa(self):
        "Test vonMisesKappaConjugate energy by changing kappa"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                         self.kappa, c, R0)
        for i in range(100):
            no = uniform(0.1, 100)
            self.kappa.set_scale(no)
            ratio = i1(no) / i0(no)
            py = -no * R0 + c * log(i0(no))
            cpp = self.J.evaluate(False)
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testValueEc(self):
        "Test vonMisesKappaConjugate energy by changing c"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        R0 = 1
        no = 1.0
        self.kappa.set_scale(no)
        for i in range(100):
            c = uniform(1.0, 100)
            self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                             self.kappa, c, R0)
            ratio = i1(no) / i0(no)
            py = -no * R0 + c * log(i0(no))
            cpp = self.J.evaluate(False)
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testValueER0(self):
        "Test vonMisesKappaConjugate energy by changing R0"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        c = 10.0
        no = 1.0
        self.kappa.set_scale(no)
        for i in range(100):
            R0 = uniform(0.0, 10.0)
            self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                             self.kappa, c, R0)
            ratio = i1(no) / i0(no)
            py = -no * R0 + c * log(i0(no))
            cpp = self.J.evaluate(False)
            self.assertAlmostEqual(cpp, py, delta=0.001)

    def testDerivativeKappa(self):
        "Test vonMisesKappaConjugate derivative by changing kappa"
        try:
            from scipy.special import i0, i1
        except ImportError:
            self.skipTest("this test requires the scipy Python module")
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                         self.kappa, c, R0)
        for i in range(100):
            no = uniform(0.1, 100)
            self.kappa.set_scale(no)
            self.J.evaluate(True)
            ratio = i1(no) / i0(no)
            self.assertAlmostEqual(self.kappa.get_scale_derivative(),
                                   -R0 + c * i1(no) / i0(no), delta=0.001)

    def test_get_inputs(self):
        "Test vonMisesKappaConjugateRestraint::get_inputs()"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                         self.kappa, c, R0)
        self.assertEqual([x.get_name() for x in self.J.get_inputs()],
                         [self.kappa.get_name()])

    def testNonzeroE(self):
        "vonMisesKappaConjugate errors on evaluate with zero scale"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                         self.kappa, c, R0)
        self.kappa.set_scale(0.0)
        self.assertRaises(
            IMP.ModelException,
            self.J.unprotected_evaluate,
            self.DA)

    def testNegativeE(self):
        "vonMisesKappaConjugate errors on evaluate with negative scale"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(self.m,
                                                         self.kappa, c, R0)
        self.kappa.set_scale(-1.0)
        self.assertRaises(
            IMP.ModelException,
            self.J.unprotected_evaluate,
            self.DA)

    def testR0(self):
        "vonMisesKappaConjugate constructor error with R0 < 0"
        c = 10
        R0 = -1
        self.assertRaises(IMP.ModelException,
                          IMP.isd.vonMisesKappaConjugateRestraint, self.m, self.kappa, c, R0)

    def testR0c(self):
        "vonMisesKappaConjugate constructor error with R0 > c"
        c = 10
        R0 = 20
        self.assertRaises(IMP.ModelException,
                          IMP.isd.vonMisesKappaConjugateRestraint, self.m, self.kappa, c, R0)

    def testc(self):
        "vonMisesKappaConjugate constructor error with c < 0"
        c = -1
        R0 = c
        self.assertRaises(IMP.ModelException,
                          IMP.isd.vonMisesKappaConjugateRestraint, self.m, self.kappa, c, R0)

    def testNonzeroP(self):
        "Test vonMisesKappaConjugate get_prob with zero scale"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(
            self.m, self.kappa, c, R0)
        self.kappa.set_scale(0.0)
        self.assertRaises(IMP.ModelException, self.J.get_probability)

    def testNegativeP(self):
        "Test vonMisesKappaConjugate get_prob with negative scale"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(
            self.m, self.kappa, c, R0)
        self.kappa.set_scale(-1.0)
        self.assertRaises(IMP.ModelException, self.J.get_probability)

    def testSanityEP(self):
        "Test if vonMisesKappaConjugate score is -log(prob)"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(
            self.m, self.kappa, c, R0)
        for i in range(100):
            no = uniform(0.1, 75)  # can't go higher because overflow errors
            self.kappa.set_scale(no)
            prob = self.J.get_probability()
            self.assertAlmostEqual(self.J.unprotected_evaluate(self.DA),
                                   -log(prob))

    def testSanityPE(self):
        "Test if vonMisesKappaConjugate prob is exp(-score)"
        c = 10
        R0 = 1
        self.J = IMP.isd.vonMisesKappaConjugateRestraint(
            self.m, self.kappa, c, R0)
        for i in range(100):
            no = uniform(0.1, 100)
            self.kappa.set_scale(no)
            self.assertAlmostEqual(self.J.get_probability(),
                                   exp(-self.J.unprotected_evaluate(self.DA)))


if __name__ == '__main__':
    IMP.test.main()
