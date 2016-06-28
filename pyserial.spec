#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyserial
Version  : 3.0.1
Release  : 12
URL      : https://pypi.python.org/packages/source/p/pyserial/pyserial-3.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pyserial/pyserial-3.0.1.tar.gz
Summary  : Python Serial Port Extension
Group    : Development/Tools
License  : Python-2.0
Requires: pyserial-bin
Requires: pyserial-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=================================
pySerial  |build-status| |docs|
=================================

%package bin
Summary: bin components for the pyserial package.
Group: Binaries

%description bin
bin components for the pyserial package.


%package python
Summary: python components for the pyserial package.
Group: Default

%description python
python components for the pyserial package.


%prep
%setup -q -n pyserial-3.0.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/miniterm.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
