Summary: Sys-Syslog Perl module
Name: perl-Sys-Syslog
Version: 0.18
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Sys-Syslog/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Sys-Syslog-0.18.tar.gz

%description
Sys-Syslog Perl module

%description
Sys-Syslog Perl module
%prep
%setup -q -n Sys-Syslog-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > Sys-Syslog-%{version}-filelist
if [ "$(cat Sys-Syslog-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Sys-Syslog-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

