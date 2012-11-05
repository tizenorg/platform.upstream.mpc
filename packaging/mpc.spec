#
# spec file for package mpc
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mpc
Version:        1.0
Release:        0
License:        LGPL-3.0+
Summary:        MPC multiple-precision complex shared library
Url:            http://www.multiprecision.org/mpc/
Group:          Development/Libraries/C and C++
Source:         mpc-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package -n libmpc
Summary:        MPC multiple-precision complex shared library
Group:          Development/Libraries/C and C++

%description -n libmpc
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%package devel
Summary:        MPC multiple-precision complex library development files
Group:          Development/Libraries/C and C++
Requires:       libmpc = %{version}
Requires:       mpfr-devel

%description devel
MPC multiple-precision complex library development files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/libmpc.la

%post -n libmpc -p /sbin/ldconfig


%postun -n libmpc -p /sbin/ldconfig


%files -n libmpc
%defattr(-,root,root)
%{_libdir}/libmpc.so.3*

%files devel
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING.LESSER
%doc %{_infodir}/mpc.info.gz
%{_libdir}/libmpc.a
%{_libdir}/libmpc.so
/usr/include/mpc.h

%changelog
