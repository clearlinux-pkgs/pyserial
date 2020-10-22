#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyserial
Version  : 3.4
Release  : 30
URL      : https://files.pythonhosted.org/packages/cc/74/11b04703ec416717b247d789103277269d567db575d2fd88f25d9767fe3d/pyserial-3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/74/11b04703ec416717b247d789103277269d567db575d2fd88f25d9767fe3d/pyserial-3.4.tar.gz
Summary  : Python Serial Port Extension
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: pyserial-bin = %{version}-%{release}
Requires: pyserial-license = %{version}-%{release}
Requires: pyserial-python = %{version}-%{release}
Requires: pyserial-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=================================
pySerial  |build-status| |docs|
=================================

%package bin
Summary: bin components for the pyserial package.
Group: Binaries
Requires: pyserial-license = %{version}-%{release}

%description bin
bin components for the pyserial package.


%package license
Summary: license components for the pyserial package.
Group: Default

%description license
license components for the pyserial package.


%package python
Summary: python components for the pyserial package.
Group: Default
Requires: pyserial-python3 = %{version}-%{release}

%description python
python components for the pyserial package.


%package python3
Summary: python3 components for the pyserial package.
Group: Default
Requires: python3-core
Provides: pypi(pyserial)

%description python3
python3 components for the pyserial package.


%prep
%setup -q -n pyserial-3.4
cd %{_builddir}/pyserial-3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603401532
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyserial
cp %{_builddir}/pyserial-3.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyserial/a9101277c5fbc32be71ed35135d6949722287ccb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/miniterm.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyserial/a9101277c5fbc32be71ed35135d6949722287ccb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
