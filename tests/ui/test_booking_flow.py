import pytest
from page_objects.search_page import SearchPage
from page_objects.booking_page import BookingPage
from utilities.test_data import TestData

class TestBookingFlow:
    
    @pytest.mark.ui
    def test_complete_flight_booking(self, driver, logger):
        """Test end-to-end flight booking flow"""
        search_page = SearchPage(driver)
        booking_page = BookingPage(driver)
        test_data = TestData.get_flight_booking_data()
        
        logger.info("Starting flight booking test")
        
        # Search for flights
        search_page.enter_origin(test_data["origin"])
        search_page.enter_destination(test_data["destination"])
        search_page.enter_dates(test_data["departure_date"], 
                              test_data["return_date"])
        search_page.click_search()
        
        # Select flight
        search_page.select_first_available_flight()
        
        # Fill booking details
        booking_page.enter_passenger_details(
            test_data["passenger_first_name"],
            test_data["passenger_last_name"],
            test_data["passenger_email"]
        )
        booking_page.enter_payment_details(
            test_data["card_number"],
            test_data["expiry_date"],
            test_data["cvv"]
        )
        
        # Complete booking
        booking_reference = booking_page.complete_booking()
        
        assert booking_reference is not None
        logger.info(f"Booking completed successfully: {booking_reference}")
