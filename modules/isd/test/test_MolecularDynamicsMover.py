#!/usr/bin/env python

# general imports
from numpy import *
from random import uniform


# imp general
import IMP

# our project
from IMP.isd import Scale, MolecularDynamicsMover

# unit testing framework
import IMP.test

vel_key_xyz = IMP.FloatsKey("linvel")
vel_key_nuisance = IMP.FloatKey("vel")


class TestMolecularDynamicsMover(IMP.test.TestCase):

    def setUp(self):
        IMP.test.TestCase.setUp(self)
        IMP.set_log_level(0)
        self.m = IMP.Model()
        self.xyzs = []
        self.nuisances = []
        self.restraints = []
        self.setup_system()
        self.setup_mover()

    def setup_xyz(self, coords, mass):
        a = IMP.Particle(self.m)
        IMP.core.XYZ.setup_particle(a, coords)
        IMP.core.XYZ(a).set_coordinates_are_optimized(True)
        IMP.atom.Mass.setup_particle(a, mass)
        return a

    def setup_scale(self, coords, mass):
        a = IMP.Particle(self.m)
        IMP.isd.Scale.setup_particle(a, coords)
        IMP.isd.Scale(a).set_scale_is_optimized(True)
        IMP.atom.Mass.setup_particle(a, mass)
        return a

    def setup_system(self):
        """setup two xyzs and two nuisances linked by a Lognormal restraint"""
        a = self.setup_xyz(IMP.algebra.Vector3D((0, 0, 0)), 1.0)
        b = self.setup_xyz(IMP.algebra.Vector3D((1, 1, 1)), 1.0)
        si = self.setup_scale(1.0, 1.0)
        ga = self.setup_scale(1.0, 1.0)
        ln = IMP.isd.NOERestraint(self.m, a, b, si, ga, 1.0)
        self.xyzs.append(a)
        self.xyzs.append(b)
        self.nuisances.append(si)
        self.nuisances.append(ga)
        self.restraints.append(ln)

    def setup_mover(self, nsteps=10, tstep=1.0):
        self.mv = IMP.isd.MolecularDynamicsMover(self.m, nsteps, tstep)
        self.mv.set_was_used(True)
        self.mv.get_md().assign_velocities(300.)
        self.mv.get_md().set_scoring_function(self.restraints)

    def get_nuisance_coordinates(self):
        a = [i.get_value(IMP.isd.Scale.get_scale_key())
             for i in self.nuisances]
        b = [i.get_value(vel_key_nuisance) for i in self.nuisances]
        return a + b

    def get_xyz_coordinates(self):
        a = [[i.get_value(fl) for fl in IMP.core.XYZ.get_xyz_keys()]
             for i in self.xyzs]
        b = [i.get_value(vel_key_xyz) for i in self.xyzs]
        return a + b

    def test_move(self):
        """test that the mover moves the particles"""
        self.mv.get_md().optimize(0)
        oldn = self.get_nuisance_coordinates()
        oldx = self.get_xyz_coordinates()
        self.mv.propose()
        newn = self.get_nuisance_coordinates()
        newx = self.get_xyz_coordinates()
        for i, j in zip(newx, oldx):
            self.assertNotAlmostEqual(i[0], j[0], delta=1e-7)
            self.assertNotAlmostEqual(i[1], j[1], delta=1e-7)
            self.assertNotAlmostEqual(i[2], j[2], delta=1e-7)
        for i, j in zip(newn, oldn):
            self.assertNotAlmostEqual(i, j, delta=1e-7)

    def test_reject(self):
        """reject should revert to the first set of coordinates"""
        self.mv.get_md().optimize(0)
        oldn = self.get_nuisance_coordinates()
        oldx = self.get_xyz_coordinates()
        self.mv.propose()
        self.mv.reject()
        newn = self.get_nuisance_coordinates()
        newx = self.get_xyz_coordinates()
        for i, j in zip(newx, oldx):
            self.assertAlmostEqual(i[0], j[0], delta=1e-7)
            self.assertAlmostEqual(i[1], j[1], delta=1e-7)
            self.assertAlmostEqual(i[2], j[2], delta=1e-7)
        for i, j in zip(newn, oldn):
            self.assertAlmostEqual(i, j, delta=1e-7)

    def test_consistence(self):
        """rejectting the move without redrawing velocities should lead to the
        same point
        """
        self.mv.get_md().optimize(0)
        self.mv.propose()
        oldn = self.get_nuisance_coordinates()
        oldx = self.get_xyz_coordinates()
        self.mv.reject()
        self.mv.propose()
        newn = self.get_nuisance_coordinates()
        newx = self.get_xyz_coordinates()
        for i, j in zip(newx, oldx):
            self.assertAlmostEqual(i[0], j[0], delta=1e-7)
            self.assertAlmostEqual(i[1], j[1], delta=1e-7)
            self.assertAlmostEqual(i[2], j[2], delta=1e-7)
        for i, j in zip(newn, oldn):
            self.assertAlmostEqual(i, j, delta=1e-7)

    def test_consistence_2(self):
        """rejectting the move by redrawing velocities should lead to a different
        point
        """
        self.mv.get_md().optimize(0)
        self.mv.propose()
        oldn = self.get_nuisance_coordinates()
        oldx = self.get_xyz_coordinates()
        self.mv.reject()
        self.mv.get_md().assign_velocities(300.)
        self.mv.propose()
        newn = self.get_nuisance_coordinates()
        newx = self.get_xyz_coordinates()
        for i, j in zip(newx, oldx):
            self.assertNotAlmostEqual(i[0], j[0], delta=1e-7)
            self.assertNotAlmostEqual(i[1], j[1], delta=1e-7)
            self.assertNotAlmostEqual(i[2], j[2], delta=1e-7)
        for i, j in zip(newn, oldn):
            self.assertNotAlmostEqual(i, j, delta=1e-7)

    def test_get_set(self):
        """test get/set the number of MD steps.
        """
        self.assertEqual(self.mv.get_number_of_md_steps(), 10)
        self.mv.set_number_of_md_steps(100)
        self.assertEqual(self.mv.get_number_of_md_steps(), 100)

    def test_n_md(self):
        """changing the length of the simulation should lead to a different
        point
        """
        self.mv.get_md().optimize(0)
        self.mv.set_number_of_md_steps(100)
        self.mv.propose()
        oldn = self.get_nuisance_coordinates()
        oldx = self.get_xyz_coordinates()
        self.mv.reject()
        self.mv.set_number_of_md_steps(10)
        self.mv.propose()
        newn = self.get_nuisance_coordinates()
        newx = self.get_xyz_coordinates()
        for i, j in zip(newx, oldx):
            self.assertNotAlmostEqual(i[0], j[0], delta=1e-7)
            self.assertNotAlmostEqual(i[1], j[1], delta=1e-7)
            self.assertNotAlmostEqual(i[2], j[2], delta=1e-7)
        for i, j in zip(newn, oldn):
            self.assertNotAlmostEqual(i, j, delta=1e-7)


if __name__ == '__main__':
    IMP.test.main()
