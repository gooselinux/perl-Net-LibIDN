%define pkgname Net-LibIDN

Summary: 	Perl bindings for GNU LibIDN
Name: 		perl-Net-LibIDN
Version: 	0.12
Release: 	3%{?dist}
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/%{pkgname}/
Source:		http://search.cpan.org/CPAN/authors/id/T/TH/THOR/%{pkgname}-%{version}.tar.gz
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	libidn-devel >= 0.4.0, perl >= 5.8.0, perl(ExtUtils::MakeMaker)
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Provides perl bindings for GNU Libidn, a C library for
handling Internationalized Domain Names according to
IDNA (RFC 3490), in a way very much inspired by Turbo
Fredriksson's PHP-IDN.

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL PREFIX=$RPM_BUILD_ROOT%{_prefix} INSTALLDIRS=vendor
make %{?_smp_mflags}

# Change man page encoding into UTF-8
iconv -f latin1 -t utf-8 -o "blib/man3/Net::LibIDN.3pm.utf8" "blib/man3/Net::LibIDN.3pm"
mv -f "blib/man3/Net::LibIDN.3pm.utf8" "blib/man3/Net::LibIDN.3pm"

# Package is lacking GPL file
perldoc -t perlgpl > COPYING

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Artistic Changes COPYING README
%{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.12-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 03 2009 Robert Scheck <robert@fedoraproject.org> 0.12-1
- Upgrade to 0.12

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 0.11-2
- Rebuilt against gcc 4.4 and rpm 4.6

* Sun Jan 25 2009 Robert Scheck <robert@fedoraproject.org> 0.11-1
- Upgrade to 0.11

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.10-2
- Rebuild for new perl

* Sun Feb 10 2008 Robert Scheck <robert@fedoraproject.org> 0.10-1
- Upgrade to 0.10

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 0.09-4
- Updated the license tag according to the guidelines

* Mon May 07 2007 Robert Scheck <robert@fedoraproject.org> 0.09-3
- Rebuild

* Thu Apr 26 2007 Robert Scheck <robert@fedoraproject.org> 0.09-2
- Added build requirement to perl(ExtUtils::MakeMaker)

* Sun Sep 03 2006 Robert Scheck <robert@fedoraproject.org> 0.09-1
- Upgrade to 0.0.9 and rebuild for Fedora Core 6

* Fri Jun 23 2006 Robert Scheck <robert@fedoraproject.org> 0.08-5
- Changes to match with Fedora Packaging Guidelines (#193960)

* Sun Dec 25 2005 Robert Scheck <robert@fedoraproject.org> 0.08-4
- Rebuilt against gcc 4.1 and libidn 0.6.0

* Fri Apr 01 2005 Robert Scheck <robert@fedoraproject.org> 0.08-3
- Some spec file cleanup

* Mon Mar 14 2005 Robert Scheck <robert@fedoraproject.org> 0.08-2
- Rebuilt against gcc 4.0

* Thu Jan 20 2005 Robert Scheck <robert@fedoraproject.org> 0.08-1
- Upgrade to 0.0.8

* Sun Oct 03 2004 Robert Scheck <robert@fedoraproject.org> 0.07-2
- Use perl(:MODULE_COMPAT_*) as requirement for perl
- Lots of spec file cleanups

* Mon May 24 2004 Robert Scheck <robert@fedoraproject.org> 0.07-1
- Upgrade to 0.0.7

* Mon Apr 05 2004 Robert Scheck <robert@fedoraproject.org> 0.06-1
- Upgrade to 0.0.6
- Initial spec file for Red Hat Linux and Fedora Core
