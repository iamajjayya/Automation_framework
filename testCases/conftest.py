import pytest
import undetected_chromedriver as uc
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, or edge"
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # Use undetected_chromedriver to bypass Cloudflare
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = uc.Chrome(options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


# Set a custom title for the HTML report
def pytest_html_report_title(report):
    report.title = "Automation Test Report - nopCommerce"


# Add custom environment details to the summary section of the report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Project Name   : nopCommerce",
        "Module Name    : Customers",
        "Tester         : Ajjayya"
    ])
