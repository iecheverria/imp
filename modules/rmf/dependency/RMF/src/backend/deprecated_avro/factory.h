
#ifndef SRC_BACKEND_AVRO_FACTORY__H_
#define SRC_BACKEND_AVRO_FACTORY__H_

#include "RMF/config.h"
#include "backend/IOFactory.h"

RMF_ENABLE_WARNINGS

namespace RMF {
namespace avro_backend {
RMFEXPORT std::vector<boost::shared_ptr<backends::IOFactory> > get_factories();
}
}

RMF_DISABLE_WARNINGS
#endif
