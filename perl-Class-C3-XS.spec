#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	C3-XS
Summary:	Class::C3::XS - XS speedups for Class::C3
#Summary(pl.UTF-8):	
Name:		perl-Class-C3-XS
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb19c19a2660f89765765c6c029184f1
URL:		http://search.cpan.org/dist/Class-C3-XS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This contains XS performance enhancers for Class::C3 version
0.16 and higher.  The main Class::C3 package will use this
package automatically if it can find it.  Do not use this
package directly, use Class::C3 instead.

The test suite here is not complete, although it does verify
a few basic things.  The best testing comes from running the
Class::C3 test suite *after* this module is installed.

This module won't do anything for you if you're running a
version of Class::C3 older than 0.16.  (It's not a
dependency because it would be circular with the optional
dep from that package to this one).



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
