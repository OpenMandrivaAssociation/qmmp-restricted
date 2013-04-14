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
Version:	0.7.0
Release:	2%{?extrarelsuffix}
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

#  ffmpeg-legacy in LTS
%if %{mdvver} >= 201210
%package -n %{name}-ffmpeg
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description -n %{name}-ffmpeg
This is the FFMPEG Input Plugin for Qmmp
#
%else
%package -n %{name}-ffmpeg-legacy
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound
Obsoletes:  %{name}-ffmpeg

%description -n %{name}-ffmpeg-legacy
This is the FFMPEG Input Plugin for Qmmp
%endif

#
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
This is the AAC Input plug-in for Qmmp

This package is in restricted repository because AAC codec is patent-protected.
%endif

%package -n %{name}-plugins
Summary:	Qmmp Plugins
Group:		Sound

%description -n %{name}-plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plug-in distribution.

%prep
%setup -q

%build
#oss3 support is deprecated upstream for now I'll enable it ...
%cmake_qt4 -DUSE_HAL:BOOL=FALSE \
	-DUSE_OSS:BOOL=TRUE \
	-DUSE_OSS:UDISKS2=TRUE \
	-DUSE_RPATH=TRUE \
	-DCMAKE_INSTALL_PREFIX=/usr

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
%doc AUTHORS ChangeLog
%{_libdir}/libqmmp.so.%{major}*

%files -n %{libnameui}
%doc AUTHORS ChangeLog
%{_libdir}/libqmmpui.so.%{major}*

%files -n %{libname_devel}
%doc AUTHORS ChangeLog
%{_includedir}/%{name}
%{_libdir}/libqmmp.so
%{_libdir}/pkgconfig/qmmpui.pc
%{_libdir}/pkgconfig/qmmp.pc

%files -n %{libnameui_devel}
%doc AUTHORS ChangeLog
%{_includedir}/qmmpui
%{_libdir}/libqmmpui.so

%files -n %{name}-jack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/libjack.so

%files -n %{name}-oss
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/liboss.so

%files -n %{name}-musepack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmpc.so

# ffmpeg-legacy in LTS
%if %{mdvver} >= 201210
%files -n %{name}-ffmpeg
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg.so
#
%else
%files -n %{name}-ffmpeg-legacy
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg_legacy.so
%endif
#
%files -n %{name}-wavpack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libwavpack.so

%files -n %{name}-modplug
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmodplug.so

%if %{build_plf}
%files -n %{name}-aac
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libaac.so
%endif

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
%{_libdir}/%{name}/Engines/libmplayer.so
%{_libdir}/%{name}/General/libstreambrowser.so
%{_libdir}/%{name}/General/libconverter.so
%{_libdir}/%{name}/General/libcopypaste.so
%{_libdir}/%{name}/General/libtrackchange.so
%{_libdir}/%{name}/General/libudisks2.so

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

%{_libdir}/%{name}/FileDialogs/libqmmpfiledialog.so

%{_libdir}/%{name}/Transports/libhttp.so
%{_libdir}/%{name}/Transports/libmms.so

%{_libdir}/%{name}/Visual/libanalyzer.so
%{_libdir}/%{name}/Visual/libprojectm.so

%{_libdir}/%{name}/Ui/libskinned.so




