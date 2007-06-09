Summary:	Cairo graphics library wrapper for Guile Scheme
Summary(pl.UTF-8):	Wrapper biblioteki graficznej Cairo dla Guile Scheme
Name:		guile-cairo
Version:	1.3.91
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://download.gna.org/guile-cairo/%{name}-%{version}.tar.gz
# Source0-md5:	969fb008899bb81f6fb7441b6131d118
Patch0:		%{name}-headers.patch
URL:		http://home.gna.org/guile-cairo/
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	guile-devel >= 5:1.6.4
BuildRequires:	pkgconfig >= 1:0.9.0
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libguile-cairo.so.*.*.*
%{_datadir}/guile/site/cairo.scm
%{_datadir}/guile/site/cairo

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguile-cairo.so
%{_libdir}/libguile-cairo.la
%{_includedir}/guile-cairo
%{_pkgconfigdir}/guile-cairo.pc
