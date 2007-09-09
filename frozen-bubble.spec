%define name    frozen-bubble
%define version 2.1.0
%define release %mkrel 3
%define title       Frozen Bubble
%define longtitle   Frozen Bubble arcade game

# TODO 
#  server package, with initscript, for people wanting to have a complete
#   server
#  zeroconf integration, with this initscript ( and in konqueror )
Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Frozen Bubble arcade game
License:        GPL
Group:          Games/Arcade
URL:            http://www.frozen-bubble.org/
Source:         http://www.frozen-bubble.org/data/%{name}-%{version}.tar.bz2
Requires:       perl-SDL >= 1.18
Requires:       %{name}-server-common
BuildRequires:  libSDL_mixer-devel >= 1.2.2
BuildRequires:  libsmpeg-devel
BuildRequires:  perl-SDL
BuildRequires:  perl-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  libSDL_mixer-devel >= 1.2.2 
BuildRequires:  SDL_Pango-devel 
BuildRequires:  glib2-devel

%description
Colorful 3D rendered penguin animations, 100 levels of 1p game,
hours and hours of 2p game, nights and nights of 2p/3p/4p/5p game
over LAN or Internet, a level-editor, 3 professional quality
digital soundtracks, 15 stereo sound effects, 8 unique graphical
transition effects, 8 unique logo eye-candies.


%package server-common
Summary: Frozen bubble server, used for multiplayer game
Group: Games/Arcade
Conflicts: %name < 2.1


%description server-common
This package only contains the server of Frozen bubble, for people
wanting to host a multiplayer server on their computer without installing
the whole game. If you wish to play, install frozen-bubble.

%prep
%setup -q

%build
make OPTIMIZE="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS `pkg-config glib-2.0 --cflags`" LIBS="`pkg-config glib-2.0 --libs`" LIBDIR=%{_libdir} DATADIR=%{_gamesdatadir} INSTALLDIRS=vendor

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} DATADIR=%{_gamesdatadir} BINDIR=%{_gamesbindir} MANDIR=%{_mandir} LOCALEDIR=%{_datadir}/locale
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

install -m 644 icons/frozen-bubble-icon-16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 icons/frozen-bubble-icon-32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m 644 icons/frozen-bubble-icon-48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}



%files  server-common 
%defattr(-, root, root)
%{_libdir}/%{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS TIPS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/*.pm
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png


