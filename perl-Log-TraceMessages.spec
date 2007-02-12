#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	TraceMessages
Summary:	Log::TraceMessages - Perl extension for trace messages used in debugging
Summary(pl.UTF-8):   Log::TraceMessages - rozszerzenie Perla do śledzenia komunikatów
Name:		perl-Log-TraceMessages
Version:	1.4
Release:	1
# same as perl (REMOVE THIS LINE IF NOT TRUE)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	77687c9858a476628f0299cf4f29c727
BuildRequires:	perl-HTML-FromText
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a slightly better way to put trace statements into your
code than just calling print(). It provides an easy way to turn trace
on and off for particular sections of code without having to comment
out bits of source.

%description -l pl.UTF-8
Ten moduł to nieco lepszy sposób umieszczania instrukcji do śledzenia
we własnym kodzie niż zwykłe wywoływanie print(). Udostępnia on łatwy
sposób włączania i wyłączania śledzenia dla różnych sekcji kodu bez
potrzeby zamiany na komentarze kawałków kodu źródłowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%dir %{perl_vendorlib}/auto/Log
%dir %{perl_vendorlib}/auto/Log/TraceMessages
%{perl_vendorlib}/auto/Log/TraceMessages/autosplit.ix
%{_mandir}/man3/*
