Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Name:		alsa-lib
Version:	0.5.7
Release:	1
License:	GPL
Group:		System/Libraries
Group(pl):	System/Biblioteki
Source0:	ftp://ftp.alsa-project.org/pub/lib/alsa-lib-%{version}.tar.bz2
URL:		http://www.alsa-project.org/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildConflicts:	alsa-lib <= 0.4.0
Obsoletes:	alsa-libs
ExcludeArch:	sparc
ExcludeArch:	sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features
========
* general
  - modularized architecture with support for 2.2
  - support for versioned and exported symbols
  - full proc filesystem support - /proc/sound
* ISA soundcards
  - support for 128k ISA DMA buffer
* mixer
  - new enhanced API for applications
  - support for unlimited number of channels
  - volume can be set in three ways (percentual (0-100), exact and decibel)
  - support for mute (and hardware mute if hardware supports it)
  - support for mixer events
    - this allows two or more applications to be synchronized
* digital audio (PCM)
  - new enhanced API for applications
  - full real duplex support
  - full duplex support for SoundBlaster 16/AWE soundcards
  - digital audio data for playback and record should be read back using
    proc filesystem
* OSS/Lite compatibility
  - full mixer compatibity
  - full PCM (/dev/dsp) compatibility

%description -l pl
Advanced Linux Sound Architecture (ALSA) - Biblioteka

Nowinki
=======
* generalne
  - zmodularyzowana architektura ze wsparciem dla kerneli 2.2
  - pe³ne wsparcie dla systemu plików proc - /proc/sound
* karty d¼wiêkowe ISA
  - wsparcie dla buforu 128k ISA DMA
* mikser
  - nowe rozszerzone API dla aplikacji
  - wsparcie dla nielimitowanej liczby kana³ów
  - g³o¶no¶æ mo¿e byæ ustawiana na trzy ró¿ne sposoby (procentowo (0-100),
    liniowo oraz w skali decybelowej)
  - wsparcie dla mute (oraz dla sprzêtowego mute)
  - wsparcie dla zdarzeñ miksera
    - to pozwala dwum lub wiêkszej liczbie aplikacji siê synchronizowac
* cyfrowe audio (PCM)
  - nowe rozszerzone API dla aplikacji
  - pe³ne realne wsparcie dla trybu duplex
  - dane cyfrowego d¼wiêku dla odtwarzania i nagrywania powinny byæ odczytywane
    poprzez system plików /proc
* kompatybilno¶æ z OSS/Lite
  - pe³na kompatybilno¶æ miksera
  - pe³na kompatybilno¶æ PCM (/dev/dsp)

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - pliki nag³ówkowe
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
 
%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%description -l pl devel
Advanced Linux Sound Architecture (ALSA) - pliki nag³ówkowe.

%package static
Summary:	Advanced Linux Sound Architecture (ALSA) - Static library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Advanced Linux Sound Architecture (ALSA) - Static library.

%description -l pl static
Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf ChangeLog

%post  -p /sbin/ldconfig
%preun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_datadir}/aclocal/alsa.m4
%{_includedir}/sys/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
