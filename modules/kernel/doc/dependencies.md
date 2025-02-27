Dependencies {#dependencies}
============

# Overview #

The state of IMP::Particle objects, IMP::Container objects and others often depends on the current state of other particles in the IMP::Model. For example, the members of a rigid body have their global coordinates computed from the IMP::algebra::ReferenceFrame3D of the IMP::core::RigidBody as well as their internal coordinates (IMP::core::RigidMember::get_internal_coordinates()). And the contents of an IMP::container::ClosePairContainer are computed from the coordinates of the particles in the input IMP::SingletonContainer. These dependencies are implemented through IMP::ScoreState objects which are registered with the IMP::Model when they are created.

In order to properly evaluate an IMP::Restraint, all of its input IMP::Particle and IMP::Container objects must first be updated (e.g., the non-bonded list contents must be correct and the coordinates of rigid body members must be correct). This requires processing the set of all dependencies among particles, containers, restraints and determining which need to be updated and in what order (so that IMP::ScoreState objects are only asked to update things after their inputs are updated).

# Dependency graph # {#dependency_graph}
This graph of inter-dependencies is represented by the IMP::DependencyGraph, which captures all the relationships between the different IMP::ModelObject objects (IMP::Restraint, IMP::Particle, IMP::ScoreState etc.) in a particular IMP::Model. You can get the IMP::DependencyGraph for a given model by calling IMP::get_dependency_graph(). It is a directed graph with one node per IMP::ModelObject and an edge from one object to another if the source is an input of the latter or the latter is an output of the former. See the kernel/dependency_graph.py example.

Given the graph, one can simply walk up from an IMP::Restraint to determine the full set of input particles or input IMP::ScoreState objects. A topological sort of the input IMP::ScoreStates provides a safe ordering to call e.g. IMP::ScoreState::before_evaluate() (since it means that all of the IMP::ScoreState inputs are up to date).

When an IMP::ScoringFunction is evaluated, it needs to determine all the IMP::ScoreState objects needed by its IMP::Restraints and an appropriate order to evaluate them in. It can then, in order, call IMP::ScoreState::before_evaluate(), evaluate the restraints, and then call IMP::ScoreState::after_evaluate().

# Caching dependencies # {#dependency_caching}

Since generating and traversing the dependency graph is reasonably expensive, the relationships encoded in it are cached in the IMP::Model. Specifically, when dependencies are needed, the graph is generated and, for each restraint, the ordered list of required (upstream) IMP::ScoreState objects is computed. This is stored in the IMP::Restraint. Subsequent evaluations of the restraint can simply used the cached data. These caches are cleared whenever
- a new IMP::Restraint or IMP::ScoreState is created
- an IMP::ScoreState is destroyed
- the contents of a container like IMP::container::ListSingletonContainer is changed
