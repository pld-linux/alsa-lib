#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_without	python		# smixer-python binding
%bcond_with	resmgr		# Resource Manager support
#
Summary:	Advanced Linux Sound Architecture (ALSA) - Library
Summary(es.UTF-8):	Advanced Linux Sound Architecture (ALSA) - Biblioteca
Summary(pl.UTF-8):	Advanced Linux Sound Architecture (ALSA) - Biblioteka
Summary(pt_BR.UTF-8):	Biblioteca para o ALSA (Advanced Linux Sound Architecture)
Summary(ru.UTF-8):	Библиотека API для работы с драйвером ALSA
Summary(uk.UTF-8):	Бібліотека API для роботи з драйвером ALSA
Name:		alsa-lib
Version:	1.0.23
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.alsa-project.org/pub/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	f48b50421d8a69d2d806d9c47e534f0d
Source1:	%{name}-modprobe.conf
Source2:	%{name}-asound.conf
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-driver-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
%if %{with python}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules
%endif
%{?with_resmgr:BuildRequires:	resmgr-devel}
BuildConflicts:	alsa-lib <= 0.4.0
Obsoletes:	alsa-libs
Conflicts:	alsa-utils < 1.0.20-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced Linux Sound Architecture (ALSA) - Library

Features:
- general
	- modularized architecture
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

%description -l pl.UTF-8
Advanced Linux Sound Architecture (ALSA) - Biblioteka

Możliwości:
- generalne
	- zmodularyzowana architektura
	- pełne wsparcie dla systemu plików proc - /proc/sound
- karty dźwiękowe ISA
	- obsługa bufora 128k ISA DMA
- mikser
	- nowe rozszerzone API dla aplikacji
	- obsługa nielimitowanej liczby kanałów
	- głośność może być ustawiana na trzy różne sposoby (procentowo
	  (0-100), liniowo oraz w skali decybelowej)
	- obsługa wyciszania (oraz sprzętowego wyciszania)
	- obsługa zdarzeń miksera
		- to pozwala dwum lub większej liczbie aplikacji się synchronizować
- cyfrowe audio (PCM)
	- nowe rozszerzone API dla aplikacji
	- pełna, prawdziwa obsługa trybu duplex
	- pełna obsługa trybu duplex dla kart SoundBlaster 16/AWE
	- dane cyfrowego dźwięku dla odtwarzania i nagrywania powinny być
	  odczytywane poprzez system plików /proc
- kompatybilność z OSS/Lite
	- pełna kompatybilność miksera
	- pełna kompatybilność PCM (/dev/dsp)

%description -l pt_BR.UTF-8
Bibliotecas para o ALSA. Esse pacote é necessário para rodar programas
Linux queusam o driver de som ALSA.

%description -l ru.UTF-8
Библиотека API для работы с драйвером ALSA.

%description -l uk.UTF-8
Бібліотека API для роботи з драйвером ALSA.

%package devel
Summary:	Advanced Linux Sound Architecture (ALSA) - header files
Summary(es.UTF-8):	Archivos de desarrollo de ALSA
Summary(pl.UTF-8):	Advanced Linux Sound Architecture (ALSA) - pliki nagłówkowe
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento do ALSA (Advanced Linux Sound Architecture)
Summary(ru.UTF-8):	Библиотека API для работы с драйвером ALSA - файлы программиста
Summary(uk.UTF-8):	Бібліотека API для роботи з драйвером ALSA - файли програміста
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	alsa-driver-devel
Obsoletes:	alsa-devel
Obsoletes:	alsa-lib-devel-doc

%description devel
Advanced Linux Sound Architecture (ALSA) - header files.

%description devel -l es.UTF-8
Este paquete contiene los archivos necesarios para compilar programas
que usan la biblioteca del sistema ALSA. No es necesario instalarlo si
lo que se desea es solamente ejecutar programas.

%description devel -l pl.UTF-8
Advanced Linux Sound Architecture (ALSA) - pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Esse pacote contém os arquivos necessários para compilar programas que
usam a biblioteca do ALSA. Não é necessário instalar esse pacote para
apenas rodar programas.

%description devel -l ru.UTF-8
Библиотеки разработчика и хедера для библиотеки API для работы с
драйвером ALSA.

%description devel -l uk.UTF-8
Бібліотеки програміста та хедери для бібліотеки API для роботи з
драйвером ALSA.

%package static
Summary:	Advanced Linux Sound Architecture (ALSA) - static library
Summary(pl.UTF-8):	Advanced Linux Sound Architecture (ALSA) - biblioteka statyczna
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a alsa-lib
Summary(ru.UTF-8):	Статическая библиотека API для работы с драйвером ALSA
Summary(uk.UTF-8):	Статична бібліотека API для роботи з драйвером ALSA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Advanced Linux Sound Architecture (ALSA) - static library.

%description static -l pl.UTF-8
Advanced Linux Sound Architecture (ALSA) - biblioteka statyczna.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com a alsa-lib

%description static -l ru.UTF-8
Статическая библиотека API для работы с драйвером ALSA.

%description static -l uk.UTF-8
Статична бібліотека API для роботи з драйвером ALSA.

%package smixer-python
Summary:	Python binding module for ALSA Mixer Interface
Summary(pl.UTF-8):	Moduł wiązania Pythona dla interfejsu miksera architektury ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description smixer-python
Python binding module for ALSA Mixer Interface.

%description smixer-python -l pl.UTF-8
Moduł wiązania Pythona dla interfejsu miksera architektury ALSA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{!?with_python:--disable-python} \
	%{?with_resmgr:--enable-resmgr} \
	%{!?with_static_libs:--disable-static}

%{__make}
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{alsa,modprobe.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D utils/alsa.m4 $RPM_BUILD_ROOT%{_aclocaldir}/alsa.m4
install %{SOURCE1} $RPM_BUILD_ROOT/etc/modprobe.d/alsa-base.conf
install %{SOURCE2} $RPM_BUILD_ROOT/etc/asound.conf

rm -f $RPM_BUILD_ROOT%{_libdir}/alsa-lib/smixer/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/asoundrc.txt
%attr(755,root,root) %{_bindir}/aserver
%attr(755,root,root) %{_libdir}/libasound.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libasound.so.2
%dir %{_libdir}/alsa-lib
%dir %{_libdir}/alsa-lib/smixer
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-ac97.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-hda.so
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-sbase.so
%{_datadir}/alsa
%dir %{_sysconfdir}/alsa
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asound.conf
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/alsa-base.conf

%files devel
%defattr(644,root,root,755)
%doc doc/doxygen/html/*
%attr(755,root,root) %{_libdir}/libasound.so
%{_libdir}/libasound.la
%{_includedir}/sys/asoundlib.h
%{_includedir}/alsa
%{_aclocaldir}/alsa.m4
%{_pkgconfigdir}/alsa.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libasound.a
%endif

%if %{with python}
%files smixer-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/alsa-lib/smixer/smixer-python.so
%endif
