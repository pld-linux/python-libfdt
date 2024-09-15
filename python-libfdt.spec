Summary:	Python 2 binding for fdt library
Summary(pl.UTF-8):	Wiązanie Pythona 2 do biblioteki fdt
Name:		python-libfdt
# keep 1.7.0 here for python2 support
Version:	1.7.0
Release:	1
License:	GPL v2+ or BSD
Group:		Libraries/Python
Source0:	https://www.kernel.org/pub/software/utils/dtc/dtc-%{version}.tar.xz
# Source0-md5:	228576aceed3aa89f54283aa0f1eb820
Patch0:		dtc-python2.patch
URL:		https://www.devicetree.org/
BuildRequires:	python-devel >= 2
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 2.0.10
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libfdt >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 binding for fdt library.

%description -l pl.UTF-8
Wiązanie Pythona 2 do biblioteki fdt.

%prep
%setup -q -n dtc-%{version}
%patch0 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%py_build

%install
rm -rf $RPM_BUILD_ROOT

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.license README.md
%attr(755,root,root) %{py_sitedir}/_libfdt.so
%{py_sitedir}/libfdt.py[co]
%{py_sitedir}/libfdt-%{version}-py*.egg-info
