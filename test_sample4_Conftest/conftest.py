import pytest

@pytest.fixture
def common_condition():
    print("Precondition")
    yield
    print("Post condition")