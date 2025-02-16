import pytest
from utilities.test_data import TestData
import json
import os
from unittest.mock import patch
import config

@pytest.fixture(scope="session")
def mock_responses():
    """Load mock response data from JSON file"""
    with open("test_data/mock_responses.json", "r") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def mock_api_session(monkeypatch, mock_responses):
    """Mock requests.Session to return predefined responses"""
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    class MockSession:
        def __init__(self):
            self.mock_responses = mock_responses

        def get(self, url, **kwargs):
            if '/flights/search' in url:
                return MockResponse(self.mock_responses["search_flights"])
            elif '/bookings/' in url:
                return MockResponse(self.mock_responses["booking_confirmation"])
            return MockResponse({}, 404)

        def post(self, url, **kwargs):
            if '/bookings' in url:
                return MockResponse(self.mock_responses["booking_confirmation"], 201)
            return MockResponse({}, 404)

    with patch('requests.Session') as mock:
        mock.return_value = MockSession()
        yield mock

@pytest.fixture(scope="function")
def api_client(env, mock_api_session):
    """Configure API client with mocked session"""
    from utilities.api_client import APIClient
    try:
        base_url = getattr(config, f"{env.upper()}_API_URL")
    except AttributeError:
        raise ValueError(f"Invalid environment: {env}. Available environments: dev, staging, prod")
    return APIClient(base_url)

@pytest.fixture(autouse=True)
def setup_teardown(logger):
    """Setup and teardown for each test"""
    logger.info("Starting test")
    yield
    logger.info("Test completed")