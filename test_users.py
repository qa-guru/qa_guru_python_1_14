"""
Пример из обсуждения на уроке
"""
import pytest


@pytest.fixture()
def role(request):
    return request.param


@pytest.fixture()
def login(role, request: pytest.Item):
    if role == 'manager':
        user, password = "manager", request.config.getoption("--manager-password")


all_roles = pytest.mark.parametrize("role", ["operator", "manager", "viewer"], indirect=True)
operator = pytest.mark.parametrize("role", ["operator"], indirect=True)
viewer = pytest.mark.usefixtures("viewer_role")


@all_roles
def test_some(role, login):
    pass


@operator
def test_operator(role, login):
    pass


@viewer
def test_viewer(role, login):
    pass
