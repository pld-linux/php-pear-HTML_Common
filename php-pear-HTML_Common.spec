%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PEAR::HTML_Common is a base class for other HTML classes
Summary(pl.UTF-8):   %{_pearname} - PEAR::HTML_Common jest podstawową klasą dla innych klas HTML
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3598dd20e3be90ae445501e9c2d59506
URL:		http://pear.php.net/package/HTML_Common/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Common package provides methods for HTML code display
and attributes handling:
- Methods to set, remove, update HTML attributes.
- Handles comments in HTML code.
- Handles layout and tabs for nicer HTML code.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::HTML_Common dostarcza metody do wyświetlania kodu HTML
oraz obsługę atrybutów.
- Zawiera metody do ustawiania, usuwania, aktualizacji atrybutów HTML.
- Obsługuje komentarze w kodzie HTML.
- Obsługuje ułożenie i tabulacje dla ładniejszego wyglądu kodu HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
