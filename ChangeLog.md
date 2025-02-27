ChangeLog {#changelog}
=========

# 2.17.0 - 2022-06-23 # {#changelog_2_17_0}
- IMP::atom::Selection no longer checks that the passed hierarchies are valid,
  as this can be quite computationally expensive. If in doubt, call
  IMP::atom::Hierarchy::get_is_valid() on each one first.
- The IMP::em::CoarseCC class has been removed. Use similarly-named free
  functions instead to calculate coarse cross correlation.
- The Windows .exe installer no longer supports Python 2 (it works with
  Python 3.6 through 3.10).
- Binary packages are now provided for Ubuntu 22.04 LTS, Jammy Jellyfish
  and RedHat Enterprise Linux 9 (and variants, such as Rocky or Alma).
- IMP now requires a C++11 compiler and SWIG 3 (or later) to build. Most
  recent compilers should support C++11, such as gcc, clang
  or MS Visual Studio 2012 or later. Various IMP macro and header workarounds
  for pre-C++11 environments are thus no longer needed and are deprecated:
  `IMP_NULLPTR`, `IMP_NULLPTR_T`, `IMP_OVERRIDE`, `IMP_FINAL`, `IMP_UNIQUE_PTR`,
  `IMP_FOREACH`, `IMP/nullptr.h`, and `IMP/nullptr_macros.h`.
- The IMP::core::IncrementalScoringFunction class is now deprecated. Use
  IMP::core::MonteCarlo::set_score_moved or
  IMP::ScoringFunction::evaluate_moved instead.
- A new application of IMP is now available:
  - [Integrative modeling of nanobody binding modes to the SARS-CoV-2 Spike protein](https://integrativemodeling.org/systems/nbspike)

# 2.16.0 - 2021-12-16 # {#changelog_2_16_0}
- OpenCubicSpline now throws a ValueException for out-of-range values, to
  be consistent with ClosedCubicSpline (previously it threw ModelException).
- SAXS tools (such as `compute_rg`, `foxs`) can now read input structures
  in mmCIF format.
- Most IMP functions that return arrays of integer or floating point values,
  or lists of ParticleIndexes, now return NumPy arrays if IMP is built with
  NumPy. Code that adds lists or searches for particle pairs in a list may
  need to be modified as NumPy arrays are slightly different from Python lists.
- IMP::pmi now handles MSE (selenomethionine) residues in input structures;
  structure is read for such residues and they are considered equivalent to
  regular MET in the FASTA sequence.
- The Windows .exe installer now supports Python 3.10.
- Scoring function evaluation can now be done more efficiently in some cases
  by using information on which particles have moved since the last evaluation.
  This behavior can be turned on (by default it is off) using
  IMP::core::MonteCarlo::set_score_moved() or by setting the `score_moved`
  parameter to IMP::pmi::macros::ReplicaExchange0.
- The orientation-dependent scoring function IMP::score_functor::OrientedSoap
  now caches the system topology and so should be roughly twice as fast in
  typical applications.
- IMP::pmi::macros::BuildSystem::add_state() now assigns multi-character
  chain IDs by default, so that it is no longer limited to creating 62
  molecules.
- IMP::pmi::output::Output now reports a ValueError if asked to write out
  a PDB file containing multi-character chain IDs, rather than silently
  truncating them.
- The unused IMP::piecewise_linear_distribution class has been removed.
  Use boost::piecewise_linear_distribution instead.
- The deprecated methods
  IMP::{Singleton,Pair,Triplet,Quad}Predicate::get_value() have been removed.
  Use the get_value_index() methods instead.
- The deprecated methods IMP::SingletonContainer::get_particles(),
  IMP::PairContainer::get_particle_pairs(),
  IMP::TripletContainer::get_particle_triplets(), and
  IMP::QuadContainer::get_particle_quads() have been removed. Use the
  get_contents() method instead.
- The deprecated IMP::isd::Weight::get_number_of_states() method has been
  removed. Use get_number_of_weights() instead.
- We no longer provide packages for Ubuntu 16.04 LTS (Xenial Xerus), as it
  reached end of life in April 2021.

# 2.15.0 - 2021-06-02 # {#changelog_2_15_0}
- The [Homebrew](https://brew.sh/) Mac packages now support Apple Silicon.
- We no longer provide RPMs for CentOS 6, since it has reached end of life.
- Python 2.6 is no longer supported; Python 2.7 is the oldest version of
  Python that works with IMP (although Python 3 is recommended).
- IMP now requires Boost 1.53 or later; support for Boost 1.41 has been dropped.
- IMP::em::FitRestraint::cast() has been removed. Use `get_from()` instead.
- The deprecated methods IMP::SingletonContainer::get_particle(),
  IMP::PairContainer::get_particle_pair(),
  IMP::TripletContainer::get_particle_triplet(), and
  IMP::QuadContainer::get_particle_quad() have been removed. Use the
  get_contents() method instead.
- The IMP::em::CoarseCC class is deprecated. Use similarly-named free
  functions instead to calculate coarse cross correlation.
- A new numerically stable grid-based Bayesian scoring function,
  IMP::em::FitRestraintBayesEM3D, has been added for cryo-EM data. Note that
  this is still in development.
- The IMP::pmi::mmcif::ProtocolOutput constructor no longer takes a file
  handle argument, and the IMP::pmi::mmcif::ProtocolOutput::flush() method
  has been removed. Instead, use the python-ihm library to output mmCIF
  (or BinaryCIF).
- IMP can now be built using external (system) copies of the RMF and/or
  python-ihm libraries, instead of those bundled with IMP itself; use the
  `IMP_USE_SYSTEM_RMF` or `IMP_USE_SYSTEM_IHM` CMake variables.
- MRC file handling has been extended; MRC files not aligned with the xyz
  axes (mapc/mapr/maps not 1,2,3) are now automatically transposed rather than
  raising an exception, and the origin is now set from the
  nxstart/nystart/nzstart fields if present and the file origin is zero.
- New applications of IMP are now available:
  - [Integrative model of the γTuSC-Spc110 complex](https://salilab.org/gtuscSpc110)
  - [Integrative structure of the Smc5/6-Nse2/5/6 complex](https://integrativemodeling.org/systems/smc56_nse256)
- IMP's copies of the old Template Numerical Toolkit (TNT) and
  JAMA/C++ library have been removed from IMP::algebra::internal.
  Use equivalent functionality in the Eigen library instead.

# 2.14.0 - 2020-12-02 # {#changelog_2_14_0}
- All IMP.parallel worker classes are now subclasses of IMP.parallel.Worker;
  the old class names still exist as aliases, but are deprecated.
- The IMP.kinematics module has had a major overhaul.
- The Windows .exe installer now supports Python 3.9, and has dropped support
  for Python 3.5.
- New applications of IMP are now available:
  - [Integrative structures of the Nef-CD4-AP2 complex](https://salilab.org/Nef_CD4_AP2/)
  - [Integrative Modeling of Yeast Exocyst Complex](https://salilab.org/exocyst/)
  - [Integrative threading of protein structure using secondary structure elements](https://salilab.org/SSEThread/)
- Bugfix: fix near-infinite loop in FoXS JavaScript output when no models
  are fit.
- Bugfix: IMP.saxs.Restraint should now work correctly when some or all
  particles are members of rigid bodies.

# 2.13.0 - 2020-05-14 # {#changelog_2_13_0}
- Ubuntu .deb packages now use Python 3 by default (install the imp-python2
  package if you want to use Python 2) and support MPI (install the
  imp-openmpi package if you want to use the IMP::mpi or IMP::spb modules).
- A binary package is now provided for Ubuntu 20.04 LTS, Focal Fossa.
- The new IMP::sampcon module implements the protocol described in
  [Viswanath et al, 2017](https://www.ncbi.nlm.nih.gov/pubmed/29211988). 
  This can be used in analysis to estimate the highest precision at which
  the sampling is exhaustive. 
- RMF files, particularly those output by IMP::pmi, now contain more information
  on the restraints used, such as restraint parameters, and links to
  non-Cartesian particles containing restraint information, such as Gaussians
  used to represent EM densities, or Bayesian nuisances. Much of this
  information can now be shown in
  [ChimeraX](https://www.rbvi.ucsf.edu/chimerax/) using the
  [RMF plugin](https://github.com/salilab/rmf_chimerax).
- IMP modules that contain no C++ code can now be marked as "Python only"
  in `dependencies.py`. IMP::test, IMP::mmcif, IMP::parallel, IMP::EMageFit,
  IMP::pepdock, and IMP::saxs\_merge are so marked. This speeds up the build
  since such modules do not need to be run through SWIG or compiled, and
  saves space by eliminating their shared libraries.
- The `crosslink_restraints` argument to IMP.pmi.macros.ReplicaExchange0 
  is now ignored (and deprecated). All cross-link restraints are now
  automatically added to RMF files.
- The `CrossLinkDataBase` argument to
  IMP.pmi.restraints.crosslinking.CrossLinkingMassSpectrometryRestraint
  is deprecated.  Use `database` instead.
- IMP.pmi.restraints.crosslinking.CrossLinkingMassSpectrometryRestraint now
  takes a `linker` argument which can be used to specify the chemistry of
  the linker.
- IMP.pmi.output.Output now supports output of pseudo-atomic PDBs in mmCIF
  format. This can be useful for quick visualization of output models that
  contain a large number of chains in software that does not understand
  the mmCIF IHM extension (for integrative models) or RMF.
- IMP.pmi now has improved support for RNA/DNA (previously all nucleic acid
  residues were treated as RNA). IMP.pmi.topology.Molecule now takes an
  `alphabet` argument which can be used to specify any of the alphabets
  provided in the IMP.pmi.alphabets module (amino acids, RNA, or DNA) or a
  custom alphabet.
- A new application of IMP is now available:
  - [Structural dynamics of the human COP9 signalosome revealed by cross-linking mass spectrometry and integrative modeling](https://salilab.org/CSN2019/)
- 'Object "foo" never used' warnings are now emitted only when IMP is run with
  internal checks turned on, as these warnings are primarily intended for
  IMP developers, not end users.
- Bugfix: fix infinite loop when reading some corrupt mol2 files.

# 2.12.0 - 2019-12-06 # {#changelog_2_12_0}
- The Windows .exe installer now supports Python 3.8, and has dropped support
  for Python 3.4.
- Packages are no longer provided for Ubuntu 14.04 (Trusty Tahr) since
  it has reached end of life.
- The IMP distribution now includes the IMP::bayesianem module developed at
  Institut Pasteur, Paris, for Bayesian handling of cryo-electron microscopy
  density map data. See Bonomi et al. at https://doi.org/10.1101/113951 for
  more information.
- The old IMP::pmi::representation::Representation class has been removed
  from IMP.pmi. New applications should use IMP::pmi::topology::System instead.
- The IMP::pmi::restraints::crosslinking::ISDCrossLinkMS class for handling
  crosslinking has been removed. Use
  IMP::pmi::restraints::crosslinking::CrossLinkingMassSpectrometryRestraint
  instead.
- The `rg` tool (part of the IMP::saxs module, used to compute radius of
  gyration from a SAXS profile) is now called `compute_rg` for consistency
  with other SAXS tools and to avoid conflicts with other packages.
- We now provide RPM packages for RedHat Enterprise Linux 8 (or compatible
  operating systems such as CentOS 8).
- The RPM packages for RedHat Enterprise Linux 8 and for Fedora now use
  Python 3 by default. If you need Python 2, install the IMP-python2 package
  as well.
- IMP::algebra::Rotation3D::get_derivative(),
  IMP::algebra::Rotation3D::get_gradient(),
  IMP::algebra::get_gradient_of_composed_with_respect_to_first(), and
  IMP::algebra::get_gradient_of_composed_with_respect_to_second() have been
  deprecated and are superseded by
  IMP::algebra::Rotation3D::get_gradient_of_rotated(),
  IMP::algebra::Rotation3D::get_jacobian_of_rotated(),
  IMP::algebra::get_jacobian_of_composed_wrt_first(), and
  IMP::algebra::get_jacobian_of_composed_wrt_second(), respectively. By
  default, the derivatives are now computed with respect to the unnormalized
  quaternion and do not include the normalization operation.
- New methods are added to compute adjoint derivatives (reverse-mode
  sensitivities) for compositions and actions of IMP::algebra::Rotation3D and
  IMP::algebra::Transformation3D upon 3D vectors.
- Fixed a bug in nested rigid body derivative accumulation, where derivatives
  with respect to quaternions were incorrectly projected to be orthogonal to
  the quaternion.
- Reimplemented rigid body derivative accumulation to use the new adjoint
  methods. The many-argument versions of
  IMP::core::RigidBody::add_to_derivatives(),
  IMP::core::RigidBody::add_to_rotational_derivatives(), and
  IMP::core::NonRigidMember::add_to_internal_rotational_derivatives(), which
  previously pulled adjoints from member global reference frame to member
  local reference frame and parent global reference frame are now deprecated.
  Pullback functionality is now handled by
  IMP::core::RigidBody::pull_back_members_adjoints().
- IMP::isd::Weight is now constrained to the unit simplex, and methods were
  added for adding to its derivatives. IMP::isd::Weight::add_weight() no longer
  resets all the weights to the barycenter of the unit simplex and instead
  initializes the new weight to 0. IMP::isd::Weight::get_number_of_states()
  and IMP::isd::Weight::get_nstates_key() were deprecated and superseded by
  IMP::isd::Weight::get_number_of_weights() and
  IMP::isd::Weight::get_number_of_weights_key(), respectively.

# 2.11.1 - 2019-07-18 # {#changelog_2_11_1}
- Bugfix: fix build system failures with CMake 3.12 and 3.13, and on Windows.
- Bugfix: IMP::atom::create_clone() now always copies mass, even of particles
  that are not atoms.
- Bugfix: IMP::rmf::create_hierarchies() should no longer fail with
  "The filename cannot be empty".

# 2.11.0 - 2019-06-25 # {#changelog_2_11_0}
- A number of new tutorials are now available covering a variety of topics
  from modeling complexes with IMP::pmi to writing new C++ code. See
  the [tutorial index](https://integrativemodeling.org/tutorials/) for
  more details.
- The build system has been updated to use new CMake functionality
  (if available) to detect Python. If you have CMake 3.14 or later, this should
  do a much better job of handling multiple Python installations (e.g. Macs
  with Homebrew). It will default to using Python 3. To force use of Python 2,
  pass `-DUSE_PYTHON2=on` to your CMake invocation.
- CMake files are now provided to make it straightforward to use IMP as
  a library in other programs. See
  [the tutorial](https://integrativemodeling.org/tutorials/using_cpp/)
  for more details.
- CMake files are now provided to build new IMP modules outside of the IMP
  build tree (i.e. a module can be built against an IMP binary).
- The IMP::OptionParser class has been removed. Use IMP::ArgumentParser instead.
- The IMP::test::TempDir and IMP::test::RunInTempDir utility classes have been
  removed. Use the IMP::test::temporary_directory and
  IMP::test::temporary_working_directory context managers instead.

# 2.10.1 - 2019-02-26 # {#changelog_2_10_1}
- Add support for OpenCV 4.
- Fix IMP::isd `create_gmm.py` script to handle command line options correctly.
- Command line tools in the Mac and Ubuntu packages should now use system
  Python (/usr/bin/python), not the first Python (e.g. Anaconda Python)
  found in PATH (which might not be compatible with IMP's Python libraries).

# 2.10.0 - 2019-01-08 # {#changelog_2_10_0}
- Applications using IMP::pmi should now use the IMP::pmi::topology::System
  class to set up the system (sometimes referred to as "PMI2"), rather than
  the older IMP::pmi::representation::Representation class ("PMI1").
  This new class is faster and produces standard IMP Hierarchy objects. The
  old PMI1-style classes are deprecated in this release and will be removed
  in the next one. For support of published studies using "PMI1", a legacy
  IMP::pmi1 module is provided (to use it, simply replace all imports of
  "IMP.pmi" with "IMP.pmi1"). This module will receive only minor bug fixes,
  and no new features.
- All IMP Python command line tools now use
  [argparse](https://docs.python.org/2/library/argparse.html) rather than
  [optparse](https://docs.python.org/2/library/optparse.html) for handling
  options, as optparse is deprecated in modern Python versions. The
  IMP::OptionParser class, which extends optparse to add standard IMP options,
  is now deprecated. Use the similar IMP::ArgumentParser class instead.
- The bundled copy of [python-ihm](https://github.com/ihmwg/python-ihm) is
  updated to the latest release. This supports faster (C-accelerated) reading
  of mmCIF files, read and write support for BinaryCIF files, and support
  for output of PMI2-style models. The new IMP::atom::read_mmcif function
  allows reading a PDB file in mmCIF format, similarly to the existing
  IMP::atom::read_pdb function.
- A new application of IMP is now available:
  - [Architecture of Pol II(G) and molecular mechanism of transcription regulation by Gdown1](https://salilab.org/pol_ii_g/)
- The deprecated IMP::isd::FNormal::density() method has been removed.
  Use IMP::isd::FNormal::get_density() instead.
- Handling of quaternions (for example in the calculation of rotational
  derivatives) is now faster and more numerically stable.
- IMP::mpi now includes a workaround for an OpenMPI failure when used
  with Python, so previous hacks (building OpenMPI with the
  `--disable-dlopen` flag, or using `sys.setdlopenflags` in Python)
  should no longer be necessary.

# 2.9.0 - 2018-07-02 # {#changelog_2_9_0}
- [Eigen](https://eigen.tuxfamily.org/) is now required to build IMP.
- The Windows .exe IMP installer no longer supports Python 2.6. Python 2.7,
  3.4, 3.5, and 3.6 are supported by this installer.
- A binary package is now provided for Ubuntu 18.04 LTS, Bionic Beaver.
- The IMP::atom::setup_as_rigid_body() function has been removed.
  Use IMP::atom::create_rigid_body() instead.
- Constructors for IMP::container classes, IMP::core::BallMover,
  IMP::core::RigidBodyMover, and IMP::core::IncrementalScoringFunction taking
  a RigidBody or Particles have been removed. Use constructors taking
  ParticleIndexes instead.
- The IMP::core::ConnectivityRestraint::get_connected_pairs() method has been
  removed. Use get_connected_index_pairs() instead.
- The stats() profiling method has been removed from
  IMP::isd::GaussianProcessInterpolationRestraint and
  IMP::isd::MultivariateFNormalSufficient. Use a third party package (such as
  gperftools) for profiling instead.
- Scores in IMP.saxs (and FoXS) now use the chi-square value rather than chi.
- New applications of IMP are now available:
  - [Modeling of the entire yeast nuclear pore complex](https://salilab.org/npc2018), as well as
    [modeling of the flexible FG regions](https://salilab.org/npc_fg_2018) and
    modeling of the individual [Nup133](https://salilab.org/nup133),
    [Nup82](https://salilab.org/nup82), and
    [Pom152](https://salilab.org/pom152) subcomplexes.
  - [Modeling of the Ecm29-proteasome complex](https://salilab.org/ecm29)
- The new modules IMP::npc and IMP::npctransport provide specialized
  restraints and other functionality for modeling static nuclear pore complex
  structures and transport through these structures, respectively, although
  may also be useful for other modeling applications.
- IMP's mmCIF support for deposition of models in
  [PDB-Dev](https://pdb-dev.wwpdb.org/), in the IMP::pmi and IMP::mmcif modules,
  now utilizes the [python-ihm](https://github.com/ihmwg/python-ihm) library,
  a copy of which is included with IMP.
- RMF files now store additional metadata, such as the primary sequence of
  each chain, software used, information on each restraint (such as fit values),
  and provenance (classes derived from IMP::core::Provenance) that describes
  transformations of the system, such as initial input from a PDB file,
  sampling, clustering, and filtering.
- The new experimental IMP::mmcif module allows generating basic mmCIF files
  directly from an IMP::Model and/or RMF files.

# 2.8.0 - 2017-08-16 # {#changelog_2_8_0}
- New applications of IMP are now available:
  - [Modeling of the yeast Spindle Pole Body core](https://salilab.org/spb/)
  - [Modeling of the SEA complex, a modulator of the TORC1 pathway](https://salilab.org/sea/)
- This will be the last release that includes packages for Ubuntu 12.04
  (Precise Pangolin) since it has reached end of life. We will continue to
  provide packages for newer Ubuntu LTS releases.
- The Anaconda and Windows .exe packages are now MPI-enabled. On Windows, in
  order to use MPI, install [MS-MPI](https://msdn.microsoft.com/en-us/library/bb524831.aspx).
- IMP::em2d::PCAFitRestraint now uses binary PGM files as output, rather than
  the less well supported text PGM format. (It can still read both text and
  binary PGM files as input.)
- IMP::em::FitRestraint::cast() is deprecated. Use `get_from()` instead.
- The deprecated profiling (timing statistics) support has been removed.
  A number of third party packages (such as gperftools) are available
  for profiling and should be used instead.
- The new module IMP::spb provides specialized restraints, samplers, and
  other objects to support modeling of the Spindle Pole Body (SPB). While
  designed specifically for this system, they may be useful for modeling
  similar systems.

# 2.7.0 - 2017-04-13 # {#changelog_2_7_0}
- New applications of IMP are now available:
  - [Modeling of the yeast Mediator complex](https://salilab.org/mediator/)
  - [Modeling of the yeast and human TFIIH complex](https://salilab.org/tfiih/)
  - [Modeling of complexes between the 26S proteasome and proteasome interacting proteins](https://salilab.org/26S-PIPs)
  - [Human Complement modeling](https://salilab.org/Complement)
  - [Modeling of a region of the fly genome](https://integrativemodeling.org/systems/?sys=22) using IMP and [TADbit](http://sgt.cnag.cat/3dg/tadbit/)
- Memory and CPU performance improvements across the code, particularly
  in IMP::pmi.
- Preview of mmCIF support for deposition of integrative models in
  [PDB-Dev](https://pdb-dev.wwpdb.org/). See the IMP::pmi::mmcif
  module for more details.
- This will be the last release that includes packages for RedHat Enterprise
  Linux 5 (and variants, such as CentOS 5), since RHEL 5 has reached end
  of life.
- The IMP::em::SurfaceShellDensityMap::binaries() method has been replaced
  with the (correctly spelled) IMP::em::SurfaceShellDensityMap::binarize()
  method.
- IMP::multifit::WeightedExcludedVolumeRestraint no longer expects that the
  IMP::core::RigidBody particles it acts on are also IMP::atom::Hierarchy
  objects.  Use an IMP::multifit::RigidLeavesRefiner in place of
  IMP::core::LeavesRefiner to get the old behavior.
- IMP::modeller::MultipleBinormalRestraint has moved to the IMP::core
  module.
- The IMP::core::setup_as_rigid_body() method has been removed.
  Use IMP::core::create_rigid_body() instead.
- IMP::test:TempDir and IMP::test::RunInTempDir are deprecated in favor
  of similar functions that work as Python context managers
  (IMP::test::temporary_directory() and IMP::test::temporary_working_directory()
  respectively).

# 2.6.2 - 2016-05-25 # {#changelog_2_6_2}
- Add support for SWIG 3.0.8.
- Add support for Ubuntu 16.04, Xenial Xerus.
- Minor documentation fixes.
- Bugfix: fix detection of termini in IMP::atom::Selection.

# 2.6.1 - 2016-04-14 # {#changelog_2_6_1}
- The 'cluster' binary is now called 'rmsd_cluster' to avoid conflicts with
  other packages (e.g. graphviz also provides a 'cluster' binary).
- Minor bug fixes to PMI.
- Minor documentation fixes.

# 2.6.0 - 2016-03-28 # {#changelog_2_6_0}
- This release includes most of the functionality of PMI2. This is an improved
  version of PMI that is faster than PMI1, more modular, and easier to use.
  See IMP::pmi for more information.
- A new application of IMP is now available:
  [Modeling of exosome complexes from cross-link MS data](http://salilab.org/exosome).
- The IMP::base and IMP::kernel namespaces have been removed (use the top-level
  IMP namespace instead).
- The IMP::display::ChimeraWriter class has been removed (use IMP::rmf instead).
- IMP::Model no longer has an implicit scoring function. This means that
  Model::evaluate() and Model::add_restraint() have been removed (use an
  IMP::ScoringFunction instead). IMP::Optimizer and IMP::Sampler now also
  require an IMP::ScoringFunction to be explicitly set before they are used.
- IMP::atom::Hierarchy::get_as_xxx() methods are deprecated; use regular
  decorators instead. For example, instead of h.get_as_residue() use
  Residue(h). If you want to check for validity first,
  use Residue::get_is_setup(h).
- IMP::atom::Selection can now select by element.
- IMP::modeller::load_restraints_file() and IMP::modeller::read_pdb() have
  been removed. Use the IMP::modeller::ModelLoader class instead.
- IMP::atom::PDBSelector subclasses are more flexible, with a new
  IMP::atom::XorPDBSelector class, and can be combined using standard
  Python operators, in similar fashion to sets (&, |, ^, -, ~ operators).
- The following modules that use FFTW (which is licensed under the GPL)
  are themselves now also licensed under the GPL: IMP::EMageFit,
  IMP::cnmultifit, IMP::em2d, IMP::integrative_docking, and IMP::multifit.
- Bugfix: sampled EM density maps should now handle resolution correctly; maps
  generated by the fixed code agree well with those generated by EMAN. The old
  radius-dependent kernel parameter code is no longer used.

# 2.5.0 - 2015-06-30 # {#changelog_2_5_0}
- Documentation has been revised and updated; the main manual now gives a
  gentler introduction to IMP, with more technical details on the code
  provided in a separate reference guide.
- The IMP::base and IMP::kernel namespaces are now deprecated. Functionality
  in both base and kernel now lives in the top-level "IMP" namespace.
- IMP::atom::Selection::get_selected_particle_indexes() has a new
  'with_representation' parameter. If turned on (the default), Selection
  returns all representational (XYZ) particles that match the request -
  for example, selecting a residue will typically return all of its atoms.
  If turned off, Selection returns the highest matching particle instead -
  so, in this case, the residue particle itself.
- All IMP::RAII objects (e.g. IMP::SetLogState) now support the context
  manager protocol in Python (e.g. "with IMP.SetLogState() as s:")
- Several long-deprecated functions have been removed. These include:
  - Several Restraint constructors that take Particles. Use equivalent
    constructors that take an IMP::Model pointer and ParticleIndexes instead.
  - IMP::core::MonteCarlo::get_number_of_forward_steps() (use
    get_number_of_accepted_steps() instead).
  - IMP::Model::remove_restraint(), IMP::Model::get_restraints(),
    IMP::Model::get_number_of_restraints(), IMP::Model::get_restraints().
    Store your restraints in an IMP::RestraintSet or use an
    IMP::core::RestraintsScoringFunction. Related methods such as
    IMP::Model::evaluate() will be removed in the next IMP release.
  - IMP::Model::set_maximum_score() and related methods. Set the maximum
    scores on the IMP::Restraint or IMP::RestraintSet directly, using
    IMP::Restraint::set_maximum_score().
  - IMP::Restraint::get_input_containers() and
    IMP::Restraint::get_input_particles(). Use IMP::Restraint::get_inputs()
    instead (similarly for get_outputs()).
  - IMP::rmf::save_frame() no longer takes a frame index argument (it was
    previously ignored anyway).
- Several functions have been deprecated in this release (and will be removed
  in the next). These include several Restraint constructors that take Particle
  or Particles objects (use constructors that take an IMP::Model and
  ParticleIndex or ParticleIndexes instead); and add_particle*(),
  set_particle*() and clear_particle*() in several Container objects (use add(),
  set() and clear() with particle indexes instead).
- On platforms that support it, OpenMP is turned on by default. To speed up
  some parts of IMP, call IMP::base::set_number_of_threads(). By default,
  only a single thread is used.
- The RPM packages now include an -mpich subpackage that can be installed
  to enable parallel computation, using the IMP.mpi module in concert
  with the mpich library.
- We now provide packages for both of the currently-supported Ubuntu LTS
  releases: Ubuntu 12.04 (Precise Pangolin) and Ubuntu 14.04 (Trusty Tahr).
- The default log level has changed from NONE to WARNING.
- A new command line tool, `multi_foxs`, allows for enumeration and scoring
  of multi-state models against SAXS profiles.
- A new command line tool, `ligand_score_multiple`, acts similarly to the
  existing `ligand_score` tool but scores each ligand pose generated by
  docking software (such as PatchDock).
- New applications of IMP are now available:
  - [Multi-state modeling of the histidine kinase, PhoQ](http://salilab.org/phoq).
  - [Determination of the molecular architecture of the 40S•eIF1•eIF3 translation initiation complex](http://salilab.org/40S-eIF1-eIF3).
- IMP::domino::DiscreteSampler::set_restraints() now allows the set of
  restraints used in DOMINO filtering to be controlled (previously, all
  restraints in the IMP::Model were used).
- IMP::modeller::IMPRestraints now transfers an IMP::ScoringFunction into the
  MODELLER score, not the implicit (and deprecated) score of the
  entire IMP::Model.
- Bugfix #775: coordinates of voxels in EM maps were previously inconsistently
  treated (they are supposed to be the centers of the voxels, but in some
  cases they were the lower left edge). The fix may result in maps and their
  bounding boxes appearing shifted by half the voxel size.

# 2.4.0 - 2015-02-27 # {#changelog_2_4_0}
- Python 3 is now supported. The Windows package now works out of the box
  with Python 3.3 or 3.4; a `-python3` subpackage is provided for Ubuntu
  and Fedora. (Apple does not yet provide Python 3 so the Mac package is not
  built with Python 3 support, but if you install Python 3 you can compile
  IMP from source to work with it.)
- A new command line tool, `rrt_sample`, allows for running rapidly exploring
  random tree (RRT) based sampling, e.g. to sample conformations of multiple
  domains connected by flexible linkers.
- Command line tools are now placed in the `bin` directory of modules (the
  old `bin` directory, used for utility programs that are not installed, is
  now called `utility`). The `applications` directory is removed.
- Several Python modules that were only used by EMageFit have been moved from
  IMP::em2d to IMP::EMageFit.
- A new tutorial that uses the IMP::pmi module is now available (modeling of
  the RNA Polymerase II stalk).

# 2.3.1 - 2014-12-01 # {#changelog_2_3_1}
- Minor bug fixes.
- Update to IMP::pmi to support the Nup84 and rnapolii biological systems.

# 2.3.0 - 2014-10-24 # {#changelog_2_3_0}
- A new IMP::pmi module was added, containing high-level Python classes to simplify the representation, scoring, sampling and analyzing of models in IMP. This module is still under heavy development, and should be considered experimental.
- Binary installers for 64-bit Windows are now available.
- The `.py` extension has been removed from all Python applications, so that they are consistent with the C++ applications.
- IMP::atom::Selection objects can now be combined using basic set operations (union, intersection, difference, symmetric difference). In Python the equivalent operators (|, &, -, ^ respectively) can be used.
- The integrative docking (idock) application now employs SOAP to improve the scoring.
- IMP::atom::CHARMMParameters::create_topology() now works with a wider range of hierarchies (previously it would only accept Residues that were direct children of Chains). For example, it should do the right thing when given a Hierarchy that contains no Chain particles, or one where Residues are grouped under Fragments.
- Only Python 2.6 or later is now supported. We still provide IMP for RedHat Enterprise 5 (which ships with Python 2.4) but you will need to use the `python26` binary (part of EPEL) rather than the system default Python.

# 2.2.1 - 2014-08-11 # {#changelog_2_2_1}
- Bugfix: PoseScore (see the ligand_score application) should now match that used by the Pose&Rank web server (http://salilab.org/poseandrank/)

# 2.2.0 - 2014-04-09 # {#changelog_2_2_0}
- A module IMP.template was added to act as a template for creating new external modules. It includes setting up git hooks for format checks and things like that.
- The Python support for grids was cleaned up. Hopefully this makes it more robust. If you were using a grid in Python that no longer exists, ping us, we can add it back.
- The generic geometry functions were simplified slightly and renamed to IMP::algebra::get_vector_geometry().
- The IMP::base::Flag class was added to simplify adding flags in C++.
- The `--log_level` and `--check_level` command line argument now take strings (eg VERBOSE) to specify their values, rather than cryptic (and a bit unstable) numbers.
- Command line options are now divided into normal and advanced ones. You do `--help_advanced` to show the advanced ones.
- Support for computing Connolly surfaces was added with IMP::algebra::get_connolly_surface(). In addition, there is now IMP::algebra::get_uniform_surface_cover(const IMP::algebra::Sphere3Ds&,double) to sample the surface of a collection of balls.
- IMP::atom::reate_simplified_from_volume() was added to create a simplified representation of a hierarchy that preserves the surface are and occupied volume. It uses IMP::algebra::get_simplified_from_volume(). If you want to play with such representations, you can use the rmf_simply application.
- IMP::atom::get_rmsd(IMP::atom::Selection, IMP::atom::Selection, const IMP::algebra::Transformation3D&) was deprecated. Use IMP::atom::get_rmsd_transforming_first() instead.
- IMP::algebra::get_rmsd() and IMP::algebra::get_rmsd_transforming_first() were added.
- The family of macros IMP_BASE_[SMALL,LARGE]_[UNORDERED,ORDERED]_[MAP,SET] have been added (eg IMP_BASE_SMALL_ORDERED_SET ()). They provide platform and boost-version independent ways to take advantage of the best set/map for an application. In particular, they use boost::container::flat_set and kin when available.
- IMP::atom::State and IMP::atom::Representation decorators have been added to provide support for multiple states and multiple representation schemes. They are integrated with RMFs and IMP::atom::Selection. See atom/multiresolution.py and atom/multistate.py for examples.
- The container implementations has been cleaned up and simplified a bit. This should not change most usage.
- [RMF](http://salilab.github.io/rmf) has been updated. There are a few minor API changes, in addition to a new, faster format (`.rmf3`).
- [Eigen](#Eigen) is now included with IMP.
- The deprecated function IMP::kernel::Optimizer::set_restraints() was removed. Use IMP::kernel::Optimizer::set_scoring_function() instead.
- The deprecated constructor for IMP::kernel::ModelObject that does not take an IMP::kernel::Model was removed. This propagates to constructors IMP::kernel::Restraint, IMP::kernel::ScoreState and kin. Make sure you pass an IMP::kernel::Model as the first constructor argument. Related to this, deprecated functions like get_is_part_of_model(), set_model() were removed as they don't serve any purpose.
- The deprecated methods in IMP::kernel::Optimizer that pertain to attribute optimization were removed. Inherit from IMP::kernel::AttributeOptimizer instead if you want to use them in your optimizer.
- Some deprecated functionality was removed. If you encounter problems, replace IMP::base::OwnerPointer with IMP::base::PointerMember, find logging stuff in IMP/base/log.h, object in IMP/base/Object.h and random in IMP/base/random.h.
- IMP::atom::Chain now uses strings for the chain ids, to be consistent with changes in the PDB. PDB files are written using the first character of the chain string.
- Added orientation-dependent SOAP scoring (IMP::score_functor::OrientedSoap and IMP::atom::OrientedSoapPairScore). Orientation-dependent SOAP scores include those that score loops (SOAP-Loop), protein-peptide interfaces (SOAP-Peptide) and proteins (SOAP-Protein). The library files themselves are rather large (~1.5GB) and so are not included with IMP. They can be downloaded separately from http://salilab.org/SOAP/.

# 2.1.1 - 2013-11-04 # {#changelog_2_1_1}
- Added support for Mac OS 10.9

# 2.1.0 - 2013-10-24 # {#changelog_2_1_0}
- There is now some limited IMP-wide gathering of timing statistics. You can add `--statistics=filename` to the command line or use the IMP::base::show_timings() function to view a summary of where IMP has spent time.
- Slack was being used inconsistently (and not always correctly) among the various containers and restraints. If you had heavily optimized the slack value for speed, you may want to revisit it.
- Class name OwnerPointer was switched to PointerMember, to denote more clearly a ref-counting pointer that is a class member.
- The dependency handling in IMP has been rewritten to simplify it and fix a bunch of bugs. There are now more checks of correctness, so behavior that might have silently worked (or not worked) before may now trigger errors. In particular, restraints/score states must have access to the IMP::kernel::Model to do much of anything, so either use constructors that take the model or call IMP::kernel::ModelObject::set_model(). Also, changing your set of inputs or outputs without calling IMP::kernel::ModelObject::set_has_dependencies(false) is now likely to trigger a check failure (it would just silently do the wrong thing before).
- Decorators have been cleaned up to make them behave consistently regarding IMP::kernel::Particle vs IMP::kernel::ParticleIndexes. This change shouldn't break existing code, but decorators should move to the new macros IMP_DECORATOR_METHODS(), IMP_DECORATOR_SETUP_0() etc.
- The IMP_GRAPH() and IMP_WEIGHTED_GRAPH() macros got an extra argument describing how to show the vertexes in the graph. They also now expose a method, eg IMP::kernel::show_as_graphviz() that writes the graph in graphviz format to an IMP::base::TextOutput.
- Support and rules for deprecating code in IMP have been updated. There are new macros and instructions on how to use them that should result in much better visibility about changes. See the C++ wiki for IMP for more information. And there is now an encoded policy of keeping deprecated things around for 1 release after deprecation.
- IMP is now much more selective about when it invalidates the dependency graph. See [Dependencies](http://github.com/salilab/imp/wiki/Dependencies) for more information. This change should make evaluation of isolated restraints much faster in certain situations where they were unexpectedly slow before.
- IMP::atom::Selection has been completely rewritten as it was very brittle. The set of particles returned may change in some cases, in some cases because it was buggy before, in some cases because of new bugs.
- Reminder: the IMP_PROTECTED macros didn't work out well, and are now deprecated. If you had Python implementations on top of IMP base classes that implement protected virtual methods, you may need to remove a leading `_` on the method name, if you get `Swig director pure virtual method called IMP::kernel::PairScore::do_get_inputs` messages.
- The generated `cmake` files are no longer stored in the repository. Instead `tools/build/setup_cmake.py` is run after checkouts and other git events that change the repository tree (assuming you have run `setup_git.py`).
- Generation of documentation using `doxygen` has been refactored. It is now done on a per-module basis, via targets like `IMP.core-doc`. The main advantage is that changes to the doc for a module can be tested comparatively quickly, just by building that module's docs. On the down side, docs are no longer quite so heavily interconnected, so dependencies only work to things that the module actually depends on.
- The restraint and score state statistics functions were removed from IMP::Model. They had been broken for quite a while, with no one complaining. Statistics can be added back easily if requested.
- Added an IMP-specific fork of `git-flow`. It handles things like `README.md` files when you start and finish feature branches and provides a tool to nicely update IMP and display the change log. The main commands of use are `git imp feature start <feature_name>`, `git imp feature finish <feature_name>`, and `git imp update`. You may want to remove the `git-flow` lines from your `.git/config` file as you may accidentally type `git flow` instead of `git imp`. You need to run `setup_git.py` to set things up.
- [RMF](https://github.com/salilab/rmf) is now included as a git submodule rather than copied into the IMP repository. You should rerun `setup_git.py` to make sure submodule stuff is initialized.


# For IMP 2.0 and earlier # {#changelog_2_0}
## Spring 2013
- Modules and applications now have a _Maintainer_ in their `README.md`, giving the github id of the person to whom issues should be assigned.
- `setup_git.py` supports the `--module` flag which will set up git hooks and things for a git repository that contains a module.
- To clean up for the release, the module dependencies are now described in a file called `dependencies.py` and the module docs in a `README.md`, both in the main module directory.
- IMP-wide support for progress bars was added with the IMP::base::set_progress_display() function and helpers. These are only displayed when the IMP::base::get_log_level() is IMP::base::PROGRESS.

## Winter 2012-2013
- Scons support was removed. Use cmake to build IMP, it is way better.
- Examples are run with a `--test` argument when IMP is built with internal checks. Expensive examples should check this flag and shorten what they do in order to try to test all their code without taking too long.
- The class IMP::core::NonRigidMember was added to allow particles that are not rigid but whose coordinates are specified via internal coordinates in some IMP::algebra::Reference3D that is part of an IMP::core::RigidBody.
- The IMP_BIG_ENDIAN and IMP_LITTLE_ENDIAN preprocessor symbols are deprecated in favor of the BOOST_BIG_ENDIAN and BOOST_LITTLE_ENDIAN symbols.
- Support for asymmetric moves was added to IMP::core::MonteCarlo. To do this, IMP::core::MonteCarloMover was added and IMP::core::Mover and IMP::core::MoverBase were deprecated and implemented in terms of the new class. This should require few or no changes in code that uses Monte Carlo support or implements movers (although movers should move to IMP::core::MonteCarlo). All IMP::core::MonteCarloMover objects keep track of statistics (number of moves and number of accepted moves), rather than that being done in the IMP::core::SerialMover. In addition, the poorly defined move probability was removed from IMP::core::MonteCarlo.
- IMP::base::WarningContext now outputs warnings immediately. This change was needed as the previous behavior resulted in occasional core dumps when the libraries for log support were unloaded before the libraries where static IMP::base::WarningContexts were declared. And there was no easy way to detect such problems.
- You can now (probably) build IMP with [CMake on IMP wiki](https://github.com/salilab/imp/wiki/Cmake).
- The maximum logging level and check level can now be controlled independently of the build mode. To, for example, enable progress level logging in a fast build, add maxlog="PROGRESS" to your config. The maximum check level for `release` has been reduced to IMP::USAGE as that speeds things up a bit.
- The way applications are structured and specified has been regularized and simplified. Python files are automatically copied/installed and binary executables are compiled from each found `.cpp` file linked with any `.cpp` files contained in a subdirectory called `lib`. Nothing needs to be put into the SConscript file.
- The Python constants like IMP.algebra.has_cgal went away as swig autogenerates ones like IMP.algebra.IMP_ALGEBRA_HAS_IMP_CGAL. While the latter are a bit uglier, the constants aren't used much and having them be auto generated is nice.
- There have been some major changes to the build system. The main one is that the SConscripts in the directories below the module directory aren't really used. They are being removed from the repository. Now everything really is off of file locations (eg all test_* in test is a test, each *.cpp in bin becomes a program etc). This greatly simplifies the build system, which has, historically been a disaster. You can now define dependencies by dropping files into a dependency subdirectory in your module, no need to mess with the SConscript.
- Building IMP now always requires specifying a `repository` argument. This was always required for out of source builds, which is what one should be doing, but is now required for in source builds to, so as to make accidentally polluting your source with an in-source build harder. Use `repository="."` in that case.
- The HDF5 functionality in RMF was reorganized. Specifically, the headers were moved into `RMF/HDF5`, the Python functionality into `RMF_HDF5` and the code into namespace `RMF::HDF5` and all mentions of `HDF5` or `hdf5` in the class and function names were removed.
- Support for IMP-wide command line flags have been added to IMP::base in the base/flags.h file. They provide a simple command line parsing interface that can be used from C++ and Python. In addition, various functionality in IMP is automatically exposed on the command line when those functions are used. For example, one can control logging, checks or profiling. See IMP/base/flags.h for (some) more info.
- OpenMP support in IMP is officially released. All tests pass. But there has been little specific testing so far.
- Access to attributes using IMP::ParticleIndex and the IMP::Model now works from Python. See IMP::Model::add_attribute() and kin.
- IMP::ParticleKey and IMP::ParticlesKey were renamed to IMP::ParticleIndexKey and IMP::ParticleIndexesKey respectively as that is what they store. Typedefs were provided to support old code.
- Indexes have been added to the docs connecting classes with all the methods that return them, examples that use them and methods that take them. And all methods that are used in examples with the examples they are used in. Please check them out and report issues and ways to improve things. You can find links on the main page.
- The docs for a modules/biological systems/applications should now be found in an `overview.dox` in the module `doc` folder. Modules in IMP svn have been updated. For external modules, you can just move a `overview.dox` from that was previously generated into your `doc` folder and (eventually) remove the lines from your `doc/SConscript`. This makes it easier to use the full range of doxygen markup, as well as removes the need to escape doxygen markup for Python.
- Examples have now been simplified into full blown doxygen examples. This involves merging the `.py` and `.readme` files (putting `\#\#` in front of each line of the `.readme`) and adding a `## \\example module/examplename.py` line at the beginning. You can use `./tools/updaters/update_examples.py modules/mymodule` to update a module that was not already updated.
- IMP::base::FailureHandler has been removed as it wasn't used.
- Handling of data and includes has been simplified. All appropriate files in the corresponding directories are linked into build/installed. This is only likely to be a problem if you had broken headers sitting around `include`. If so, just comment them out, or move them some place nicer.
- Modules now must be in a folder called `modules`, which must have a `description.py` file.
- The build system should now be a little better about cleaning up after itself.
- How headers/doc files/data/examples
- The IMP_PROTECTED macros didn't work out well, and are now deprecated. Sorry. If you had Python implementations on top of IMP base classes that implement protected virtual methods, you may need to remove a leading "_" from the method name.
- Nice version numbers will now be generated if you use git. You need to rerun
tools/git/developer_tools/init_git if you have an existing clone.

## Fall 2012
- 11/9: RMF is now an external library shipped with IMP. IMP will build it and install it automatically if you have cmake version 2.8 or higher installed.
- 11/9: Updated support macros for IMP::Restraint and IMP::ScoreState classes have been added (IMP_RESTRAINT_2() and IMP_SCORE_STATE_2()) that make it easier to return dependencies on things other than IMP::Particle and IMP::ScoreState objects. In addition, the dependency functions on scores and modifiers have been updated similarly and standardized. In general this should not cause backward compatibility problems unless you were overriding the IMP::ModelObject::do_get_inputs() in IMP::Restraint and using the IMP_RESTRAINT() macro. In that case update to the IMP_RESTRAINT_2() macro.
- 11/8: Support has been added for the C++11 keywords override (IMP_OVERRIDE) and final (IMP_FINAL). They allow you to tell the compiler to produce an error if the marked method does not override/implement a parent's method and if anything overrides a given method, respectively.
- 11/8: IMP::SingletonModifier::apply_indexes() and IMP::SingletonScore::evaluate_indexes() now require an upper and lower bound index (you can just pass 0 and the size of the array). We can make them option if there is a good reason.
- 11/8: IMP::SingletonDerivativeModifier and kin were merged into IMP::SingletonModifier and kin as the only difference, the presence of the IMP::DerivativeAccumulator (whose weight was always 1) wasn't very interested and the split added lots of complexity. If this has an impact on your code, let us know.
- 11/8; Evaluation with containers was greatly simplified, moving many methods on containers. We can add backwards compatibility versions if that is interesting.
- 11/7: Predicates, scores and modifiers written in Python need to update their methods for returning inputs and outputs. They should now have a method \c _do_get_outputs(self, m, particle_indexes) which should probably just return \c [m.get_particle(i) for in in particle_indexes] to return all the passed particles.
- 11/7: It is now preferred that IMP::Restraint and IMP::ScoreState descendants report dependencies directly using IMP::ModelObject::do_get_inputs() and IMP::ModelObject::do_get_outputs(). To do this, you should use the IMP_RESTRAINT_2() and IMP_CONSTRAINT_2() macros instead. Methods like IMP::Restraint::get_input_particles() are now deprecated. This change was made as the old mechanism introduced a lot of extra complication and made it so that there was no way to directly depend on something that was not a Particle or a Container.
- 11/3: IMP::container::InContainerPairFilter and friends now treat pairs as unordered. A flag was added to control this.
- 9/5: IMP::base::Object classes now have a method IMP::base::Object::clear_caches() that clears all cache data in the object. This is not universally implemented, but now provides a correct path for doing that. The IMP_LIST() type macros call that method when their contents changes.
## Summer 2012
- 7/3: IMP_PERIODIC_OPTIMIZER_STATE() was superseded by the class IMP::core::PeriodicOptimizerState as it is rather cleaner than the macro.
- 7/2: in order to make various base classes in IMP more Python friendly, macros IMP_PROTECTED_METHOD(), IMP_PROTECTED_CONSTRUCTOR() were added that properly expose such methods to Python. The standards checks now complain if \c protected is used an a class in the API.
- 6/24: Executables from \c module/bin are now put in \b build/module_bin/module. This removes a recurring source of errors in the build script due to the origin and destination directory have the same name in scons.
- 6/24: Benchmarks are now put int \c module/benchmark and build to \c build/benchmark/module to remove a recurring source of errors.
- 6/18: The IMP::benchmark module supports the GPerfTools profilers when available. Benchmark executables (things in \c bin whose name starts with \c benchmark_) that use the IMP_BENCHMARK() macro have command line flags to turn on and cpu and memory profiling.
- 6/12: The naming rules for .i files that are in module \c pyext directories changed. They should now be \c IMP_modulename.name.i instead of \c IMP_modulename_name.i. This is to better support underscores in names.
## Winter 2011/2012
- 20/4: A method, IMP::atom::read_pdb(IMP::base::TextInput, int, IMP::atom::Hierarchy), was added to load coordinates from a pdb file into an existing IMP::atom::Hierarchy.
- 4/4: the filter types were superseded by the predicate types. You will only see a difference if you develop a filter class (eg IMP::PairFilter -derived class) or directly call methods on filters (specifically IMP::PairFilter::get_contains()).
- 29/3: IMP::Particle::get_has_model() has been changed to IMP::ModelObject::get_is_part_of_model() to be consistent with other classes.
- 28/3: IMP::core::Mover changed slightly, adding an extra method IMP::core::Mover::get_output_particles() and requiring the IMP::Model be passed to the constructor. All movers in IMP SVN were updated without any difficulty. This allows movers to use information contained in the dependency graph amongst particles so they can, for example, weight moves based on scores.
- 26/3: IMP::SingletonContainerInput etc were added. Methods that take these as their arguments can be passed either containers or lists of particles (or tuples), as convenient. All methods that take IMP::SingletonContainer objects should eventually move over to taking this (changing just requires changing the argument from a pointer to an Input).
- 22/3: Over the last week or so, which IMP headers include which other heads have been substantially simplified. This may result in compilation errors for code outside of \c svn that depended on IMP headers including other headers. In general, you want to explicitly include the header defining each thing you use.
- 15/3: The vector used throughout IMP is now exposed at IMP::base::Vector and what it does it documented.
- 10/3: IMP::domino::RestraintCache was introduced to provide a documented centralized place to handle restraint evaluation and caching in DOMINO. In the switch various bugs involving maximum scores and IMP::RestraintSet objects were fixed.
- 10/3: Scoring functions in IMP are now implemented in IMP::ScoringFunction objects. All restraint evaluation is handled by them and they can cache various useful information to aid in accelerating restraint evaluation. Backward compatibility interfaces have mostly been provided, please complain if some important interface went away. This has greatly simplified the code as well as fixed various bugs in various types of restraint evaluation (particularly in the handling of maximum scores on IMP::Restraint and IMP::RestraintSet objects.
- 29/2: The macros IMP_NAMED_TUPLE_1(),IMP_NAMED_TUPLE_2(),IMP_NAMED_TUPLE_3() were added for easy generation of simply struct for use in passing and returning values. The generated structs support comparison, output, hashing and have constructors. Use the macros instead of a boost::tuple or a a POD struct.
- 16/2: Restraints now are evaluated with the correct weights when evaluated by themselves as opposed to always returning their weight as seen by the model as a whole.
- 15/2: The IMP::algebra grid support was rearranged and simplified. Most of the changes should be transparent. However, the IMP::algebra::grids namespace got folded into IMP::algebra, which might break some code. And various (obscure) constructors of IMP::algebra::GridD were removed. All code in svn has been changed as needed.
- 3/2: The IMP::domino HDF5 container has been revamped. This involves splitting it into a write version (IMP::domino::WriteHDF5AssignmentContainer) and a read version (IMP::domino::ReadHDF5AssignmentContainer).
- 3/2: IMP::domino::WriteAssignmentContainer and IMP::domino::ReadAssignmentContainer were added to do direct binary file writing. This is faster than the HDF5 versions.
- 3/2: The installation instructions have been revamped and the developer instruction, in particular, have been greatly simplified.
- 24/1: \c tools/show-changes has been added that shows the changes in the history log since you last updated.
- 24/1: \c tools/make-source has been added that adds a source/header pair to a module
- 24/1: principal components analysis in IMP::algebra was generalized to work in any dimension. This required renaming the class to IMP::algebra::PrincipalComponentAnalysisD.
- 24/1: the output of the IMP::algebra::PrincipalComponentAnalysisD::show() was changed to reflect the standards (values produce compact, single line output on show). The old show has been moved to IMP::multifit
- 19/1: IMP::container::ConsecutivePairContainer had IMP::container::ExclusiveConsecutivePairContainer split off of it to make the two operating mode clearer and so that there could be a clear IMP::container::ExclusiveConsecutivePairFilter to use.
- IMP::algebra::Grid::apply was added to provide faster access to all (or, later, part of a grid). It can be an order of magnitude or more faster than using the iterators when doing simple operations.
- the scons config options \c pretty and \c color were added (defaulting to True). When they are true, build commands are mostly suppressed and a much briefer description of what is being done is printed out (in color). Note that \c color mode and compilation in emacs don't get along too well.
- IMP::algebra::ParabolicFit was renamed to IMP::algebra::ParabolicFit2D (a backwards compatibility typedef is currently provided)
- IMP::algebra::LinearFit was renamed to IMP::algebra::LinearFit2D. It now supports error bars on the y-values.
## Fall 2011
- IMP::compatibility::checked_vector was renamed to IMP::compatibility::vector and made available to IMP as IMP::vector. Typedefs should use this type (IMP::vector).
- Various IMP::algebra plural typedefs which had been using std::vector (since they never were updated), have now been moved to IMP::vector.
- IMP::statistics::HistogramD now supports display with \c matplotlib.
- IMP::statistics::HistogramD supersedes IMP::statistics::Histogram
- predicate base classes have been added: IMP::SingletonPredicate, IMP::PairPredicate etc. These take particles and return an integer. Current functionality using them includes IMP::core::PredicateSingletonScore that uses a predicate to choose which score to apply.
- the core generic restraint and score state support was moved to the kernel to avoid breaking various scores outside of IMP svn.
- the IMP::display module was refactored and moved up to be a dependency of IMP::core and IMP::atom rather than vice versa. The main observable results are that you should now use IMP::atom::HierarchyGeometry, IMP::atom::SelectionGeometry, IMP::atom::HierarchiesGeometry, IMP::core::XYZRGeometry, IMP::atom::BondGeometry etc instead of finding them in IMP::display. This change means that, display can be used internally when testing and debugging functionality in IMP::core and IMP::atom and that tests that use IMP::display don't need to build all of IMP::atom.
- Decomposition of restraints now results in restraints that are faster to evaluate, using the generic restraint mechanism in IMP kernel.
- IMP::algebra::get_unit_bounding_box_d() was changed to return a bounding box with radius 1 to be consistent with IMP::algebra::get_unit_sphere_d()
- A general purpose scheme to associate data with tuples of hierarchy nodes was added to the RMF format. This deprecates the special purpose bond support.
- the way various types of geometry is stored in RMF files was changed, breaking backwards compatibility.
## Summer 2011
- some functionality from the kernel has been spun off into a new module IMP.base. You probably won't notice anything. The only significant changes are that functions that accept or return IMP::base::TextInput and IMP::base::TextOutput must declare them with the \c base qualifier (eg base::TextInput) so that swig is happy.
- the source for the kernel has been moved from \c kernel to \c modules/kernel. This is unlikely to effect anyone.
- IMP::core::ExcludedVolumeRestraint now supports filters
- IMP::domino::HDF5AssignmentTable now caches internally, which makes it several times faster than before.
- you can now pick which Python to use with the \c python argument to scons.
- the units for BD diffusion coefficients changed to be consistent with other IMP units.
- IMP::domino::get_interaction_graph() now takes an IMP::RestraintsTemp, like other functions
- The assert failure handling function was documented and renamed to IMP::handle_error() so it is easier to find when  you want to use gdb.
- to work around various issues with ref counting pointers and compiler eccentricities, we added emulation of the C++0x \c nullptr. You should prefer that to \c NULL in IMP code that you want to run cross platform.
- IMP::IntsList, IMP::FloatsList and IMP::StringsList have been added to replace the various scattered solutions for passing such types.
- IMP::Restraint::get_decomposition() and IMP::Restraint::get_current_decomposition() changed to return a single Restraint, instead of a list. This makes it easier to propagate the weight and maximum reliably.
- IMP now supports usage of restraints without adding them to the IMP::Model scoring function. To do this, do IMP::Restraint::set_model(), passing the model. The restraint can then be evaluated.
- IMP::domino::DominoSampler does not use the IMP::domino::OptimizeRestraints restraint optimization by default. Instead, if it is asked to create the IMP::domino::RestraintScoreSubsetFilterTable, it decomposes the restraints first (via IMP::create_decomposition()). This avoids several bugs and very fragile code.
- the IMP::core::DiameterRestraint was ignoring the radii of the particles involved and so was giving artificially low scores. It now is on the actual diameter of this molecule.
- the IMP::core::MonteCarlo optimizers now support incremental evaluation. This can be a lot faster when only a few particles are moved each step.
- all the plural types in IMP have moved to bounds checked vectors when using debug builds with gcc. If you get a non-imp error about an invalid access, it is probably some code that walks off the end of an array. Please report it.
- The IMP::core::MoverBase was changed to move it off of the IMP::SingletonContainer. This resulted in the IMP::core::BallMover and IMP::core::NormalMover having new constructors. Now create them from a list of particles, a list of float keys and a radius/standard deviation. This removes some complexity and inefficiencies as well is removes some scope for errors.
- Temp and non-temp decorator lists have been merged in C++. This was done to simplify code since no one was using the non-temp variants. Now all decorator lists are temp (non-reference counted) variants.
- restraints and restraint sets are now evaluated only using "canonical" weights. That is, each restraint has one weight for the model (the total over all the restraint sets it is contained in and will always be evaluated with that weight). This allows the evaluation of simple restraints to be faster.
- The IMP_LIST() macros have been changed slightly. If your usage needs to take action upon addition, removal or changes to the list, use the IMP_LIST_ACTION() variant in your header. The IMP_LIST_IMPL() macro no longer takes the actions, and the last three (generally empty arguments) will have to be removed from the call to get it to work. This is needed to move towards more flexible and efficient passing of lists of values.
- IMP::domino uses the new IMP::Model::evaluate_if_good() support to accelerate computations
- IMP::core::MonteCarlo can use the IMP::Model::evaluate_if_good() support to more quickly reject
  very bad conformations. See IMP::core::MonteCarlo::set_maximum_difference().
- IMP::core::ExcludedVolumeRestraint has been rewritten to be faster. It is especially
  faster when used with IMP::Model::evaluate_if_good()
- a new evaluation mode IMP::Model::evaluate_if_good() and IMP::Model::evaluate_if_below() has been added. It allows restraints to shortcut score computation when the score can be shown to be worse than a maximum value.
- as part of moving towards more efficient use of evaluate_if_good() various deprecated methods have been removed from IMP::core::ExcludedVolumeRestraint and IMP::core::RigidClosePairsFinder.
- incremental evaluation support was removed from IMP. The reason for doing this was that the code was complicated, created overhead even when incremental support was not used and was not commonly used. Further, decomposing the restraints and using the dependency graph yields similar results and is more transparent.
- the RMF helper binaries have been moved to their own application so that they get installed.
- IMP::display::Writer has been revised to better support writers that write multiple frames to a single file and ones that write binary data. The noticeable changes are that the existing IMP::display::Writer instances must be created with a file name. And the IMP::display::WriteOptimizerState just takes a writer rather than a write and a file name template. IMP::display::Writer::set_frame() has been added so that you can directly control the frame being written.

## Spring 2011
- An interactive mode has been added to IMP::domino::DominoSampler. The interactive mode is useful for understanding domino sampling runs and distributing domino computations across a cluster.
- Functions IMP::domino::set_assignments() and IMP::domino::get_assignments() were added which support
  writing subset assignments to data fields in hdf5 files. These can be used to helping to distribute
  domino on a cluster as well as debugging the sampling process.
- a Python function IMP.show_graphviz() has been added that attempts to render a graph with \c dot and then open the pdf.
- The Python functions IMP.show_altgraph() and IMP.get_networkx_graph() have been added to provide alternatives for quick viewing of IMP graphs. Unfortunately, they still pale compared to graphviz.
- IMP.atom.create_cover() was added to facilitate creating a summary particle for part of a hierarchy in order to accelerate restraints.
- IMP.hdf5 was renamed to IMP.rmf, the proposed name of the file format that it supports. That also better separates the hdf5 support from the file format support.
- The old I/O functions have been marked as deprecated in favor of IMP.hdf5. You may need to compile with deprecated="yes" if you use them.
- The Python graph interface now has a remove_vertex method.
- One can now access the model restraint evaluation statistics programmatically using IMP::Model::get_restaint_statistics(). Restraint statistics can be logged to a file during optimization using IMP::core::WriteRestraintScoreStatisticsOptimizerState.
- IMP::domino::DominoSampler now allows you to specify the tree on which merges occur directly. Also, you now need to specify the merge tree rather than the JunctionTree if you want to do non-loopy inference and specify something about how it is done. Sorry, it makes the code a lot easier.
- Preliminary symmetry support has been added via the IMP::core::TransformationSymmetry and IMP::core::TransformationAndReflectionSymmetry classes.

## Winter 2011
- There now is a common base class IMP::atom::Simulation for IMP::atom::BrownianDynamics and IMP::atom::MolecularDynamics. In merging them there were several minor changes made to both. The most noticeable may be that the function for setting the maximum time step length is now IMP::atom::Simulation::set_maximum_time_step(). The last time step length can be extracted by IMP::atom::Simulation::get_last_time_step()
- IMP::core::MonteCarlo::set_temperature() was renamed to IMP::core::MonteCarlo::set_kt() as that is what it is doing.
- A new module IMP.hdf5 has been added to provide more general support for saving and loading IMP::atom::Hierarchy structures to files. Multiple conformations of each hierarchy can be saved as well as information about geometry and restraints (although these can't be read at the moment, so they are not so useful).
- IMP::algebra::grids::GridD now supports dense grids in arbitrary dimension through use of IMP::algebra::grids::DenseGridStorageD.
- IMP::Optimizer now can use a list of restraint sets to compute the score rather than the complete Model score.
- each IMP::Restraint now has its own weight. This is lightly tested.
- A new log level IMP::PROGRESS has been added. The idea is that IMP::Sampler::get_sample() calls and other expensive loops can show a boost progress meter at this log level to give some idea when things are moving forward.
- IMP::domino::TrivialParticleStates renamed to IMP::domino::IndexParticleStates to be less judgmental
- IMP::domino::CompoundParticleStates and IMP::domino::RecursiveParticleStates added
- IMP::domino::DominoSampler now supports maximum scores on IMP::RestraintSets (untested).
- the name of the clustering methods have been changed to create_ from get_ since they create objects.
- the names of the recently added metric based clustering support has been changed to Metric rather than Distance.
- IMP now has the ability to have certain tests designated as expensive and to skip those tests when test-fast is run. The motivation for this is that the tests take a really long time making it impractical to run before every commit. And it is hard to tell which tests have not been run when running with the necessary multiple build processes. My thought is that tests that take about a second or less on a debug build should be left along (this is probably  >95% of the tests), but the few that take longer should be marked as expensive. To do that, rename the test to expensive_text_XXX.py (from test_XXX.py) and add expensive_python_tests= env.IMPModuleGetExpensivePythonTests() to the IMPModuleTest call in the test SConscript.
- the function IMP::display::create_restraint_geometry() was added to do what its name says.
- runtime dimensional geometric objects have been added. These include IMP::algebra::VectorKD, IMP::algebra::BoundingBoxKD and IMP::algebra::SphereKD. The IMP::statistics::Embedding classes now use IMP::algebra::VectorKD instead of Floats. The sparse grids also support variable dimensions as to the nearest neighbor searches.
- IMP::atom::DopePairScore has been added to IMP.
- IMP::atom::CHARMMStereochemistryRestraint provides a high-level simplified
interface to the bonded part of the CHARMM forcefield.
- IMP modules are now built by first combining all the .cpp files into one, and then building that file. This greatly accelerates building of a module from scratch as build time is dominated by parsing headers. This does change the semantics of .cpp files as they see headers included by and functions declared by an arbitrary subset of other .cpp files. For now they are still required to be able to be compiled separately. To get the only behavior back either globally or on a per-module basis, see the percppcompilation parameter to scons.
- Instructions and scripts have been added for building modules and things externally to the IMP build. See the installation guide.
- IMP::atom::CHARMMParameters can now automatically map CHARMM-style atom and
residue naming to PDB-style, so CHARMM topology files can be used unmodified.
- IMP::atom::CHARMMTopology::add_sequence() provides a simple way to generate a topology from a string of amino acid one-letter codes.
- IMP::atom::CHARMMTopology::add_coordinates() will generate atomic Cartesian coordinates from CHARMM internal coordinate information.
- IMP::atom::CHARMMTopology::add_missing_atoms() and
IMP::atom::remove_charmm_untyped_atoms() can now be used to ensure that atoms
read from a PDB file match the CHARMM topology.
- building of deprecated functionality is now false by default
- the IMP_COMPARISONS(), IMP_COMPARISONS_1(), IMP_COMPARISONS_2() macros now take the name of the class as an additional (first) argument. This avoids the formerly needed, \c This typedef and makes them more consistent with the other macros in IMP.
- modules can now be built externally to the IMP svn in addition to applications and biological systems. To do so, create a directory with your module in a subdir containing links to the IMP SConscript file and scons_tools and a config.py that has information needed to run IMP (eg an appropriate \c pythonpath, \c ldpath).
- removed IMP::algebra::GridD::get_index(VectorD) as it wasn't very safe (in that vectors coordinates can get rounded between the IMP::algebra::GridD::get_has_index() and IMP::algebra::GridD::get_index() calls. Use IMP::algebra::GridD::get_nearest_index() or IMP::algebra::GridD::get_extended_index() or IMP::algebra::GridD::operator[]() instead.
- renamed IMP::domino::ParticleStatesTable::get_particles() to IMP::domino::ParticleStatesTable::get_subset() as it is more useful to be able to get the subset containing all the particles.
- rename IMP::restrainer::Restraint::print_all_restraints() to IMP::restrainer::Restraint::show_all_restraints() to be consistent with the rest of IMP.
- renamed IMP::atom::get_conect_record_string() to IMP::atom::get_pdb_conect_record_string() to make clearer what it is.
- class and method names are now spell checked. Add missing words to spelling_exceptions in the module test call.
- the plural names (eg IMP.Particles()) have been removed from the Python side as they are just Python lists.
- biological systems can now include internal modules. These provide a convenient place to put application specific C++ and Python code. See the example system for more info.
- IMP_VALUES() now includes IMP_OUTPUT_OPERATOR() so you no longer need two namespace macros for each value.
- the function IMP::core::Harmonic::k_from_standard_deviation was renamed to IMP::core::Harmonic::get_k_from_standard_deviation() to conform to the standards.
- the IMP::atom::PDBSelector and IMP::atom::Mol2Selector became IMP::Object classes. All this
  means is that they need to be created with \c new in C++ code. It also means that one is
  no longer prohibited from storing them (not that there is much use in doing that).
- the standards tests have been improved to test more useful aspects. Now class and function names are checked some as well as all modules have the checks for show and plural types. The error messages should explain how to fix things.
- IMP::core::RigidBody::lazy_set_reference_frame() was renamed to IMP::core::RigidBody::set_reference_frame_lazy() to fit with the standards better.
- the transform based methods on reference frame which have been deprecated for a while were removed
- the hierarchy visiting and searching functions have been renamed to better fit the IMP naming scheme as we don't expect they were used outside of the IMP source.
- IMP::atom::NonhydrogenMol2Selector was renamed IMP::atom::NonHydrogenMol2Selector to be consistent with the PDB version

## Fall 2010
- IMP::display::PlaneGeometry was added to display planes
- the optimize methods on optimizers was moved to a "non-virtual interface". Usage has not changed, but optimizers should implement IMP::Optimizer::do_optimize() instead of IMP::Optimizer::optimize() to
benefit from better checking.
- the two-vector constructor for IMP::algebra::Plane3D now expects the second vector to be a unit vector as otherwise one could switch the order around without noticing.
- the io functions in the kernel have been cleaned up a bit (the old ones are there for backwards compatibility). See IMP::write_particles(), IMP::write_particles_binary(), IMP::write_particles_to_buffer() and IMP::read_particles(), IMP::read_particles_binary(), IMP::read_particles_from_buffer()
- IMP::core::WriteModelOptimizerState is going away as it duplicated IMP::WriteParticlesOptimizerState.
- the IMP::algebra::Grid3D has been changed to make it support any (fixed) dimension when used with sparse storage. The template arguments have also been changed to remove a redundant one. See IMP::algebra::GridD.
- the biological systems specification has been improved a little adding ability to run some rudimentary tests to make sure the scripts are ok and to not require that everything be run from the svn directory.
- A new method IMP::atom::create_compatible_rigid_body() which creates a rigid body from a hierarchy which has the same internal coordinates as another rigid body. A way to make the rigid body construction more canonical would be nice (so we don't need this function), but I'm not sure how to do that.
- Logging has been improved to better report the name of methods producing the log messages
- a macro IMP_FUNCTION_LOG has been added which should be added to the start of non-member functions which produce significant logging output.
- IMP::algebra::get_distance(const Rotation3D&,const Rotation3D&) was changed to use the Euclidean distance in R4 as that seems better behaved than the prior metric.
- IMP.domino2 was renamed to IMP.domino and the old IMP.domino was moved
- the documentation for classes and some methods now includes a list of all examples which use the class. Please report any incorrect links or phantom classes appearing in the docs. Unfortunately, functions have to be added individually. Please request any functions of particular interest.
- applications and biological systems now have their own documentation pages
- IMP::atom::Hierarchy requires radii on its leaves
- IMP::atom::read_pdb add radii to the atoms
- IMP::helper was merged into IMP::restrainer as all the functionality there was primarily to provide support for restrainer
- IMP::domino2::SubsetEvaluatorTable was removed. Pass the model and IMP::domino2::ParticleStatesTable to the IMP::domino2::RestraintScoreSubsetFilterTable instead.
- IMP::atom::Selection was added to allow specification of parts of IMP::atom::Hierarchy using biological sorts of names. A few functions to create restraints from them were added too.
- a new example was added in the kernel to show IMP used on a biological system
- IMP::display::PymolWriter now supports adding labels to things
- IMP::display::PairRestraintGeometry and IMP::display::ConnectivityRestraintGeometry were added to aid in visualizing those restraints.
- IMP::bullet was added with an optimizer to use hard body physics to resolve local collisions.
- IMP::atom::setup_as_rigid_body() has been deprecated and replaced by IMP::atom::create_rigid_body(). The latter creates the rigid body as a separate particle so that the molecular hierarchy doesn't have to worry about having its bounding sphere large enough to enclose all the members.
- IMP::core::KClosePairsPairScore was added to have count based cutoffs for close pair scoring.
- IMP::algebra::get_surface_area_and_volume() was added to compute the two numbers for a set of balls

## Summer 2010
- The IMP::core::RigidDistancePairScore and IMP::core::ClosePairsPairScore have been revised to remove certain inconsistencies and ambiguities and to make them faster. Existing code using them will need to be slightly tweaked to work.
- Javi added his 2D EM scoring functionality as IMP::em2D
- some new ways to speed up scons have been added. See IMP::core::HarmonicDistancePairScore, IMP::core::SoftSpherePairScore and, for C++ users, the generic restraint support IMP::container::create_restraint() and IMP::core::create_restraint(). These each offer between 2x and 1.2x speedup when using simple scores (like harmonics on distances). In addition, a function IMP::container::get_slack_estimate() has been added which will estimate the correct slack to use with a IMP::container::ClosePairContainer. This will be extended to support IMP::core::ExcludedVolumeRestraint eventually.
- support for dense and sparse grids have been added to IMP::algebra. See the IMP::algebra module page (I'm still working on how to make the docs clearer).
- all write functions now have associated IMP::OptimizerState and IMP::FailureHandler classes. For examples, see IMP::WriteOptimizerState, IMP::WriteBinaryOptimizerState, IMP::WriteFailureHandler, IMP::atom::WritePDBOptimizerState etc.
- functions IMP::write_binary_model(), IMP::read_binary_model() and IMP::read_configurations() have been added to support space and filesystem efficient storage of model configurations. Multiple configuration can be written to a single file. This functionality requires NetCDF be installed (NetCDF is a standard library for reading and writing binary data).
- domino2 has been added. It provides a simpler interface on Keren's domino optimize as well as a number of new optimization and hooks for customizing the optimization process
- a better explanation of how to use reference counted pointers has been added to IMP::Pointer.
- all simple, planar polygons are now supported for display when CGAL is present

## Week of April 1, 2010

- All plural objects in Python are now simply Python lists rather than C++ recreations of Python lists. This makes compilation of the wrappers much, much, much faster. The visible changes are
   - types are not checked until the lists are passed to C++
   - passing std::vector types by pointer and storing passed std::vector types by pointer will not work (but should never have been done anyway from code exposed to Python)
   - swig has issues with some overloads (not always for obvious reasons). These are being sorted out. None are commonly used.
   - get_particles() on a plural object doesn't work in Python (and is not needed in C++). Implicit conversions will always work.

- All containers need to know the model at time of construction. If, after updating, you get an error on a container constructor, just add the model as the first argument. This also means that empty lists of particles in the constructors cause check failures. We can figure out a work around if this is too annoying.

## Week of March 13, 2010
- function get_rotation_in_radians_about_axis() was renamed to get_rotation_about_axis() as it didn't parse and we don't have the "in radians" elsewhere.

- Added IMP::algebra::ReferenceFrame3D. As part of the cleanup, IMP::core::RigidBody::set_reference_frame() replaces set_transformation(). And the reference-frame related transformation construction functions were replaced. IMP::algebra::get_rotation_from_x_y_axes() was added to aid in the construction of reference frames (and replaces the algebra function taking three vectors).

## Week of March 6, 2010
- Publications now have a description field to give browsers an indication of what is in the publication to aid selection of what to read/cite.


## Week of Feb 27, 2010
- IMP::algebra::decompose_rotation_into_axis_angle() was renamed to IMP::algebra::get_angle_and_axis().

- renamed IMP::atom::bond() and IMP::atom::unbond() to IMP::atom::create_bond() and IMP::atom::destroy_bond() to be more consistent with things

- renamed IMP::core::root() to IMP::core::get_root()


## Week of Feb 21, 2010

- IMP::Object::set_was_owned() was changed to IMP::Object::set_was_used() as that better reflects what the flag means.
- various more interpolation and endian methods had their names fixed (by adding \c get_)
- the function get_mean() on vectors was removed as it duplicated IMP::algebra::get_centroid()
- build_Transformation3D_from_transformation3D was replaced by IMP.algebra.get_transformation_3d()
- IMP::algebra::almost_equal() is now IMP::algebra::get_are_almost_equal() to fit the naming conventions.
- the random vector generators have been cleaned up to remove redundant ones and make the names more consistent. They now have the form of either
  - IMP::algebra::get_random_vector_in() or IMP::algebra::get_random_vector_on() where there is one argument describing the volume or shape (such as an IMP::algebra::SphereD<4>).
  - or IMP::algebra::get_uniform_surface_cover() where the first argument is the primitive whose surface we are covering and the second is the number of points.
 Some good sed strings are
  - "s\#random_vector_in_unit_sphere()\#get_random_vector_in(IMP.algebra.get_unit_sphere_3d())\#g"
  - "s\#random_vector_in_unit_box()\#get_random_vector_in(IMP.algebra.get_unit_bounding_box_3d())\#g"
  - "s\#random_vector_on_unit_sphere()\#get_random_vector_on(IMP.algebra.get_unit_sphere_3d())\#g"
  - "s\#random_vector_on_unit_box()\#get_random_vector_on(IMP.algebra.get_unit_bounding_box_3d())\#g"
  - "s\#random_vector_in_box(\#get_random_vector_in(\#g"
  - "s\#random_vector_on_box(\#get_random_vector_on(\#g"
  - "s\#random_vector_in_sphere(\#get_random_vector_in(\#g"
  - "s\#random_vector_on_sphere(\#get_random_vector_on(\#g"
  - "s\#grid_cover\#get_grid_surface_cover\#g"
  - "s\#uniform_coverr\#get_uniform_surface_cover\#g"
  .
- Spheres in IMP::algebra are now supported in general dimensions. See IMP::algebra::SphereD.
- Many methods in IMP::algebra were renamed to be more consistent with other methods or general conventions. Most of these simply involved adding \c get_ as a prefix and/or add a \c _3d suffix when they did not take any arguments.
   - build_Rotation2D_from_Vector2D became IMP::algebra::get_rotation_to_x_axis()
   - most of the Rotation3D and Transformation3D functions (in addition, IMP::algebra::get_identity_rotation_3d() and IMP::algebra::get_identity_transformation_3d() added the \c _3d so we can add 2D versions at some point)
   - IMP::algebra::Transformation3D::get_transformed() and IMP::algebra::Rotation3D::get_rotated(). Replacing \c ".transform(" worked in the IMP code base.
   - IMP::algebra::get_distance(), this also carries over to the IMP::core::get_distance()
  The following global replacements are probably safe (in sed expressions)
   - "s\#core.distance(\#core.get_distance\#g"
   - "s\#algebra.distance(\#algebra.get_distance\#g"
   - "s\#\.transform(\#.get_transformed(\#g" Only in C++
   - "s\#\.rotate(\#.get_rotated(\#g" Only in C++
   - "s\#rotation_from\#get_rotation_from\#g"
   - "s\#rotation_in\#get_rotation_in\#g"
   - "s\#identity_rotation(\#get_identity_rotation_3d("
   - "s\#::distance(\#::get_distance(\#g"
   .
- IMP::algebra::Vector3D and IMP::algebra::Vector3Ds were replaced by the expanded (non-typedef) version in functions parsed by SWIG as the current situation was extremely brittle. For the moment, you should not use the typedefs in definitions that swig sees. Sorry.
- IMP::algebra::Sphere3DPatch was renamed to IMP::algebra::SpherePatch3D to be consistent with the other geometry and allow us to support higher dimensions in the future.
- rigid_align_first_to_second was renamed to IMP::algebra::get_transformation_aligning_first_to_second() and build_Transformation2D_from_point_sets was renamed to IMP::algebra::get_transformation_aligning_pair()

## Week of Feb 14, 2010

- The IMP::atom::Bond types were rearranged to reconcile the protein-centric classification with ligand support.

- IMP::atom::Atom no longer has charge since we have IMP::atom::Charged.

- IMP::atom::read_mol2() and IMP::atom::write_mol2() were added

- IMP::atom::Selector and descendants renamed to IMP::atom::PDBSelector since we will soon have Mol2Selectors. In addition, the IMP::atom::IgnoreAlteriativesSelector is now IMP::atom::NonAlternativeSelector to keep the name positive, like the others. In the IMP body, all instances of the string Selector were for PDBSelectors and so sed was safe to use.

- IMP::atom::read_pdb() lost the "ignore_alternatives" argument. Instead, all of the provided selectors, other than IMP::atom::AllSelector ignore alternatives internally. Code that uses the IMP::atom::AllSelector should probably change to the IMP::atom::NonAlternativeSelector.

- IMP::example renamed (from examples)

- The IMP_USAGE_CHECK() macro lost the (unused) third argument.

## Week of February 3, 2010

- The model io code as moved into the kernel so it is now IMP::write_model() and IMP::read_model()

- Remove the version_info argument from the implementation macros. Instead, just pick up the module version info automatically.

- Add a function Object::get_type_name() and Object::get_module() to get the respective bits of information about each object.

- Change Object::show() to be a non-virtual wrapper which prints the object name and other info before passing control off to Object::do_show().

- The containers were moved to IMP.container. See that module page for a full list of what moved. In the process, the backwards compatibility functions were removed from IMP::container::PairsRestraint and kin.

- IMP.atom.create_protein() now returns the created protein

- the simplify functions have been moved from IMP.helper. They are now IMP.atom.create_simplified_along_backbone().

- IMP.helper.clone() has been renamed to IMP.atom.create_clone()

- IMP.misc.ConnectingPairContainer has been moved to IMP.core.ConnectingPairContainer

- The locations for pixels in IMP::em::DensityMap have been moved to the center of the corresponding voxel from the lower left corner.

- IMP::em::get_transformed(), IMP::em::get_resampled() and IMP::em::get_density() have been added.

- The documentation has been majorly cleaned up and simplified. Please look around and see if you like it. There are now two main pages, the introduction and the developers guide, rather than the previous plethora of pages.

- IMP::algebra::Cone3D::get_bounding_sphere() has been removed since it was not of general use, not returning the bounding sphere you would expect and was trivial to implement.

- IMP::algebra::projection() was removed since it didn't actually project onto the segment and the name didn't follow the normal conventions. And it wasn't used.

- Most geometry now has namespace methods IMP::algebra::get_bounding_box(), IMP::algebra::get_surface_area(), IMP::algebra::get_volume().

## Week of January 22, 2010

- A generic geometry layer has been added (see \ref genericgeometry). Using it, IMP::atom::rmsd(),
  IMP::algebra::alignment_taking_first_to_second() and the new IMP::atom::native_overlap() all
  can work on either collections of either IMP::core::XYZ particles or IMP::algebra::Vector3Ds.

- Deprecated functionality has been removed from IMP.core. For those still using it, IMP::core::ClosePairsScoreState was replaced by IMP::core::ClosePairContainer and IMP::core::CloseBipartitePairsScoreState was replaced by IMP::core::CloseBipartitePairContainer.

- The macros for Scores changed slightly. Scores not in IMP svn which use the IMP_*_SCORE macros now have to implement the get_is_changed() function outside of the class declaration and scores which use the IMP_SIMPLE_*_SCORE now don't have to implement the functions to get interactions and used particles.

- Rename IMP::core::MinimumPairScoreRestraint (and kin, Maximum, Singleton, Triplet and Quad) to IMP::core::MinimumPairRestraint.

- Add IMP::core::MinumumPairScore (and kin).

## Week of January 1, 2010

- IMP::em is now using Particles to resample density maps and for fitting restraints. The previous ParticleAccessPoint mechanism is removed.

- IMP::UsageException and IMP::InternalException are now reserved for their respective
  checks (and cannot be thrown by IMP_THROW()). This makes the distinction between API
  exceptions (which are thrown in any build mode and should be documented and tested)
  and helper exceptions which are only thrown when checks are turned on (and hence
  should not be documented) clearer.

- IMP::core::RestraintSet moved to IMP::RestraintSet. The restraint sets now simply define a tree
  with weights which the model traverses as opposed to being an opaque IMP::Restraint themselves.
  This means that incremental evaluation of restraints in restraint sets now works and that
  restraints in restraint sets can be individually evaluated. Existing working usage should not
  have changed (so \c sed should manage updates just fine), but the internal
  implementation is completely new, so pay attention.

- IMP now has a text i/o layer consisting of IMP::TextInput and IMP::TextOutput. These classes are
  convertible to C++ streams and implicitly constructable from both streams and file paths. As a result,
  functions that take them will work when called with a string for a file path, a Python file or a
  C++ stream.

- The IMP.examples module now documents how to use the needed aspects of scons and SWIG.

- The IMP.examples module is used as the basis for new modules created by the make-module script, so those include more documentation and are tested.

- Module overview pages are now generated from the information passed in the SConscript file, rather than from the (now removed) modulename.dox file. See the examples file for an example of the things you can do there.

- boost program options is now a checked for dependency.

- The IMP::Model now uses dependency information from IMP::ScoreStates to automatically reorder the IMP::ScoreStates so that they are evaluated in the right order. Also, IMP::Model::evaluate() on a subset of the restraints now only updates the needed score states, not all of them.

- Functions on rigid bodies no longer provide the IMP::core::RigidMemberRefiner as a default as it is, pretty much always, the wrong thing to use. That class may go away without notice in the future and is no longer documented.

- the IMP::helper::create_simple_connectivity_on_rigid_bodies() and IMP::helper::create_simple_excluded_volume_on_rigid_bodies() now both take an IMP::Refiner as an (optional) final argument. This makes it so they can be used with the rigid bodies created from molecular hierarchies. This code still needs to be updated and the docs don't reflect what the code was or is doing, so use with caution (see notes in the header file).

- The IMP::helper create* functions now all take non-Object inputs as const& to make clear what is input and that there are no memory management gotchas.

- a new base class IMP::Constraint has been added for constraints. Various
other classes have been renamed to be consistent.

## Week of December 11

- The interface of IMP::PairScore changed slightly to make the function signatures more uniform across various methods. Now all methods that take a pair of IMP::Particle objects take a const IMP::ParticlePair&. Previously some took that, some took an IMP::ParticlePair and some took two IMP::Particle*s. If you have an implementation of an IMP::PairScore outside of svn, you will have to update your function signatures (the compiler will tell you where). Backward compatible IMP::PairScore::evaluate() methods have been provided, so simple users of pair scores shouldn't see a difference.

- IMP::core::PairRestraint takes a IMP::ParticlePair in the constructor instead of two IMP::Particle*s. A backwards compatible constructor can be added if needed.

- IMP::ParticlePair::first and second went away since no one claimed to be using it and it complicated the implementation.

- The generic restraints/score states/scores infrastructure has been extended to triplets and quads (for angles and torsion angles).

## Week of December 4

- IMP now makes use of Boost.Filesystem to manipulate paths. Things may not work well on systems where boost libs are not available which does not support posix paths. But libless boost installs generally don't exist outside of our test systems.

- new functions like IMP::core::get_example_path(filename) and IMP::core::get_data_path(filename) allow one to easily find a data file named 'filename' for the examples and library internal data.

- The IMP::display module has been revamped in order to support non-linear geometry. VRML support has been dropped. CMM support will be dropped unless someone requests it (as IMP::display::ChimeraWriter does all it does and more).

## Week of November 19

- imp.xcodeproj was moved into tools and updated accordingly

- the bin directory finally went away

- IMP::display::ChimeraWriter now supports the latest version of Chimera

- IMP::display::CGOWriter was renamed to IMP::display::PymolWriter as it can do more than just CGO.

- IMP::VectorOfRefCounted::operator[] can now be used for assignments just like a normal vector. No more need to use the IMP::VectorOfRefCounted::set() method.

- the IMP::atom::Hierarchy constructor from an IMP::Particle* is now explicit (as were the decorator constructors)


## Week of November 12

- All exception types are now mapped to equivalent classes in Python. The
class hierarchy is similar (e.g. IMP::ModelException derives from IMP::Exception
in both C++ and Python) so all IMP exceptions can be caught in Python using
"except IMP.Exception". For convenience, the IMP::IOException,
IMP::ValueException and IMP::IndexException classes in Python also derive from
the similarly-named standard Python classes (IOError, ValueError and IndexError
respectively).

## week of October 29 Update

- You can now add members to rigid bodies via IMP::core::RigidBody::add_member(). These members can be other rigid bodies (although this functionality is only lightly tested).

- The code to get bounding volumes for IMP::atom::Hierarchy has been moved to the atom module, as as the clone and destroy code. They can be found at IMP::atom::clone(), IMP::atom::destroy(), IMP::atom::get_bounding_box().

- Added IMP::core::VolumeRestraint.

- Several functions have been added to helper in creating restraints. They are create_simple_connectivity_on_rigid_bodies(), create_simple_connectivity_on_molecules(), create_simple_distance(), create_simple_diameter(), create_simple_em_fit(), and create_simple_excluded_volume_on_rigid_bodies(). Functions load_em_density_map() and set_rigid_bodies() are added as well. See IMP::helper for more information.


- IMP::ScoreStates are further hidden. Namely, IMP::core::RigidBody constructs the needed score states internally, doing away with the need for the create functions (which have been done away with). In addition there are new decorators IMP::core::Cover and IMP::core::Centroid which manage their respective score states, further doing away with more create methods. The hierarchy-based create method for rigid bodies has been moved to the atom module and is called IMP::atom::rigid_body_setup_hierarchy().

- IMP::em::read_map() will figure out the file type to use automatically from the extension. Other such methods should follow suite.

- A class IMP::core::StructureSet has been added to provide a convenient way to manage solutions of optimization runs.

- IMP::core::RigidBodyMover now takes its angle argument in radians and is documented as such.

- IMP::core::ClosePairsScoreState and IMP::core::CloseBipartitePairsScoreState have been replaced by IMP::core::ClosePairContainer and IMP::core::CloseBipartitePairContainer. The score states have been marked as deprecated and are mostly still there, but are more limited than they were.

- IMP::core::AllPairsPairContainer has been renamed to IMP::core::AllPairContainer and a bipartite version has been added.

- All containers now keep track of what they looked like on the previous time step.

- The IMP::core::ListPairContainer and IMP::core::ListSingletonContainer have had their interface reduced a bit in order to make implementing change tracking easier.

- The set of exceptions has been simplified to go along with simplification of the checks. We now have IMP::InternalException and IMP::UsageException which are thrown by the respective checks (and the former is thrown by IMP_FAILURE()). When you want to to pass an exception back to Python use one of IMP::ValueException or IMP::IndexException or IMP::IOException. There is also a new macro, IMP_THROW() to be used when you want to throw an exception with a nice error message. Please look at code you have worked on and make sure that the exceptions make sense given the new clarifications.

- An IMP::ModelException is now thrown when IMP::Particle attributes attain invalid values. This exception can be caught to recover from failures of IMP::core::ConjugateGradients or difficult restraints.

## Week of October 15

- The set of functions needed to get meta information about IMP::Restraint and IMP::ScoreState objects has hopefully stabilized. Sorry about the thrashing. If you have restraints or score states not in SVN, see the corresponding IMP_RESTRAINT type macros, the IMP::Interaction class and base classes for what exactly you need to implement.

## Week of October 8

- IMP::Interaction was modified to split IMP::interaction::get_used_particles() into IMP::interaction::get_read_particles() and IMP::interaction::get_write_particles(). This makes it possible to check for IMP::ScoreState objects being in an inconsistent order (so that the input to one is updated after it is read). Later, we will be able to automatically order the score states ensure that there are no problems.

- IMP::atom::Hierarchy has been modifier to get rid of the IMP::atom::Hierarchy::Type. Instead, all types are contained in the decorators. IMP::atom::get_by_type() was also updated to reflect this.

- IMP_check() and IMP_assert() have been
replaced with IMP_USAGE_CHECK() and IMP_INTERNAL_CHECK()
respectively. Hopefully this makes it clearer when to use
which. IMP::set_check_level() has been revised accordingly (to use
IMP::USAGE and IMP::USAGE_AND_INTERNAL). Also, IMP_failure() and
IMP_not_implemented() have been renamed to IMP_FAILURE() and
IMP_NOT_IMPLEMENTED() to make all macros be all caps. To update
external code,
      - replace IMP.EXPENSIVE with IMP.USAGE_AND_INTERNAL
      - replace IMP.CHEAP with IMP.USAGE
      - replace IMP_assert and IMP_check as above.

## Week of October 1
- IMP::ScoreState and IMP::Restraint now better track the set of particles that they use and the dependencies between the particles. To this end, a new base class IMP::Interaction has been added with methods to get the inter-particle interactions and the set of particles used.

- .cpp, .h, .py and SConscript files which contain the string "DO NOT COMMIT" will be rejected on checkin. Use this to make experimental or debugging changes you are making so you don't accidentally commit them.

- The search module is no longer built by default and is not longer supported. It will get moved out of svn shortly.

- IMP::ScoreState objects now also have IMP::Interacting::get_interacting_particles() methods. Soon IMP::PairScore and IMP::SingletonScore objects will too.

## Week of September 27

- Some support for gather statistics has been added to IMP::Model (see IMP::Model::set_gather_statistics()). If requested, an API can be provided so that the individual data points can be returned to programs.

- A class IMP::core::RigidBodyDistancePairScore has been added which provides accelerated computations for the distance between two rigid bodies.

- The SWIG input files were renamed from swig.i to swig.i-in to aid in dependency tracking.

- rigid bodies now have two sets of particles associated with them in the various places they are used. One is the IMP::core::RigidBodyMember particles, as was previously the case. The other is defined through a refiner (and could be the RigidBodyMember particles if a IMP::core::RigidMembersRefiner is used). The idea is that you sometimes want some particles which are transformed along with the rigid body, but which are not really part of the representation of the rigid body. Examples would include marker points or multiresolution representations of proteins.

## Week of September 20

- all \c .i files have been renamed to start with \c IMP_ to help make dependency tracking easier.

- static builds (builds with \c static=True) build both the static and dynamic libraries and just static executables

- the \c profile build target has been removed as \c static=True does the important bit of what is needed. Just do \c linkflags=['-pg'] to add the needed link flag for \c gprof.

- Restraints should now implement IMP::Restraint::unprotected_evaluate() instead of IMP::Restraint::evaluate(). The latter can now be called outside of IMP::Model::evaluate() and will return the right answer always.

- \c bin/imppy.sh no longer works, as was previously warned. Use \c tools/imppy.sh instead. The bin directory will go away eventually, for now the script just tells you to use the tools version.

## Week of August 30

- A new score IMP::core::BoundingBox3DSingletonScore has been added to keep particles
  in a box.

- str should now work better in Python when applied to IMP::Object objects and a few others. Objects
  should use the new IMP_SHOWABLE and IMP_SHOWABLE_INLINE macros instead of declaring show
  functions directory to make it so that they work in Python. It is now a bug to \c print or \c str
  to not return something useful in Python for any IMP object.

## Week of August 23

- each module now has a version, eg IMP::get_module_version_info() which is also returned by the various restraints of the module. The Python code checks that loaded libraries have the expected version numbers to try to provide better messages when runtime linking problems occur.

- the various bounding_box methods have been renamed to ::get_bounding_box() to be more consistent with the other names.

- Python documentation is now parsed by doxygen

## Week of August 15

- The Object::get_version_info() result now includes the SVN revision info when building from SVN. This means you can use it to more easily tell exactly what a built version of IMP was built from.

## Week of August 8

- Treatment of hetatoms in hierarchies (and hence pdbs) is now documented. See IMP::atom::Hierarchy. This involved broadening IMP::atom::Residue to handle ligands and having IMP::atom::Hierarchy::LIGAND, IMP::atom::Hierarchy::AMINOACID and IMP::atom::Hierarchy::NUCLEICACID be handled by IMP::atom::Residue.

- IMP::atom::read_pdb() currently drops HOH ATOM records on the floor. We should add a IMP::atom::Water decorator if anyone wants to handle them (since they aren't atoms and don't have elements).

- IMP::atom::Mass() has been added for decorating particles with mass. IMP::atom::Atom mass has been moved to that.

- The scheme for generating atom types is now fully specified. See the IMP::atom::AtomType documentation.

- IMP::atom::Atom and IMP::atom::Residue have been somewhat restructured. Some of the helper functions have been renamed to be more descriptive or removed (if they duplicated other easily accessible functionality). get_residue_index() has been removed (since you can just call get_index() on the return result of the IMP::atom::get_residue()). IMP::atom::get_chain() now returns an IMP::atom::Chain. root() was renamed to IMP::atom::get_root() for consistency.

- SWIG files are now generated from a file called swig.i in the pyext directory. This file only has to contain module-specific commands such as lines to wrap headers and instantiate module templates. No more boilerplate.

- The contents of bin are moving to tools since the two directories both contained assorted development tools
  (not all of which were executable). For now, bin/imppy.sh will still work, but that will go away soon.

- IMP::Decorator::show() now just takes the stream (it used to take a prefix also, which was often ignored).
  Anyone who implemented a decorator will have to delete the second argument of their show function.

## Week of August 1

- Containers now have methods IMP::SingletonContainer::evaluate(), IMP::PairContainer::evaluate(),
  IMP::SingletonContainer::apply() and IMP::PairContainer::apply(). Using these can be significantly
  faster than looping over the particles externally. Similarly, there is IMP::SingletonScore::evaluate(),
  IMP::PairScore::evaluate(), IMP::SingletonModifier::apply(), IMP::PairModifier::apply().

- The decorator functions have been renamed to IMP::Decorator::setup_particle(), IMP::Decorator::decorate_particle()
  and IMP::Decorator::particle_is_instance(). A shell script \c tools/update-decorators is provided which
  updates the names in all code in subdirectories of the current directory. Please backup things first.

- a function, IMP::Restraint::safe_evaluate() has been added to be used
  when requesting the value of restraints outside of the IMP::Model::evaluate().

## Week of July 18

- The atom::BondPairContainer has been renamed to atom::BondPairFilter
  since it wasn't a real container. A real atom::BondPairContainer has
  been added.

- Out of source builds mostly works. To do an out of source build, make a link
  to \c scons_tools and \c SConstruct from the source directory in the build
  directory and then add the line \command{repository="../path_to_src_dir"} in
  the \c config.py in the build directory. Then running \c scons in the build
  directory will put generated files there. This allows you to make both a
  \c release and \c fast build off of the same set of sources. Proper docs
  will be added soon.

- The SConscript setup for a module has been greatly simplified so it should
  be easy enough for users to maintain their own module and updates to the
  build system shouldn't involve changes to user SConscripts any more. This does
  mean that any non-svn modules need to be updated. Look at IMP.core or another
  module and copy what is there. Again, proper docs will be added soon.


## Week of July 11

- Per Javi's suggestion, the conventions have been split into
  "Coding conventions" and "API conventions" and linked from the main page.

- benchmarks got moved to their own module, IMP::benchmark and will
  now be tracked over time

## Week of July 4

- FilteredListSingletonContainer and FilteredPairSingletonContainer
  went away as there was too much hard to factor code shared with
  IMP::core::ListSingletonContainer and IMP::core::PairSingletonContainer. The
  IMP::core::ClosePairsScoreState is now handled by a list of filters
  on the class itself. That is, do
  IMP::core::ClosePairsScoreState::add_close_pair_filter() to add a
  filter.

- Hooks have been added to allow actions to be taken on an assertion
  or check failure. See IMP::HandleFailure and its descendants for
  more details.

- IMP::display::CGOWriter has been much improved and now allows
  provides lots of display-time control and easy building of
  animations.

- Generic optimizer states have been added
  (IMP::core::SingletonsOptimizerState and
  IMP::core::PairsOptimizerState).

## Week of June 15

- box distributions (IMP::algebra::random_vector_on_box(),
  IMP::algebra::random_vector_in_box()) take bounding boxes

- IMP::em::DensityMap are now IMP::Object objects. Some current
  allocations on the stack may need to be changed (since ref counted
  objects can't be stack allocated).

- IMP::em::DensityMap::Read() is now deprecated (as is
  IMP::em::DensityMap::Write) as they violated a slew of
  conventions. Use IMP::em::read_map() and IMP::em::write_map()
  instead.


## Week of June 8

- new methods IMP::atom::add_radii() and IMP::atom::add_bonds();

- Hierarchys to IMP::atom::Hierarchies

- IMP::Particles has been changed to a new type. It no longer plays
  quite so well with Python lists (you can't create one from an
  arbitrary Python list).

- The containers for multiple decorators have been revised to make them
  more useful. See IMP::Decorators. You can now implicitly convert,
  for %example, a IMP::core::XYZs to an IMP::Particles (as well as use
  IMP::Decorators::get_particles()). All methods that take a
  collection of particles with a certain type now instead take a
  IMP::Decorators.

- A method that has expectations about the particles it takes should
  take decorators rather than particles. That is, anything which
  expects IMP::core::XYZ particles, should take an IMP::core::XYZs
  instead of IMP::Particles.

- IMP_LIST() now takes an extra argument (the name of the plural
  container)

- In C++ IMP::Decorator objects are implicitly convertible to
  IMP::Particle* objects. Unfortunately, making this work in Python is
  problematic.

- More methods take and return decorators rather than
  IMP::Particles. This means it is clearer what their expectations are
  and what they produce.

## Week of May 15

- The IMP::helper module was added and various functionality moved
  there. See its documentation page for a list of what is there.

- IMP::algebra::SphericalCoords was renamed to
  IMP::algebra::SphericalVector3D to be consistent with other algebra
  classes.

- IMP::algebra::Rotation2D is now IMP::InvalidDefault to be consistent
  with the other similar classes.

- We are trying to be a bit more specific about what is expected from
  a IMP::atom::Hierarchy. Towards that end, there are two methods for
  extracting a representation from a hierarchy,
  IMP::atom::get_detailed_representation(), and
  IMP::atom::get_simplified_representation()

- A method has been added to produce a simplified copy of an
  IMP::atom::Hierarchy.  The method is still a bit crude and could
  benefit from other people inspecting the output and saying how it
  should be improved.

- There is now an IMP::algebra::BoundingBoxD (and
  IMP::algebra::BoundingBox3D) to track bounding boxes. There are
  methods like IMP::algebra::bound_box(Sphere3D) which gets the
  bounding box of a sphere.

- Each IMP::Object has its own log level. If
  IMP::Object::set_log_level() is called with a value other than
  IMP::DEFAULT, the value is used for code within and called by the
  object. To support this in your objects you need to add
  IMP_OBJECT_LOG to the start of each major method. It has been added
  to some of the core objects.

## Week of May 8

- IMP::atom::MolecularHierarchy has been renamed to
  IMP::atom::Hierarchy. Use \command{sed -i.old
  "s\#MolecularHierarchy\#Hierarchy\#g" my_files}

- the long-deprecated Name(Decorator) was removed

- The decorator suffix has been removed from decorator names.

- Unit conventions have been established and documented for distance,
  energy, force and angle.

- there is a function IMP::atom::create_protein() to create a coarse
  grained protein. The function is crude so far, but the idea is that
  we should have standard ways of generating such things so that
  everyone can benefit from best practices.

- a class IMP::atom::BondGraph has been added so Boost.Graph
  algorithms can be used with bond graphs

- the IMP-specific doxygen commands have been documented.

- the doxygen commands unstable{name} and untested{name} have been
  added to doxygen to be used for marking methods and functions as
  likely to change or not well tested. Pass the name of the class or
  method as name.

- bonds can now be added to molecular hierarchies automatically see
  IMP::atom::add_bonds()

## Week of May 1

- There is a IMP::Rotation2D

- You can now extract fixed Euler ZYZ angles from a
  IMP::Rotation3D. This code can serve as a template for extracting
  other Euler angle conventions if they are needed.

- IMP::algebra::rotation_between_two_vectors() changed to
  IMP::algebra::rotation_taking_first_to_second() to make it clear
  which direction the rotation goes.

## Week of April 27

- IMP::Decorator derived objects are now convertible to bool. So code
like \code if (d) { blah } \endcode works.

- IMP::Decorator::cast now returns a null decorator (\c
  DecoratorName()) rather than throwing an exception. This might make
  it actually useful.

- New IMP::statistics module for statistical methods
  (e.g. clustering).

## Week of April 20

- Support for taking advantage of rigid bodies in collision detection
  has been added via the IMP::core::RigidClosePairsFinder.

- All IMP::core::ClosePairsScoreState-related functionality has been
  optimized and should be noticeably faster.

- The EMBED project has been merged into the IMP::em module. Thus, it
  is no longer necessary to obtain EMBED separately to build IMP::em.

- All C++ methods which work with std::istream or std::ostream
  arguments should now be usable from Python: any Python file-like
  object can be used.

- The SWIG interface now ties in to the reference counting mechanism
  used in the C++ code, for all classes derived from
  IMP::RefCounted. So, for %example, deleting a Python object should
  not free the underlying C++ object if another C++ object holds a
  reference to it, and unrefing a C++ object should not delete it if a
  Python object still holds a reference to it. There should be no
  further need to manually keep references to Python objects to
  prevent things from being prematurely cleaned up. This should be
  transparent to the user; please report any problems.

- IMP::atom::AtomDecorator no longer inherits from
  IMP::core::XYZDecorator.

## Week of April 13

- The decorators IMP::atom::AtomDecorator, IMP::atom::ChainDecorator,
  IMP::atom::ResidueDecorator etc. now inherit from
  IMP::atom::MolecularHierarchyDecorator. This means they can set
  their IMP::atom::MolecularHierarchyDecorator::Type properly and
  saves a lot of typing in the common case. We can always make
  hierarchy decorators zero memory overhead if we find that the cost
  matters.

- The base classes IMP::Comparable, IMP::NullDefault,
  IMP::ValidDefault and IMP::UninitializedDefault were added to
  document what the default constructors do for various objects in
  IMP.

## Week of April 6

- IMP::Object now defines pure virtual methods
  IMP::Object::get_version_info() and IMP::Object::show(). All
  non-abstract classes which inherit from IMP::Object must implement
  them. Doing this means they are more uniformly implemented and are
  documented in one place.

- IMP::Object is now reference counted (the only objects this changes
  are IMP::Model and IMP::Optimizer). As a result optimizers and
  IMP::Model objects must be created on the heap.

- IMP::RefCounted has had its name changed and no longer inherits from
  IMP::Object. This makes it easier to use independently.

- the docs for reference counting (IMP::RefCounted) and and IMP::Decorator
  have been improved

- running doxygen produces no warnings. Let's try to keep it that
  way. Run \command{scons doc > /dev/null} before you check in large
  blocks of new code to make sure that you didn't introduce warnings.

- Helper classes have been added to make SingletonModifier and
  PairModifier objects look like functors for C++ and Python. This
  makes it so you can use \c map in Python and \c for_each in C++. See
  IMP::SingletonFunctor and IMP::PairFunctor for more information.

- The recent changes page has moved to a doxygen page to make it
  easier to link changes back to the relevant source code.

## Week of March 20:

- create_rigid_body(), create_rigid_bodies(), create_centroid()
  etc. now require you to add the score state to the model
  yourself. Whether the rigid body is enforced or not can be
  controlled by adding or removing the returned IMP::ScoreState.

- All previously deprecated code has been removed. This includes
  indexes in particles, the no-argument constructor for particles and
  the functionality that was moved from core to atom.

- The IMP::core::RigidBodyDecorator and
  IMP::core::RigidMemberDecorator have been simplified by removing the
  traits classes. There is now only one type of rigid body and it
  stores the list of member particles internally.

- IMP::core::NameDecorator has been deprecated as IMP::Particles have
  built in names (use IMP::Particle::get_name(),
  IMP::Particle::set_name()).

- IMP::atom::ChainDecorator has been added

## Week of March 13:

- A new IMP::display::Writer, IMP::display::ChimeraWriter has been
  added which exports geometry to native Chimera constructs. It
  probably should be used instead of bild and cmm for most purposes as
  it combines the best of both types.

- compose() for transformation is now a free function so
  compose(rotation, vector) will work via promotions.

 - the geometry classes have been cleaned up and are now more
   consistent with IMP standards (and more likely to do what their
   names/comments suggest). See IMP::algebra::Sphere3D,
   IMP::algebra::Cylinder3D, IMP::algebra::Segment3D,
   IMP::algebra::Plane3D etc.

- ParticleRefiner has been renamed to IMP::Refiner since the Particle
  was long and unnecessary.
