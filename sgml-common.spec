Summary:     text formatting system used by the Linux Documentation Project
%define      packagename sgml-tools
%define      packver 1.0.9
Name:        %{packagename}
Obsoletes:   linuxdoc-sgml
Version:     %{packver}
Release:     1d
Copyright:   freeware
Group:       Utilities/Text/SGML
Group(pl):	Narzêdzia/Tekst/SGML
Source:      http://ftp.nllgg.nl/pub2/SGMLtools/1.0/%{name}-%{version}.tar.gz
Url:         http://www.nllgg.nl/SGMLtools
Patch:       %{name}.patch
Buildroot:   /tmp/%{name}-%{version}-root
Requires:	sp, sgmls, iso-entitles
Summary(de): Textformatierungssystem, das vom Linux Documentation Project benutzt wird
Summary(fr): Système de formattage de texte utilisé par le Linux Documentation Project.
Summary(nl): Tekstformateringssysteem welke door het Linux Documentatie Project wordt gebruikt.
Summary(pl): Narzêdzia konweruj±ce do linuxdoc-dtd 
Summary(tr): GNU belge biçimlendirme sistemi

%description
SGMLtools is a SGML-based text formatter which allows you to
produce a variety of output formats. You can create PostScript and
dvi (with LaTeX), plain text (with groff), HTML, and texinfo files
from a single SGML source file.

%description -l pl
Narzêdzia konweruj±ce do linuxdoc-dtd 

%description -l de
SGMLtools ist ein Textformatierer auf SGML-Basis, der eine Vielzahl
von Ausgabeformaten erzeugen kann. Sie können aus einer einzigen 
SGML-Quelldatei PostScript-, dvi- (mit LaTeX), Nur-Text- 
(mit groff), HTML- und texinfo-Dateien erstellen.

%description -l fr
SGMLtools est un formatteur de texte basé sur SGML qui vous permet
de produire de nombreux formats de fichiers de sortie. vous pouvez
créer du PostScript et du dvi (avec LaTeX), du texte simple (avec groff),
du HTML, et des fichiers texinfo depuis un simple fichier SGML.

%description -l tr
SGMLtools, SGML tabanlý deðiþik biçimlerde çýktýlar üretmenizi saðlayan bir
metin biçimleyicisidir. PostScript, dvi (LaTeX ile), düz metin (groff ile),
HTML dosyalarýný tek bir SGML kaynak dosyasýndan yaratabilirsiniz.

%description -l nl
SGMLtools is een op SGML gebaseerd tekstverwerkingssyteem waarmee een
aantal verschillende andere bestanden kan worden gemaakt. Uitvoer is
mogelijk in: ASCII, DVI, HTML, LaTeX, PostScript en RTF (Windows help)

%package -n  sgmls
Summary:     sgmls
version:     1.1
Group:       Utilities/Text/SGML
Summary(pl): sgmls

%description -n sgmls
Sgmls

%description -n sgmls
Sgmls

%prep
%setup -q
%patch -p1

%build
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/tmp/opt --with-installed-nsgmls 

make OPTIMIZE="$RPM_OPT_FLAGS"

cd sgmls-1.1 
make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=/tmp/opt
make install 
cd ..
rm -rf $RPM_BUILD_ROOT
install -d  /tmp/opt/{lib,bin,share,man,man/man1}
install -d  /tmp/opt/lib/sgml-tools
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls /tmp/opt/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.pl /tmp/opt/bin/
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast /tmp/opt/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.man /tmp/opt/man/man1/sgmls.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmlsasp.man /tmp/opt/man/man1/sgmlsasp.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast.man /tmp/opt/man/man1/rast.1

make prefix=/tmp/opt install

