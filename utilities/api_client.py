import requests
from config import ENDPOINTS
import logging

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = logging.getLogger('travel_booking_tests')

    def _handle_response(self, response, expected_status=200):
        """Handle API response and log appropriately"""
        if response.status_code != expected_status:
            self.logger.error(f"API call failed with status {response.status_code}")
            self.logger.error(f"Response: {response.text}")
            response.raise_for_status()
        return response

    def search_flights(self, params):
        """Search flights API call"""
        url = self.base_url + ENDPOINTS["search_flights"]
        self.logger.info(f"Searching flights with params: {params}")
        response = self.session.get(url, params=params)
        return self._handle_response(response)

    def create_booking(self, booking_data):
        """Create booking API call"""
        url = self.base_url + ENDPOINTS["book_flight"]
        self.logger.info(f"Creating booking with data: {booking_data}")
        response = self.session.post(url, json=booking_data)
        return self._handle_response(response, expected_status=201)

    def get_booking(self, booking_id):
        """Get booking details API call"""
        url = self.base_url + ENDPOINTS["get_booking"]
        url = url.format(booking_id=booking_id)
        self.logger.info(f"Getting booking details for ID: {booking_id}")
        response = self.session.get(url)
        return self._handle_response(response)