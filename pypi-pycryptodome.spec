#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pycryptodome
Version  : 3.15.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/11/e4/a8e8056a59c39f8c9ddd11d3bc3e1a67493abe746df727e531f66ecede9e/pycryptodome-3.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/e4/a8e8056a59c39f8c9ddd11d3bc3e1a67493abe746df727e531f66ecede9e/pycryptodome-3.15.0.tar.gz
Summary  : Cryptographic library for Python
Group    : Development/Tools
License  : BSD-2-Clause Python-2.0
Requires: pypi-pycryptodome-filemap = %{version}-%{release}
Requires: pypi-pycryptodome-lib = %{version}-%{release}
Requires: pypi-pycryptodome-license = %{version}-%{release}
Requires: pypi-pycryptodome-python = %{version}-%{release}
Requires: pypi-pycryptodome-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://github.com/Legrandin/pycryptodome/workflows/Integration%20test/badge.svg?branch=master
:target: https://github.com/Legrandin/pycryptodome/actions

%package filemap
Summary: filemap components for the pypi-pycryptodome package.
Group: Default

%description filemap
filemap components for the pypi-pycryptodome package.


%package lib
Summary: lib components for the pypi-pycryptodome package.
Group: Libraries
Requires: pypi-pycryptodome-license = %{version}-%{release}
Requires: pypi-pycryptodome-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pycryptodome package.


%package license
Summary: license components for the pypi-pycryptodome package.
Group: Default

%description license
license components for the pypi-pycryptodome package.


%package python
Summary: python components for the pypi-pycryptodome package.
Group: Default
Requires: pypi-pycryptodome-python3 = %{version}-%{release}

%description python
python components for the pypi-pycryptodome package.


%package python3
Summary: python3 components for the pypi-pycryptodome package.
Group: Default
Requires: pypi-pycryptodome-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pycryptodome)

%description python3
python3 components for the pypi-pycryptodome package.


%prep
%setup -q -n pycryptodome-3.15.0
cd %{_builddir}/pycryptodome-3.15.0
pushd ..
cp -a pycryptodome-3.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655999637
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycryptodome
cp %{_builddir}/pycryptodome-3.15.0/Doc/LEGAL/copy/LICENSE.python-2.2 %{buildroot}/usr/share/package-licenses/pypi-pycryptodome/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7
cp %{_builddir}/pycryptodome-3.15.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/pypi-pycryptodome/2f38e6ee60a1176611d852cf7fce799b477cd6b6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pycryptodome

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pycryptodome/2f38e6ee60a1176611d852cf7fce799b477cd6b6
/usr/share/package-licenses/pypi-pycryptodome/e2e326a9a73b4a86d3aa275bb1b9797ab1f047b7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
