import allure
import pytest


def pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager):
    parser.addoption(
        "--browser",
        choices=['chrome', 'firefox'],
        # default='chrome',
    )
    parser.addoption(
        "--mobile-only",
        type=bool,
        default=False,
    )


def pytest_configure(config: pytest.Config):
    if config.getoption("--mobile-only") and config.getoption("--browser") == 'firefox':
        raise ValueError("Нет мобильных тестов на Firefox")


def pytest_sessionstart(session: pytest.Session):
    pass


def pytest_collection_modifyitems(session: pytest.Session, config: pytest.Config, items: list[pytest.Item]):
    for item in items:
        if "mobile" not in item.name and config.getoption("--mobile-only"):
            item.add_marker(pytest.mark.skip(reason="Mobile tests only"))
    return items.sort(key=lambda x: x.name, reverse=True)


def pytest_runtest_call(item: pytest.Item):
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).title())
    yield


def pytest_sessionfinish(session: pytest.Session):
    pass


def pytest_report_teststatus(report, config):
    pass
