"""
Lind Static Resources
====

Lind static resources is a package with static files containing pre-computed
experimental designs for the package Lind. These static designs offer optional
functionality for users of Lind.

"""

from os.path import dirname as _dirname, abspath as _abspath

static_files_abs_path = _dirname(_abspath(__file__))

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
