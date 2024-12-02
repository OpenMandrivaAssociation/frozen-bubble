%define	module	Games-FrozenBubble
%define version 2.212

# TODO 
#  server package, with initscript, for people wanting to have a complete
#   server
#  zeroconf integration, with this initscript ( and in konqueror )
Summary:	Frozen Bubble arcade game
Name:		frozen-bubble
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Games/Arcade
Url:		https://www.frozen-bubble.org/
Source0:	https://cpan.metacpan.org/authors/id/K/KT/KTHAKORE/%{module}-%{version}.tar.gz
Patch1:		frozen-bubble-2.2.1-Use-true-number-instead-of-quoted-version-number.patch
BuildRequires:	perl-devel
BuildRequires:	smpeg-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_Pango)
BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.2
BuildRequires:	perl(Alien::SDL)
BuildRequires:	perl(Archive::Extract)
BuildRequires:	perl(Compress::Bzip2)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(IPC::System::Simple)
BuildRequires:	perl(Locale::Maketext::Extract)
BuildRequires:	perl(SDL)
BuildRequires:	perl(autodie)
BuildRequires:	perl(parent)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)
Requires:	perl-SDL
Requires:	perl(Compress::Bzip2)

%description
A Puzzle Bobble / Bust-a-Move like game featuring colorful 3D rendered
penguin animations, 100 levels, local and Internet-based multiplayer,
a level editor, 3 professional quality digital soundtracks, 15 stereo
sound effects, 8 unique graphical transition effects, 8 unique logo
eye-candies.


%prep
%autosetup -p1 -n %{module}-%{version}

%build
export CFLAGS="%{optflags} -Wno-error"
perl Build.PL installdirs=vendor
./Build

#check
#./Build test || echo "Failed"

%install
./Build install destdir=%{buildroot}
rm -f %{buildroot}%{_gamesdatadir}/frozen-bubble/gfx/shoot/create.pl

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Frozen Bubble
Name[ru]=Frozen Bubble
Comment=Frozen Bubble arcade game
Comment[ru]=Игра Frozen Bubble
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

install -m 644 share/icons/frozen-bubble-icon-16x16.png -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m 644 share/icons/frozen-bubble-icon-32x32.png -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m 644 share/icons/frozen-bubble-icon-48x48.png -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
# language files not located in standard location, so let's screw it for now..
#%find_lang %{name}

%files
#-f %{name}.lang
%doc README AUTHORS META.yml HISTORY
%{_bindir}/*
#{_gamesdatadir}/%{name}
#{perl_vendorlib}/*
%{perl_vendorarch}/*
#{perl_vendorarch}/*.pm
%{_mandir}/*/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
