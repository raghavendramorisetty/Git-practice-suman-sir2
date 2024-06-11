import pytest

@pytest.fixture
def common_condition():
    print("Precondition")
    yield
    print("Post condition")

def test_f11(common_condition):
    print("test_f11")

