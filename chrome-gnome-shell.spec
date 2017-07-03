%global debug_package %{nil}

Name:           chrome-gnome-shell
Version:        9
Release:        1%{?dist}
Summary:        Support for managing GNOME Shell Extensions through web browsers

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  /usr/bin/base64
BuildRequires:  /usr/bin/head
BuildRequires:  /usr/bin/jq
BuildRequires:  /usr/bin/sha256sum
BuildRequires:  /usr/bin/tr

Requires:       dbus
Requires:       gnome-icon-theme
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Requires:       mozilla-filesystem
Requires:       python-gobject-base
Requires:       python-requests

%description
Browser extension for Google Chrome/Chromium, Firefox, Vivaldi, Opera (and
other Browser Extension, Chrome Extension or WebExtensions capable browsers)
and native host messaging connector that provides integration with GNOME Shell
and the corresponding extensions repository https://extensions.gnome.org.

%prep
%autosetup

%build
mkdir build
pushd build
  %cmake -DBUILD_EXTENSION=OFF \
         -DCMAKE_INSTALL_LIBDIR=%{_lib} \
         -DPython_ADDITIONAL_VERSIONS=2 \
         ..
  %make_build
popd

%install
pushd build
  %make_install
popd

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop

%files
%license LICENSE
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/chrome-gnome-shell
%{_libdir}/mozilla/native-messaging-hosts/
%{python_sitelib}/chrome_gnome_shell-*.egg-info
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_datadir}/icons/gnome/*/apps/org.gnome.ChromeGnomeShell.png

%changelog
* Thu Jun 22 2017 Pete Walter <pwalter@fedoraproject.org> - 9-1
- Update to 9

* Fri Mar 10 2017 Pete Walter <pwalter@fedoraproject.org> - 8.2-2
- Package review fixes (#1343710)
- Validate the desktop file
- Don't own /etc/opt directory
- Depend on mozilla-filesystem instead of co-owning mozilla directories
- Depend on dbus and gnome-icon-theme/hicolor-icon-theme for directory
  ownership

* Fri Mar 03 2017 Pete Walter <pwalter@fedoraproject.org> - 8.2-1
- Update to 8.2
- Simplify files list
- Build with Python 3 (#1343710)
- Add missing python3-requests dependency (#1343710)
- Update package description

* Tue Jun 07 2016 Pete Walter <pwalter@fedoraproject.org> - 6.1-1
- Update to 6.1

* Sat May 14 2016 Maxim Orlov <murmansksity@gmail.com> - 6-1
- Update to Ver.6
- Fix "orphaned directory"

* Mon Apr 11 2016 Maxim Orlov <murmansksity@gmail.com> - 5.2-1
- Initial package.
