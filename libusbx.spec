%bcond_with	doc

Summary:	Application access to USB devices
Name:		libusbx
Version:	1.0.14
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libusbx/%{name}-%{version}.tar.bz2
# Source0-md5:	0a6a75edb4b4eae7dc82c1dd71ddc470
URL:		http://libusbx.org
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with doc}
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	doxygen
BuildRequires:	openjade
%endif
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%package devel
Summary:	Header files for libusb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and other resources you can use to
incorporate libusb into applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%if %{with doc}
%{__make} -C doc docs
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libusb-*.so.?
%attr(755,root,root) %{_libdir}/libusb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc doc/html/*}
%attr(755,root,root) %{_libdir}/libusb-*.so
%{_libdir}/libusb-*.la
%{_includedir}/libusb-*
%{_pkgconfigdir}/libusb-*.pc

