# tests/ui/test_example.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    """Set up Selenium Chrome WebDriver"""
    options = Options()
    options.add_argument("--headless")       # run without opening browser UI
    options.add_argument("--disable-gpu")    # required for some CI environments
    options.add_argument("--no-sandbox")     # required for some CI/CD like GitHub Actions
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_example_domain(browser):
    """Simple UI test with Selenium"""
    browser.get("https://example.com")   # navigate to page
    assert "Example Domain" in browser.title   # verify title
