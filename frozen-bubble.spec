%define title		Frozen Bubble
%define longtitle	Frozen Bubble arcade game

# TODO 
#  server package, with initscript, for people wanting to have a complete
#   server
#  zeroconf integration, with this initscript ( and in konqueror )
Name:		frozen-bubble
Version:	2.2.0
Release:	%mkrel 4
Summary:	Frozen Bubble arcade game
License:	GPLv2+
Group:		Games/Arcade
URL:		http://www.frozen-bubble.org/
Source:		http://www.frozen-bubble.org/data/%{name}-%{version}.tar.bz2
Patch0:     frozen-bubble-2.2.0-fix_new_sdl.diff
Requires:	perl-SDL >= 1.18
Requires:	%{name}-server-common = %{version}-%{release}
BuildRequires:	libSDL_mixer-devel >= 1.2.2
BuildRequires:	libSDL_image-devel
BuildRequires:	libsmpeg-devel
BuildRequires:	perl-SDL
BuildRequires:	perl-devel
BuildRequires:	SDL_Pango-devel 
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Puzzle Bobble / Bust-a-Move like game featuring colorful 3D rendered
penguin animations, 100 levels, local and Internet-based multiplayer,
a level editor, 3 professional quality digital soundtracks, 15 stereo
sound effects, 8 unique graphical transition effects, 8 unique logo
eye-candies.


%package server-common
Summary:	Frozen bubble server, used for multiplayer game
Group:		Games/Arcade
Conflicts:	%{name} < 2.1

%description server-common
This package only contains the server of Frozen Bubble, for people
wanting to host a multiplayer server on their computer without installing
the whole game. If you wish to play the game, install frozen-bubble.

%prep
%setup -q
%patch0 -p0

%build
%make OPTIMIZE="%{optflags}" CFLAGS="%{optflags} `pkg-config glib-2.0 --cflags`" LIBS="`pkg-config glib-2.0 --libs`" LIBDIR=%{_libdir} DATADIR=%{_gamesdatadir} INSTALLDIRS=vendor PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
%makeinstall_std DESTDIR=%{buildroot} LIBDIR=%{_libdir} DATADIR=%{_gamesdatadir} BINDIR=%{_gamesbindir} MANDIR=%{_mandir} LOCALEDIR=%{_datadir}/locale
rm -f %{buildroot}/%{_gamesdatadir}/frozen-bubble/gfx/shoot/create.pl

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{longtitle}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

install -m 644 icons/frozen-bubble-icon-16x16.png -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 644 icons/frozen-bubble-icon-32x32.png -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 icons/frozen-bubble-icon-48x48.png -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%files server-common 
%defattr(-, root, root)
%{_libdir}/%{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS NEWS TIPS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/*.pm
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
