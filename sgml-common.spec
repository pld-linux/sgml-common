Summary:     Common SGML catalog and DTD files
Summary(pl): Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:        sgml-common
Version:     0.0
Release:     6
Vendor:      Cygnus Solutions -- UNSUPPORTED
Source0:     sgml-common.tgz
Source1:     install-catalog
Copyright:   (C) International Organization for Standardization 1986
Group:       Utilities/Text/SGML
BuildArchitectures: noarch
provides:    iso-entitles, iso-entities-8879.1986, sgml-catalog
BuildRoot:   /tmp/%{name}-%{version}-root

%description
sgml-common is a collection of entities and dtds that are useful for
SGML processing, but shouldn't need to be included in multiple packages.
It also includes an up-to-date Open Catalog file.

%description -l pl
sgml-common jest zestawem wspólnych dla wiekszo¶ci aplikacji SGMLa 
(bo opisanych w normie ISO 8879/1986) encji i DTD.   
Poza tym zawiera aktualizowany przy dodawaniu nowych pakietów 
plik CATALOG oraz instalator nowych DTD. 

%prep
%setup -c -q 

%build
gawk --posix '/Typical invocation:/,/\-\-\>/ { print }' sgml-common/* |
gawk --posix '/PUBLIC/ { sys=$3 } 
	/8879:1986.*\"\>/ { saveline=""; print "PUBLIC " $0 " " sys; next }
	/8879:1986[^>]*$/ { saveline = $0; next }
	/\"\>/ { print "PUBLIC " saveline  $0 " " sys; saveline="";next }
' |
sed 's/\">/\"/' > newcat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,share/sgml}

install sgml-common/* $RPM_BUILD_ROOT/usr/share/sgml
install newcat $RPM_BUILD_ROOT/usr/share/sgml/sgml-common.cat

install %{SOURCE1} $RPM_BUILD_ROOT/usr/bin

touch $RPM_BUILD_ROOT/usr/share/sgml/CATALOG

%post
/usr/bin/install-catalog --install sgml-common --version %{version}-%{release}

%preun
/usr/bin/install-catalog --remove sgml-common --version %{version}-%{release}

%files
%defattr(644, root, root, 755)
/usr/share/sgml/ISO*
/usr/share/sgml/sgml-common.cat
%attr(755, root, root) /usr/bin/install-catalog
%ghost /usr/share/sgml/CATALOG

%changelog
* Fri Oct  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.0-6]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added /usr/share/sgml/CATALOG to files as %ghost,
- %postun changed to %preun,
- simplification in %post and %preun,
- added full path to install-catalog in %post and %preun,
- install-catalog is now in separated Source#.

* Mon Sep 07 1998 Ziemek Borowski <ziembor@faq-bot.ziembor.waw.pl>
  [0.0-5]
- added pl translation,
- relocated libraries to /usr/share,
- normalized .spec.

* Mon Sep 07 1998 Mark Galassi <rosalia@cygnus.com>
  [0.0-4] 
- first release
