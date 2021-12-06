Name:           adwaita-icon-theme
Version:        41.0
Release:	1
Summary:        Adwaita icon theme
License:        LGPLv3+ or CC-BY-SA-3.0
URL:            http://www.linuxfromscratch.org/blfs/view/svn/x/adwaita-icon-theme.html
Source0:	https://download.gnome.org/sources/adwaita-icon-theme/41/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gtk3-devel intltool librsvg2

Requires:       adwaita-cursor-theme = %{version}-%{release}

%description
Adwaita icon theme that GNOME desktop used is contained in %{name},Contain a modern set
of cursors which is user for the GNOME desktop are contained by adwaita-cursor-theme.

%package -n     adwaita-cursor-theme
Summary:        Adwaita cursor theme
 
%description -n adwaita-cursor-theme
The adwaita-cursor-theme package contains a modern set of cursors originally
designed for the GNOME desktop.

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
%exclude %{_datadir}/icons/Adwaita/cursors/
%{_datadir}/icons/Adwaita/*/
%{_datadir}/icons/Adwaita/index.theme
%ghost %{_datadir}/icons/Adwaita/icon-theme.cache
	
%files -n adwaita-cursor-theme
%defattr(-,root,root)
%license COPYING*
%dir %{_datadir}/icons/Adwaita/
%{_datadir}/icons/Adwaita/cursors/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/adwaita-icon-theme.pc

%changelog
* Sat Dec 27 2021 wangkerong <wangkerong@huawei.com> - 41.0-1
- update to 41.0
- splite adwaita-cursor-theme subpackage

* Thu Jan 28 2021 yanglu <yanglu60@huawei.com> - 3.38.0-1
- Version update

* Wed Dec 16 2020 hanhui <hanhui15@huawei.com> - 3.37.2-2
- modify url

* Mon Jul 20 2020 wangye <wangye70@huawei.com> - 3.37.2-1
- Version update

* Mon Sep 02 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.32.0-1
- Package init
