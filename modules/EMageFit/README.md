\brief Build assembly models consistent with EM images (class averages).

EMageFit is an application to build models of macromolecular assemblies using
restraints from EM images (class averages).

Apart from EM images, the method relies on other types of restraints:
  - Maximum distance restraints imposing a maximum distance between a pair
    of residues, as derived from cross-linking experiments. You can of course
    impose maximum distance between any part of the complex. As shown in
    the paper, this type of restraint is required to accurately determine
    the orientation between the subunits of an assembly.
  - Proximity restraints forcing a pair of subunits to be within a certain
    distance, suitable for proteomics data.
  - Excluded volume restraints preventing the components of the assembly
    from interpenetrating.
  - Geometric complementarity restraints favoring large contact surfaces
    between interacting subunits. These restraints can be somewhat useful
    if the subunits of the assembly are expected to have large contact
    surfaces. Among all of the restraints considered here, they are the
    least useful.

EMageFit samples for good conformations of the macromolecular assembly using
multiple molecular docking (optional, but it can be very useful), Simulated
Annealing Monte Carlo optimization, and sampling with the discrete optimizer
DOMINO. It is also straightforward to incorporate other restraints to the
method.

If available, EMageFit will use the docking program
[HEXDOCK](http://hex.loria.fr/) to do docking between subunits that
are related by cross-links. But it is worth mentioning that EMageFit can also
work with any other docking program, or simply using the cross-linking
restraints and no docking at all.

More detail on the functioning of EMageFit can be found on the
\ref emagefit_protocol "protocol page", and many of the scripts and
utilities are documented on the \ref emagefit_scripts "scripts page".

_Examples_:
 - [Modeling of 3sfd](@ref emagefit_3sfd)

# Info

_Author(s)_: Javier Velázquez-Muriel

_Maintainer_: `benmwebb`

_License_: [GPL](https://www.gnu.org/licenses/gpl.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
 - Javier A. Velázquez-Muriel, Keren Lasker, Daniel Russel, Jeremy Phillips, Benjamin M. Webb, Dina Schneidman, Andrej Sali, \quote{Assembly of macromolecular complexes by satisfaction of spatial restraints from electron microscopy images}, <em>Proc Natl Acad Sci USA 109(46), 18821-18826</em>, 2012.
