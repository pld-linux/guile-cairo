Summary:	Cairo graphics library wrapper for Guile Scheme
Summary(pl.UTF-8):	Wrapper biblioteki graficznej Cairo dla Guile Scheme
Name:		guile-cairo
Version:	1.4.1
Release:	7
License:	LGPL v3+
Group:		Libraries
Source0:	http://download.gna.org/guile-cairo/%{name}-%{version}.tar.gz
# Source0-md5:	70c6d977e7fdffb2c717eb9bff04eec1
Patch0:		%{name}-headers.patch
Patch1:		%{name}-info.patch
URL:		http://home.gna.org/guile-cairo/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	guile-devel >= 5:1.6.4
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	texinfo
Requires:	cairo >= 1.4.0
Requires:	guile >= 5:1.6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guile-Cairo wraps the Cairo graphics library for Guile Scheme.

%description -l pl.UTF-8
Guile-Cairo obudowuje bibliotekę graficzną Cairo dla Guile Scheme.

%package devel
Summary:	Header files for guile-cairo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki guile-cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 1.4.0
Requires:	guile-devel >= 5:1.6.4

%description devel
Header files for guile-cairo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki guile-cairo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	DEBUG_CFLAGS="-I%{_includedir}/cairo"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libguile-cairo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-cairo.so.0
%{_datadir}/guile/site/cairo.scm
%{_datadir}/guile/site/cairo

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguile-cairo.so
%{_libdir}/libguile-cairo.la
%{_includedir}/guile-cairo
%{_pkgconfigdir}/guile-cairo.pc
%{_infodir}/guile-cairo.info*
