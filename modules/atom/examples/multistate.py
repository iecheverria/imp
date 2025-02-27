## \example multistate.py
#

from __future__ import print_function
import IMP.atom
import sys

IMP.setup_from_argv(sys.argv, "multistate")

m = IMP.Model()

rt = IMP.atom.Hierarchy.setup_particle(m, m.add_particle("root"))


def create_one():
    h = IMP.atom.read_pdb(IMP.atom.get_example_path("1d3d-protein.pdb"), m)
    return h


h0 = create_one()
rt.add_child(h0)
IMP.atom.State.setup_particle(h0, 0)
h1 = create_one()
rt.add_child(h1)
IMP.atom.State.setup_particle(h1, 1)


r8 = IMP.atom.Selection(
    rt,
    state_index=1,
    residue_index=8,
    atom_type=IMP.atom.AT_CA)

# we get the 8th CA from state 1
for p in r8.get_selected_particles():
    print(IMP.atom.get_state_index(p), p)
