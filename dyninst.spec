Summary:	API for Run-time Code Generation
Summary(pl.UTF-8):	API do generowania kodu w czasie działania
Name:		dyninst
Version:	9.3.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# http://www.dyninst.org/downloads/dyninst-9.x
#Source0Download: https://github.com/dyninst/dyninst/releases
Source0:	https://github.com/dyninst/dyninst/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	995e1d0a718148e93251d12b982caffc
Patch0:		%{name}-libname.patch
Patch1:		%{name}-x32.patch
Patch2:		%{name}-types.patch
URL:		http://www.dyninst.org/dyninst
# libiberty
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.47
BuildRequires:	cmake >= 2.6.4
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	libdwarf-devel >= 0.20130126
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libxml2-devel >= 2
BuildRequires:	sed >= 4.0
BuildRequires:	texlive-format-pdflatex
Requires:	libdwarf >= 0.20130126
ExclusiveArch:	%{ix86} %{x8664} x32 aarch64 ppc ppc64 aarch64
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
Requires:	libstdc++-devel >= 6:4.7

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

%package doc
Summary:	Documentation for dyninst libraries
Summary(pl.UTF-8):	Dokumentacja do bibliotek dyninst
Group:		Documentation

%description doc
Documentation for dyninst libraries.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek dyninst.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake . \
	-DINSTALL_CMAKE_DIR:PATH=%{_libdir}/cmake/Dyninst \
	-DINSTALL_DOC_DIR:PATH=%{_docdir}/dyninst \
	-DINSTALL_INCLUDE_DIR:PATH=%{_includedir}/dyninst \
	-DINSTALL_LIB_DIR:PATH=%{_libdir} \

%{__make}

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
%doc COPYRIGHT CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/parseThat
%attr(755,root,root) %{_libdir}/libdynC_API.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynC_API.so.9.3
%attr(755,root,root) %{_libdir}/libdynDwarf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynDwarf.so.9.3
%attr(755,root,root) %{_libdir}/libdynElf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynElf.so.9.3
%attr(755,root,root) %{_libdir}/libdyncommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyncommon.so.9.3
%attr(755,root,root) %{_libdir}/libdyninstAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyninstAPI.so.9.3
%attr(755,root,root) %{_libdir}/libdyninstAPI_RT.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdyninstAPI_RT.so.9.3
%attr(755,root,root) %{_libdir}/libinstructionAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinstructionAPI.so.9.3
%attr(755,root,root) %{_libdir}/libparseAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libparseAPI.so.9.3
%attr(755,root,root) %{_libdir}/libpatchAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpatchAPI.so.9.3
%attr(755,root,root) %{_libdir}/libpcontrol.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpcontrol.so.9.3
%attr(755,root,root) %{_libdir}/libstackwalk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstackwalk.so.9.3
%attr(755,root,root) %{_libdir}/libsymLite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsymLite.so.9.3
%attr(755,root,root) %{_libdir}/libsymtabAPI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsymtabAPI.so.9.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynC_API.so
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
%{_libdir}/cmake/Dyninst

%files static
%defattr(644,root,root,755)
%{_libdir}/libdyninstAPI_RT.a

%files doc
%defattr(644,root,root,755)
%{_docdir}/dyninst
