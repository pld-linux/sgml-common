Summary:     Common SGML catalog and DTD files
Summary(pl): Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:        sgml-common
Version:     0.2
Release:     1pld
Vendor:      Cygnus Solutions -- UNSUPPORTED
Source0:     sgml-common.tgz
Source1:     install-catalog
Source2:	sgml.sh
Source3:	sgml.csh
Source4:	iso-entities.cat
Source5:	sgml-common.cat
Copyright:   (C) International Organization for Standardization 1986
Group:  Applications/Publishing/SGML
Group(pl):      Aplikacje/Publikowanie/SGML
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/profile.d
install -d $RPM_BUILD_ROOT/usr/{sbin,share/sgml,share/sgml/iso-entities-8879.1986,lib}

install %{SOURCE1} $RPM_BUILD_ROOT/usr/sbin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
install %{SOURCE3} $RPM_BUILD_ROOT/etc/profile.d


install sgml-common/* $RPM_BUILD_ROOT/usr/share/sgml/iso-entities-8879.1986
install %{SOURCE4} $RPM_BUILD_ROOT/usr/share/sgml/iso-entities-8879.1986
install %{SOURCE5} $RPM_BUILD_ROOT/usr/share/sgml

cd $RPM_BUILD_ROOT/usr/lib 
ln -s ../share/sgml 
touch $RPM_BUILD_ROOT/usr/share/sgml/CATALOG

%post
/usr/sbin/install-catalog --install sgml-common --version %{version}-%{release}

%preun
/usr/sbin/install-catalog --remove sgml-common --version %{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%dir /usr/share/sgml
/usr/share/sgml/iso-entities-8879.1986
/usr/share/sgml/sgml-common.cat
%attr(755, root, root) /usr/sbin/install-catalog
%ghost /usr/share/sgml/CATALOG
%config /etc/profile.d 

%changelog
* Thu Jan 07 1999 Ziemek Borowski <zmb@faq-bot.ziembor.waw.pl> 
[1.0-1] 
- install-catalog moved to /usr/sbin 
- added files: /etc/profile/sgml.{sh,csh} 
- version from 0.0 to 0.2 

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
