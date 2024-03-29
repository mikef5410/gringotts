Summary: Gringotts, an electronic strongbox
Name: gringotts
Version: 1.2.10
Release: 1
License: GPL
Group: Applications/Productivity
URL: http://devel.pluto.linux.it/projects/Gringotts/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Germano Rizzo <mano78@users.sourceforge.net>

Source: http://devel.pluto.linux.it/projects/Gringotts/current/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildPrereq: gtk2-devel, popt, textutils, libgringotts-devel >= 1.2.0, pkgconfig

%description
Gringotts is a small but (hopely ;) useful utility that stores sensitive
data (passwords, credit card numbers, friends' addresses) in an organized,
optimized and most of all very secure form.
It uses libGringotts to provide a strong level of encryption, just aiming
to be as trustworthy as possible.

%prep
%setup

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%attr(4755, -, -) %{_bindir}/*
%{_datadir}/pixmaps/gringotts.xpm
%{_datadir}/gnome/apps/Utilities/gringotts.desktop
%{_datadir}/doc/*/*

%changelog
* Fri Apr 18 2003 Germano Rizzo <mano78@users.sourceforge.net>
- slightly modified to be included into package

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.2.5-0
- Updated to release 1.2.5.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.2.3-0
- Initial package. (using dar)
