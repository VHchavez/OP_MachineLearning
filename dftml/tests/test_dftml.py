"""
Unit and regression test for the dftml package.
"""

# Import package, test suite, and other packages as needed
import dftml
import pytest
import sys

def test_dftml_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "dftml" in sys.modules
