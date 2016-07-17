%define major		1
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d
%define libnameui	%mklibname qmmpui %{major}
%define devnameui	%mklibname qmmpui -d

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
Version:	1.1.1
Release:	1%{?extrarelsuffix}
License:	GPLv2+
Group:		Sound
Url:		http://qmmp.ylsoftware.com/index_en.php
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	libgme-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	wildmidi-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libprojectM)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	sidplay-devel
BuildRequires:	pkgconfig(libsidplay2)
# do not remove sdl-headers needed by sid-ogg.Sflo
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(opus)



%if %{build_plf}
BuildRequires:	faad2-devel
%else
BuildConflicts:	faad2-devel
%endif
Requires:	unzip
Requires:	%{libname} = %{EVRD}
Requires:	%{libnameui} = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}
Suggests:	%{name}-aac = %{EVRD}
%if %{mdvver} >= 201210
Suggests:	%{name}-ffmpeg = %{EVRD}
%else
Suggests:	%{name}-ffmpeg-legacy = %{EVRD}
%endif
Suggests:	%{name}-jack = %{EVRD}
Suggests:	%{name}-modplug = %{EVRD}
Suggests:	%{name}-musepack = %{EVRD}
Suggests:	%{name}-oss = %{EVRD}
Suggests:	%{name}-wavpack = %{EVRD}
Suggests:	%{name}-plugin-pack
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

%files
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for %{name}

%description -n	%{libname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}.

%files -n %{libname}
%doc AUTHORS ChangeLog
%{_libdir}/libqmmp.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{libnameui}
Group:		System/Libraries
Summary:	Library for %{name}

%description -n	%{libnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}.

%files -n %{libnameui}
%doc AUTHORS ChangeLog
%{_libdir}/libqmmpui.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}.

%files -n %{devname}
%doc AUTHORS ChangeLog
%{_includedir}/%{name}
%{_libdir}/libqmmp.so
%{_libdir}/pkgconfig/qmmp.pc

#----------------------------------------------------------------------------

%package -n	%{devnameui}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libnameui} = %{EVRD}
Provides:	%{name}ui-devel = %{EVRD}
Conflicts:	%{_lib}qmmp-devel < 0.7.2

%description -n	%{devnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}.

%files -n %{devnameui}
%doc AUTHORS ChangeLog
%{_includedir}/qmmpui
%{_libdir}/libqmmpui.so
%{_libdir}/pkgconfig/qmmpui.pc

#----------------------------------------------------------------------------

%if %{build_plf}
%package -n %{name}-aac
Summary:	Qmmp AAC Input Plugin
Group:		Sound

%description -n %{name}-aac
This is the AAC Input plug-in for Qmmp.

This package is in restricted repository because AAC codec is patent-protected.

%files -n %{name}-aac
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libaac.so
%endif

#----------------------------------------------------------------------------

#  ffmpeg-legacy in LTS
%if %{mdvver} >= 201210
%package -n %{name}-ffmpeg
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description -n %{name}-ffmpeg
This is the FFMPEG Input Plugin for Qmmp.

%files -n %{name}-ffmpeg
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg.so

%else

%package -n %{name}-ffmpeg-legacy
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description -n %{name}-ffmpeg-legacy
This is the FFMPEG Input Plugin for Qmmp.

%files -n %{name}-ffmpeg-legacy
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg_legacy.so
%endif

#----------------------------------------------------------------------------

%package -n %{name}-jack
Summary:	Qmmp Jack Output Plugin
Group:		Sound

%description -n %{name}-jack
This is the Jack Output Plugin for Qmmp.

%files -n %{name}-jack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/libjack.so


#----------------------------------------------------------------------------

%package -n %{name}-modplug
Summary:	Qmmp Modplug Input Plugin
Group:		Sound

%description -n %{name}-modplug
This is the Modplug Input Plugin for Qmmp.

%files -n %{name}-modplug
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmodplug.so

#----------------------------------------------------------------------------

%package -n %{name}-musepack
Summary:	Qmmp MusePack Output Plugin
Group:		Sound

%description -n %{name}-musepack
This is the Musepack Input Plugin for Qmmp.

%files -n %{name}-musepack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmpc.so

#----------------------------------------------------------------------------

%package -n %{name}-oss
Summary:	Qmmp OSS Output Plugin
Group:		Sound

%description -n %{name}-oss
This is the Jack OSS Plugin for Qmmp.

%files -n %{name}-oss
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/liboss.so

#----------------------------------------------------------------------------

%package -n %{name}-wavpack
Summary:	Qmmp WavPack Input Plugin
Group:		Sound

%description -n %{name}-wavpack
This is the WavPack Input Plugin for Qmmp.

%files -n %{name}-wavpack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libwavpack.so

#----------------------------------------------------------------------------
%package -n %{name}-opus
Summary:	Qmmp Opus Input Plugin
Group:		Sound

%description -n %{name}-opus
This is the Opus Input Plugin for Qmmp.

%files -n %{name}-opus
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libopus.so

#----------------------------------------------------------------------------
%package -n %{name}-sid
Summary:	Qmmp SID Input Plugin
Group:		Sound

%description -n %{name}-sid
This is the SID Input Plugin for Qmmp.

%files -n %{name}-sid
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libsid.so

#----------------------------------------------------------------------------

%package -n %{name}-plugins
Summary:	Qmmp Plugins
Group:		Sound

%description -n %{name}-plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plug-in distribution.

%files -n %{name}-plugins
%doc AUTHORS ChangeLog
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
%{_libdir}/%{name}/General/libstreambrowser.so
%{_libdir}/%{name}/General/libconverter.so
%{_libdir}/%{name}/General/libcopypaste.so
%{_libdir}/%{name}/General/libtrackchange.so
%{_libdir}/%{name}/General/libudisks2.so
%{_libdir}/%{name}/General/libgnomehotkey.so
%{_libdir}/%{name}/General/librgscan.so

%{_libdir}/%{name}/PlayListFormats/*

%{_libdir}/%{name}/CommandLineOptions/libincdecvolumeoption.so
%{_libdir}/%{name}/CommandLineOptions/libseekoption.so
%{_libdir}/%{name}/CommandLineOptions/libstatusoption.so
%{_libdir}/%{name}/CommandLineOptions/libplaylistoption.so

%{_libdir}/%{name}/Effect/libsrconverter.so
%{_libdir}/%{name}/Effect/libbs2b.so
%{_libdir}/%{name}/Effect/libladspa.so
%{_libdir}/%{name}/Effect/libcrossfade.so
%{_libdir}/%{name}/Effect/libstereo.so

%{_libdir}/%{name}/Engines/libmplayer.so

%{_libdir}/%{name}/FileDialogs/libqmmpfiledialog.so

%{_libdir}/%{name}/Transports/libhttp.so
%{_libdir}/%{name}/Transports/libmms.so

%{_libdir}/%{name}/Visual/libanalyzer.so
%{_libdir}/%{name}/Visual/libprojectm.so

%{_libdir}/%{name}/Ui

#----------------------------------------------------------------------------

%prep
%setup -q

%build
#oss3 support is deprecated upstream for now I'll enable it ...
%cmake_qt5 -DUSE_HAL:BOOL=FALSE \
	-DUSE_OSS:BOOL=TRUE \
	-DUSE_OSS:UDISKS2=TRUE \
	-DUSE_RPATH=TRUE \
	-DCMAKE_INSTALL_PREFIX=/usr

%make

%install
%makeinstall_std -C build
