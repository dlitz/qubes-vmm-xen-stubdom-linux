%{!?version: %define version %(cat version)}
%if 0%{?qubes_builder}
%define _builddir %(pwd)
%endif

Name: xen-hvm-stubdom-linux
Version: %{version}
Release: 1%{?dist}
Summary: Linux stubdom files for Xen

Group: System
License: GPL
URL: https://www.qubes-os.org/

BuildRequires: quilt

# genext2fs
BuildRequires: autoconf
BuildRequires: automake

# QEMU
BuildRequires: python

# QEMU Qubes gui-agent
BuildRequires: qubes-gui-common-devel
BuildRequires: qubes-kernel-vm-support

#TODO: BuildRequires

%description
This package contains the files (i.e. kernel and rootfs) for a Linux based
stubdom.


%build
make -f Makefile.stubdom %{?_smp_mflags}


%install
make -f Makefile.stubdom DESTDIR=${RPM_BUILD_ROOT} install


%files
/usr/lib/xen/boot/stubdom-linux-rootfs
/usr/lib/xen/boot/stubdom-linux-kernel


%changelog
