Name:		python-pi-heif
Version:	0.16.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pi-heif/pi_heif-%{version}.tar.gz
Summary:	Python interface for libheif library
URL:		https://pypi.org/project/pi-heif/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libheif)
#BuildArch:	noarch

%description
Python interface for libheif library

%prep
%autosetup -p1 -n pi_heif-%{version}

# disable Werror flag
sed -ie "s/, \"-Werror\"//g" setup.py

%files
%{py_platsitedir}/pi_heif
%{py_platsitedir}/pi_heif-*.*-info
%{py_platsitedir}/_pi_heif.*.so

#-----------------------------------------------------------------------

%build
%py_build

%install
%py_install

