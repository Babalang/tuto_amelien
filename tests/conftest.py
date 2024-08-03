# pylint: skip-file
"""Pytest configuration file."""

def pytest_configure(config):
    # A "local" marker to ignore tests that will fail in the Gitlab pipelines
    # Add `@pytest.mark.local` above your tests functions you want to ignore online
    config.addinivalue_line("markers", "local : mark a local test")