install -d /tmp/opt/share/sgml/sgml-tools
install /tmp/opt/lib/sgml-tools/dtd/* /tmp/opt/share/sgml/sgml-tools 

bzip2 -9 /tmp/opt/man/man1/*

export PATH=/tmp/opt/bin:$PATH

CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=/usr --with-installed-nsgmls 

make OPTIMIZE="$RPM_OPT_FLAGS"

cd sgmls-1.1 
make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=$RPM_BUILD_ROOT/usr
cd ..

%install
cd sgmls-1.1 
make install 
cd ..

install -d  $RPM_BUILD_ROOT/usr/{lib,bin,share,man,man/man1}
install -d  $RPM_BUILD_ROOT/usr/lib/sgml-tools
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls $RPM_BUILD_ROOT/usr/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.pl $RPM_BUILD_ROOT/usr/bin/
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast $RPM_BUILD_ROOT/usr/bin
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmls.man $RPM_BUILD_ROOT/usr/man/man1/sgmls.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/sgmlsasp.man $RPM_BUILD_ROOT/usr/man/man1/sgmlsasp.1
install $RPM_BUILD_DIR/%{packagename}-%{packver}/sgmls-1.1/rast.man $RPM_BUILD_ROOT/usr/man/man1/rast.1

perl -pi -e "s#sgml2#/tmp/opt/bin/sgml2#g" doc/Makedoc.sh 

make prefix=$RPM_BUILD_ROOT/usr install

strip $RPM_BUILD_ROOT/usr/bin/rast
strip $RPM_BUILD_ROOT/usr/bin/sgmls
strip $RPM_BUILD_ROOT/usr/bin/rtf2rtf
strip $RPM_BUILD_ROOT/usr/bin/sgmlsasp 
strip $RPM_BUILD_ROOT/usr/bin/sgmlpre


install -d $RPM_BUILD_ROOT/usr/share/sgml/sgml-tools
install $RPM_BUILD_ROOT/usr/lib/sgml-tools/dtd/* $RPM_BUILD_ROOT/usr/share/sgml/sgml-tools 

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man1/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/usr/lib/sgml-tools
/usr/lib/perl5/Text/EntityMap.pm
/usr/lib/sgml/*
%attr(711,root,root) /usr/bin/rtf2rtf
%attr(711,root,root) /usr/bin/sgmlpre
%attr(755,root,root) /usr/bin/sgml2* 
%attr(755,root,root) /usr/bin/sgmltools.v1 
%attr(755,root,root) /usr/bin/sgmlcheck
%attr(644,root, man) /usr/man/man1/sgml2*.1.bz2
%attr(644,root, man) /usr/man/man1/sgmlcheck.1.bz2
%attr(644,root, man) /usr/man/man1/sgmltools.1.bz2
/usr/share/sgml/sgml-tools
/usr/lib/entity-map

%files -n sgmls 
%defattr(644,root,root,755)
%doc sgmls-1.1/LICENSE sgmls-1.1/NEWS 
%attr(711,root,root) /usr/bin/rast
%attr(711,root,root) /usr/bin/sgmls
%attr(711,root,root) /usr/bin/sgmlsasp 
%attr(755,root,root) /usr/bin/sgmls.pl 
%attr(644,root, man) /usr/man/man1/rast.1.bz2
%attr(644,root, man) /usr/man/man1/sgmls*


%changelog
* Thu Dec 17 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
[1.0.9-1d]
- updated to last ,,official'' latest version
- build without instaled previous version (but there is terrible)

* Tue Sep 8 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl> 
- removed nsgmls (provides by jade) 
#- removed Entity Maps (provides by sgml-common) 
#- dtd moved to separate noarch package 
- sgmls moved to separate binary package 

* Wed Jul 01 1998 Hugo van der Kooij <hvdkooij@nllgg.nl>
- Updated to 1.0.7
- Removed the (silly) patch (thank you Donny, but Cees and I are Dutch ;-)

* Tue May 05 1998 Donnie Barnes <djb@redhat.com>

- changed default papersize to letter (from a4...sorry Europeans :-)
 use --papersize=a4 on any sgml2* command to change it or remove the
 patch from this spec file and rebuild.

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.0.6

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jan 12 1998 Donnie Barnes <djb@redhat.com>
- updated from 0.99 to 1.0.3
- added BuildRoot

* Sat Nov 01 1997 Donnie Barnes <djb@redhat.com>
- fixed man pages

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- new release - Obsoletes linuxdoc-sgml
