%define upstream_name    AutoXS-Header
%define upstream_version 1.02

Summary:	Container for the AutoXS header files
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
This module is a simple container for the newest version of the the AutoXS
manpage header file 'AutoXS.h'.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

