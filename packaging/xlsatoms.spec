Name:           xlsatoms
Version:        1.1.1
Release:        0
License:        MIT
Summary:        Utility to list interned atoms defined on an X11 server
Url:            http://xorg.freedesktop.org/
Group:          Graphics/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1001: 	xlsatoms.manifest
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
%description
xlsatoms lists the interned atoms defined on an X11 server.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1%{?ext_man}

%changelog
