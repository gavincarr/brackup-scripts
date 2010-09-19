
Summary: Brackup wrapper scripts, supporting snapshots and monthly backups
Name: brackup-scripts
Version: 0.2
Release: 1%{?org_tag}%{?dist}
Group: Applications/System
License: Artistic
URL: http://www.openfusion.net/tags/brackup
Source0: http://www.openfusion.com.au/labs/dist/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Brackup wrapper scripts, supporting snapshots, monthly backups, and 
arbitrary pre- and post-run scripts.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_bindir}

install -m0644 conf/brackup-run.conf %{buildroot}%{_sysconfdir}
install -m0644 conf/brackup-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/brackup.conf
install -m0755 brackup-run %{buildroot}%{_bindir}
install -m0755 snap %{buildroot}%{_bindir}

%files
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/*conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/httpd/conf.d/brackup.conf
%attr(0755,root,root) %{_bindir}/*

%changelog
* Sun Sep 19 2010 Gavin Carr <gavin@openfusion.com.au> - 0.2-1
- Add brackup-httpd.conf.

* Sun Sep 19 2010 Gavin Carr <gavin@openfusion.com.au> - 0.1-1
- Initial package.
