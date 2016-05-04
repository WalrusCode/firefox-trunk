AutoReqProv: no

##Init variables

%global currenf 48.0a1
%global _optdir /opt
%global packver 48
%ifarch x86_64
%global arch x86_64
%else
%global arch i686
%endif

##Package Version and Licences

Summary: Firefox Nightly 48 RPM Build
Name: firefox-48
Version: 48
Release: 0a1_%(date +%%y%%m%%d)%{?dist}
License: MPLv1.1 or GPLv2+ or LGPLv2+
Group: Applications/Internet
URL: http://www.nightly.mozilla.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

##DEPS
BuildRequires: wget tar

Requires: alsa-lib libX11 libXcomposite libXdamage libnotify libXt libXext glib2 dbus-glib libjpeg-turbo cairo-gobject libffi fontconfig freetype libgcc gtk3 gtk2 hunspell zlib
Requires: nspr >= 4.10.8
Requires: nss >= 3.19.2
Requires: sqlite >= 3.8.10.2


##Description for Package

%description
This package is a legacy package built from Mozilla's Final Nightly of Firefox 48. This package will only be updated if neccesary.

%prep

##Build Instructions

%build
wget -c --no-check-certificate -P %{_builddir} https://ftp.mozilla.org/pub/firefox/nightly/2016/04/2016-04-25-03-05-48-mozilla-central/firefox-%{currenf}.en-US.linux-%{arch}.tar.bz2
tar -jxvf firefox-%{currenf}.en-US.linux-*.tar.bz2  -C %{_builddir}

## Install Instructions

%install

install -dm 755 %{buildroot}/usr/{bin,share/{applications,icons/hicolor/128x128/apps},opt}
install -dm 755 %{buildroot}/%{_optdir}/firefox-48/browser/defaults/preferences/

install -m644 %{_builddir}/firefox/browser/icons/mozicon128.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/firefox-48.png

cp -rf %{_builddir}/firefox/* %{buildroot}/opt/firefox-48/
ln -s /opt/firefox-48/firefox %{buildroot}/usr/bin/firefox-48

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF

## Desktop File

[Desktop Entry]
Version=48.0a1
Name=Nightly
GenericName=Firefox Nightly 48
Comment=Browse the Web
Exec=firefox-48 %u
Icon=firefox-48.png
Terminal=false
Type=Application
MimeType=text/html;text/xml;application/xhtml+xml;application/vnd.mozilla.xul+xml;text/mml;x-scheme-handler/http;x-scheme-handler/https;
Categories=Network;WebBrowser;
Keywords=web;browser;internet;
EOF
## Disable Update Alert
echo '// Disable Update Alert
pref("app.update.enabled", false);' > %{buildroot}/opt/firefox-48/browser/defaults/preferences/vendor.js

##Cleanup

%clean
rm -rf $RPM_BUILD_ROOT

##Installed Files

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_optdir}/firefox-48/
