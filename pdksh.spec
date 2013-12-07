Summary:	A public domain clone of the Korn shell (ksh)
Name:		pdksh
Version:	5.2.14
Release:	33
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 5.2.14-30mdv2011.0
+ Revision: 667018
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 5.2.14-29mdv2011.0
+ Revision: 607086
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 5.2.14-28mdv2010.1
+ Revision: 523612
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 5.2.14-27mdv2010.0
+ Revision: 426395
- rebuild

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 5.2.14-26mdv2009.1
+ Revision: 366026
- fix str fmt

  + Frederic Crozat <fcrozat@mandriva.com>
    - Explicitly provides /usr/bin/ksh

* Wed Sep 24 2008 Funda Wang <fwang@mandriva.org> 5.2.14-25mdv2009.0
+ Revision: 287677
- fix bad nzombie for glibc 2.8
- drop old spec file

* Sat Sep 06 2008 Funda Wang <fwang@mandriva.org> 5.2.14-24mdv2009.0
+ Revision: 281794
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 5.2.14-23mdv2009.0
+ Revision: 223495
- rebuild

* Sun Mar 16 2008 Funda Wang <fwang@mandriva.org> 5.2.14-22mdv2008.1
+ Revision: 188131
- fix symbolic link to /bin/ksh

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 5.2.14-21mdv2008.1
+ Revision: 179163
- rebuild
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Aug 16 2007 Adam Williamson <awilliamson@mandriva.org> 5.2.14-20mdv2008.0
+ Revision: 64058
- use Fedora license policy
- From Fredrik Himpe:
  	- update Debian patch to latest version to fix #30308
  	- add D_FILE_OFFSET_BITS=64 to CFLAGS to support files >2GB


* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 5.2.14-19mdv2007.0
+ Revision: 120049
- Import pdksh

* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 5.2.14-19mdv2007.1
- Rebuild, %%mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.2.14-18mdk
- Rebuild

* Sat Apr 16 2005 Claudio Matsuoka <claudio@mandriva.com> 5.2.14-17mdk
- added a collection of patches from OpenBSD and Debian, providing
  command line completion with escape sequences, secure tempfile
  creation and proper alignment for IA64.
- redundant patches commented out

* Fri Aug 20 2004 Stew Benedict <sbenedict@mandrakesoft.com> 5.2.14-16mdk
- rebuild

