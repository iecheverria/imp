from __future__ import print_function
import io
import IMP
import IMP.test
import IMP.atom


class Tests(IMP.test.TestCase):

    def test_residues_in_domains(self):
        """Test selection of residue indices in Domain particles"""
        def assert_no_match(rh, index):
            s = IMP.atom.Selection(rh, residue_indexes=[index])
            self.assertEqual(len(s.get_selected_particle_indexes()), 0)
        def assert_match(rh, index, ai):
            s = IMP.atom.Selection(rh, residue_indexes=[index])
            i = s.get_selected_particle_indexes()
            self.assertEqual(len(i), 1)
            self.assertEqual(i[0], ai) # should match the atom particle
        m = IMP.Model()
        ri = m.add_particle("domain")
        rh = IMP.atom.Hierarchy.setup_particle(m, ri)
        d = IMP.atom.Domain.setup_particle(m, ri, [100, 200])
        ai = m.add_particle("atom")
        ah = IMP.atom.Hierarchy.setup_particle(m, ai)
        rh.add_child(ah)
        a = IMP.core.XYZR.setup_particle(m, ai,
                     IMP.algebra.Sphere3D(IMP.algebra.Vector3D(1,2,3), 4))
        IMP.atom.Mass.setup_particle(m, ai, 1.0)
        assert_no_match(rh, 99)
        assert_no_match(rh, 200) # Last residue in range should *not* match
        assert_no_match(rh, 201)
        assert_match(rh, 100, ai)
        assert_match(rh, 199, ai)

    def _get_index(self, l):
        h = IMP.atom.Hierarchy(l[0])
        p = IMP.atom.Residue(h.get_parent())
        return p.get_index()

    def test_trivial(self):
        """Trivial selection test"""
        m = IMP.Model()
        ri = m.add_particle("root")
        rh = IMP.atom.Hierarchy.setup_particle(m, ri)
        ci = m.add_particle("child")
        ch = IMP.atom.Hierarchy.setup_particle(m, ci)
        rh.add_child(ch)
        cr = IMP.core.XYZR.setup_particle(
            m,
            ci,
            IMP.algebra.get_unit_sphere_3d())
        cm = IMP.atom.Mass.setup_particle(m, ci, 1)
        # Cannot specify both hierarchy and hierarchies
        self.assertRaises(RuntimeError, IMP.atom.Selection,
                          hierarchy=rh, hierarchies=[rh])
        # Must specify either hierarchy or hierarchies
        self.assertRaises(ValueError, IMP.atom.Selection)
        s = IMP.atom.Selection([rh])
        self.assertNumPyArrayEqual(s.get_selected_particle_indexes(), [ci])

    def test_one(self):
        """Test selection of N and C termini"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            h = IMP.atom.read_pdb(fh, m)
        cterm = IMP.atom.Selection(h, terminus=IMP.atom.Selection.C)
        nterm = IMP.atom.Selection(h, terminus=IMP.atom.Selection.N)
        print(cterm.get_selected_particles())
        print(nterm.get_selected_particles())
        self.assertEqual(len(cterm.get_selected_particle_indexes()), 1)
        self.assertEqual(len(nterm.get_selected_particle_indexes()), 1)
        self.assertEqual(self._get_index(cterm.get_selected_particles()), 440)
        self.assertEqual(self._get_index(nterm.get_selected_particles()), 432)

    def test_element(self):
        """Test selection of atoms by element"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            h = IMP.atom.read_pdb(fh, m)
        c = IMP.atom.Selection(h, element=IMP.atom.C)
        fe = IMP.atom.Selection(h, element=IMP.atom.Fe)
        n = IMP.atom.Selection(h, element=IMP.atom.N)
        self.assertEqual(len(c.get_selected_particles()), 46)
        self.assertEqual(len(n.get_selected_particles()), 9)
        self.assertEqual(len(fe.get_selected_particles()), 0)

    def test_atom_type(self):
        """Test selection of CA atoms and indexes"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            h = IMP.atom.read_pdb(fh, m)
        ca = IMP.atom.Selection(h, atom_type=IMP.atom.AT_CA)
        cas = ca.get_selected_particle_indexes()
        self.assertEqual(len(cas), 9)
        for c in cas:
            self.assertEqual(
                IMP.atom.Atom(m,
                              c).get_atom_type(),
                IMP.atom.AT_CA)
        ri = IMP.atom.Selection(h, residue_indexes=[436, 437])
        ris = ri.get_selected_particle_indexes()
        self.assertEqual(len(ris), 18)
        for c in ris:
            r = IMP.atom.Residue(IMP.atom.Atom(m, c).get_parent())
            rind = r.get_index()
            self.assert_(rind in [436, 437])

    def test_residue_type(self):
        """Test selection of residue type"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            h = IMP.atom.read_pdb(fh, m)
        v = IMP.atom.Selection(h, residue_type=IMP.atom.VAL)
        ps = v.get_selected_particle_indexes()
        self.assertEqual(len(ps), 7)
        for p in ps:
            r = IMP.atom.Residue(IMP.atom.Atom(m, p).get_parent())
            rind = r.get_index()
            self.assertEqual(rind, 434)

    def test_two(self):
        """Test simple selection of N and C termini"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        ri = m.add_particle("root")
        rh = IMP.atom.Hierarchy.setup_particle(m, ri)
        ci = m.add_particle("chain")
        cc = IMP.atom.Chain.setup_particle(m, ci, "A")
        rh.add_child(cc)
        nti = m.add_particle("n")
        nth = IMP.atom.Hierarchy.setup_particle(m, nti)
        ntr = IMP.core.XYZR.setup_particle(
            m,
            nti,
            IMP.algebra.get_unit_sphere_3d())
        ntm = IMP.atom.Mass.setup_particle(m, nti, 1)
        cc.add_child(nth)
        cti = m.add_particle("c")
        cth = IMP.atom.Hierarchy.setup_particle(m, cti)
        ntr = IMP.core.XYZR.setup_particle(
            m,
            cti,
            IMP.algebra.get_unit_sphere_3d())
        ntm = IMP.atom.Mass.setup_particle(m, cti, 1)
        cc.add_child(cth)
        cs = IMP.atom.Selection([rh], terminus=IMP.atom.Selection.C)
        self.assertNumPyArrayEqual(
            cs.get_selected_particle_indexes(), [cti])
        ns = IMP.atom.Selection([rh], terminus=IMP.atom.Selection.N)
        self.assertNumPyArrayEqual(
            ns.get_selected_particle_indexes(), [nti])

    def test_mixed_coordinates(self):
        """Test a selection when only some have coordinates"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        h = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("root"))
        c0 = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("child0"))
        c1 = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("child1"))
        c2 = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("child2"))
        IMP.atom.Mass.setup_particle(c2, 1)
        h.add_child(c0)
        c0.add_child(c1)
        c1.add_child(c2)
        d0 = IMP.core.XYZR.setup_particle(c0)
        d0.set_radius(10)
        d2 = IMP.core.XYZR.setup_particle(c2)
        d2.set_radius(1)
        self.assert_(h.get_is_valid(True))
        s = IMP.atom.Selection([h])
        ps = s.get_selected_particle_indexes()
        self.assertEqual(ps, [c2.get_particle_index()])

    def test_mol(self):
        """Test selecting molecules"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        r = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("root"))
        with self.open_input_file("mini.pdb") as fh:
            h0 = IMP.atom.read_pdb(fh, m)
        h0.set_name("mini0")
        r.add_child(h0)
        with self.open_input_file("mini.pdb") as fh:
            h1 = IMP.atom.read_pdb(fh, m)
        h1.set_name("mini1")
        IMP.atom.Molecule.setup_particle(h1)
        IMP.atom.Molecule.setup_particle(h0)
        r.add_child(h1)
        IMP.atom.show_molecular_hierarchy(r)
        s0 = IMP.atom.Selection(r, molecule="mini0")
        s1 = IMP.atom.Selection(r, molecule="mini1")
        self.assertEqual(len(s0.get_selected_particle_indexes()), 68)
        self.assertEqual(len(s1.get_selected_particle_indexes()), 68)
        self.assertEqual(
            len(set(list(s0.get_selected_particle_indexes())
                    + list(s1.get_selected_particle_indexes()))),
            2 * 68)

    def test_residues_rb(self):
        """Test selecting residues from rigid bodies"""
        IMP.set_log_level(IMP.VERBOSE)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            r = IMP.atom.read_pdb(fh, m)
        rb = IMP.atom.create_rigid_body(r)
        s = IMP.atom.Selection([r], residue_indexes=[436, 437])
        pis = s.get_selected_particle_indexes()
        for pi in pis:
            a = IMP.atom.Atom(m, pi)
            print(a, IMP.atom.Residue(a.get_parent()).get_index())
        self.assertEqual(len(pis), 18)

    def test_disjoint_selections(self):
        """Test that two selections are disjoint"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        all = IMP.atom.Hierarchy.setup_particle(IMP.Particle(m))
        all.set_name("the universe")

        def create_protein(name, ds):
            h = IMP.atom.create_protein(m, name, 10, ds)
            leaves = IMP.atom.get_leaves(h)
            all.add_child(h)
        create_protein("Nup85", 570)
        create_protein("Nup145C", 442)

        IMP.set_log_level(IMP.VERBOSE)
        print("145")
        s145 = IMP.atom.Selection(hierarchy=all, molecule="Nup145C",
                                  residue_indexes=range(0, 423)).get_selected_particle_indexes()
        print("85")
        s85 = IMP.atom.Selection(
            hierarchy=all,
            molecule="Nup85").get_selected_particle_indexes()
        print(s145)
        print(s85)
        for s in s145:
            assert(s not in s85)

    def test_hierarchy_type(self):
        """Test selection of hierarchy types"""
        IMP.set_log_level(IMP.SILENT)
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            h = IMP.atom.read_pdb(fh, m)
        s = IMP.atom.Selection(h, hierarchy_types=[IMP.atom.ATOM_TYPE])
        self.assertEqual(len(s.get_selected_particle_indexes()), 68)
        s = IMP.atom.Selection(h, hierarchy_types=[IMP.atom.RESIDUE_TYPE])
        # By default, will give us all leaves in residues (i.e. atoms, so same
        # as the ATOM_TYPE search)
        self.assertEqual(len(s.get_selected_particle_indexes()), 68)
        self.assertEqual(len(s.get_selected_particles()), 68)
        # Should give just the residues themselves
        self.assertEqual(len(s.get_selected_particle_indexes(False)), 9)
        self.assertEqual(len(s.get_selected_particles(False)), 9)

    def test_fragment_terminus(self):
        """Test get terminus from fragment"""
        m = IMP.Model()
        with self.open_input_file("mini.pdb") as fh:
            r = IMP.atom.read_pdb(fh, m)
        term = IMP.atom.Selection(r,terminus=IMP.atom.Selection.N).get_selected_particles()

        # now put in fragments
        residues = IMP.atom.get_by_type(r,IMP.atom.RESIDUE_TYPE)
        numr = len(residues)
        IMP.atom.create_fragment(residues[:numr//2])
        IMP.atom.create_fragment(residues[numr//2:])

        # does selection still get the terminus?
        term2 = IMP.atom.Selection(r,terminus=IMP.atom.Selection.N).get_selected_particles()
        self.assertEqual(term,term2)
if __name__ == '__main__':
    IMP.test.main()
