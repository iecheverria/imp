from __future__ import print_function
import IMP
import IMP.test
import io
import random


class DummyRestraint(IMP.Restraint):

    """Dummy do-nothing restraint"""

    def __init__(self, m, ps=[], cs=[], name="DummyRestraint %1%"):
        IMP.Restraint.__init__(self, m, name)
        self.ps = ps
        self.cs = cs

    def unprotected_evaluate(self, accum):
        return 0.

    def get_version_info(self):
        return IMP.get_module_version_info()

    def do_get_inputs(self):
        return self.ps + self.cs


class CustomError(Exception):
    pass


class FailingRestraint(IMP.Restraint):

    """Restraint that fails in evaluate"""

    def __init__(self, m):
        IMP.Restraint.__init__(self, m, "FailingRestraint %1%")

    def unprotected_evaluate(self, accum):
        raise CustomError("Custom error message")

    def get_version_info(self):
        return IMP.get_module_version_info()

    def do_get_inputs(self):
        return []


class DummyScoreState(IMP.ScoreState):

    """Dummy do-nothing score state"""

    def __init__(self, m, ips=[], ics=[], ops=[], ocs=[],
                 name="DummyScoreState%1%"):
        IMP.ScoreState.__init__(self, m, name)
        self.ips = ips
        self.ics = ics
        self.ops = ops
        self.ocs = ocs
        self.updated = False

    def do_before_evaluate(self):
        IMP.add_to_log(
            IMP.TERSE,
            "Updating dummy " + self.get_name() + "\n")
        self.updated = True

    def do_after_evaluate(self, da):
        self.updated = True

    def do_get_inputs(self):
        return self.ips + self.ics

    def do_get_outputs(self):
        return self.ops + self.ocs


class ClassScoreState(IMP.ScoreState):

    """Score state that shows the filehandle class"""

    def __init__(self, m):
        IMP.ScoreState.__init__(self, m, "ClassScoreState%1%")

    def update(self):
        pass

    def do_show(self, fh):
        fh.write(str(fh.__class__))
        fh.write("; ")

    def get_type_name(self):
        return "ScoreStateTest"

    def get_version_info(self):
        return IMP.get_module_version_info()

    def do_get_inputs(self):
        return []

    def do_get_outputs(self):
        return []


