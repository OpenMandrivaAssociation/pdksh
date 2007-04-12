Summary:	A public domain clone of the Korn shell (ksh)
Name:		pdksh
Version:	5.2.14
Release:	%mkrel 19
License:	Public Domain
Group:		Shells
URL:		http://www.cs.mun.ca/~michael/pdksh
Source:		ftp://ftp.cs.mun.ca/pub/pdksh/%name-%version.tar.bz2
Patch3:		pdksh-5.2.14-manloc.patch
# patch3 from rh
Patch4:		pdksh-5.2.14-debian.patch
# patch4 from debian and openbsd
BuildRoot:	%_tmppath/%name-%version-root
Prereq:		coreutils, grep, rpm-helper >= 0.7

%description
The pdksh package contains PD-ksh, a clone of the Korn shell (ksh).
The ksh shell is a command interpreter intended for both interactive
and shell script use.  Ksh's command language is a superset of the
sh shell language.

Install the pdksh package if you want to use a version of the ksh
shell.

%prep
%setup -q
%patch3 -p1
%patch4 -p1 -b .debian


%build
CFLAGS="%{optflags} -DDEBIAN" %configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{/bin,%_bindir,%_mandir/man1}

install -s -c -m755 ksh $RPM_BUILD_ROOT/bin/ksh
install -c -m644 ksh.1 $RPM_BUILD_ROOT%_mandir/man1/ksh.1
ln -sf ksh.1 $RPM_BUILD_ROOT%_mandir/man1/pdksh.1
ln -sf /bin/ksh $RPM_BUILD_ROOT%_bindir/ksh
ln -sf /bin/ksh $RPM_BUILD_ROOT%_bindir/pdksh


%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/share/rpm-helper/add-shell %name $1 /bin/ksh

%postun
/usr/share/rpm-helper/del-shell %name $1 /bin/ksh

%files
%defattr(-,root,root)
%doc README NOTES PROJECTS NEWS BUG-REPORTS
/bin/*
%_bindir/*
%_mandir/*/*


