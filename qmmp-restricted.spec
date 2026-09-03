%define _disable_ld_no_undefined 1

%define major		2
%define major2		%(echo %{version} |cut -d. -f1-2)
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
Version:	2.4.2
Release:	100
License:	GPLv2+
Group:		Sound
Url:		https://qmmp.ylsoftware.com/
Source:		https://qmmp.ylsoftware.com/files/%{name}/%{major2}/%{name}-%{version}.tar.bz2
Patch0:		qmmp-2.1.1-compile.patch

BuildRequires:	make
BuildRequires:	cmake
BuildRequires:	cmake(qt6)
BuildRequires:	qmake-qt6
BuildRequires:	ffmpeg-devel
BuildRequires:	libgme-devel
BuildRequires:	libmpcdec-devel
#BuildRequires:	qt5-devel
#BuildRequires:	qt5-linguist
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Multimedia)
#BuildRequires:	%{_lib}Qt6Multimedia-devel
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
#BuildRequires:	cmake(Qt6Linguist)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	qt6-qttools
BuildRequires:	pkgconfig(opengl)
BuildRequires:  qt6-qtmultimedia-gstreamer
#BuildRequires:	pkgconfig(Qt5Multimedia)
#BuildRequires:	pkgconfig(Qt5X11Extras)
#BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	wildmidi-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libprojectM)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(librcd)
BuildRequires:	pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(mad)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:  pkgconfig(shout)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(taglib) >= 1.12
BuildRequires:	pkgconfig(udisks2)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	sidplay-devel
#libsidplay2 was pulled out from cooker. So build only with sidplay-devel(1).(penguin)
#BuildRequires:	pkgconfig(libsidplay)
# do not remove sdl-headers needed by sid-ogg.Sflo
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(soxr)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	vulkan-headers
BuildRequires:	pkgconfig(xkbcommon)
%if %{build_plf}
BuildRequires:	pkgconfig(faad2)
BuildRequires:	pkgconfig(fdk-aac)
%else
BuildConflicts: pkgconfig(faad2)
BuildConflicts:	pkgconfig(fdk-aac)
%endif
Requires:	unzip
Requires:	%{libname} = %{EVRD}
Requires:	%{libnameui} = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}
Recommends:	%{name}-aac = %{EVRD}
Recommends:	%{name}-ffmpeg = %{EVRD}
Recommends:	%{name}-jack = %{EVRD}
Recommends:	%{name}-modplug = %{EVRD}
# Seems to be removed in 1.3.x?
Obsoletes:	%{name}-musepack < %{EVRD}
Recommends:	%{name}-oss = %{EVRD}
Recommends:	%{name}-wavpack = %{EVRD}
Recommends:	%{name}-plugin-pack
#This package depend on timidity-patch-SGMPlusStein and it cost us 618.39 MB disc space... Not needed, make it suggects (penguin)
Suggests:	wildmidi

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
%{_datadir}/solid/actions/%{name}-opencda.desktop
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
%{_libdir}/%{name}-%{major2}/Input/libaac.so
%endif

#----------------------------------------------------------------------------


%package -n %{name}-oss
Summary:	Qmmp OSS Output Plugin
Group:		Sound

%description -n %{name}-oss
This is the Jack OSS Plugin for Qmmp.

%files -n %{name}-oss
%doc AUTHORS ChangeLog
%{_libdir}/%{name}-%{major2}/Output/liboss.so

#----------------------------------------------------------------------------

%package -n %{name}-wavpack
Summary:	Qmmp WavPack Input Plugin
Group:		Sound

%description -n %{name}-wavpack
This is the WavPack Input Plugin for Qmmp.

%files -n %{name}-wavpack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}-%{major2}/Input/libwavpack.so

#----------------------------------------------------------------------------
%package -n %{name}-opus
Summary:	Qmmp Opus Input Plugin
Group:		Sound

%description -n %{name}-opus
This is the Opus Input Plugin for Qmmp.

%files -n %{name}-opus
%doc AUTHORS ChangeLog
#{_libdir}/%{name}-%{major2}/Input/libopus.so

#----------------------------------------------------------------------------
%package -n %{name}-sid
Summary:	Qmmp SID Input Plugin
Group:		Sound

%description -n %{name}-sid
This is the SID Input Plugin for Qmmp.

%files -n %{name}-sid
%doc AUTHORS ChangeLog
%{_libdir}/%{name}-%{major2}/Input/libsid.so

#----------------------------------------------------------------------------

%package -n %{name}-plugins
Summary:	Qmmp Plugins
Group:		Sound

%description -n %{name}-plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plug-in distribution.

%files -n %{name}-plugins
%doc AUTHORS ChangeLog

