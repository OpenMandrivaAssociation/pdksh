Summary:	A public domain clone of the Korn shell (ksh)
Name:		pdksh
Version:	5.2.14
Release:	%mkrel 30
License:	Public Domain and BSD-like and GPLv2+
Group:		Shells
URL:		http://www.cs.mun.ca/~michael/pdksh
Source:		ftp://ftp.cs.mun.ca/pub/pdksh/%{name}-%{version}.tar.bz2
Patch0:		pdksh-5.2.14-manloc.patch
# debian patch
Patch1:		pdksh-5.2.14-debian.patch
Patch2:		pdksh-child_max.patch
Patch3:		pdksh-5.2.14-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	/usr/bin/ksh

%description
The pdksh package contains PD-ksh, a clone of the Korn shell (ksh).
The ksh shell is a command interpreter intended for both interactive
and shell script use.  Ksh's command language is a superset of the
sh shell language.

Install the pdksh package if you want to use a version of the ksh
shell.

%prep
%setup -q
%patch0 -p1 -b .manloc
%patch1 -p1 -b .debian
%patch2 -p1 -b .jobs
%patch3 -p0 -b .str

%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DDEBIAN " %configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
# Move ksh to /bin and create a symlink in /usr/bin
mkdir -p %{buildroot}/bin
mv %{buildroot}%{_bindir}/ksh %{buildroot}/bin/ksh
ln -s /bin/ksh %{buildroot}%{_bindir}/ksh
# Create symlinks for pdksh
ln -s /bin/ksh %{buildroot}%{_bindir}/pdksh
ln -s ksh.1 %{buildroot}%{_mandir}/man1/pdksh.1

%post
/usr/share/rpm-helper/add-shell %{name} $1 /bin/ksh

%postun
/usr/share/rpm-helper/del-shell %{name} $1 /bin/ksh

%files
%defattr(-,root,root)
%doc LEGAL README NOTES PROJECTS NEWS BUG-REPORTS
/bin/ksh
%{_bindir}/ksh
%{_bindir}/pdksh
%{_mandir}/*/*
