%define major			0
%define libname 		%mklibname %{name}	%{major}
%define libname_devel		%mklibname %{name} 	-d
%define libnameui 		%mklibname qmmpui 	%{major}
%define libnameui_devel		%mklibname qmmpui 	-d
%define debug_package	%{nil}

######################
# Hardcode PLF build
%define build_plf 1
######################

%if %{build_plf}
%define distsuffix plf
%define extrarelsuffix plf
%endif

Summary:	Qt-based Multimedia Player
Name:		qmmp
Version:	0.6.6
Release:	1%{?extrarelsuffix}
URL:		http://qmmp.ylsoftware.com/index_en.php
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
License:	GPLv2+
Group:		Sound

BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(flac)
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(udisks)
BuildRequires:	wildmidi-devel
BuildRequires:	libgme-devel
BuildRequires:	pkgconfig(libprojectM)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(enca)
BuildRequires:	cmake
%if %{build_plf}
BuildRequires:	libfaad2-devel
%else
BuildConflicts:	libfaad2-devel
%endif
Requires:	unzip
Requires:	%{libname} = %{version}
Requires:	%{libnameui} = %{version}
Requires:	%{name}-plugins = %{version}
Requires:	wildmidi

%description
This program is an audio-player, written with help of Qt library. The user
interface is similar to winamp or xmms.

Main opportunities:
* winamp and xmms skins support;
* plugins support;
* MPEG1 layer 1/2/3 support;
* Ogg Vorbis support;
* native FLAC support;
* Musepack support;
* WavePack support;
* ModPlug support;
* WMA support;
* PCM WAVE support;
* AlSA sound output;
* JACK sound output;
* OSS sound output;
* PulseAudio output;
* Last.fm scrobbler;
* D-Bus support;
* Spectrum Analyzer;
* sample rate conversion;
* streaming support (MP3, Vorbis via IceCast/ShoutCast).

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for %{name}

%description -n	%{libname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}

%package -n	%{libnameui}
Group:		System/Libraries
Summary:	Library for %{name}

%description -n	%{libnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}

%package -n	%{libname_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname_devel}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}

%package -n	%{libnameui_devel}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libnameui} = %{version}
Provides:	lib%{name}ui-devel = %{version}-%{release}
Provides:	%{name}ui-devel = %{version}-%{release}

%description -n	%{libnameui_devel}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}

%package -n %{name}-jack
Summary:	Qmmp Jack Output Plugin
Group:		Sound

%description -n %{name}-jack
This is the Jack Output Plugin for Qmmp

%package -n %{name}-oss
Summary:	Qmmp OSS Output Plugin
Group:		Sound

%description -n %{name}-oss
This is the Jack OSS Plugin for Qmmp

%package -n %{name}-musepack
Summary:	Qmmp MusePack Output Plugin
Group:		Sound

%description -n %{name}-musepack
This is the Musepack Input Plugin for Qmmp

%package -n %{name}-ffmpeg
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description -n %{name}-ffmpeg
This is the FFMPEG Input Plugin for Qmmp

%package -n %{name}-wavpack
Summary:	Qmmp WavPack Input Plugin
Group:		Sound

%description -n %{name}-wavpack
This is the WavPack Input Plugin for Qmmp

%package -n %{name}-modplug
Summary:	Qmmp Modplug Input Plugin
Group:		Sound

%description -n %{name}-modplug
This is the Modplug Input Plugin for Qmmp

%if %{build_plf}
%package -n %{name}-aac
Summary:	Qmmp AAC Input Plugin
Group:		Sound

%description -n %{name}-aac
This is the AAC Input plugin for Qmmp

This package is in restricted repository because AAC codec is patent-protected.
%endif

%package -n %{name}-plugins
Summary:	Qmmp Plugins
Group:		Sound

%description -n %{name}-plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plugin distribution.

%prep
%setup -q

%build
#oss3 support is deprecated upstream for now I'll enable it ...
%cmake_qt4 -DUSE_HAL=OFF -DUSE_OSS:BOOL=TRUE
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/libqmmp.so.%{major}*

%files -n %{libnameui}
%{_libdir}/libqmmpui.so.%{major}*

%files -n %{libname_devel}
%{_includedir}/%{name}
%{_libdir}/libqmmp.so
%{_libdir}/pkgconfig/qmmpui.pc
%{_libdir}/pkgconfig/qmmp.pc

%files -n %{libnameui_devel}
%{_includedir}/qmmpui
%{_libdir}/libqmmpui.so

%files -n %{name}-jack
%{_libdir}/%{name}/Output/libjack.so

%files -n %{name}-oss
%{_libdir}/%{name}/Output/liboss.so

%files -n %{name}-musepack
%{_libdir}/%{name}/Input/libmpc.so

%files -n %{name}-ffmpeg
%{_libdir}/%{name}/Input/libffmpeg.so

%files -n %{name}-wavpack
%{_libdir}/%{name}/Input/libwavpack.so

%files -n %{name}-modplug
%{_libdir}/%{name}/Input/libmodplug.so

%if %{build_plf}
%files -n %{name}-aac
{_libdir}/%{name}/Input/libaac.so
%endif

%files -n %{name}-plugins
%{_libdir}/%{name}/Input/libflac.so
%{_libdir}/%{name}/Input/libmad.so
%{_libdir}/%{name}/Input/libsndfile.so
%{_libdir}/%{name}/Input/libvorbis.so
%{_libdir}/%{name}/Input/libcdaudio.so
%{_libdir}/%{name}/Input/libcue.so
%{_libdir}/%{name}/Input/libgme.so
%{_libdir}/%{name}/Input/libwildmidi.so

