Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Name:		alsa-lib
Version:	0.3.0pre4
Release:	2
Copyright:	GPL
Group:		System/Libraries
Group(pl):	System/Biblioteki
Source:		ftp://alsa.jcu.cz/pub/lib/%{name}-%{version}.tar.gz
URL:		http://alsa.jcu.cz/
BuildPrereq:	alsa-driver-devel >= 0.3.0pre1
Requires:       alsa-driver
BuildRoot:	/tmp/%{name}-%{version}-root

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

%package devel
Summary:	Header files fo ALSA library
Summary(pl):	Pliki nag³owkowe do biblioteki ALSA
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files fo ALSA library.

%description -l pl devel
Pliki nag³owkowe do biblioteki ALSA.

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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/sys,%{_libdir}}

make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf ChangeLog doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.gz

%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/sys/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Tue May 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.3.0pre4-2]
- package is FHS 2.0 compliant,
- based on spec file made by Helge Jensen <slog@slog.dk>,
- rewritten for PLD use by Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  and Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>,
- pl translation by Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>.
