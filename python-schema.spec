#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Schema validation just got Pythonic
Summary(pl.UTF-8):	Pythonowe sprawdzanie zgodności ze schematem
Name:		python-schema
# keep 0.7.4 here for python2 support
# (despite python 2.x in classifiers, 0.7.5 uses inspect.signature, which requires python 3.3+)
Version:	0.7.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/schema/
Source0:	https://files.pythonhosted.org/packages/source/s/schema/schema-%{version}.tar.gz
# Source0-md5:	37bded9e34826015e66e98b7c700467f
Patch0:		%{name}-requirements.patch
URL:		https://pypi.org/project/schema/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if "%{py_ver}" < "2.7"
BuildRequires:	python-contextlib2 >= 0.5.5
%endif
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
schema is a library for validating Python data structures, such as
those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to
Python data-types.

%description -l pl.UTF-8
schema to biblioteka do sprawdzania poprawności pythonowych struktur
danych, takich jak pochodzące z plików konfiguracyjnych, formularzy,
usług zewnętrznych czy analizy wiersza poleceń, przekształcone z
JSON-a/YAML-a (lub czegoś innego) do typów pythonowych.

%package -n python3-schema
Summary:	Schema validation just got Pythonic
Summary(pl.UTF-8):	Pythonowe sprawdzanie zgodności ze schematem
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-schema
schema is a library for validating Python data structures, such as
those obtained from config-files, forms, external services or
command-line parsing, converted from JSON/YAML (or something else) to
Python data-types.

%description -n python3-schema -l pl.UTF-8
schema to biblioteka do sprawdzania poprawności pythonowych struktur
danych, takich jak pochodzące z plików konfiguracyjnych, formularzy,
usług zewnętrznych czy analizy wiersza poleceń, przekształcone z
JSON-a/YAML-a (lub czegoś innego) do typów pythonowych.

%prep
%setup -q -n schema-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test_schema.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_schema.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE-MIT README.rst
%{py_sitescriptdir}/schema.py[co]
%{py_sitescriptdir}/schema-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-schema
%defattr(644,root,root,755)
%doc LICENSE-MIT README.rst
%{py3_sitescriptdir}/schema.py
%{py3_sitescriptdir}/__pycache__/schema.cpython-*.py[co]
%{py3_sitescriptdir}/schema-%{version}-py*.egg-info
%endif
