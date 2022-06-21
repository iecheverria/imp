from __future__ import print_function
import IMP
import IMP.test
import IMP.core
import IMP.container
import os


class Tests(IMP.test.TestCase):

    def test_incr(self):
        """Testing incremental scoring with Monte Carlo"""
        m = IMP.Model()
        IMP.set_log_level(IMP.SILENT)
        mc = IMP.core.MonteCarlo(m)
        mc.set_log_level(IMP.SILENT)
        ps = []
        bb = IMP.algebra.get_unit_bounding_box_3d()
        for i in range(0, 10):
            p = IMP.Particle(m)
            d = IMP.core.XYZR.setup_particle(p)
            ps.append(d)
            d.set_coordinates(IMP.algebra.get_random_vector_in(bb))
            d.set_radius(.1)
            d.set_coordinates_are_optimized(True)
        cpc = IMP.container.ConsecutivePairContainer(m, ps)
        hps = IMP.core.HarmonicDistancePairScore(1, 100)
        # hps.set_log_level(IMP.VERBOSE)
        r = IMP.container.PairsRestraint(hps, cpc)
        sf = IMP.core.RestraintsScoringFunction([r])
        with IMP.allow_deprecated():
            isf = IMP.core.IncrementalScoringFunction(m, ps, [r])
            mc.set_incremental_scoring_function(isf)
        isf.set_log_level(IMP.SILENT)
        ms = [IMP.core.BallMover(m, [x], .1) for x in ps]
        mv = IMP.core.SerialMover(ms)
        mc.add_mover(mv)
        #w= IMP.display.PymolWriter(self.get_tmp_file_name("incr.pym"))
        # w.set_frame(0)
        # for p in ps:
        #    g= IMP.core.XYZRGeometry(p)
        #    w.add_geometry(g);
        for i in range(0, 10):
            print("optimizing")
            mc.optimize(1000)
            # w.set_frame(i+1)
            # for p in ps:
            #    g= IMP.core.XYZRGeometry(p)
            #    w.add_geometry(g);
        print(sf.evaluate(False))
        self.assertLess(sf.evaluate(False), 3)

    def test_incr_nbl(self):
        """Testing incremental scoring with Monte Carlo and a nbl"""
        m = IMP.Model()
        IMP.set_log_level(IMP.SILENT)
        mc = IMP.core.MonteCarlo(m)
        mc.set_log_level(IMP.SILENT)
        ps = []
        bb = IMP.algebra.get_unit_bounding_box_3d()
        for i in range(0, 10):
            p = IMP.Particle(m)
            d = IMP.core.XYZR.setup_particle(p)
            ps.append(d)
            d.set_coordinates(IMP.algebra.get_random_vector_in(bb))
            d.set_radius(.1)
            d.set_coordinates_are_optimized(True)
        cpc = IMP.container.ConsecutivePairContainer(m, ps)
        hps = IMP.core.HarmonicDistancePairScore(1, 100)
        # hps.set_log_level(IMP.VERBOSE)
        r = IMP.container.PairsRestraint(hps, cpc)
        # r.set_log_level(IMP.VERBOSE)
        sf = IMP.core.RestraintsScoringFunction([r])
        with IMP.allow_deprecated():
            isf = IMP.core.IncrementalScoringFunction(m, ps, [r])
            mc.set_incremental_scoring_function(isf)
        ms = [IMP.core.BallMover(m, [x], 2) for x in ps]
        mv = IMP.core.SerialMover(ms)
        mc.add_mover(mv)
        icpf = IMP.container.InContainerPairFilter(cpc, True)
        isf.add_close_pair_score(
            IMP.core.SoftSpherePairScore(100),
            .2,
            ps,
            [icpf])
        isf.set_log_level(IMP.SILENT)
        #w= IMP.display.PymolWriter(self.get_tmp_file_name("incr_nbl.pym"))
        # w.set_frame(0)
        # for p in ps:
        #    g= IMP.core.XYZRGeometry(p)
        #    w.add_geometry(g);
        for i in range(0, 10):
            mc.optimize(1000)
            # w.set_frame(i+1)
            # for p in ps:
            #    g= IMP.core.XYZRGeometry(p)
            #    w.add_geometry(g);
        print(sf.evaluate(False))
        self.assertLess(sf.evaluate(False), 3)


if __name__ == '__main__':
    IMP.test.main()
