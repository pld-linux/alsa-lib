Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Name:		alsa-lib
Version:	0.3.0pre3
Release:	1d
Copyright:	GPL
Vendor:		Jaroslav Kysela <perex@jcu.cz>
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://alsa.jcu.cz/pub/lib/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-buildroot
URL:		http://alsa.jcu.cz
Requires:	alsa-driver
Prereq:		/sbin/ldconfig

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features
========
* general
  - modularized architecture with support for 2.0 and latest 2.1 kernels
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
  - zmodularyzowana architektura ze wsparciem dla kerneli 2.0 jak i 2.1
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

%package	static
Summary:	Advanced Linux Sound Architecture (ALSA) - Static library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description static
Advanced Linux Sound Architecture (ALSA) - Static library

%description -l pl static
Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna

%prep
%setup -q 

%build
autoconf 
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{include/sys,lib}

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

bzip2 -9 ChangeLog doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog.bz2 doc/*.txt.bz2

%attr(755,root,root) /usr/lib/lib*.so
%attr(755,root,root) /usr/lib/lib*.so.*
%attr(644,root,root) /usr/include/sys/*.h

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jan 21 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.3.0pre3-1d]
- new upstream release

* Sat Jan 02 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.3.0pre2-1d]
- new upstream release

* Thu Nov 12 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new upstream release (0.1.3)

* Fri Nov 06 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new upstream release

* Mon Sep 28 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- changed "-" to "_" (rpm doesn't like "-" in Name or Version)

* Sun Sep 27 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added Polish translations
- rewrited spec file

* Mon May 28 1998 Helge Jensen <slog@slog.dk>
- Made SPEC file
