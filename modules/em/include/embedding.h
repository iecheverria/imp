/**
 *  \file IMP/em/embedding.h
 *  \brief Cluster sets of points.
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 *
 */

#ifndef IMPEM_EMBEDDING_H
#define IMPEM_EMBEDDING_H

#include <IMP/em/em_config.h>
#include "DensityMap.h"
#include <IMP/statistics/Embedding.h>

IMPEM_BEGIN_NAMESPACE

/** Generate a set of points from the voxels in a em::DensityMap
    which are above a certain threshold.
 */
class IMPEMEXPORT HighDensityEmbedding : public statistics::Embedding {
  algebra::Vector3Ds points_;

 public:
  HighDensityEmbedding(DensityMap *dm, double threshold);
  algebra::VectorKD get_point(unsigned int i) const override;
  unsigned int get_number_of_items() const override;
  IMP_OBJECT_METHODS(HighDensityEmbedding);
};

IMPEM_END_NAMESPACE

#endif /* IMPEM_EMBEDDING_H */
