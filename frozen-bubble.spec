%define	module	Games-FrozenBubble
%define upstream_version 2.212

# TODO 
#  server package, with initscript, for people wanting to have a complete
#   server
#  zeroconf integration, with this initscript ( and in konqueror )
Name:		frozen-bubble
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Frozen Bubble arcade game
License:	GPLv2+
Group:		Games/Arcade
Url:		http://www.frozen-bubble.org/
Source0:	http://www.frozen-bubble.org/data/%{module}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer) >= 1.2.2
BuildRequires:	libsmpeg-devel
BuildRequires:	perl(Alien::SDL)
BuildRequires:	perl(Archive::Extract)
BuildRequires:	perl(Compress::Bzip2)
BuildRequires:	perl(IPC::System::Simple)
BuildRequires:	perl(Locale::Maketext::Extract)
BuildRequires:	perl(SDL)          >= 2.400.0
BuildRequires:	perl(autodie)
BuildRequires:	perl(parent)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(SDL_Pango)

Requires:	perl-SDL >= 2.400.0
Requires:	perl(Compress::Bzip2)

%description
A Puzzle Bobble / Bust-a-Move like game featuring colorful 3D rendered
penguin animations, 100 levels, local and Internet-based multiplayer,
a level editor, 3 professional quality digital soundtracks, 15 stereo
sound effects, 8 unique graphical transition effects, 8 unique logo
eye-candies.


%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}
rm -f %{buildroot}%{_gamesdatadir}/frozen-bubble/gfx/shoot/create.pl

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Frozen Bubble
Comment=Frozen Bubble arcade game
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


%changelog
* Wed Feb 01 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 2.212.0-4
+ Revision: 770489
- drop excessive macro definitions..
- use pkgconfig() dependencies
- drop 'COPYING' as it's already provided by 'common-licenses' package
- clean spec
- ditch %%find_lang for now as translations aren't found in the expected location..
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 2.212.0-3
+ Revision: 672346
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Wed Oct 20 2010 Jani VÃ¤limaa <wally@mandriva.org> 2.212.0-2mdv2011.0
+ Revision: 586981
- fix .desktop file (#61344)

* Fri Sep 03 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.212.0-1mdv2011.0
+ Revision: 575580
- adding missing buildrequires:
- adding missing buildrequires:
- update to 2.212

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.2.0-5mdv2011.0
+ Revision: 564235
- rebuild for perl 5.12.1

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 2.2.0-4mdv2011.0
+ Revision: 556962
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-3mdv2010.1
+ Revision: 522672
- rebuilt for 2010.1

* Sun Aug 23 2009 Michael Scherer <misc@mandriva.org> 2.2.0-2mdv2010.0
+ Revision: 420214
- fix bug 52945, some constants are no longer exported with latest perl-SDL

* Fri Dec 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.0-1mdv2009.1
+ Revision: 313696
- export %%_prefix
- update to new version 2.2.0
- add buildrequires on libSDL_image-devel
- fix mixture of tabs and spaces
- use macros
- spec file clean

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.1.0-7mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-7mdv2008.1
+ Revision: 151781
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 2.1.0-5mdv2008.0
+ Revision: 91113
- don't package license
- fd.o icons
- improve description
- new license policy

* Sun Sep 09 2007 David Walluck <walluck@mandriva.org> 2.1.0-4mdv2008.0
+ Revision: 83394
- rebuild (package was unsigned)

* Sun Sep 09 2007 Emmanuel Andry <eandry@mandriva.org> 2.1.0-3mdv2008.0
+ Revision: 83323
- Drop old menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Dec 01 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.1.0-2mdv2007.0
+ Revision: 89694
- release
- fix upgrade (#27435)

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.1.0-1mdv2007.1
+ Revision: 87021
- new release
- new source URL
- fix source url

  + Michael Scherer <misc@mandriva.org>
    - split server from main package, to host a server without pulling the whole set of deps

* Wed Nov 01 2006 Michael Scherer <misc@mandriva.org> 2.0.0-1mdv2007.1
+ Revision: 74955
- version 2.0, specfile merged from upstream with mandriva one
- fix bug #7778
- Import frozen-bubble

* Mon Sep 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.0-11mdv2007.0
- Really migrate to xdg menu

* Fri Jul 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-10mdv2007.0
- xdg menu
- spec cleanup

* Tue Mar 28 2006 Pixel <pixel@mandriva.com> 1.0.0-9mdk
- fix "make install" using DESTDIR
  (MakeMaker generated Makefile doesn't handle PREFIX anymore)

* Fri Dec 16 2005 Michael Scherer <misc@mandriva.org> 1.0.0-8mdk
- mkrel
- fix #20223 ( by simply rebuilding it, this is weird ).

* Mon Nov 15 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-7mdk
- Rebuild for new perl

