# $Id: flash-plugin.spec 5067 2007-01-11 00:54:46Z dag $
# Authority: dag

# ExcludeDist: rh7 el2

### Disable stripping
%define __spec_install_post /usr/lib/rpm/brp-compress

%define real_name install_flash_player_9_linux

Summary: Macromedia Flash Player
Name: flash-plugin
Version: 9.0.289.0
Release: 1%{?dist}
License: Commercial
Group: Applications/Internet
URL: http://www.macromedia.com/downloads/

#Source: http://macromedia.rediris.es/rpmsource/flash-player-plugin-%{version}.tar.bz2
Source: http://download.macromedia.com/pub/flashplayer/installers/current/9/install_flash_player_9.tar.gz
#Source: http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_9_linux.tar.gz
#Source: http://fpdownload.macromedia.com/get/shockwave/flash/english/linux/7.0r25/install_flash_player_7_linux.tar.gz
Source1: http://macromedia.rediris.es/rpmsource/LICENSE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386
Obsoletes: mozilla-flash <= %{version}-%{release}
#Requires: %{_libdir}/mozilla/plugins/

%description
Macromedia Flash Player

By downloading and installing this package you agree to the included LICENSE:

    http://macromedia.rediris.es/rpmsource/LICENSE


%prep
%setup -c
%{__install} -Dp -m0644 %{SOURCE1} LICENSE

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
#%{__install} -Dp -m0755 flashplayer.xpt %{buildroot}%{_libdir}/mozilla/plugins/flashplayer.xpt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE
%{_libdir}/mozilla/plugins/

%changelog
* Tue Nov 09 2010 Dag Wieers <dag@wieers.com> - 9.0.289.0-1
- Updated to release 9.0.289.0.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 9.0.152.0-1
- Updated to release 9.0.152.0.

* Wed Nov 12 2008 Dag Wieers <dag@wieers.com> - 9.0.151.0-1
- Updated to release 9.0.151.0.

* Wed Apr 23 2008 Dag Wieers <dag@wieers.com> - 9.0.124.0-1
- Updated to release 9.0.124.0.

* Wed Dec 05 2007 Dag Wieers <dag@wieers.com> - 9.0.115.0-1
- Updated to release 9.0.115.0.

* Thu Jul 19 2007 Dag Wieers <dag@wieers.com> - 9.0.48.0-1
- Updated to release 9.0.48.0.

* Wed Jan 17 2007 Dag Wieers <dag@wieers.com> - 9.0.31.0-1
- Updated to release 9.0.31.0.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 7.0.69-1
- Updated to release 7.0.69.

* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 7.0.68-1
- Updated to release 7.0.68.
- Renamed package from mozilla-flash to flash-plugin.

* Wed Mar 15 2006 Dag Wieers <dag@wieers.com> - 7.0.63-1
- Updated to release 7.0.63.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 7.0.61-1
- Updated to release 7.0.61.

* Sun Jun 27 2004 Dag Wieers <dag@wieers.com> - 7.0.25-1
- Initial package. (using DAR)
