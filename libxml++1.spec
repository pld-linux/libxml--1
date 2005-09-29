
%define		_realname	libxml++
Summary:	C++ interface for working with XML files
Summary(pl):	Interfejs C++ do pracy z plikami XML
Name:		libxml++1
Version:	1.0.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{_realname}/1.0/%{_realname}-%{version}.tar.bz2
# Source0-md5:	10c178eb992be70d45450020bf0cc2aa
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.8
BuildRequires:	pkgconfig
Obsoletes:	libxml++ < 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%description -l pl
libxml++ jest interfejsem C++ do biblioteki libxml.

%package devel
Summary:	Header files for libxml++
Summary(pl):	Pliki nag³ówkowe do libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.5.8
Obsoletes:	libxml++-devel < 2.0.0

%description devel
Header files for libxml++.

%description devel -l pl
Pliki nag³ówkowe do libxml++.

%package static
Summary:	Static libxml++ libraries
Summary(pl):	Biblioteka statyczna libxml++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxml++-static < 2.0.0

%description static
Static libxml++ libraries.

%description static -l pl
Biblioteka statyczna libxml++.

%prep
%setup -q -n %{_realname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
