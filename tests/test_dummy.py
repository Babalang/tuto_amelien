# pylint: skip-file
"""Delete this module when another test file is created."""
import pytest

@pytest.mark.local
def test_dummy_local():
    """An example of a test function with a "local" marker.
    
    This pytest marker can be added to your test functions to ignore this test in our GitLab pipelines.
    """

def test_dummy():
    """An example of a test function."""
