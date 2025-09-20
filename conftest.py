import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def api_base_url():
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")

@pytest.fixture
def http_client():
    s = requests.Session()
    yield s
    s.close()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Test environment")


