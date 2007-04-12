%define name fortune-kernelnewbies
%define version 20060120
%define release %mkrel 1

Summary: The best IRC moments by kernel hacker
Name: %{name}
Version: %{version}
Release: %{release}
Source0: kernelnewbies-fortunes.tar.bz2
License: GPL
Group: Toys
URL: http://kernelnewbies.org/kernelnewbies-fortunes.tar.gz
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


