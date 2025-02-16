import pytest
from utilities.test_data import TestData

class TestBookingAPI:

    @pytest.mark.api
    def test_search_flights(self, api_client, logger):
        """Test flight search API endpoint"""
        search_params = TestData.get_flight_search_params()
        logger.info(f"Searching flights with params: {search_params}")

        response = api_client.search_flights(search_params)
        response_data = response.json()

        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert "flights" in response_data, "Response missing 'flights' key"
        assert len(response_data["flights"]) > 0, "No flights found in response"

        # Validate flight data structure
        first_flight = response_data["flights"][0]
        required_fields = ["flight_id", "origin", "destination", "price"]
        for field in required_fields:
            assert field in first_flight, f"Flight missing required field: {field}"

        logger.info("Flight search API test passed successfully")

    @pytest.mark.api
    def test_create_booking(self, api_client, logger):
        """Test booking creation API endpoint"""
        booking_data = TestData.get_booking_data()
        logger.info(f"Creating booking with data: {booking_data}")

        response = api_client.create_booking(booking_data)
        response_data = response.json()

        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        assert "booking_id" in response_data, "Response missing 'booking_id'"
        assert response_data["booking_id"] is not None, "Booking ID is null"

        logger.info(f"Booking created successfully with ID: {response_data['booking_id']}")

    @pytest.mark.api
    def test_get_booking_details(self, api_client, logger):
        """Test get booking details API endpoint"""
        # First create a booking
        booking_data = TestData.get_booking_data()
        create_response = api_client.create_booking(booking_data)
        booking_id = create_response.json()["booking_id"]
        logger.info(f"Created test booking with ID: {booking_id}")

        # Get booking details
        response = api_client.get_booking(booking_id)
        response_data = response.json()

        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert response_data["booking_id"] == booking_id, "Booking ID mismatch"

        # Validate booking details structure
        required_fields = ["status", "flight_details", "passenger_details"]
        for field in required_fields:
            assert field in response_data, f"Response missing required field: {field}"

        logger.info("Get booking details test passed successfully")