%bcond_with	doc

Summary:	Application access to USB devices
Name:		libusb
Version:	1.0.19
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2
# Source0-md5:	f9e2bb5879968467e5ca756cb4e1fa7e
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
BuildRequires:	udev-devel
Provides:	libusbx = %{version}-%{release}
Obsoletes:	libusbx = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a library for application access to USB devices.

%package devel
Summary:	Header files for libusb library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libusbx-devel = %{version}-%{release}
Obsoletes:	libusbx-devel = %{version}-%{release}

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
	--disable-log		\
	--disable-silent-rules	\
	--disable-static
%{__make}

%if %{with doc}
%{__make} -C doc docs
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libusb-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog TODO
%attr(755,root,root) %ghost %{_libdir}/libusb-*.so.?
%attr(755,root,root) %{_libdir}/libusb-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{?with_doc:%doc doc/html/*}
%attr(755,root,root) %{_libdir}/libusb-*.so
%{_includedir}/libusb-*
%{_pkgconfigdir}/libusb-*.pc

