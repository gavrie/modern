Modern Software Development Techniques with Python
==================================================

* Target audience: Python developers who want to deepen their expertise. Anyone who knows Python and uses it, and wants to get better at his skills.

* Prerequisites: Python course or equivalent knowledge

Syllabus
========

The Modern Development Environment
----------------------------------

* Background
  * `pip` and `setuptools`
  * Why not use plain `pip` to install?

* Deploying with Vagrant and Ansible
  * Plain vagrant
    * No need to learn a lot about virtual machines
    * Great for developers, automatable
  * Vagrant with ansible
    * Installing packages via apt

* Packaging your code
  * setuptools (superset of distutils)
  * `setup.py`
  * requirements.txt
  * wheels
  * pypi

* Developing with virtualenv, pip
  * Plain virtualenv
  * virtualenvwrapper
  * hooks: postactivate etc.

* Checking code
  * pep8
  * pylint
  * pyflakes

* Debugging: pdb++


Test Driven Development (TDD)
-----------------------------

* Introduction to TDD
* Writing effective Unit Tests with `py.test`
* Mock
* coverage
* Continuous Integration (CI)
  * Jenkins
    * apt: install git jenkins (via ansible or aptitude)
    * Add port forwarding in vagrantfile
    * Add jenkins git plugin
    * Set up job to build `/vagrant` dir
  * Integration with `coverage`
    pip install pytest-cov
    ./run_tests.sh --cov modern

Unicode awareness
-----------------

* The Unicode Sandwich
* Python 2/3


Resources
=========

* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
* [Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.org/en/latest/)


<!--
vim:lbr:wrap:nolist:ft=markdown
-->
