%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id xclear@as-computer.de
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

Name:           mozilla-xclear
Version:        1.8.2
Release:        1%{?dist}
Summary:        Xclear extension for Mozilla Firefox

Group:          Applications/Internet
License:        GPLv2
URL:            https://addons.mozilla.org/en/firefox/addon/xclear
Source0:        https://addons.cdn.mozilla.net/user-media/addons/13078/xclear-%{version}-fx+sm.xpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Adds a 'clear text' button to fields like the address bar and search.

%prep
%setup -q -c

%build

rm -rf %{buildroot}
install -Dp -m 644 %SOURCE0 %{buildroot}%{inst_dir}.xpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{inst_dir}.xpi

%changelog
* Fri Dec 2 2016 Chris Smart <csmart@kororaproject.org>- 1.8.2-1
- Update to 1.8.2

* Thu Jan 7 2016 Chris Smart <csmart@kororaproject.org>- 1.8.1-1
- Update to 1.8.1
- Use signed xpi from Mozilla so it works in Firefox 43

* Thu Sep 26 2013 Ian Firns <firnsy@kororaproject.org>- 1.8-2
- Updated upstream URL.

* Sun Dec 11 2011 Chris Smart <chris@kororaa.org>- 1.8.1
- Update to upstream 1.8 release.

* Sun Dec 11 2011 Chris Smart <chris@kororaa.org>- 1.6.1
- Update to upstream 1.6 release.

* Sun Aug 21 2011 Chris Smart <chris@kororaa.org>- 1.4-4
- Hack to enable in Firefox 8 and 9.

* Sun Aug 21 2011 Chris Smart <chris@kororaa.org>- 1.4-3
- Hack to enable in Firefox 6 and 7.

* Sat Jul 09 2011 Chris Smart <chris@kororaa.org>- 1.4-2
- Hack to enable in Firefox 5.

* Mon Mar 28 2011 Chris Smart <chris@kororaa.org>- 1.4-1
- Updated to 1.4, firefox4 compatible.

* Sat Mar 18 2011 Chris Smart <chris@kororaa.org>- 1.3-1
- Initial port.
