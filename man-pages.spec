#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : man-pages
Version  : 4.12
Release  : 37
URL      : https://www.kernel.org/pub/linux/docs/man-pages/man-pages-4.12.tar.xz
Source0  : https://www.kernel.org/pub/linux/docs/man-pages/man-pages-4.12.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Distributable
Requires: man-pages-doc
Requires: man-db
BuildRequires : groff
BuildRequires : man-db
BuildRequires : util-linux
Patch1: build.patch

%description
This package contains Linux man pages for sections 1 through 8.  Some
more information is given in the 'man-pages-x.y.Announce' file.

%package doc
Summary: doc components for the man-pages package.
Group: Documentation

%description doc
doc components for the man-pages package.


%prep
%setup -q -n man-pages-4.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500664232
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check-groff-warnings

%install
export SOURCE_DATE_EPOCH=1500664232
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man2/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man4/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man6/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*
%exclude /usr/share/man/man2/fgetxattr.2
%exclude /usr/share/man/man2/flistxattr.2
%exclude /usr/share/man/man2/fremovexattr.2
%exclude /usr/share/man/man2/fsetxattr.2
%exclude /usr/share/man/man2/getxattr.2
%exclude /usr/share/man/man2/lgetxattr.2
%exclude /usr/share/man/man2/listxattr.2
%exclude /usr/share/man/man2/llistxattr.2
%exclude /usr/share/man/man2/lremovexattr.2
%exclude /usr/share/man/man2/lsetxattr.2
%exclude /usr/share/man/man2/removexattr.2
%exclude /usr/share/man/man2/setxattr.2
%exclude /usr/share/man/man3/getspnam.3
%exclude /usr/share/man/man5/passwd.5
%exclude /usr/share/man/man7/keyrings.7
%exclude /usr/share/man/man7/persistent-keyring.7
%exclude /usr/share/man/man7/process-keyring.7
%exclude /usr/share/man/man7/session-keyring.7
%exclude /usr/share/man/man7/thread-keyring.7
%exclude /usr/share/man/man7/user-keyring.7
%exclude /usr/share/man/man7/user-session-keyring.7
