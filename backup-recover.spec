Name:       backup-recover		
Version:	3.2
Release:	1%{?dist}.1
Summary:	Backup and recover the server system for NfsChina.

Group:		System Environment/Base
License:	GPLv2
URL:		http://www.nfs-china.com/index.html
Source0:	%{name}-%{?version}.tar.gz
Source1:	nfsbr.iso
#Source2 is the source code of GUI interface in nfsbr.iso.
Source2:	nfs-backup-recovery-1.0.tar.gz

Requires: grub2-tools

%description
Backup and recover the server system for NfsChina.

%global _rootbuilddir %{_builddir}/%{name}-%{?version}

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/recovery/efi-script
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grub.d/

install -m 755  %{SOURCE1} $RPM_BUILD_ROOT/recovery
install -m 755  %{_rootbuilddir}/check_file.sh $RPM_BUILD_ROOT/recovery
install -m 755  %{_rootbuilddir}/efi-script/* $RPM_BUILD_ROOT/recovery/efi-script

install -m 755  %{_rootbuilddir}/00_header_backup.efi $RPM_BUILD_ROOT%{_sysconfdir}/grub.d/00_header_backup
install -m 755  %{_rootbuilddir}/50_custom_backup.efi $RPM_BUILD_ROOT%{_sysconfdir}/grub.d/50_custom_backup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license
%doc README
/recovery/nfsbr.iso
/recovery/efi-script/*
/recovery/check_file.sh
%{_sysconfdir}/grub.d/00_header_backup
%{_sysconfdir}/grub.d/50_custom_backup

%changelog
* Wed Jul 29 2020 Zhang Tao <zhangtao@cpu-os.ac.cn> - 3.2-1.nfs.1
- Adapt to nfs server system 4.0 and centos 8.
- Add backup and recover system menuentry in grub.cfg.
