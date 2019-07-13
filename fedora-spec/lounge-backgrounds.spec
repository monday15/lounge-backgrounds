Name:           lounge-backgrounds
Version:        1.0
Release:        1%{?dist}
Summary:        Dynamic background for gnome desktop

License:        GPLv2+
License:        Unsplash

URL:            https://github.com/monday15/lounge-backgrounds
Source0:        https://github.com/monday15/lounge-backgrounds/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson >= 0.41.0

%description
%{summary}

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE LICENSE-Unsplash COPYRIGHT
%doc README.md
%{_datadir}/backgrounds/lounge/*
%{_datadir}/gnome-background-properties/lounge.xml

%changelog
* Sat Jul 13 2019 Alex Monday <monday15@gmx.com>
- Initial package
