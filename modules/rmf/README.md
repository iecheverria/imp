\brief Support for the [RMF file format](https://integrativemodeling.org/rmf/nightly/doc/) for storing hierarchical molecular data and markup.

RMF can store hierarchical molecular data (such as atomic or coarse grained
representations of proteins), along with markup, including geometry
and score data.

 IMP.rmf supports I/O of IMP::atom::Hierarchy and associated types as
 well as output of IMP::display::Geometry, IMP::Restraint and
 arbitrary IMP::Particles. For each of these there are methods like:
 - IMP::rmf::add_hierarchies() to add them to an RMF file (note this does not,
   for various reasons, write the state to frame 0)
 - IMP::rmf::create_hierarchies() to create hierarchies from an RMF file
 - IMP::rmf::link_hierarchies() to link existing hierarchies to corresponding
   ones in the RMF file

 Once objects are linked/added/created, they are attached to the RMF file.
 IMP::rmf::load_frame() can be used to change the state of the linked objects
 to that of an arbitrary frame and IMP::rmf::save_frame() can be used to save
 the current state of the objects into a frame in the RMF file.

 See the [RMF library](https://integrativemodeling.org/rmf/nightly/doc/)
for more information.

Several helper programs are also provided:

# rmf_display {#rmf_display_bin}
Export an RMF file to a viewer.
`rmf_display` outputs an arbitrary
RMF file to pymol or chimera as appropriate (based on the file name of the
second argument). It supports hierarchies, restraints and geometry.

# pdb_rmf {#pdb_rmf_bin}
Make an RMF file from a PDB.

# rmf_simplify {#rmf_simplify_bin}
Create a simplified representation of a PDB.

# Info

_Author(s)_: Daniel Russel

_Maintainer_: `benmwebb`

_License_: [LGPL](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
 - See [main IMP papers list](@ref publications).
