%define upstream_name    AutoXS-Header
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Container for the AutoXS header files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is a simple container for the newest version of the the AutoXS
manpage header file 'AutoXS.h'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4mdv2012.0
+ Revision: 765072
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-3
+ Revision: 763488
- rebuilt for perl-5.14.x

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2
+ Revision: 654878
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 504581
- rebuild using %%perl_convert_version

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2010.0
+ Revision: 387750
- update to new version 1.02

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2010.0
+ Revision: 385208
- update to new version 1.01

* Mon May 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.00-1mdv2010.0
+ Revision: 377148
- update to new version 1.00

* Sun May 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 376592
- update to new version 0.06

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2010.0
+ Revision: 372678
- update to new version 0.05
- fixing source url, since this subdir does not exist on remote server

* Mon Dec 01 2008 Jérôme Quelin <jquelin@mandriva.org> 0.03-1mdv2009.1
+ Revision: 308838
- import perl-AutoXS-Header


* Mon Dec 01 2008 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist

