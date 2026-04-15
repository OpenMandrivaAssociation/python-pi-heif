%define module pi-heif
%define oname pi_heif

Name:		python-pi-heif
Version:	1.3.0
Release:	1
Summary:	Python interface for libheif library
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/pi-heif/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python)
# Use unrestricted version of libheif
BuildRequires:	heif-free-devel
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python interface for libheif library

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%files
%{py_platsitedir}/_%{oname}.cpython*.so
%{py_platsitedir}/%{oname}
%{py_platsitedir}/%{oname}-%{version}.dist-info