%{_libdir}/%{name}/Output/libalsa.so
%{_libdir}/%{name}/Output/libpulseaudio.so
%{_libdir}/%{name}/Output/libnull.so

%{_libdir}/%{name}/General/libnotifier.so
%{_libdir}/%{name}/General/libscrobbler.so
%{_libdir}/%{name}/General/libstatusicon.so
%{_libdir}/%{name}/General/libfileops.so
%{_libdir}/%{name}/General/libhotkey.so
%{_libdir}/%{name}/General/liblyrics.so
%{_libdir}/%{name}/General/libmpris.so
%{_libdir}/%{name}/General/libcovermanager.so
%{_libdir}/%{name}/General/libkdenotify.so
%{_libdir}/%{name}/General/libudisks.so
%{_libdir}/%{name}/General/libconverter.so
%{_libdir}/%{name}/Engines/libmplayer.so
%{_libdir}/%{name}/General/libstreambrowser.so

%{_libdir}/%{name}/CommandLineOptions/libincdecvolumeoption.so
%{_libdir}/%{name}/CommandLineOptions/libseekoption.so
%{_libdir}/%{name}/CommandLineOptions/libstatusoption.so
%{_libdir}/%{name}/CommandLineOptions/libplaylistoption.so

%{_libdir}/%{name}/Effect/libsrconverter.so
%{_libdir}/%{name}/Effect/libbs2b.so
%{_libdir}/%{name}/Effect/libladspa.so
%{_libdir}/%{name}/Effect/libcrossfade.so
%{_libdir}/%{name}/Effect/libstereo.so

%{_libdir}/%{name}/FileDialogs/libqmmpfiledialog.so

%{_libdir}/%{name}/PlaylistFormats/libm3uplaylistformat.so
%{_libdir}/%{name}/PlaylistFormats/libplsplaylistformat.so
%{_libdir}/%{name}/PlaylistFormats/libxspfplaylistformat.so

%{_libdir}/%{name}/Transports/libhttp.so
%{_libdir}/%{name}/Transports/libmms.so

%{_libdir}/%{name}/Visual/libanalyzer.so
%{_libdir}/%{name}/Visual/libprojectm.so

%{_libdir}/%{name}/Ui/libskinned.so



%changelog
* Sat Aug 18 2012 Andrey Bondrov <abondrov@mandriva.org> 0.6.3-1
+ Revision: 815295
- New version 0.6.3, convert BR to pkgconfig style, add PLF build conditions

* Thu Jul 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.1-1
+ Revision: 811157
- version update 0.6.1

  + Sergey Zhemoitel <serg@mandriva.org>
    - update to 0.6.0
    - drop aac decoder
    - update to 0.5.5
    - add new release 0.5.4. Correct spec from 2010.1 build and later
    - new version 0.5.2
    - new release 0.5.1, aac-plugin

  + Götz Waschk <waschk@mandriva.org>
    - rebuild for new libcdio

* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 0.5.1-1
+ Revision: 676418
- update file list
- update to new version 0.5.1

  + Sergey Zhemoitel <serg@mandriva.org>
    - correct require wildmidi
    - add require wildmidi
    - add require wildmidi 0.2.3.4 version

* Sat Mar 26 2011 Funda Wang <fwang@mandriva.org> 0.5.0-1
+ Revision: 648585
- update file list
- new version 0.5.0

* Sat Mar 12 2011 Funda Wang <fwang@mandriva.org> 0.4.5-1
+ Revision: 644009
- update to new version 0.4.5

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.4.3-1mdv2011.0
+ Revision: 593058
- new version 0.4.3

* Fri Oct 29 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.4.2-1mdv2011.0
+ Revision: 589920
- update to 0.4.2
- clean spec and remove the "mdkversion < 200900" macros

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 550677
- update file list
- New version 0.4.1

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdv2011.0
+ Revision: 550644
- rebuild for new libmodplug

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.3.4-1mdv2010.1
+ Revision: 536549
- new version 0.3.4

* Thu Mar 11 2010 Funda Wang <fwang@mandriva.org> 0.3.3-1mdv2010.1
+ Revision: 517894
- New version 0.3.3

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0.3.2-1mdv2010.1
+ Revision: 493275
- update to new version 0.3.2

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 463500
- new version 0.3.1

* Sun Jul 05 2009 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2010.0
+ Revision: 392518
- New version 0.3.0

* Mon May 04 2009 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2010.0
+ Revision: 371561
- use ulong rather than uint
- New version 0.2.4

* Fri Dec 05 2008 Funda Wang <fwang@mandriva.org> 0.2.3-1mdv2009.1
+ Revision: 310111
- New versio n0.2.3
- drop upstream patches

* Sun Oct 19 2008 Funda Wang <fwang@mandriva.org> 0.2.2-3mdv2009.1
+ Revision: 295181
- rebuild for new ffmpeg

* Tue Sep 02 2008 Funda Wang <fwang@mandriva.org> 0.2.2-2mdv2009.0
+ Revision: 278804
- add patch fixing parallel build and fixes for lib64
- add patch (upstream) to build out of source

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2009.0
+ Revision: 278050
- New version 0.2.2

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 263664
- add conflicts to ease upgrading
- use cmake to build
- New version 0.2.0
- fix URL

* Sat Jul 12 2008 Funda Wang <fwang@mandriva.org> 0.1.6-1mdv2009.0
+ Revision: 234151
- BR ffmpeg
- import qmmp


