%include        /usr/lib/rpm/macros.perl
Summary:	ArchWay is a new advanced GUI for GNU Arch
Summary(pl):	ArchWay to nowy, zaawansowany GUI dla GNU Arch
Name:		archway
Version:	0.1.0
Release:	1
License:	GPL
Group:		Development/Version Control
Source0:	http://savannah.nongnu.org/download/archway/%{name}-%{version}.tar.gz
# Source0-md5:	6787692dbeb8cc3df3d089e552ad2622
URL:		http://www.nongnu.org/archway/
BuildRequires:	perl-Gtk2
BuildRequires:	rpm-perlprov
Requires:	tla
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ArchWay is a new advanced GUI for GNU Arch.

%description -l pl
ArchWay to nowy, zaawansowany graficzny interfejs użytkownika (GUI)
dla GNU Arch.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	PERL=%{_bindir}/perl

%{__perl} -pi -e "s#$RPM_BUILD_ROOT##g" \
	$RPM_BUILD_ROOT%{_bindir}/* \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/perllib/ArchWay/Session.pm

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
