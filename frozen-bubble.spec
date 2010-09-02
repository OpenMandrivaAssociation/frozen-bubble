%define upstream_name    Games-FrozenBubble
%define upstream_version 2.212

%define title		Frozen Bubble
%define longtitle	Frozen Bubble arcade game

# TODO 
#  server package, with initscript, for people wanting to have a complete
#   server
#  zeroconf integration, with this initscript ( and in konqueror )
Name:		frozen-bubble
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Frozen Bubble arcade game
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.frozen-bubble.org/
Source:     http://www.frozen-bubble.org/data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	glib2-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel >= 1.2.2
BuildRequires:	libsmpeg-devel
BuildRequires:	perl(Alien::SDL)
BuildRequires:	perl(SDL)          >= 2.400.0
BuildRequires:	perl-devel
BuildRequires:	SDL_Pango-devel 

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl-SDL >= 2.400.0

%description
A Puzzle Bobble / Bust-a-Move like game featuring colorful 3D rendered
penguin animations, 100 levels, local and Internet-based multiplayer,
a level editor, 3 professional quality digital soundtracks, 15 stereo
sound effects, 8 unique graphical transition effects, 8 unique logo
eye-candies.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}
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

install -m 644 share/icons/frozen-bubble-icon-16x16.png -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 644 share/icons/frozen-bubble-icon-32x32.png -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 share/icons/frozen-bubble-icon-48x48.png -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
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

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING META.yml HISTORY
%{_bindir}/*
#{_gamesdatadir}/%{name}
#{perl_vendorlib}/*
%{perl_vendorarch}/*
#{perl_vendorarch}/*.pm
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
