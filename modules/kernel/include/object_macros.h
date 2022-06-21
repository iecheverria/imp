/**
 *  \file IMP/object_macros.h
 *  \brief Helper macros for implementing \imp Objects.
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 *
 */

#ifndef IMPKERNEL_OBJECT_MACROS_H
#define IMPKERNEL_OBJECT_MACROS_H
#include <IMP/kernel_config.h>
#include "doxygen_macros.h"
#include "ref_counted_macros.h"
#include "Vector.h"
#include "Pointer.h"
#include "WeakPointer.h"
#include "SetLogState.h"

//! Define the basic things needed by any Object
/** This defines
    - IMP::Object::get_version_info()
    - IMP::Object::get_type_name()
    - a protected destructor
*/
#define IMP_OBJECT_METHODS(Name)                                              \
 public:                                                                      \
  virtual std::string get_type_name() const override { return #Name; }        \
  virtual ::IMP::VersionInfo get_version_info() const override {        \
    return ::IMP::VersionInfo(get_module_name(), get_module_version()); \
  }                                                                           \
                                                                              \
 protected:                                                                   \
  virtual ~Name() { IMP::Object::_on_destruction(); }                   \
                                                                              \
 public:

//! Define the types for storing lists of object pointers
/** The macro defines the types PluralName and PluralNameTemp,
    which are vectors of either reference-counting or non reference-counting
    pointers to Name objects, respectively.
    PluralName should be Names unless the English spelling is
    different.
 */
#define IMP_OBJECTS(Name, PluralName)                              \
  /** A vector of reference-counting object pointers.*/                                    \
  typedef IMP::Vector<IMP::Pointer<Name> > PluralName; \
  /** A vector of weak (non reference-counting) pointers to specified objects. \see Name */                          \
  typedef IMP::Vector<IMP::WeakPointer<Name> > PluralName##Temp;

//! Typedefs a default instantiation for a generic (templated) object 
/**
 Define type [Name] to be an an instantiation of of Generic[Name] with
 template targument, and a function create_[lcname]() that generates a
 newly allocated object of type [Name], taking parameters [crguments]
 and internally paassing [cparguments] to the constructor.

 @note doxygen documentatio prior to this macro will be applied to the type
 definition
 */
#define IMP_GENERIC_OBJECT(Name, lcname, targument, carguments, cparguments) \
  typedef Generic##Name<targument> Name;                                     \
  template <class targument>                                                 \
  Generic##Name<targument> *create_##lcname carguments {                     \
    return new Generic##Name<targument> cparguments;                         \
  }

//! Declare a ref counted pointer to a new object
/** \param[in] Typename The namespace qualified type being declared
    \param[in] varname The name for the ref counted pointer
    \param[in] args The arguments to the constructor, or ()
    if there are none.
    Please read the documentation for IMP::Pointer before using.
*/
#define IMP_NEW(Typename, varname, args) \
  IMP::Pointer<Typename> varname(new Typename args)

#endif /* IMPKERNEL_OBJECT_MACROS_H */
