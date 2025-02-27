/**
 *  \file RMF/compiler_macros.h
 *  \brief Various compiler workarounds
 *
 *  Copyright 2007-2022 IMP Inventors. All rights reserved.
 */

#ifndef RMF_INTERNAL_COMPILER_MACROS_H
#define RMF_INTERNAL_COMPILER_MACROS_H

#define RMF_STRINGIFY(x) #x

// recommended by http://gcc.gnu.org/gcc/Function-Names.html
#if defined(_MSC_VER)
#define __func__ __FUNCTION__
#elif defined(__STDC_VERSION__) && __STDC_VERSION__ < 199901L
#if __GNUC__ >= 2
#define __func__ __FUNCTION__
#else
#define __func__ "<unknown>"
#endif
#endif

// Deprecated; just use 'override' keyword instead
#define RMF_OVERRIDE override

// Deprecated; just use 'final' keyword instead
#define RMF_FINAL final

#if defined(__GNUC__) && __cplusplus >= 201103L
#define RMF_HAS_NOEXCEPT 1
#elif defined(__clang__) && defined(__has_feature)
#define RMF_HAS_NOEXCEPT __has_feature(cxx_noexcept)
#else
#define RMF_HAS_NOEXCEPT 0
#endif

#if RMF_HAS_NOEXCEPT
#define RMF_NOEXCEPT noexcept
#define RMF_CANEXCEPT noexcept(false)
#define RMF_CXX11_DEFAULT_COPY_CONSTRUCTOR(Name) \
  Name(const Name &) = default;                  \
  Name &operator=(const Name &) = default
#else
// probably should be finer here
#define RMF_NOEXCEPT throw()
#define RMF_CANEXCEPT
#define RMF_CXX11_DEFAULT_COPY_CONSTRUCTOR(Name)
#endif

#if defined(__clang__) || defined(__GNUC__)
#define RMF_PRAGMA(x) _Pragma(RMF_STRINGIFY(x))
#elif defined(_MSC_VER)
#define RMF_PRAGMA(x) __pragma(x)
#else
#define RMF_PRAGMA(x)
#endif

// Compiler-specific pragma support
#if defined(__clang__)
#define RMF_CLANG_PRAGMA(x) RMF_PRAGMA(clang x)
#define RMF_GCC_PRAGMA(x)
#define RMF_VC_PRAGMA(x)

#elif defined(__GNUC__)
#define RMF_CLANG_PRAGMA(x)
#define RMF_GCC_PRAGMA(x) RMF_PRAGMA(GCC x)
#define RMF_VC_PRAGMA(x)

#elif defined(_MSC_VER)
#define RMF_CLANG_PRAGMA(x)
#define RMF_GCC_PRAGMA(x)
#define RMF_VC_PRAGMA(x) RMF_PRAGMA(x)

#else
#define RMF_CLANG_PRAGMA(x)
#define RMF_GCC_PRAGMA(x)
#define RMF_VC_PRAGMA(x)
#endif

// Support for pushing and popping of warning state
#if defined(__clang__)
#define RMF_PUSH_WARNINGS RMF_CLANG_PRAGMA(diagnostic push)
#define RMF_POP_WARNINGS RMF_CLANG_PRAGMA(diagnostic pop)

#elif defined(__GNUC__)
#if __GNUC__ > 4 || __GNUC_MINOR__ >= 6
#define RMF_PUSH_WARNINGS RMF_GCC_PRAGMA(diagnostic push)
#define RMF_POP_WARNINGS RMF_GCC_PRAGMA(diagnostic pop)

#else
#define RMF_PUSH_WARNINGS
#define RMF_POP_WARNINGS

#endif

#elif defined(_MSC_VER)
#define RMF_PUSH_WARNINGS RMF_VC_PRAGMA(warning(push))
#define RMF_POP_WARNINGS RMF_VC_PRAGMA(warning(pop))

#else
#define RMF_PUSH_WARNINGS
#define RMF_POP_WARNINGS

#endif

// Turning on and off compiler-specific warnings
#ifdef __clang__
#define RMF_COMPILER_WARNINGS                                   \
  RMF_CLANG_PRAGMA(diagnostic warning "-Wall")                  \
      RMF_CLANG_PRAGMA(diagnostic warning "-Wextra")            \
      RMF_CLANG_PRAGMA(diagnostic ignored "-Wconversion")       \
      RMF_CLANG_PRAGMA(diagnostic ignored "-Wc++11-extensions") \
      RMF_CLANG_PRAGMA(diagnostic ignored "-Wc++11-compat")     \
      RMF_CLANG_PRAGMA(diagnostic ignored "-Wunused-member-function")

#elif defined(__GNUC__)

/*ret+=["-Wno-deprecated",
  "-Wstrict-aliasing=2",
  -fno-operator-names",]*/
#if __GNUC__ > 4 || __GNUC_MINOR__ >= 6
#define RMF_GCC_CXX0X_COMPAT        \
  RMF_GCC_PRAGMA(diagnostic ignored \
                 "-Wc++0x-compat")
#ifdef RMF_SWIG_WRAPPER
#define RMF_GCC_PROTOTYPES
#else
#define RMF_GCC_PROTOTYPES \
  RMF_GCC_PRAGMA(diagnostic warning "-Wmissing-declarations")
#endif

#else
#define RMF_GCC_CXX0X_COMPAT
#define RMF_GCC_PROTOTYPES
#endif

// Warn about missing override on virtual methods if gcc is new enough
#if __GNUC__ > 5 || (__GNUC__ == 5 && __GNUC_MINOR__ >= 1)
#ifdef RMF_SWIG_WRAPPER
#define RMF_GCC_OVERRIDE
#else
#define RMF_GCC_OVERRIDE \
  RMF_GCC_PRAGMA(diagnostic warning "-Wsuggest-override")
#endif
#else
#define RMF_GCC_OVERRIDE
#endif

#define RMF_COMPILER_WARNINGS                                   \
  RMF_GCC_PRAGMA(diagnostic warning "-Wall")                    \
      RMF_GCC_PRAGMA(diagnostic warning "-Wextra")              \
      RMF_GCC_PRAGMA(diagnostic warning "-Winit-self")          \
      RMF_GCC_PRAGMA(diagnostic warning "-Wcast-align")         \
      RMF_GCC_PRAGMA(diagnostic warning "-Woverloaded-virtual") \
      RMF_GCC_PRAGMA(diagnostic ignored "-Wconversion")         \
      RMF_GCC_PRAGMA(diagnostic warning "-Wundef")              \
      RMF_GCC_PROTOTYPES RMF_GCC_CXX0X_COMPAT RMF_GCC_OVERRIDE

#elif defined(_MSC_VER)
#define RMF_COMPILER_WARNINGS                                           \
  RMF_VC_PRAGMA(warning(disable : 4275; disable : 4251; disable : 4244; disable : 4068; disable : 4297))

#else
#define RMF_COMPILER_WARNINGS

#endif

#define RMF_ENABLE_WARNINGS RMF_PUSH_WARNINGS RMF_COMPILER_WARNINGS

#define RMF_DISABLE_WARNINGS RMF_POP_WARNINGS

#endif /* RMF_INTERNAL_COMPILER_MACROS_H */
