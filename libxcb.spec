Summary:	X protocol C-language Binding library
Name:		libxcb
Version:	1.9.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	324c76024a73dba8a902638696ba87de
URL:		http://xcb.freedesktop.org/
BuildRequires:	check-devel
BuildRequires:	libpthread-stubs
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	xorg-libXau-devel
BuildRequires:	xorg-libXdmcp-devel
BuildRequires:	xorg-proto >= 7.7-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X protocol C-language Binding library.

libxcb provides an interface to the X Window System protocol, slated
to replace the current Xlib interface.

%package devel
Summary:	Header files for XCB library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libpthread-stubs
Requires:	xorg-proto

%description devel
Header files for XCB library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libxcb

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxcb-*.so.?
%attr(755,root,root) %ghost %{_libdir}/libxcb.so.?
%attr(755,root,root) %{_libdir}/libxcb-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libxcb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/tutorial
%attr(755,root,root) %{_libdir}/libxcb-*.so
%attr(755,root,root) %{_libdir}/libxcb.so
%{_libdir}/libxcb-*.la
%{_libdir}/libxcb.la
%{_includedir}/xcb
%{_pkgconfigdir}/xcb-*.pc
%{_pkgconfigdir}/xcb.pc

