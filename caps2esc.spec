Name:       caps2esc
Version:    1.3
Release:    1%{?dist}
Summary:    Transforming the most useless key ever in the most useful one

License:    GPLv3+
URL:        https://github.com/oblitum/caps2esc
Source0:    %{name}.c
Source1:    %{name}.service

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  libevdev-devel
BuildRequires:  libgudev-devel


%description
Rebind Capskey to ESC or CTRL.


%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
cd %{name}-%{version}
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
chmod -Rf a+rX,u+w,g-w,o-w .


%build
gcc caps2esc.c -o caps2esc -s -O2 -I/usr/include/libevdev-1.0 -levdev -ludev


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 0755 %{name} %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{_unitdir}
install -p -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service


%preun
if [ "$1" -eq "0" ]; then
    /usr/bin/systemctl stop %{name} >/dev/null 2>&1
fi


%post
if [ "$1" -gt "0" ]; then
    /usr/bin/systemctl restart %{name} >/dev/null 2>&1
    /usr/bin/systemctl enable %{name} >/dev/null 2>&1
fi


%changelog
* Fri Aug 18 2017 Aurelien Fusil-Delahaye <aurelien.fusil-delahaye@shengis.org> - 1.3-1
- Initial package