class Tests(IMP.test.TestCase):

    def test_state_show(self):
        """Test score state show method"""
        m = IMP.Model("score state show")
        IMP.set_log_level(IMP.VERBOSE)
        s = ClassScoreState(m)
        sio = io.BytesIO()
        s.show(sio)
        m.add_score_state(s)
        for s in m.get_score_states():
            s.show(sio)
        # Output should work for a direct call (in which the filehandle is
        # just the Python file-like object) or via a C++ proxy (in which case
        # the filehandle is a std::ostream adapter)
        self.assertGreater(len(sio.getvalue()), 0)

    def test_score_state(self):
        """Check score state methods"""
        m = IMP.Model("score state model")
        IMP.set_log_level(IMP.VERBOSE)
        # self.assertRaises(IndexError, m.get_score_state,
        #                  0);
        s = DummyScoreState(m)
        m.add_score_state(s)
        news = m.get_score_state(0)
        self.assertIsInstance(news, IMP.ScoreState)
        # self.assertRaises(IndexError, m.get_score_state,
        #                  1);
        for s in m.get_score_states():
            s.show()
        dg = IMP.get_dependency_graph(m)

    def test_show(self):
        """Check Model.show() method"""
        class BrokenFile(object):

            def write(self, str):
                raise NotImplementedError()
        m = IMP.Model("model show")
        IMP.set_log_level(IMP.VERBOSE)
        self.assertRaises(NotImplementedError, m.show, BrokenFile())
        self.assertRaises(AttributeError, m.show, None)
        s = io.BytesIO()
        m.show(s)
        self.assertGreater(len(s.getvalue()), 0)

    def test_refcount_director_score_state(self):
        """Refcounting should prevent director ScoreStates from being deleted"""
        dirchk = IMP.test.DirectorObjectChecker(self)
        m = IMP.Model("ref counting score states")
        IMP.set_log_level(IMP.VERBOSE)
        s = DummyScoreState(m)
        s.python_member = 'test string'
        m.add_score_state(s)
        # Since C++ now holds a reference to s, it should be safe to delete the
        # Python object (director objects should not be freed while C++ holds
        # a reference)
        del s
        news = m.get_score_state(0)
        self.assertEqual(news.python_member, 'test string')
        # Make sure we kept a reference somewhere to this director object
        dirchk.assert_number(1)
        # Cleanup should touch nothing as long as we have Python reference news
        dirchk.assert_number(1)
        del news
        # Should also touch nothing as long as we have C++ references (from m)
        dirchk.assert_number(1)
        del m
        # No refs remain, so make sure all director objects are cleaned up
        dirchk.assert_number(0)

    def test_director_python_exceptions(self):
        """Check that exceptions raised in directors are handled"""
        with IMP.SetNumberOfThreads(1):
            m = IMP.Model("director exceptions")
            IMP.set_log_level(IMP.VERBOSE)
            r = FailingRestraint(m)
            self.assertRaises(CustomError, r.evaluate, False)
        # print "done"

    def test_temp_restraints(self):
        """Check free restraint methods"""
        m = IMP.Model("free restraint methods")
        IMP.set_log_level(IMP.VERBOSE)
        r = DummyRestraint(m)
        r.set_name("dummy")
        print(r.evaluate(False))
        del r

    def test_refcount_director_restraints(self):
        """Refcounting should prevent director Restraints from being deleted"""
        dirchk = IMP.test.DirectorObjectChecker(self)
        m = IMP.Model("ref count dir restraints")
        rs = IMP.RestraintSet(m)
        IMP.set_log_level(IMP.VERBOSE)
        r = DummyRestraint(m)
        r.python_member = 'test string'
        rs.add_restraint(r)
        # Since C++ now holds a reference to r, it should be safe to delete the
        # Python object (director objects should not be freed while C++ holds
        # a reference)
        del r
        newr = rs.get_restraint(0)
        self.assertEqual(newr.python_member, 'test string')
        # Make sure that all director objects are cleaned up
        dirchk.assert_number(1)
        del newr, m, rs
        dirchk.assert_number(0)

    def test_particles(self):
        """Check particle methods"""
        m = IMP.Model("particle methods")
        IMP.set_log_level(IMP.VERBOSE)
        p = IMP.Particle(m)
        self.assertEqual(len(m.get_particle_indexes()), 1)

    def _select(self, ps, n):
        ret = []
        for i in range(0, n):
            ret.append(random.choice(ps))
        return ret

    def test_ranges(self):
        """Test float attribute ranges"""
        m = IMP.Model("float ranges")
        IMP.set_log_level(IMP.VERBOSE)
        ps = [IMP.Particle(m) for i in range(0, 2)]
        for k in [IMP.FloatKey(0), IMP.FloatKey(4), IMP.FloatKey(7)]:
            ps[0].add_attribute(k, k.get_index())
            ps[1].add_attribute(k, k.get_index() + 1)
            rg = IMP._get_range(m, k)
            self.assertEqual(rg[0], k.get_index())
            self.assertEqual(rg[1], k.get_index() + 1)

    def test_dependencies(self):
        """Check dependencies with restraints and score states"""
        IMP.set_log_level(IMP.VERBOSE)
        m = IMP.Model("dependencies")
        ps = [IMP.Particle(m) for i in range(0, 20)]
        cs = [DummyScoreState(m, ips=self._select(ps[:5], 2),
                              ops=self._select(ps[5:], 2),
                              name="BSS%1%")
              for i in range(5)] +\
            [DummyScoreState(m, ops=self._select(ps[:5], 2),
                             ips=[], name="ASS%1%")
             for i in range(5)]
        for c in cs:
            m.add_score_state(c)
        rs = [DummyRestraint(m, ps=self._select(ps, 4), name="R%1%")
              for i in range(5)]
        for r in rs:
            r.set_was_used(True)
        selected = self._select(rs, 4)
        rss = IMP.RestraintSet(selected, 1.0)
        sf = rss.create_scoring_function()

        dg = IMP.get_dependency_graph(m)
        IMP.show_graphviz(dg)

        # test is broken
        return
        required = []
        for r in selected:
            inputs = r.get_inputs()
            for i in inputs:
                for j in cs:
                    if i in j.get_outputs():
                        required.append(j)
        required = sorted(set(required))
        print(required)
        sf.set_has_required_score_states(True)
        found = sorted(sf.get_required_score_states())
        self.assertEqual(required, found)
        sf.evaluate(False)
        for s in cs:
            print(s.get_name())
            self.assertEqual(s.updated, s in required)
            # IMP.show_graphviz(rdg)
        for p in ps:
            p.set_has_required_score_states(True)

    def test_save_restore_dependencies(self):
        """Test save_dependencies() and restore_dependencies()"""
        m = IMP.Model()
        # No dependencies yet
        self.assertEqual(m.get_dependencies_updated(), 0)
        m.save_dependencies()
        p2 = IMP.Particle(m)
        # Adding p2 should update the dependency graph
        self.assertEqual(m.get_dependencies_updated(), 1)
        m.remove_particle(p2)
        m.restore_dependencies()
        # Should be back to "no dependencies" state after restore
        self.assertEqual(m.get_dependencies_updated(), 0)

    def test_save_restore_dependencies_bad(self):
        """Test save/restore_dependencies() with incorrect state"""
        m = IMP.Model()
        m.save_dependencies()
        p2 = IMP.Particle(m)
        # Cannot restore dependencies since graph does not match original
        # (as p2 was added)
        self.assertRaisesInternalException(m.restore_dependencies)


if __name__ == '__main__':
    IMP.test.main()