%{_libdir}/%{name}-%{major2}/Input/libarchive.so
%{_libdir}/%{name}-%{major2}/Input/libffmpeg.so
%{_libdir}/%{name}-%{major2}/Input/libflac.so
%{_libdir}/%{name}-%{major2}/Input/libsndfile.so
%{_libdir}/%{name}-%{major2}/Input/libopus.so
%{_libdir}/%{name}-%{major2}/Input/libvorbis.so
%{_libdir}/%{name}-%{major2}/Input/libcdaudio.so
%{_libdir}/%{name}-%{major2}/Input/libcue.so
%{_libdir}/%{name}-%{major2}/Input/libgme.so
%{_libdir}/%{name}-%{major2}/Input/libwildmidi.so
%{_libdir}/%{name}-%{major2}/Input/libmpeg.so

%{_datadir}/metainfo/com.ylsoftware.qmmp.metainfo.xml

%{_libdir}/%{name}-%{major2}/Output/libalsa.so
%{_libdir}/%{name}-%{major2}/Output/libjack.so
%{_libdir}/%{name}-%{major2}/Output/libpulseaudio.so
%{_libdir}/%{name}-%{major2}/Output/libnull.so
%{_libdir}/%{name}-%{major2}/Output/libqtmultimedia.so
%{_libdir}/%{name}-%{major2}/Output/libshout.so
%{_libdir}/%{name}-%{major2}/Output/libpipewire.so

%{_libdir}/%{name}-%{major2}/General/libconverter.so
%{_libdir}/%{name}-%{major2}/General/librgscan.so
%{_libdir}/%{name}-%{major2}/General/libnotifier.so
%{_libdir}/%{name}-%{major2}/General/libscrobbler.so
%{_libdir}/%{name}-%{major2}/General/libstatusicon.so
%{_libdir}/%{name}-%{major2}/General/libfileops.so
%{_libdir}/%{name}-%{major2}/General/libhistory.so
%{_libdir}/%{name}-%{major2}/General/libhotkey.so
%{_libdir}/%{name}-%{major2}/General/liblibrary.so
%{_libdir}/%{name}-%{major2}/General/liblyrics.so
%{_libdir}/%{name}-%{major2}/General/libbatchtageditor.so
%{_libdir}/%{name}-%{major2}/General/libmpris.so
%{_libdir}/%{name}-%{major2}/General/libcovermanager.so
%{_libdir}/%{name}-%{major2}/General/libkdenotify.so
%{_libdir}/%{name}-%{major2}/General/libstreambrowser.so
#{_libdir}/%{name}-%{major2}/General/libconverter.so
%{_libdir}/%{name}-%{major2}/General/libcopypaste.so
%{_libdir}/%{name}-%{major2}/General/libtrackchange.so
%{_libdir}/%{name}-%{major2}/General/libudisks.so
%{_libdir}/%{name}-%{major2}/General/libgnomehotkey.so
#{_libdir}/%{name}-%{major2}/General/librgscan.so
%{_libdir}/%{name}-%{major2}/General/liblistenbrainz.so
%{_libdir}/%{name}-%{major2}/General/libsleepinhibitor.so

%{_libdir}/%{name}-%{major2}/PlayListFormats/*

%{_libdir}/%{name}-%{major2}/CommandLineOptions/libincdecvolumeoption.so
%{_libdir}/%{name}-%{major2}/CommandLineOptions/libseekoption.so
%{_libdir}/%{name}-%{major2}/CommandLineOptions/libstatusoption.so
%{_libdir}/%{name}-%{major2}/CommandLineOptions/libplaylistoption.so

#{_libdir}/%{name}-%{major2}/Effect/libsoxr.so
%{_libdir}/%{name}-%{major2}/Effect/libbs2b.so
%{_libdir}/%{name}-%{major2}/Effect/libladspa.so
%{_libdir}/%{name}-%{major2}/Effect/libcrossfade.so
%{_libdir}/%{name}-%{major2}/Effect/libmonotostereo.so
%{_libdir}/%{name}-%{major2}/Effect/libstereo.so
%{_libdir}/%{name}-%{major2}/Effect/libsoxr.so
%{_libdir}/%{name}-%{major2}/Effect/libfilewriter.so

%{_libdir}/%{name}-%{major2}/FileDialogs/libqmmpfiledialog.so
%{_libdir}/%{name}-%{major2}/FileDialogs/libtwopanelfiledialog.so

%{_libdir}/%{name}-%{major2}/Transports/libhttp.so

%{_libdir}/%{name}-%{major2}/Visual/libanalyzer.so
%optional %{_libdir}/%{name}-%{major2}/Visual/libprojectm.so

%{_libdir}/%{name}-%{major2}/Ui

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#oss3 support is deprecated upstream for now I'll enable it ...
%cmake -DUSE_HAL:BOOL=FALSE \
	-DUSE_OSS:BOOL=TRUE \
	-DUSE_OSS:UDISKS2=TRUE \
	-DUSE_RPATH=TRUE \
	-DUSE_FLAC=TRUE \
	-DUSE_VORBIS=TRUE \
	-DUSE_MPC=TRUE \
	-DUSE_ARCHIVE=TRUE \
	-DUSE_FFMPEG=TRUE \
	-DUSE_OPUS=TRUE \
	-DCMAKE_INSTALL_PREFIX=/usr

%make_build

%install
%make_install -C build
