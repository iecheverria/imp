\brief Basic utilities for handling cryo-electron microscopy 3D density maps.

The main functionalities are:
1. Reading and writing various density map formats such as XPLOR, MRC, EM and SPIDER.
2. Simulating density maps of particles, supports particles of any radii and mass.
3. Calculating cross-correlation scores between a density map and a set of particles.
4. Implements several Restraints.

The restraints vary based on how accurately the fit to the density is scored, which is usually related to the evaluation speed. Pick more accurate Restraints for higher resolution maps and models. Below is the Restraints list sorted from the fastest and most simple to the slowest and most accurate.

- PCAFitRestraint - compares how well the principal components of the density map fit to the principal components of the particles
- DensityFillingRestraint - estimates the percentage of volume of the density map that is covered by particles
- EnvelopePenetrationRestraint - estimates the number of particles that fall outside the density map
- EnvelopeFitRestraint - scores how well the particles fit the density map using MapDistanceTransform that transforms a density map into a Distance Transform of the map envelope
- FitRestraint - computes the fit using cross correlation

We also provide a number of command line tools to handle electron microscopy
density maps and associated files:

# estimate_threshold_from_molecular_mass {#est_from_molec_mass_bin}

Estimate EM density threshold.

# map2pca {#map2pca_bin}

Write out density map principal components in cmm format.

# mol2pca {#mol2pca_bin}

Write out protein principal components in cmm format.

# resample_density {#resample_density_bin}

Resample a density map.

# simulate_density_from_pdb {#simulate_density_from_pdb_bin}

Samples a protein into a simulated 3D density map.

# view_density_header {#view_density_header_bin}

Display the header information for a density map.

# Info

_Author(s)_: Keren Lasker, Javier Velázquez-Muriel, Friedrich Förster, Daniel Russel, Dina Schneidman

_Maintainer_: `benmwebb`

_License_: [LGPL](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
 - See [main IMP papers list](@ref publications).
