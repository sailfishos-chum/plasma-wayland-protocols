
%global wayland_min_version 1.4
%global debug_package %{nil}

Name:    plasma-wayland-protocols
Version: 1.13.0
Release: 1%{?dist}
Summary: Plasma Specific Protocols for Wayland

License: LGPLv2+ and MIT and BSD
URL:     https://invent.kde.org/libraries/%{name}
Source0: %{name}-%{version}.tar.bz2

## upstream patches (lookaside cache)

BuildRequires: opt-extra-cmake-modules
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-kf5-rpm-macros

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%files
%license COPYING.LIB
%{_opt_kf5_datadir}/plasma-wayland-protocols/

%files devel
%{_opt_kf5_libdir}/cmake/PlasmaWaylandProtocols/
