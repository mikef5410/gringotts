# DarContact: Germano Rizzo <mano@pluto.linux.it>

Summary: libGringotts, a strongbox library
Name: libgringotts
Version: 1.2.1
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://devel.pluto.linux.it/projects/Gringotts/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Germano Rizzo <mano@pluto.linux.it>

Source: http://devel.pluto.linux.it/projects/libGringotts/current/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildPrereq: libmcrypt-devel, mhash-devel, zlib-devel, bzip2-devel, textutils

%description
libGringotts is a thread-safe C library that allows the programmer
to save data in a particular file format. The data are compressed
and encrypted with a strong encryption algorithm, and saved to the
disk in a secure way. The library gives control over every algorithm
involved in the process, and provides additional security-related
utility functions.
It is very easy to use, and designed to be very light for the system.

%package devel
Summary: Headers and static libraries for gringotts-lib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
These are the files needed to develop applications with libGringotts

%prep
%setup

%build
%configure
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall pcdir="%{buildroot}%{_libdir}/pkgconfig/"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/manual.htm
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%changelog
* Fri Apr 18 2003 Germano Rizzo <mano@pluto.linux.it>
- slightly modified to be included into package

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 1.2.0-0
- Updated to release 1.2.0.

* Wed Apr 02 2003 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Fixed libgringotts.pc.

* Tue Jan 07 2003 Dag Wieers <dag@wieers.com> - 1.1.1-0
- Initial package. (using dar)
