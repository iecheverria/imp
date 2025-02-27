\brief General purpose algebraic and geometric methods that are expected to be used by a wide variety of IMP modules.

# Geometric primitives # {#geometricprimitives}

IMP has a number of geometric primitives. They support the following namespace
functions as appropriate
  - IMP::algebra::get_bounding_box()
  - IMP::algebra::get_surface_area()
  - IMP::algebra::get_volume()
  .
In addition, they cannot be compared against one another due to floating point
implementation issues (eg `Vector3D v=v2` does not imply `v==v2`).

Geometric primitives are not put into a defined state by their
constructor. Such classes mimic POD types (int, float etc) in C++ and
are optimized for efficiency.  All operations on a default initialized
instance other than assigning to it from a non-default initialized
instance should be assumed to be invalid.

# Geometry and dimensions

Many of the geometric primitives and operations in IMP are written to work in any dimension.
In C++, this is implemented via templates (such as IMP::algebra::VectorD).
In the Python side, the different dimensions are named explicitly instead. That
means, a 2-D point is IMP::algebra::VectorD<2> in C++, and IMP::algebra::Vector2D in Python
and the function IMP::algebra::get_basis_vector_d<3>() in C++ becomes `IMP.algebra.get_basis_vector_3d()` in Python.
Similarly, a collection of 2D points is
IMP::Vector<IMP::algebra::VectorD<2> > in C++ and IMP.algebra.Vector2Ds in Python, which
as with all collections, look like Python lists.
For convenience, we provide typedefs in C++ to the IMP::algebra::Vector2D and
IMP::algebra::Vector2Ds style names.

# Generic geometry # {#genericgeometry}

 Geometry in IMP can be stored in a variety of ways. For %example, a
 point in 3D can be stored using an IMP::algebra::VectorD<3> or using an
 IMP::core::XYZ particle. It is often useful to be able to write
 algorithms that work on sets of points without worrying how they are
 stored, the Generic Geometry layer provides that. It works using a
 set of functions get_vector_3d() and
 set_vector_3d() which manipulate the geometry in terms of the IMP::algebra
 representation of the geometry in question. That is, get_vector_3d()
 returns a IMP::algebra::VectorD<3> for both an IMP::algebra::Vector3D and
 a IMP::core::XYZ. Algorithms take their arguments as C++
 templates and use the generic geometry methods to manipulate the
 geometry. And versions of the function for both types of storage are
 exported to Python, so one could also write generic functions in Python.

 For example, IMP::atom::get_rmsd() takes any combination of IMP::algebra::Vector3Ds
 or IMP::core::XYZs or IMP::core::XYZsTemp as arguments. Versions for all combinations
 of those are exported to Python.

# ANN # {#ANN}
[ ANN](http://www.cs.umd.edu/~mount/ANN) is a library implementing fast
nearest neighbor searches. Certain data structures will be faster if
it is installed. While compilation of the library from source is quite
straightforward, it is not available as a package for common platforms.
In addition, ANN must be built as a shared library rather than a static
library.

# Info

_Author(s)_: Daniel Russel, Keren Lasker, Ben Webb, Javier Angel Velázquez-Muriel

_Maintainer_: `benmwebb`

_License_: [LGPL](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
 - See [main IMP papers list](@ref publications).
