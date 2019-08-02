"""
DFT + ML
Generates a correction to DFT calculations
"""

# Add imports here
from .datagen import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
