Summary:	Common SGML catalog and DTD files
Summary(pl):	Opisane w normie ISO 8879/1986 katalogi i DTD SGMLowe
Name:		sgml-common
Version:	0.2
Release:	7
Vendor:		Cygnus Solutions -- UNSUPPORTED
Source0:	sgml-common.tgz
Source1:	fix-sgml-catalog
Source2:	iso-entities.cat
Copyright:	(C) International Organization for Standardization 1986
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
BuildArch:	noarch
Provides:	iso-entities, iso-entities-8879.1986, sgml-catalog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sgml-common is a collection of entities and dtds that are useful for SGML
processing, but shouldn't need to be included in multiple packages. It also
includes an up-to-date Open Catalog file.

%description -l pl
sgml-common jest zestawem wspólnych dla wiêkszo¶ci aplikacji SGMLa
(bo opisanych w normie ISO 8879/1986) encji i DTD. Poza tym zawiera
aktualizowany przy dodawaniu nowych pakietów  plik CATALOG oraz instalator
nowych DTD.

%prep
%setup -c -q 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/{iso-entities-8879.1986,catalogs}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}

install sgml-common/* $RPM_BUILD_ROOT%{_datadir}/sgml/iso-entities-8879.1986
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/sgml/iso-entities-8879.1986
ln -s ../iso-entities-8879.1986/iso-entities.cat $RPM_BUILD_ROOT%{_datadir}/sgml/catalogs/


touch $RPM_BUILD_ROOT%{_datadir}/sgml/CATALOG

%post
%{_sbindir}/fix-sgml-catalog

#%postun
#if [ "$1" = "0" ]; then
#	%{_sbindir}/install-catalog --remove sgml-common --version %{version}-%{release}
#fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/sgml
%dir %{_datadir}/sgml/catalogs
%{_datadir}/sgml/iso-entities-8879.1986
%{_datadir}/sgml/catalogs/*
%attr(755,root,root) %{_sbindir}/*
%ghost %{_datadir}/sgml/CATALOG
