Summary:	API for Run-time Code Generation
Summary(pl.UTF-8):	API do generowania kodu w czasie działania
Name:		dyninst
Version:	8.1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://www.dyninst.org/downloads/dyninst-8.x
Source0:	http://www.dyninst.org/sites/default/files/downloads/dyninst/%{version}/DyninstAPI-%{version}.tgz
# Source0-md5:	bf03b33375afa66fe0efa46ce3f4b17a
Patch0:		%{name}-libname.patch
Patch1:		%{name}-link.patch
URL:		http://www.dyninst.org/dyninst
BuildRequires:	autoconf >= 2.63
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.42
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	libdwarf-devel >= 0.20130126
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	nasm
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel >= 8.5
Requires:	libdwarf >= 0.20130126
ExclusiveArch:	%{ix86} %{x8664} ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dyninst is an Application Program Interface (API) to permit the
insertion of code into a running program. The API also permits
changing or removing subroutine calls from the application program.
Run-time code changes are useful to support a variety of applications
including debugging, performance monitoring, and to support composing
applications out of existing packages. The goal of this API is to
provide a machine independent interface to permit the creation of
tools and applications that use run-time code patching.

%description -l pl.UTF-8
Dyninst to API (interfejs programowy) pozwalający na wstawianie kodu
do działającego programu. API pozwala także na zmianę lub usuwanie
wywołań funkcji z programu aplikacji. Zmiany kodu w czasie działania
są przydatne w wielu zastosowaniach, w tym diagnostyce, monitorowaniu
wydajności oraz wsparciu składania aplikacji z istniejących pakietów.
Celem tego API jest zapewnienie niezależnego od maszyny interfejsu
pozwalającego na tworzenie narzędzi i aplikacji wykorzystujących
modyfikowanie kodu w czasie działania.

%package devel
Summary:	Header files for dyninst libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek dyninst
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for dyninst libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek dyninst.

%package static
Summary:	Static dyninst libraries
Summary(pl.UTF-8):	Statyczne biblioteki dyninst
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dyninst libraries.

%description static -l pl.UTF-8
Statyczne biblioteki dyninst.

%prep
%setup -q -n DyninstAPI-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's/tcl8\.4/tcl8.5/' configure.in

%build
%{__autoconf}
%configure \
	--includedir=%{_includedir}/dyninst

%{__make} \
	VERBOSE_COMPILATION=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README
%attr(755,root,root) %{_libdir}/libdynDwarf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynDwarf.so.8.1
%attr(755,root,root) %{_libdir}/libdynElf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynElf.so.8.1
%attr(755,root,root) %{_libdir}/libdyncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyncommon.so.8.1
%attr(755,root,root) %{_libdir}/libdyninstAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyninstAPI.so.8.1
%attr(755,root,root) %{_libdir}/libdyninstAPI_RT.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyninstAPI_RT.so.8.1
%attr(755,root,root) %{_libdir}/libinstructionAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinstructionAPI.so.8.1
%attr(755,root,root) %{_libdir}/libparseAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libparseAPI.so.8.1
%attr(755,root,root) %{_libdir}/libpatchAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpatchAPI.so.8.1
%attr(755,root,root) %{_libdir}/libpcontrol.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcontrol.so.8.1
%attr(755,root,root) %{_libdir}/libstackwalk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstackwalk.so.8.1
%attr(755,root,root) %{_libdir}/libsymLite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsymLite.so.8.1
%attr(755,root,root) %{_libdir}/libsymtabAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsymtabAPI.so.8.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynDwarf.so
%attr(755,root,root) %{_libdir}/libdynElf.so
%attr(755,root,root) %{_libdir}/libdyncommon.so
%attr(755,root,root) %{_libdir}/libdyninstAPI.so
%attr(755,root,root) %{_libdir}/libdyninstAPI_RT.so
%attr(755,root,root) %{_libdir}/libinstructionAPI.so
%attr(755,root,root) %{_libdir}/libparseAPI.so
%attr(755,root,root) %{_libdir}/libpatchAPI.so
%attr(755,root,root) %{_libdir}/libpcontrol.so
%attr(755,root,root) %{_libdir}/libstackwalk.so
%attr(755,root,root) %{_libdir}/libsymLite.so
%attr(755,root,root) %{_libdir}/libsymtabAPI.so
%{_includedir}/dyninst

%files static
%defattr(644,root,root,755)
%{_libdir}/libdyninstAPI_RT.a
