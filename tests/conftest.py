from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

import chromedriver_binary  # Adds chromedriver binary to path
driver = None


@pytest.fixture(scope='class')
def setup(request):
    global driver
<<<<<<< HEAD
    driver = webdriver.Chrome('C:/Users/rajan/Downloads/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(0.5)
=======
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
>>>>>>> f2597c849d6f313a723aea42463fb037773bd5e6
    driver.get('https://master.chargeautomation.com/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    now = datetime.now()
    # create report target dir
    reports_dir = Path('reports')
    # reports_dir.mkdir(parents=True, exist_ok=True)
    # custom report file
    # report = reports_dir / f"report_{now.strftime('%H%M')}.html"
    report = reports_dir / f"report.html"
    # adjust plugin options
    config.option.htmlpath = report
    config.option.self_contained_html = True


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = file_name.strip()
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    yield
    driver.get_screenshot_as_file('reports/' + name)


@pytest.fixture()
def loginData():
    return {'email': 'pgtest@yopmail.com', 'password': 'Rajan@123'}
