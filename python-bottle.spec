%define srcname bottle

Name:           python-%{srcname}
Version:        0.13.1
Release:        1
Summary:        Fast and simple WSGI-framework for small web-applications

Group:          Development/Python
License:        MIT
URL:            http://bottlepy.org
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%description
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%prep
%setup -q -n %{srcname}-%{version}
sed -i '/^#!/d' bottle.py

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%py_build

%install
%py_install
rm %{buildroot}%{_bindir}/bottle.py

%files
%doc README.rst PKG-INFO
%{python_sitelib}/*
