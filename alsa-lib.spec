Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Summary(ru):	Библиотека API для работы с драйвером ALSA
Summary(uk):	Б╕бл╕отека API для роботи з драйвером ALSA
Name:		alsa-lib
Version:	0.9.0rc1
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
#Source1:	http://www.alsa-project.org/~perex/alsa-lib/%{name}.tgz
Patch0:		%{name}-m4_fix.patch
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-driver-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	flex
BuildConflicts:	alsa-lib <= 0.4.0
Obsoletes:	alsa-libs
ExcludeArch:	sparc
ExcludeArch:	sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc
%define 	__prefix	/usr/share
%define		__cc		%{kgcc}

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features ========
- general
  - modularized architecture with support for 2.2
  - support for versioned and exported symbols
  - full proc filesystem support - /proc/sound
- ISA soundcards
  - support for 128k ISA DMA buffer
- mixer
  - new enhanced API for applications
  - support for unlimited number of channels
  - volume can be set in three ways (percentual (0-100), exact and
    decibel)
  - support for mute (and hardware mute if hardware supports it)
  - support for mixer events
    - this allows two or more applications to be synchronized
- digital audio (PCM)
  - new enhanced API for applications
  - full real duplex support
  - full duplex support for SoundBlaster 16/AWE soundcards
  - digital audio data for playback and record should be read back using
    proc filesystem
- OSS/Lite compatibility
  - full mixer compatibity
  - full PCM (/dev/dsp) compatibility

%description -l pl
Advanced Linux Sound Architecture (ALSA) - Biblioteka

Nowinki =======
- generalne
  - zmodularyzowana architektura ze wsparciem dla kerneli 2.2
  - peЁne wsparcie dla systemu plikСw proc - /proc/sound
- karty d╪wiЙkowe ISA
  - wsparcie dla buforu 128k ISA DMA
- mikser
  - nowe rozszerzone API dla aplikacji
  - wsparcie dla nielimitowanej liczby kanaЁСw
  - gЁo╤no╤Ф mo©e byФ ustawiana na trzy rС©ne sposoby (procentowo
    (0-100), liniowo oraz w skali decybelowej)
  - wsparcie dla mute (oraz dla sprzЙtowego mute)
  - wsparcie dla zdarzeЯ miksera
    - to pozwala dwum lub wiЙkszej liczbie aplikacji siЙ synchronizowac
- cyfrowe audio (PCM)
  - nowe rozszerzone API dla aplikacji
  - peЁne realne wsparcie dla trybu duplex
  - dane cyfrowego d╪wiЙku dla odtwarzania i nagrywania powinny byФ
    odczytywane poprzez system plikСw /proc
- kompatybilno╤Ф z OSS/Lite
  - peЁna kompatybilno╤Ф miksera
  - peЁna kompatybilno╤Ф PCM (/dev/dsp)

%description -l ru
Библиотека API для работы с драйвером ALSA.

%description -l uk
Б╕бл╕отека API для роботи з драйвером ALSA.

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - pliki nagЁСwkowe
Summary(ru):	Библиотека API для работы с драйвером ALSA - файлы программиста
Summary(uk):	Б╕бл╕отека API для роботи з драйвером ALSA - файли програм╕ста
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	alsa-driver-devel
Obsoletes:	alsa-lib-devel-doc
Obsoletes:	alsa-devel

%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%description devel -l pl
Advanced Linux Sound Architecture (ALSA) - pliki nagЁСwkowe.

%description devel -l ru
Библиотеки разработчика и хедера для библиотеки API для работы с
драйвером ALSA.

%description devel -l uk
Б╕бл╕отеки програм╕ста та хедери для б╕бл╕отеки API для роботи з
драйвером ALSA.

#%package static
#Summary:	Advanced Linux Sound Architecture (ALSA) - Static library
#Summary(pl):	Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna
#Summary(ru):	Статическая библиотека API для работы с драйвером ALSA
#Summary(uk):	Статична б╕бл╕отека API для роботи з драйвером ALSA
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}

#%description static
#Advanced Linux Sound Architecture (ALSA) - Static library.

#%description static -l pl
#Advanced Linux Sound Architecture (ALSA) - Biblioteka statyczna.

#%description static -l ru
#Статическая библиотека API для работы с драйвером ALSA.

#%description static -l uk
#Статична б╕бл╕отека API для роботи з драйвером ALSA.

%prep
%setup -q
%patch0

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure CC=%{__cc}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog

%post  -p /sbin/ldconfig
%preun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{__prefix}/alsa/*

%files devel
%defattr(644,root,root,755)
#%doc *.gz *.html *.gif
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_aclocaldir}/alsa.m4
%{_includedir}/sys/*.h
%{_includedir}/alsa/*.h

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
