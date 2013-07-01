%define keepstatic 1
Name:           mpc
Version:        1.0
Release:        0
License:        LGPL-3.0+
Summary:        MPC multiple-precision complex shared library
Url:            http://www.multiprecision.org/mpc/
Group:          Development/Libraries/C and C++
Source:         mpc-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	mpc.manifest
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel

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
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install

%post -n libmpc -p /sbin/ldconfig

%postun -n libmpc -p /sbin/ldconfig


%files -n libmpc
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libmpc.so.3*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING.LESSER
%doc %{_infodir}/mpc.info.gz
%{_libdir}/libmpc.a
%{_libdir}/libmpc.so
/usr/include/mpc.h

%changelog
