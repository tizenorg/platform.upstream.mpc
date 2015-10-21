%define keepstatic 1
Name:           mpc-static
Version:        1.0
Release:        0
License:        LGPL-3.0+
Summary:        MPC multiple-precision complex shared library
Url:            http://www.multiprecision.org/mpc/
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	mpc.manifest
BuildRequires:  gmp-static
BuildRequires:  mpfr-static

%description
MPC is a C library for the arithmetic of complex numbers with
arbitrarily high precision and correct rounding of the result. It is
built upon and follows the same principles as MPFR.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure \
    --disable-shared \
    --enable-static
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install

%files
%manifest mpc.manifest
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING.LESSER
%doc %{_infodir}/mpc.info.gz
%{_libdir}/libmpc.a
/usr/include/mpc.h

%changelog
