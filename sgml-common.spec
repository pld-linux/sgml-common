Summary:	Common SGML catalog and DTD files
Summary(pl):	Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:		sgml-common
Version:	0.5
Release:	9
License:	distributable
##Copyright:	(C) International Organization for Standardization 1986
URL:		http://www.iso.ch/cate/3524030.html
Group:		Applications/Publishing/SGML
Source0:	ftp://ftp.kde.org/pub/kde/devel/docbook/SOURCES/%{name}-%{version}.tgz
Source1:	%{name}-CHANGES
Source2:	sgml-iso-ent-fix
Patch0:		%{name}-oldsyntax.patch
Patch1:		%{name}-quiet.patch
Patch2:		%{name}-chmod.patch
BuildArch:	noarch
Provides:	iso-entities
Provides:	iso-entities-8879.1986
Provides:	sgml-catalog
Requires:	sed
Requires:	grep
Requires:	fileutils
Conflicts:	docbook-dtd41-sgml < 1.0-13
Conflicts:	docbook-dtd31-sgml < 1.0-13
Conflicts:	docbook-dtd30-sgml < 1.0-15
Conflicts:	docbook-style-dsssl < 1.77-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sgml-common is a collection of entities and dtds that are useful for
SGML processing, but shouldn't need to be included in multiple
packages. It also includes an up-to-date Open Catalog file.

%description -l pl
sgml-common jest zestawem wspólnych dla wiêkszo¶ci aplikacji SGMLa (bo
opisanych w normie ISO 8879/1986) encji i DTD. Poza tym zawiera
aktualizowany przy dodawaniu nowych pakietów katalog SGML oraz
instalator nowych DTD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_sysconfdir}/sgml} \
	$RPM_BUILD_ROOT%{_datadir}/sgml/{sgml-iso-entities-8879.1986,docbook}

install *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml
cd iso-entities
for ent in *.ent catalog ; do
  cat $ent | sh %{SOURCE2} >$RPM_BUILD_ROOT%{_datadir}/sgml/sgml-iso-entities-8879.1986/$ent
done
cd ..
install bin/* $RPM_BUILD_ROOT%{_bindir}/
install config/* $RPM_BUILD_ROOT%{_sysconfdir}/sgml/
install doc/man/*.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install %{SOURCE1} CHANGES
install %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- sgml-common < 0.5-9 
if ! grep -q /etc/sgml/sgml-iso-entities-8879.1986.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
fi 

%post
if ! grep -q /etc/sgml/sgml-iso-entities-8879.1986.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
fi 

%preun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
fi 

%files
%defattr(644,root,root,755)
%config %{_sysconfdir}/sgml
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sgml
%{_mandir}/*/*
