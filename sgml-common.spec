Summary:	Common SGML catalog and DTD files
Summary(pl):	Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:		sgml-common
Version:	0.6.3
Release:	1
License:	distributable
##Copyright:	(C) International Organization for Standardization 1986
URL:		http://www.iso.ch/cate/3524030.html
Group:		Applications/Publishing/SGML
Source0:	ftp://ftp.kde.org/pub/kde/devel/docbook/SOURCES/%{name}-%{version}.tgz
Patch0:		%{name}-chmod.patch
BuildArch:	noarch
BuildRequires:	/usr/bin/xmlcatalog
Provides:	iso-entities
Provides:	iso-entities-8879.1986
Provides:	sgml-catalog
Requires(post,preun): /usr/bin/xmlcatalog
Requires:	sed
Requires:	grep
Requires:	fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		xml_catalog %{_datadir}/sgml/xml-iso-entities-8879.1986/catalog.xml

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

%build
%{__autoconf}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

xmlcatalog --noout --create $RPM_BUILD_ROOT%{xml_catalog}
grep PUBLIC $RPM_BUILD_ROOT/%{_datadir}/sgml/xml-iso-entities-8879.1986/catalog|sed 's/^/xmlcatalog --noout --add /;s/PUBLIC/public/;s=$= '$RPM_BUILD_ROOT'/%{xml_catalog}=' |sh

rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

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
if ! grep -q /etc/sgml/xml-iso-entities-8879.1986.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/xml-iso-entities-8879.1986.cat /usr/share/sgml/xml-iso-entities-8879.1986/catalog > /dev/null
fi
if ! grep -q %{xml_catalog} /etc/xml/catalog ; then
	/usr/bin/xmlcatalog --noout --add nextCatalog "" %{xml_catalog} /etc/xml/catalog
fi

%preun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-iso-entities-8879.1986.cat /usr/share/sgml/sgml-iso-entities-8879.1986/catalog > /dev/null
	/usr/bin/install-catalog --remove /etc/sgml/xml-iso-entities-8879.1986.cat /usr/share/sgml/xml-iso-entities-8879.1986/catalog > /dev/null
	/usr/bin/xmlcatalog --noout --del %{xml_catalog} /etc/xml/catalog
fi 

%files
%defattr(644,root,root,755)
%doc doc/HTML/*
%config %{_sysconfdir}/sgml
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sgml
%{_mandir}/*/*
