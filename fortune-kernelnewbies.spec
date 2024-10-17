%define name fortune-kernelnewbies
%define version 20060120
%define release 7

Summary: The best IRC moments by kernel hacker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: kernelnewbies-fortunes.tar.bz2
License: GPL
Group: Toys
URL: https://kernelnewbies.org/kernelnewbies-fortunes.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: fortune-mod

%description
The best "famous word" of famous kernel hackers.

%prep
%setup -q -c %name

%build
# nothing to do

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_datadir/games/fortunes
install -m 644 kernelnewbies $RPM_BUILD_ROOT/%_datadir/games/fortunes/
install -m 644 kernelnewbies.dat $RPM_BUILD_ROOT/%_datadir/games/fortunes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_datadir/games/fortunes/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20060120-6mdv2011.0
+ Revision: 618334
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20060120-5mdv2010.0
+ Revision: 428877
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20060120-4mdv2009.0
+ Revision: 245326
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060120-3mdv2009.0
+ Revision: 239586
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060120-1mdv2008.1
+ Revision: 125192
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 24 2007 trem <trem@mandriva.org> 20060120-1mdv2007.1
+ Revision: 148718
- Import fortune-kernelnewbies

* Sat Feb 25 2006 trem <trem@mandriva.org> 20060120-1mdk
- last modified 2006/01/20

* Sun Dec 04 2005 trem <trem@zarb.org> 20051003-1mdk
- First beautifull and wonderfull package for contrib

