%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Common
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - PEAR::HTML_Common is a base class for other HTML classes
Summary(pl):	%{_pearname} - PEAR::HTML_Common jest podstawow± klas± dla innych klas HTML
Name:		php-pear-%{_pearname}
Version:	1.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6147e6d0c37d8a8110f3373b593c0094
URL:		http://pear.php.net/package/HTML_Common/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

%description -l pl
Klasa PEAR::HTML_Common dostarcza metody do wy¶wietlania kodu HTML
oraz obs³ugê atrybutów.
- Zawiera metody do ustawiania, usuwania, aktualizacji atrybutów HTML.
- Obs³uguje komentarze w kodzie HTML.
- Obs³uguje u³o¿enie i tabulacje dla ³adniejszego wygl±du kodu HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
