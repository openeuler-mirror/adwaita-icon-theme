Name:           adwaita-icon-theme
Version:        3.37.2
Release:	1
Summary:        Adwaita icon theme
License:        LGPLv3+ or CC-BY-SA
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme
Source0:	https://download.gnome.org/sources/adwaita-icon-theme/3.37/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gtk3-devel intltool librsvg2

Provides:       adwaita-cursor-theme
Obsoletes:      adwaita-cursor-theme

%description
Adwaita icon theme that GNOME desktop used is contained in %{name},Contain a modern set
of cursors which is user for the GNOME desktop are contained by adwaita-cursor-theme.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Pkgconfig file that used for %{name}  developing applications is contained by
this package.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install

touch %{buildroot}%{_datadir}/icons/Adwaita/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/icons/Adwaita
gtk-update-icon-cache --force %{_datadir}/icons/Adwaita &>/dev/null || :

%files
%defattr(-,root,root)
%license COPYING*
%{_datadir}/icons/Adwaita/*/
%{_datadir}/icons/Adwaita/index.theme
%{_datadir}/icons/Adwaita/cursors/
%ghost %{_datadir}/icons/Adwaita/icon-theme.cache

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
* Mon Jul 20 2020 wangye <wangye70@huawei.com> - 3.37.2-1
- Version update

* Mon Sep 02 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.32.0-1
- Package init
