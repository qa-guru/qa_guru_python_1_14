import time

import pytest


@pytest.fixture(scope="session", autouse=True)
def session_scoped_fixture():
    pass


@pytest.mark.parametrize("param", range(20))
def test_many_params(param, session_scoped_fixture):
    time.sleep(1)
