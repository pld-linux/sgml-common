Summary:	Common SGML catalog and DTD files
Summary(pl):	Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:		sgml-common
Version:	0.5
Release:	8
License:	Distibutable
##Copyright:	(C) International Organization for Standardization 1986
URL:		http://www.iso.ch/cate/3524030.html
Group:		Applications/Publishing/SGML
Source0:	ftp://ftp.kde.org/pub/kde/devel/docbook/SOURCES/%{name}-%{version}.tgz
Source1:	%{name}-CHANGES
Patch0:		%{name}-oldsyntax.patch
Patch1:		%{name}-quiet.patch
Patch2:		%{name}-chmod.patch
BuildArch:	noarch
Provides:	iso-entities, iso-entities-8879.1986, sgml-catalog
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
install iso-entities/{*.ent,catalog} $RPM_BUILD_ROOT%{_datadir}/sgml/sgml-iso-entities-8879.1986
install bin/* $RPM_BUILD_ROOT%{_bindir}/
install config/* $RPM_BUILD_ROOT%{_sysconfdir}/sgml/
install doc/man/*.8 $RPM_BUILD_ROOT/%{_mandir}/man8/
install %{SOURCE1} CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Update the centralized catalog
/usr/bin/install-catalog --add /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null

%preun
/usr/bin/install-catalog --remove /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null

%files
%defattr(644,root,root,755)
%config %{_sysconfdir}/sgml
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sgml
%{_mandir}/*/*
