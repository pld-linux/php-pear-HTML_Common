%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - PEAR::HTML_Common is a base class for other HTML classes
Summary(pl):	%{_class}_%{_subclass} - PEAR::HTML_Common jest podstawow� klas� dla innych klas HTML
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Common package provides methods for html code display
and attributes handling.
- Methods to set, remove, update html attributes.
- Handles comments in HTML code.
- Handles layout and tabs for nicer HTML code.

%description -l pl
Klasa PEAR::HTML_Common dostarcza metody do wy�wietlania kodu html
oraz obs�ug� atrybut�w.
- metody do ustawiania, usuwania, aktualizacji atrybut�w html.
- manipulacje komentarzami w kodzie HTML.
- manipulacje wygl�dem oraz tabsami dla �adniejszego wygl�du kodu HTML.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
