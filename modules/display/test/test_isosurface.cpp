#include "IMP/display/display_config.h"
#include "IMP/display/PymolWriter.h"
#include "IMP/display/geometry.h"
#include "IMP/algebra/standard_grids.h"
#include <IMP/flags.h>

int main(int argc, char *argv[]) {
  IMP::setup_from_argv(argc, argv, "Test isosurface");
#if IMP_DISPLAY_HAS_IMP_CGAL
  typedef IMP::algebra::DenseGrid3D<double> G;
  G g(2.5, IMP::algebra::BoundingBox3D(IMP::algebra::Vector3D(-10, -10, -10),
                                       IMP::algebra::Vector3D(10, 10, 10)));
  for(G::Index i : g.get_all_indexes()) {
    double m = g.get_center(i).get_magnitude();
    g[i] = 100 - m;
  }
  IMP_NEW(IMP::display::IsosurfaceGeometry, gg, (g, 95.0));
  std::string name = IMP::create_temporary_file_name("iso", ".pym");
  std::cout << "Writing " << name << std::endl;
  IMP_NEW(IMP::display::PymolWriter, w, (name));
  w->add_geometry(gg);
  return 0;
#else
  std::cerr << "No IMP.cgal" << std::endl;
  return 0;
#endif
}
