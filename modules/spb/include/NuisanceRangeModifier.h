/**
 *  \file IMP/spb/NuisanceRangeModifier.h
 *  \brief Ensure that a Nuisance stays within its set range.
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 */

#ifndef IMPSPB_NUISANCE_RANGE_MODIFIER_H
#define IMPSPB_NUISANCE_RANGE_MODIFIER_H

#include <IMP/SingletonModifier.h>
#include <IMP/isd/Nuisance.h>
#include <IMP/singleton_macros.h>
#include <IMP/spb/spb_config.h>

IMPSPB_BEGIN_NAMESPACE

//! Ensure that a Nuisance stays within its set range.
class IMPSPBEXPORT NuisanceRangeModifier : public SingletonModifier {
 public:
  NuisanceRangeModifier(){};

  // note, Doxygen wants a semicolon at the end of macro lines
  virtual void apply_index(IMP::Model *m,
                           IMP::ParticleIndex p) const override;
  virtual IMP::ModelObjectsTemp do_get_inputs(
      IMP::Model *m, const IMP::ParticleIndexes &pis) const override;
  virtual IMP::ModelObjectsTemp do_get_outputs(
      IMP::Model *m, const IMP::ParticleIndexes &pis) const override;

  IMP_SINGLETON_MODIFIER_METHODS(NuisanceRangeModifier);
  IMP_OBJECT_METHODS(NuisanceRangeModifier);

  IMP_SHOWABLE(NuisanceRangeModifier);
};

IMPSPB_END_NAMESPACE

#endif /* IMPSPB_NUISANCE_RANGE_MODIFIER_H */
