Summary:	API for Run-time Code Generation
Summary(pl.UTF-8):	API do generowania kodu w czasie działania
Name:		dyninst
Version:	13.0.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/dyninst/dyninst/releases
Source0:	https://github.com/dyninst/dyninst/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e594b64007d63f641cda3eef97e94b50
Patch0:		%{name}-libname.patch
Patch1:		%{name}-x32.patch
Patch2:		%{name}-x86.patch
Patch3:		%{name}-install.patch
URL:		https://dyninst.org/dyninst
# libiberty
BuildRequires:	binutils-devel
BuildRequires:	boost-devel >= 1.71.0
BuildRequires:	cmake >= 3.14.0
BuildRequires:	elfutils-devel >= 0.186
BuildRequires:	flex
BuildRequires:	libgomp-devel
BuildRequires:	libstdc++-devel >= 6:6.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	tbb-devel >= 2021.4
Requires:	elfutils >= 0.186
Requires:	tbb >= 2021.4
Obsoletes:	dyninst-doc < 12.2
ExclusiveArch:	%{ix86} %{x8664} x32 aarch64 ppc ppc64 aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abiver			13.0
%define		skip_post_check_so	libparseAPI\.so.*

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
Requires:	boost-devel >= 1.71.0
Requires:	elfutils-devel >= 0.186
Requires:	libstdc++-devel >= 6:6.0
Requires:	tbb-devel >= 2021.4

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
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
export CXXFLAGS="%{rpmcxxflags} -DTBB_DEFINE_STD_HASH_SPECIALIZATIONS"
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR:PATH=include/dyninst \
	-DENABLE_DEBUGINFOD=ON

# -DLIGHTWEIGHT_SYMTAB enabled libsymLite and disables libdyninstAPI

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
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
%ghost %{_libdir}/libdynC_API.so.%{abiver}
%attr(755,root,root) %{_libdir}/libdynDwarf.so.*.*.*
%ghost %{_libdir}/libdynDwarf.so.%{abiver}
%attr(755,root,root) %{_libdir}/libdynElf.so.*.*.*
%ghost %{_libdir}/libdynElf.so.%{abiver}
%attr(755,root,root) %{_libdir}/libdyncommon.so.*.*.*
%ghost %{_libdir}/libdyncommon.so.%{abiver}
%attr(755,root,root) %{_libdir}/libdyninstAPI.so.*.*.*
%ghost %{_libdir}/libdyninstAPI.so.%{abiver}
%attr(755,root,root) %{_libdir}/libdyninstAPI_RT.so.*.*.*
%ghost %{_libdir}/libdyninstAPI_RT.so.%{abiver}
%attr(755,root,root) %{_libdir}/libinstructionAPI.so.*.*.*
%ghost %{_libdir}/libinstructionAPI.so.%{abiver}
%attr(755,root,root) %{_libdir}/libparseAPI.so.*.*.*
%ghost %{_libdir}/libparseAPI.so.%{abiver}
%attr(755,root,root) %{_libdir}/libpatchAPI.so.*.*.*
%ghost %{_libdir}/libpatchAPI.so.%{abiver}
%attr(755,root,root) %{_libdir}/libpcontrol.so.*.*.*
%ghost %{_libdir}/libpcontrol.so.%{abiver}
%attr(755,root,root) %{_libdir}/libstackwalk.so.*.*.*
%ghost %{_libdir}/libstackwalk.so.%{abiver}
%attr(755,root,root) %{_libdir}/libsymtabAPI.so.*.*.*
%ghost %{_libdir}/libsymtabAPI.so.%{abiver}

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdynC_API.so
%{_libdir}/libdynDwarf.so
%{_libdir}/libdynElf.so
%{_libdir}/libdyncommon.so
%{_libdir}/libdyninstAPI.so
%{_libdir}/libdyninstAPI_RT.so
%{_libdir}/libinstructionAPI.so
%{_libdir}/libparseAPI.so
%{_libdir}/libpatchAPI.so
%{_libdir}/libpcontrol.so
%{_libdir}/libstackwalk.so
%{_libdir}/libsymtabAPI.so
%{_includedir}/dyninst
%{_libdir}/cmake/Dyninst

%files static
%defattr(644,root,root,755)
%{_libdir}/libdyninstAPI_RT.a
