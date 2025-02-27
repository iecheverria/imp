/**
 *  \file IMP/core/RestraintsScoringFunction.h
 *  \brief A scoring function on a list of restraints
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 *
 */

#ifndef IMPCORE_RESTRAINTS_SCORING_FUNCTION_H
#define IMPCORE_RESTRAINTS_SCORING_FUNCTION_H

#include <IMP/core/core_config.h>
#include <IMP/ScoringFunction.h>
#include <IMP/Restraint.h>
#include <IMP/internal/RestraintsScoringFunction.h>

IMPCORE_BEGIN_NAMESPACE

//! Create a scoring function on a list of restraints.
class RestraintsScoringFunction :
#if defined(IMP_DOXYGEN) || defined(SWIG)
    public ScoringFunction
#else
    public IMP::internal::RestraintsScoringFunction
#endif
    {
 public:
  RestraintsScoringFunction(const RestraintsAdaptor &rs,
                            double weight = 1.0, double max = NO_MAX,
                            std::string name = "RestraintsScoringFunction%1%")
      : IMP::internal::RestraintsScoringFunction(rs, weight, max, name) {}
  RestraintsScoringFunction(const RestraintsAdaptor &rs,
                            std::string name)
      : IMP::internal::RestraintsScoringFunction(rs, 1.0, NO_MAX, name) {}
#if defined(SWIG)
  void do_add_score_and_derivatives(
           ScoreAccumulator sa, const ScoreStatesTemp &ss) override;

  void do_add_score_and_derivatives_moved(
           ScoreAccumulator sa, const ParticleIndexes &moved_pis,
           const ParticleIndexes &reset_pis,
           const ScoreStatesTemp &ss) override;

  virtual Restraints create_restraints() const override;
  virtual ModelObjectsTemp do_get_inputs() const override;
  IMP_OBJECT_METHODS(RestraintsScoringFunction);
#endif
};

IMPCORE_END_NAMESPACE

#endif /* IMPCORE_RESTRAINTS_SCORING_FUNCTION_H */
