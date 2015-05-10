%define name jenkins-job-builder
%define version 1.2.0.post49
%define unmangled_version 1.2.0.post49
%define unmangled_version 1.2.0.post49
%define release 1%{?dist}

Summary: Manage Jenkins jobs with YAML
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache License, Version 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: OpenStack Infrastructure Team <openstack-infra@lists.openstack.org>
Url: http://ci.openstack.org/jjb.html

Requires: PyYAML
Requires: python-six >= 1.5.2
Requires: python-pbr >= 0.8.2
Requires: python-jenkins >= 0.4.1

BuildRequires: python
BuildRequires: python-setuptools

# Per-distro special cases
%if 0%{?fedora} == 21
Requires: python >= 2.7
%endif

%if 0%{?fedora} == 20
Requires: python >= 2.7
%endif

%if 0%{?fedora} == 19
Requires: python >= 2.7
%endif

%if 0%{?rhel} == 7
Requires: python >= 2.7
%endif

%if 0%{?rhel} == 6
Requires: python
Requires: python-argparse
Requires: python-ordereddict
%endif

Patch1: packaging.fc21.patch
Patch2: packaging.fc20.patch
Patch3: packaging.fc19.patch
Patch4: packaging.el7.patch
Patch5: packaging.el6.patch

%description
README
======

Jenkins Job Builder takes simple descriptions of Jenkins_ jobs in YAML_ format,
and uses them to configure Jenkins. You can keep your job descriptions in human
readable text format in a version control system to make changes and auditing
easier. It also has a flexible template system, so creating many similarly
configured jobs is easy.

To install::

    $ sudo python setup.py install

Online documentation:

* http://ci.openstack.org/jenkins-job-builder/

Developers
----------
Bug report:

* https://storyboard.openstack.org/#!/project/723

Repository:

* https://git.openstack.org/cgit/openstack-infra/jenkins-job-builder

Cloning::

    git clone https://git.openstack.org/openstack-infra/jenkins-job-builder

Patches are submitted via Gerrit at:

* https://review.openstack.org/

Please do not submit GitHub pull requests, they will be automatically closed.

More details on how you can contribute is available on our wiki at:

* http://docs.openstack.org/infra/manual/developers.html

Writing a patch
---------------

We ask that all code submissions be pep8_ and pyflakes_ clean.  The
easiest way to do that is to run tox_ before submitting code for
review in Gerrit.  It will run ``pep8`` and ``pyflakes`` in the same
manner as the automated test suite that will run on proposed
patchsets.

When creating new YAML components, please observe the following style
conventions:

* All YAML identifiers (including component names and arguments)
  should be lower-case and multiple word identifiers should use
  hyphens.  E.g., "build-trigger".
* The Python functions that implement components should have the same
  name as the YAML keyword, but should use underscores instead of
  hyphens. E.g., "build_trigger".

This consistency will help users avoid simple mistakes when writing
YAML, as well as developers when matching YAML components to Python
implementation.

Installing without setup.py
---------------------------

For YAML support, you will need libyaml_ installed.

Mac OS X::

    $ brew install libyaml

Then install the required python packages using pip_::

    $ sudo pip install PyYAML python-jenkins

.. _Jenkins: http://jenkins-ci.org/
.. _YAML: http://www.yaml.org/
.. _pep8: https://pypi.python.org/pypi/pep8
.. _pyflakes: https://pypi.python.org/pypi/pyflakes
.. _tox: https://testrun.org/tox
.. _libyaml: http://pyyaml.org/wiki/LibYAML
.. _pip: https://pypi.python.org/pypi/pip



%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}
%if 0%{?fedora} == 21
%patch1 -p1
%endif
%if 0%{?fedora} == 20
%patch2 -p1
%endif
%if 0%{?fedora} == 19
%patch3 -p1
%endif
%if 0%{?rhel} == 6
%patch4 -p1
%endif
%if 0%{?rhel} == 7
%patch5 -p1
%endif


%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
