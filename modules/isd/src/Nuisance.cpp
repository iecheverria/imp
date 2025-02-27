/**
 *  \file Nuisance.cpp
 *  \brief defines a one-dimensional nuisance parameter (sigma, gamma, ...)
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 *
 */

#include <IMP/isd/Nuisance.h>

IMPISD_BEGIN_NAMESPACE

void Nuisance::do_setup_particle(Model *m, ParticleIndex pi,
                                 double nuisance) {
  if (!Nuisance::get_is_setup(m, pi)) {
    m->add_attribute(get_nuisance_key(), pi, nuisance);
  } else {
    Nuisance(m, pi).set_nuisance(nuisance);
  }
}

FloatKey Nuisance::get_nuisance_key() {
  static FloatKey k("nuisance");
  return k;
}
void Nuisance::set_nuisance(Float d) {
  Float d_ = d;
  Particle *p = get_particle();
  if (get_has_lower()) {
    Float lo = get_lower();
    if (d < lo) d_ = lo;
  }
  if (get_has_upper()) {
    Float up = get_upper();
    if (d > up) d_ = up;
  }
  p->set_value(get_nuisance_key(), d_);
}

bool Nuisance::get_has_lower() const {
  Pointer<Particle> p = get_particle();
  return p->has_attribute(get_lower_key()) ||
         p->has_attribute(get_lower_particle_key());
}
Float Nuisance::get_lower() const {
  Particle *p = get_particle();
  FloatKey lk(get_lower_key());
  ParticleKey lp(get_lower_particle_key());
  bool hasfloat = p->has_attribute(lk);
  bool hasparticle = p->has_attribute(lp);
  if (hasfloat) {
    double floatval = p->get_value(lk);
    if (hasparticle) {
      Particle *d = p->get_value(lp);
      double particleval = d->get_value(get_nuisance_key());
      if (floatval > particleval) {
        return floatval;
      } else {
        return particleval;
      }
    } else {
      return floatval;
    }
  } else if (hasparticle) {
    Particle *d = p->get_value(lp);
    return d->get_value(get_nuisance_key());
  } else {
    return -std::numeric_limits<double>::infinity();
  }
}
FloatKey Nuisance::get_lower_key() {
  static FloatKey k("lower");
  return k;
}
ParticleIndexKey Nuisance::get_lower_particle_key() {
  static ParticleIndexKey k("lower");
  return k;
}
void Nuisance::set_lower(Float d) {
  Pointer<Particle> p = get_particle();
  FloatKey k(get_lower_key());
  if (!p->has_attribute(k)) p->add_attribute(k, d);
  p->set_value(k, d);
  enforce_bounds();
}
void Nuisance::set_lower(Particle *d) {
  Pointer<Particle> p = get_particle();
  ParticleKey k(get_lower_particle_key());
  if (!p->has_attribute(k)) p->add_attribute(k, d);
  p->set_value(k, d);
  enforce_bounds();
}
void Nuisance::remove_lower() {
  Pointer<Particle> p = get_particle();
  FloatKey k(get_lower_key());
  if (p->has_attribute(k)) p->remove_attribute(k);
  FloatKey kp(get_lower_key());
  if (p->has_attribute(kp)) p->remove_attribute(kp);
  remove_bounds();
}

bool Nuisance::get_has_upper() const {
  Pointer<Particle> p = get_particle();
  return p->has_attribute(get_upper_key()) ||
         p->has_attribute(get_upper_particle_key());
}
Float Nuisance::get_upper() const {
  Particle *p = get_particle();
  FloatKey ku(get_upper_key());
  ParticleKey kp(get_upper_particle_key());
  bool hasfloat = p->has_attribute(ku);
  bool hasparticle = p->has_attribute(kp);
  if (hasfloat) {
    double floatval = p->get_value(ku);
    if (hasparticle) {
      Particle *d = p->get_value(kp);
      double particleval = d->get_value(get_nuisance_key());
      if (floatval < particleval) {
        return floatval;
      } else {
        return particleval;
      }
    } else {
      return floatval;
    }
  } else if (hasparticle) {
    Particle *d = p->get_value(kp);
    return d->get_value(get_nuisance_key());
  } else {
    return std::numeric_limits<double>::infinity();
  }
}
FloatKey Nuisance::get_upper_key() {
  static FloatKey k("upper");
  return k;
}
ParticleIndexKey Nuisance::get_upper_particle_key() {
  static ParticleIndexKey k("upper");
  return k;
}
void Nuisance::set_upper(Float d) {
  Pointer<Particle> p = get_particle();
  FloatKey k(get_upper_key());
  if (!p->has_attribute(k)) p->add_attribute(k, d);
  p->set_value(k, d);
  enforce_bounds();
}
void Nuisance::set_upper(Particle *d) {
  Pointer<Particle> p = get_particle();
  ParticleKey k(get_upper_particle_key());
  if (!p->has_attribute(k)) p->add_attribute(k, d);
  p->set_value(k, d);
  enforce_bounds();
}
void Nuisance::remove_upper() {
  Pointer<Particle> p = get_particle();
  FloatKey k(get_upper_key());
  if (p->has_attribute(k)) p->remove_attribute(k);
  ParticleKey kp(get_upper_particle_key());
  if (p->has_attribute(kp)) p->remove_attribute(kp);
  remove_bounds();
}

void Nuisance::show(std::ostream &out) const {
  if (get_has_lower()) out << get_lower() << " < ";
  out << " Nuisance = " << get_nuisance();
  if (get_has_upper()) out << " < " << get_upper();
}

ObjectKey Nuisance::get_ss_key() {
  static ObjectKey k("nuisance_ss");
  return k;
}
void Nuisance::enforce_bounds() {
  Pointer<Particle> p = get_particle();
  ObjectKey k(get_ss_key());
  if (p->has_attribute(k)) return;
  Pointer<NuisanceScoreState> ss(new NuisanceScoreState(p));
  ss->set_was_used(true);
  p->add_attribute(k, ss);
}
void Nuisance::remove_bounds() {
  Pointer<Particle> p = get_particle();
  ObjectKey k(get_ss_key());
  if (!p->has_attribute(k)) return;
  Pointer<NuisanceScoreState> ss(
      dynamic_cast<NuisanceScoreState *>(p->get_value(k)));
  p->remove_attribute(k);
}

void NuisanceScoreState::do_before_evaluate() {
  IMP_LOG_TERSE("NSS: do_before_evaluate()" << std::endl);
  Nuisance nuis(p_);
  nuis.set_nuisance(nuis.get_nuisance());
}
void NuisanceScoreState::do_after_evaluate(DerivativeAccumulator *) {}
ModelObjectsTemp NuisanceScoreState::do_get_inputs() const {
  ModelObjectsTemp pt;
  pt.push_back(p_);
  ParticleIndexKey pu(Nuisance(p_).get_upper_particle_key());
  if (p_->has_attribute(pu)) pt.push_back(p_->get_value(pu));
  ParticleIndexKey pd(Nuisance(p_).get_lower_particle_key());
  if (p_->has_attribute(pd)) pt.push_back(p_->get_value(pd));
  return pt;
}
ModelObjectsTemp NuisanceScoreState::do_get_outputs() const {
  return ModelObjectsTemp(1, p_);
}

IMPISD_END_NAMESPACE
