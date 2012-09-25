
Summary: Brackup wrapper scripts, supporting snapshots and monthly backups
Name: brackup-scripts
Version: 0.3.12
Release: 1%{?org_tag}%{dist}
Group: Applications/System
License: Artistic
URL: http://www.openfusion.net/tags/brackup
Source0: http://www.openfusion.com.au/labs/dist/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch
Requires: brackup
BuildRequires: /usr/bin/pod2man

%description
Brackup wrapper scripts, supporting snapshots, monthly backups, and 
arbitrary pre- and post-run scripts.

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/brackup
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_localstatedir}/www/brackup

install -m0644 conf/brackup-run.conf %{buildroot}%{_sysconfdir}/brackup
install -m0644 conf/brackup-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/brackup.conf
install -m0755 brackup-run %{buildroot}%{_bindir}
install -m0755 snap %{buildroot}%{_bindir}
/usr/bin/pod2man brackup-run > %{buildroot}%{_mandir}/man1/brackup-run.1

cd %{buildroot}%{_bindir} && ln -s snap unsnap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/brackup/brackup-run.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/brackup.conf
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/brackup-run*
%attr(0755,apache,apache) %{_localstatedir}/www/brackup

%changelog
* Tue Sep 25 2012 Gavin Carr <gavin@openfusion.com.au> 0.3.12-1
- Fix message typo in snap fix.

* Tue Sep 25 2012 Gavin Carr <gavin@openfusion.com.au> 0.3.11-1
- Fix bug with snap script not checking for run3 failures correctly.

* Mon Nov 28 2011 Gavin Carr <gavin@openfusion.com.au> 0.3.10-1
- Fix buglet with run_dir change.

* Mon Nov 28 2011 Gavin Carr <gavin@openfusion.com.au> 0.3.9-1
- Allow run_dir to be set in brackup-run.conf.

* Tue Oct 04 2011 Gavin Carr <gavin@openfusion.com.au> 0.3.8-1
- Fix buglet in brackup-run script if snapshot size specified.

* Fri Jul 01 2011 Gavin Carr <gavin@openfusion.com.au> 0.3.7-1
- Suppress bogus(?) LVM file descriptor warning in snap/unsnap.

* Tue Jan 25 2011 Gavin Carr <gavin@openfusion.com.au> - 0.3.6-1
- Tweak brackup-run monthly url content handling to make more robust.

* Mon Jan 17 2011 Gavin Carr <gavin@openfusion.com.au> - 0.3.5-2
- Add %dist tag back to spec file due to rhel6 incompatibilities.

* Fri Jan 14 2011 Gavin Carr <gavin@openfusion.com.au> - 0.3.5-1
- Remove %dist tag from spec file, since nothing distro-specific.

* Fri Nov 26 2010 Gavin Carr <gavin@openfusion.com.au> - 0.3.4-1
- Allow brackup-run snapshot,monthly{,_url} to be set per source.

* Fri Nov 26 2010 Gavin Carr <gavin@openfusion.com.au> - 0.3.3-1
- Add /var/www/brackup directory creation.

* Sun Nov 14 2010 Gavin Carr <gavin@openfusion.com.au> - 0.3.2-1
- Migrate snap from IPC::Run to IPC::Run3.

* Thu Nov 11 2010 Gavin Carr <gavin@openfusion.com.au> - 0.3.1-1
- Fix buglet in snap mount table handling.

* Mon Sep 20 2010 Gavin Carr <gavin@openfusion.com.au> - 0.3-1
- Add support for pre_run and post_run scripts to brackup-run.
- Add initial perldoc to brackup-run.

* Sun Sep 19 2010 Gavin Carr <gavin@openfusion.com.au> - 0.2-1
- Add brackup-httpd.conf.

* Sun Sep 19 2010 Gavin Carr <gavin@openfusion.com.au> - 0.1-1
- Initial package.
