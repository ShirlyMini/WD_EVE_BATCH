import pytest
@pytest.fixture()
def setup1():
    print("\nTEST SETUP1")
    yield
    print("\nTEST TEARDOWN")

@pytest.fixture(scope="class")
def setup_class():
    print("\nSUITE SETUP1")
    yield
    print("\nSUITE TEARDOWN")


@pytest.fixture(scope="module")
def setup_module():
    print("\nModule SETUP1")
    yield
    print("\nModule TEARDOWN")


def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: sanity test cases")
    config.addinivalue_line("markers", "regression: regression test cases")
    config.addinivalue_line("markers", "functionality: functionality test cases")