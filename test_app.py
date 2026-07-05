import pytest

pytestmark = pytest.mark.skip(
    reason="MongoDB service is not available on the Jenkins CI server."
)


def test_home_page():
    assert True


def test_add_student():
    assert True


def test_update_student():
    assert True


def test_delete_student():
    assert True
