#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Schema validation just got Pythonic
Summary(pl.UTF-8):	Pythonowe sprawdzanie zgodności ze schematem
Name:		python3-schema
Version:	0.7.8
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/schema/
Source0:	https://files.pythonhosted.org/packages/source/s/schema/schema-%{version}.tar.gz
# Source0-md5:	937d1deed2d7e96385cde49d37da4d05
URL:		https://pypi.org/project/schema/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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

%prep
%setup -q -n schema-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_schema.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE-MIT README.rst
%{py3_sitescriptdir}/schema
%{py3_sitescriptdir}/schema-%{version}-py*.egg-info
