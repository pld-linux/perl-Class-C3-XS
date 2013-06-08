#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	C3-XS
Summary:	Class::C3::XS - XS speedups for Class::C3
Summary(pl.UTF-8):	Class::C3::XS - przyspieszacze XS dla Class::C3
Name:		perl-Class-C3-XS
Version:	0.13
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92a48fe74206b803315749de29c30b88
URL:		http://search.cpan.org/dist/Class-C3-XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This contains XS performance enhancers for Class::C3 version 0.16 and
higher. The main Class::C3 package will use this package automatically
if it can find it. Do not use this package directly, use Class::C3
instead.

%description -l pl.UTF-8
Ten pakiet zawiera moduły XS przyspieszające Class::C3 w wersji 0.16 i
późniejszych. Główny pakiet Class::C3 używa tego pakietu automatycznie
jeśli go znajdzie. Nie należy używać go bezpośrednio, jedynie przez
Class::C3.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorarch}/Class/C3/*.pm
%dir %{perl_vendorarch}/Class/C3
%dir %{perl_vendorarch}/auto/Class/C3
%dir %{perl_vendorarch}/auto/Class/C3/XS
%{perl_vendorarch}/auto/Class/C3/XS/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Class/C3/XS/*.so
%{_mandir}/man3/*
